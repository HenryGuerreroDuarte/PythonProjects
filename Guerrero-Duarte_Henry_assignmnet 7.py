###Guerrero_Duarte, Henry, 918600766

###########################Complete these functions############################

file_name = 'test_file.txt'


def load_file(file_name):
    """This function loads the values from the file and returns the contents"""
    file = open(file_name, 'r')#open the file
    colors = file.read() #reads entire contents of the file and assigns it to names. This is the processing of the file
    file.close() #always close the file

    return colors


def write_data_to_file(data1, data2, data3, data4, data5):
    """This function writes the supplied data to a file, each on a new line"""
    with data_file as open('data_file.txt','w'):
        data_file.write(data1 +'\n')
        data_file.write(data2 +'\n')
        data_file.write(data3 +'\n')
        data_file.write(data4 +'\n')
        data_file.write(data5 +'\n')

###############################################################################


#####################Your Functions go here####################################

#imports
import math

#global constants
gravity = 9.8

#Functions

#i_vy initial velocity for y vector
#g    gravity
#i_h  initial height
#i_vx initial velocity for x vector

def max_height(i_vy , g , i_h):
    """This function takes the in inital_velocity_y_dirrection,gravity,inital_height
    from main function to output the max height in meters"""

    #Time variable
    t = float(i_vy/g)

    #Initial velocity in the y direction due to with time in the air
    i_vy_due_to_time = float(i_vy*t)

    #Gravity due to time
    g_due_time = float(.5*g*math.pow(t,2))

    #Adding all varibles into the formula
    max_height_calc= float(i_h + i_vy_due_to_time - g_due_time)

    #TestCode
    if max_height_calc == True :
        tests = [10, 9.8, 0]
        correct_results = 5.1

    return max_height_calc

def Distance_traveled_in_the_x_direction(i_vy , g , i_h, i_vx ):
    """This function takes the in inital_velocity_y_dirrection,gravity,inital_height,inital_velocity_x_dirrection
    from main function to output the Distance_traveled_in_the_x_direction in meters"""

    #Variable inside the time variable so its easier to see
    temp_inside_time = float(math.sqrt(math.pow(-i_vy,2) -4*(.5*g)*(-i_h)))

    #Real time and the inital velocity in the y directoin then divided by g
    t= float((i_vy + temp_inside_time )/g)

    #Initial velocity in the x direction due to time
    Distance_traveled_in_the_x_direction_calc =float(i_vx*t)


    #TestCode
    if Distance_traveled_in_the_x_direction_calc == True :
        tests = [10, 9.8, 0, 10]
        correct_results = 20.4

    return Distance_traveled_in_the_x_direction_calc

def How_long_the_projectile_was_in_the_air(i_vy , g , i_h):
    """This function takes the in inital_velocity_y_dirrection,gravity,inital_height
    from main function to output the time a projectile_was_in_the_air in seconds"""

    #Everything is inside a Square Root then squaring a i_vy then a small Calc inside it.
    temp_inside_projectile= float(math.sqrt((math.pow(-i_vy,2) -4*(.5*g)*(-i_h))))

    #Real projectile for time in the air
    How_long_the_projectile_was_in_the_air_Calc= float((i_vy + temp_inside_projectile)/g)


    TestCode
    if How_long_the_projectile_was_in_the_air_Calc == True :
        tests = [10, 9.8, 0]
        correct_results = 2.04

    return How_long_the_projectile_was_in_the_air_Calc

def magnitude_of_the_velocity_before_hitting_the_ground(i_vy , g , i_h, i_vx ):
    """This function takes the in inital_velocity_x_dirrection,inital_velocity_y_dirrection,gravity,
    inital_height from main function to output
    the time a magnitude_of_the_velocity_before_hitting_the_ground in m/s vel"""

    #Everything is inside a Square Root then squaring a i_vy then a small Calc inside it.
    temp_inside_projectile= float(math.sqrt((math.pow(-i_vy,2) -4*(.5*g)*(-i_h))))

    #Real projectile for time in the air
    How_long_the_projectile_was_in_the_air_Calc= float((i_vy + temp_inside_projectile)/g)

    #Time
    t= float(How_long_the_projectile_was_in_the_air_Calc)

    #Since the component of the Velocity in the x directoin is the same we need to recalculate the
    #component in the Velocity in the y directoin
    velocity_y= i_vy - (g*t)

    #The Magnitude of the velocity SquareRoot(V_x^2 + V_y^2)
    magnitude_of_the_velocity_before_hitting_the_ground_calc= float(math.sqrt((math.pow(i_vx,2)) +(math.pow(velocity_y,2))))

    #TestCode
    if magnitude_of_the_velocity_before_hitting_the_ground_calc == True :
        tests = [10, 9.8, 0, 10]
        correct_results = 14.14

    return magnitude_of_the_velocity_before_hitting_the_ground_calc


def projectile_to_hit_the_incline_plane(g ,ang_of_inc, inital_ang, i_v):
    """This function takes the in inital_velocity_x_dirrection,inital_velocity_y_dirrection,gravity,
    ,angle_of_incline, angle_of_velocity from main function to get the
    time it takes for it to hit the ground """

    #Adding both angle_of_incline + inital_angle
    total_angle= ang_of_inc + inital_ang


    #compounets in the x and y direction
    temp_y= i_v*math.sin(total_angle)
    temp_x= i_v*math.sin(total_angle)*math.tan(ang_of_inc)

    #1/2 of gravity
    half_g = g*.5

    #Finding time when projectile hing the incline
    t_incline= (temp_y -temp_x)/half_g

    #TestCode
    if t_incline == True :
        tests = [9.8,  10,  10, 10]
        correct_results = 0.66

    return t_incline
