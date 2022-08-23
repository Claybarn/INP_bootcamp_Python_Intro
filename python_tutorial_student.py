"""
Learning Objectives

This exercise was made with the following learning objectives:

(1) get students comfortable with the python environment
(2) understand how to use google while coding
(3) know the difference between accessing elements of variables and using functions
(4) understand for loops and if statements in python
(5) know how to make basic plots

The parts of this script you should edit are encapsulated by...
       FOLLOW ALONG means type what the TA is doing
       EXERCISES means you should write the code yourself

"""
import numpy as np
import matplotlib.pyplot as plt

# Now, we're going to have some fun with a dataset of neural activity


# show how to play around with the sample Data
cell_responses = np.load('cell_responses.npy')
cell_times = np.load('cell_times.npy')

############################ EXERCISES ############################
# please do this exercise in the command window

# Q1: what are the dimensions of the above data?
data_dim = ; # HINT: google what the "shape" function does for numpy objects

# Q3: what is the number stored in the 1203th row and 2nd column?
number = ; # HINT: google how to do matrix indexing in numpy/python. Note the syntax is different than matlab!


###################################################################

## for loops and if statements in python

# for loops
#       allow you to execute the same block of code many times
#       the variable you're "looping over" keeps track of the index

########################### FOLLOW ALONG ###########################

# let's make a vector of 100 numbers


# there's a function in python that returns the sum of a vector


# let's use a for loop to do the same thing


# let's check if our answers agree
 
    # we got the same answer using the for loop as the sum function!!
    print(' subscribe to PhDchef.com :) ')

    # ugh, something went wrong
    print(' welcome to grad school ')




# QUESTION: how do we know if something is a function or a variable?? 
# Unlike matlab, python uses parentheses exclusively for functions and brackets for variables. 

"""
 Let's make some basic plots with the neuronal activity data.
 In python, matplotlib is the go-to library for plotting and it functions similarly to matlab.
 The 'standard' way to import the matplotlib library is:
 import matplotlib as plt
 
 Here's a few basic functions you will need to know in order to make
 useful plots in python. We will not use all of them, but feel free to use
 them as a reference for the future.

 plt.figure()
       This "initializes" the figure. Think of this like an artist putting
       a canvas up before they start painting. Every time you put
       "figure", it's like putting a new, blank canvas up

 plt.plot(x, y)
       This is the function that will actually plot your data. There's
       also function for scatter plots, histograms, 3D plots, etc. 

 plt.xlabel( *insert string* ) and plt.ylabel( *insert string* )
       These functions are how you label the x and y axes

 plt.xlim( *insert vector of 2 numbers* ) and plt.ylim( *insert vector of 2 numbers* )
       These will set the limits for the x and y axes, in case you don't
       like the limits automatically computed by python
 plt.xticks( *insert vector of numbers* ) and plt.yticks( *insert vector of numbers* )
       These tell python what tick marks you want

 
 plt.title( *insert string* )
       This creates the title for your plot.


now let's plot a few sin waves
"""
########################### FOLLOW ALONG ###########################


dt = 0.1; # time step, seconds
t0 = 0; # initial time, seconds
tf = 50; # final time, seconds

time = ; # creates a time vector

omega = ; # sets the frequency of the 3 sin waves

; # creates a new "canvas" for me to paint on

 # loop through each frequency I want to plot
   
    
    sin_wave = ; # creates the sin wave
    
    plot( ) # plot sin wave with a linewidth of 2


      # make the font size of the figure 15
      # label the x-axis as time in seconds
      # label the y-axis
      # make x-axis limits be the initial and final time
      # make x tick marks every 5 seconds
      # make y limits be the extrema of the sin wave
      # make y-ticks appear every 0.25
      # make a title


###################################################################


# There was a lot of stuff going on above, but that was just to demonstrate
# a lot of stuff you can do with plotting. Let's get the neural activty
# data again and plot it

cell_responses = np.load('cell_responses.npy')
cell_times = np.load('cell_times.npy')


############################ EXERCISES ############################

# create a new figure here



# loop through the 4 cells

    
    # plot the time trace of that specific cell (i.e. column)

    

# label the x-axis as time in seconds
# label the y-axis as the response (unitless)
# set the fontsize to 15


###################################################################