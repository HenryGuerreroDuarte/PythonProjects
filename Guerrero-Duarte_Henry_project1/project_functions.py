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
    t = i_vy/g
    return float(i_h + (i_vy*t)-(.5*g*math.pow(t,2)))

def Distance_traveled_in_the_x_direction(i_vy , g , i_h, i_vx ):
    """This function takes the in inital_velocity_y_dirrection,gravity,inital_height,inital_velocity_x_dirrection
    from main function to output the Distance_traveled_in_the_x_direction in meters"""
    t= (i_vy + math.sqrt(math.pow(-i_vy,2) -4*(.5*g)*(-i_h)))/g
    return float(i_vx*t)

def How_long_the_projectile_was_in_the_air(i_vy , g , i_h):
   """This function takes the in inital_velocity_y_dirrection,gravity,inital_height
    from main function to output the time a projectile_was_in_the_air in seconds"""
    return float((i_vy + math.sqrt((math.pow(-i_vy,2) -4*(.5*g)*(-i_h))))/g)

###############################################################################
