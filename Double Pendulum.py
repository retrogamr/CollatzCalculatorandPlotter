#!/usr/bin/env python
# -*- coding: utf-8 -*-

import decimal
from numpy import sin, cos, pi, arange, zeros_like
#import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as anim #PERSONAL NOTE DELETE FINAL if problems arise, change this and dependencies to animation rather than anim
decimal.getcontext().prec = 12 #this sets the precision of operations to 12 digits, which should be sufficient

#Defining some constants
G = 9.80665
L1 = decimal.Decimal(raw_input("What is the length in meters of the first pendulum (the one that is fixed at the center)? "))
L2 = decimal.Decimal(raw_input("What is the length in meters of the second pendulum? "))
D = decimal.Decimal(.5) #This is the density of the pendula, I could also make this user defined
M1 = L1*D
M2= L2*D
th1 = decimal.Decimal(pi/2)
#th1 = decimal.Decimal(raw_input(“What is the initial angle of the first pendulum?”))
th2 = decimal.Decimal(0) 
#th2 = decimal.Decimal(raw_input(“What is the initial angle of the second pendulum with respect to the first pendulum?”))
w1 = decimal.Decimal(0)
w2 = decimal.Decimal(0) #these two set initial angular velocities in degree/s of each pendulum, th1 and th2 are initial angles in degrees

#defines a differential equation for the position of the pendula
def ode(state, t):

    dydx = zeros_like(state)
    dydx[0] = decimal.Decimal(state[1])

    del_ = decimal.Decimal(state[2]) - decimal.Decimal(state[0])
    den1 = (decimal.Decimal(M1) + decimal.Decimal(M2))*decimal.Decimal(L1) - decimal.Decimal(M2)*decimal.Decimal(L1)*decimal.Decimal(cos(del_))*decimal.Decimal(cos(del_))
    dydx[1] = (decimal.Decimal(M2)*decimal.Decimal(L1)*decimal.Decimal(state[1])*decimal.Decimal(state[1])*decimal.Decimal(sin(del_))*decimal.Decimal(cos(del_)) +
               decimal.Decimal(M2)*decimal.Decimal(G)*decimal.Decimal(sin(decimal.Decimal(state[2])))*decimal.Decimal(cos(del_)) + decimal.Decimal(M2)*decimal.Decimal(L2)*decimal.Decimal(state[3])*decimal.Decimal(state[3])*decimal.Decimal(sin(del_)) - (decimal.Decimal(M1) + decimal.Decimal(M2))*decimal.Decimal(G)*decimal.Decimal(sin(state[0])))/decimal.Decimal(den1)

    dydx[2] = decimal.Decimal(state[3])

    den2 = (L2/L1)*den1
    dydx[3] = (decimal.Decimal(-M2)*decimal.Decimal(L2)*decimal.Decimal(state[3])*decimal.Decimal(state[3])*decimal.Decimal(sin(del_))*cos(del_) +
               (decimal.Decimal(M1) + decimal.Decimal(M2))*decimal.Decimal(G)*decimal.Decimal(sin(state[0]))*cos(del_) -
               (decimal.Decimal(M1) + decimal.Decimal(M2))*decimal.Decimal*(L1)*state[1]*state[1]*decimal.Decimal(sin(del_)) -
               (decimal.Decimal(M1) + decimal.Decimal(M2))*decimal.Decimal(G)*decimal.Decimal(sin(state[2])))/den2

#defines interval for numerical integration as .01 seconds for maximum accuracy, sets interval of simulation to 40 seconds
dt = .01
t = arange(0.0, 40, dt)

state = [th1, w1, th2, w2]

y = integrate.odeint(ode, state, t)

#defines positions for points on the pendulum for later animation
x1 = decimal.Decimal(L1)*decimal.Decimal(sin(y[:, 0]))
y1 = decimal.Decimal(-L1)*decimal.Decimal(cos(y[:, 0]))

x2 = decimal.Decimal(L2)*decimal.Decimal(sin(y[:, 2])) + decimal.Decimal(x1)
y2 = decimal.Decimal(-L2)*decimal.Decimal(cos(y[:, 2])) + decimal.Decimal(y1)

#creates the plot and its boundaries, sets boundaries at 1.25* the sum of the pendulum lengths
fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.25*max(list), 1.25*(L1+L2)), ylim=(-1.25*(L1+L2), 1.25*(L1+L2)))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

#creates a line between points
def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text

#animates the location of each pendulum
def animate(i):
    xpos = [0, x1[i], x2[i]]
    ypos = [0, y1[i], y2[i]]

    line.set_data(xpos, ypos)
    time_text.set_text(time_template % (i*dt))
    return line, time_text

ani = anim.FuncAnimation(fig, animate, arange(1, len(y)),
                              interval=25, blit=True, init_func=init)

#creates a video of the double pendulum and plots it in real time. The former can be disabled by commenting out ani.save. The simulation runs for 40 seconds by default
ani.save('double_pendulum.mp4', fps=60)
plt.show()
quit()