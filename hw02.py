import math

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments, and then write
# additional functions for parts B and C, and fill out the same information
# for those functions as well.

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

# Example function for background reading

def nickels_to_cents(nickels):
    '''
    Purpose: Converts from a certain number of nickels to
            how many cents we have

    Input Parameter(s):
        nickels: The number of nickels we have

    Return Value:
        the amount of cents we have
    '''
    total = nickels * 5
    return total

# Part A: Two functions that you should add documentation to
def celsius_to_fahrenheit(celsius):
    '''
    Purpose:
        Converts celsius to fahrenhiet
    Input Parameter(s):
        celsius: The temperature in celsius
    Return Value:
        The given temperature in fahrenhiet
    '''
    fahr = (celsius * 9 / 5) + 32
    return fahr

def surface_area_sphere(radius):
    '''
    Purpose:
        Computes the surface area of a sphere given radius
    Input Parameter(s):
        radius: The radius of the sphere
    Return Value:
        The surface area of the sphere
    '''
    pi = 3.14159
    rsquared = radius * radius
    area = pi * 4.0 * rsquared
    return area

# Part B: Write out a few simple conversions

def circumference_circle(radius):
    '''
    Purpose:
        Computes the circumference of a sphere given radius
    Input Parameter(s):
        radius: The radius of the circle
    Return Value:
        The circumference of the circle
    '''
    pi = math.pi
    circumference = 2 * pi * radius
    return circumference

def grams_to_ounces(grams):
    '''
    Purpose:
        Coverts the given grams to ounces
    Input Parameter(s):
        grams: The number of grams
    Return Value:
        The number of ounces
    '''
    ounces = grams / 28.3495
    return ounces

def seconds_to_hours(seconds):
    '''
    Purpose:
        Converts the given seconds to hours
    Input Parameter(s):
        seconds: The number of seconds
    Return Value:
        The number of hours
    '''
    hours = seconds / 3600
    return hours

# Part C: Calculate distance based on time and average speed

def calc_distance(minutes, speed):
    """
    Purpose:
        Computes the distance traveled given time and speed
    Input Parameter(s)
        minutes: The amount of time the object took in minutes
        speed: The speed of the object in miles per hour
    Return Value:
        The distance traveled in miles
    """
    hours = minutes / 60
    distance = speed * hours
    return distance
