import numpy as np

# ======================================================================================

""" Your First 2D NumPy Array
 Before working on the actual MLB data, let's try to create a 2D numpy array from a small list of lists.

 In this exercise, baseball is a list of lists. The main list contains 4 elements. Each of these elements is a list containing the height and the weight of 4 baseball players, in this order. baseball is already coded for you in the script.

 Instructions
 100 XP
 Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
 Print out the type of np_baseball.
 Print out the shape attribute of np_baseball. Use np_baseball.shape.
"""

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)


# ======================================================================================

""" Baseball data in 2D form
You realize that it makes more sense to restructure all this information in a 2D numpy array.

You have a Python list of lists. In this list of lists, each sublist represents the height and weight of a single baseball player. The name of this list is baseball and it has been loaded for you already (although you can't see it).

Store the data as a 2D array to unlock numpy's extra functionality.

Instructions
100 XP
Use np.array() to create a 2D numpy array from baseball. Name it np_baseball.
Print out the shape attribute of np_baseball """

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

# ======================================================================================

""" np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 124th player
print(np_baseball[124, 0]) """

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 124th player
print(np_baseball[124, 0])

# ======================================================================================

""" 2D Arithmetic
2D numpy arrays can perform calculations element by element, like numpy arrays.

np_baseball is coded for you; it's again a 2D numpy array with 3 columns representing height (in inches), weight (in pounds) and age (in years). baseball is available as a regular list of lists and updated is available as 2D numpy array.

Instructions
100 XP
You managed to get hold of the changes in height, weight and age of all baseball players. It is available as a 2D numpy array, updated. Add np_baseball and updated and print out the result.
You want to convert the units of height and weight to metric (meters and kilograms, respectively). As a first step, create a numpy array with three values: 0.0254, 0.453592 and 1. Name this array conversion.
Multiply np_baseball with conversion and print out the result. """

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated) # type: ignore

# Create numpy array: conversion
conversion = np_baseball[:, 0:3] * [0.0254, 0.453592, 1]
print(conversion)

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

# ======================================================================================

""" Average versus median
You now know how to use numpy functions to get a better feeling for your data.

The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers. np_baseball is available.

Instructions
100 XP
Create numpy array np_height_in that is equal to first column of np_baseball.
Print out the mean of np_height_in.
Print out the median of np_height_in. """

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]
print(np_height_in)

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# ======================================================================================

""" Explore the baseball data
Because the mean and median are so far apart, you decide to complain to the MLB. They find the error and send the corrected data over to you. It's again available as a 2D NumPy array np_baseball, with three columns.

The Python script in the editor already includes code to print out informative messages with the different summary statistics and numpy is already loaded as np. Can you finish the job? np_baseball is available.

Instructions
100 XP
The code to print out the mean height is already included. Complete the code for the median height.
Use np.std() on the first column of np_baseball to calculate stddev.
Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. """

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball[:,0])
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
heights = np_baseball[:, 0]
weights = np_baseball[:, 1]
corr = np.corrcoef(heights, weights)
print("Correlation: " + str(corr))

# ======================================================================================

