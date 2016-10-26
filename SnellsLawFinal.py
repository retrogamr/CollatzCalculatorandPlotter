#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import sin, cos, arcsin, arccos, tan, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
ax.axhspan(0, 4, alpha=.4, color='blue') #This section to create the blue region in the bottom that represents the medium the light is being cast into from the outside, supposedly a vacuum

t = np.arange(4, 10, 0.001) #creates a set of points from 4 to 10, at intervals of .001, these are the values that will be plugged into my function
s = 45 # initial angle in degrees
x = s*(pi/180) #initial angle going counterclockwise from the 90 degree mark, converted into radians
j = np.arange(0.0, 4, 0.001)
n = 1 #index of refraction of medium being cast into
y = arcsin(sin(x)/n) #to simplify my equations
line1 = (10-t)*tan(x)
line2 = (4-j)*tan(y)  + 6*tan(x)
f, = plt.plot(line1, t, lw=2, color='blue') #defines both lines
g, = plt.plot(line2, j, lw=2, color='green')
plt.axis([0,25,0,10]) #the range that will be plotted
frame = plt.gca()
frame.axes.get_xaxis().set_ticks([]) #eliminating the ticks and numbers on the sides of the plot
frame.axes.get_yaxis().set_ticks([])
plt.title('Snells Law Simulator', loc='left') #static title
frame.set_title('Speed of light in medium: %s' % str(1/n) + 'c', loc='right') #changing title, giving speed of light in the medium
axcolor = 'lightgoldenrodyellow'
axangle = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor) #creates regions (where you see the sliders)
axindex  = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)

sangle = Slider(axangle, 'Angle of Incidence', 0, 75, valinit=s) #establishes sliders that change values in the function
sindex = Slider(axindex, 'Index of Refraction', 1, 4.00001, valinit=n)


def update(val): #function that updates values for both lines
    angle = sangle.val*pi/180
    index = sindex.val
    a = sin(angle)/index
    y2 = arcsin(a)
    f.set_xdata((10-t)*tan(angle))
    g.set_xdata((4-j)*tan(y2) + 6*tan(angle))
    frame.set_title('Speed of light in medium: %s' % str(1/index) + 'c', loc='right')
    #print index this was used for debugging purposes
    plt.draw()
sangle.on_changed(update)
sindex.on_changed(update)

plt.show()