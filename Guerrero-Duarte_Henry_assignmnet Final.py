###Guerrero_Duarte, Henry, 918600766
#This is the file where you will put the menu for your project

#imports
import matplotlib.pyplot as plt
import numpy as np
import math

#global constants
gravity = 9.8

#file_name = 'test_file.txt'


def load_file(file_name):
    """This function loads the values from the file and returns the contents"""
    #file = open(file_name, 'r')#open the file
    #colors = file.read() #reads entire contents of the file and assigns it to names. This is the processing of the file
    #file.close() #always close the file

    #return colors


def write_data_to_file(data1, data2, data3, data4, data5):
    """This function writes the supplied data to a file, each on a new line"""
    #with data_file as open('data_file.txt','w'):
        #data_file.write(data1 +'\n')
        #data_file.write(data2 +'\n')
        #data_file.write(data3 +'\n')
        #data_file.write(data4 +'\n')
        #data_file.write(data5 +'\n')

###############################################################################


#####################Your Functions go here####################################

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
    #if max_height_calc == True :
        #tests = [10, 9.8, 0]
        #correct_results = 5.1

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
    #if Distance_traveled_in_the_x_direction_calc == True :
        #tests = [10, 9.8, 0, 10]
        #correct_results = 20.4

    return Distance_traveled_in_the_x_direction_calc

def How_long_the_projectile_was_in_the_air(i_vy , g , i_h):
    """This function takes the in inital_velocity_y_dirrection,gravity,inital_height
    from main function to output the time a projectile_was_in_the_air in seconds"""

    #Everything is inside a Square Root then squaring a i_vy then a small Calc inside it.
    temp_inside_projectile= float(math.sqrt((math.pow(-i_vy,2) -4*(.5*g)*(-i_h))))

    #Real projectile for time in the air
    How_long_the_projectile_was_in_the_air_Calc= float((i_vy + temp_inside_projectile)/g)


    #TestCode
    #if How_long_the_projectile_was_in_the_air_Calc == True :
        #tests = [10, 9.8, 0]
        #correct_results = 2.04

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
    #if magnitude_of_the_velocity_before_hitting_the_ground_calc == True :
        #tests = [10, 9.8, 0, 10]
        #correct_results = 14.14

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
    #if t_incline == True :
        #tests = [9.8,  10,  10, 10]
        #correct_results = 0.66

    return t_incline

#Main
#Opening screen
while True :
    print("CS309 Projectile Motion")
    print("0.  Exist programe")
    print("1.  Distance traveled in the x-direction")
    print("2.  Max height")
    print("3.  How long the projectile was in the air")
    print("4.  load_file")
    print("5.  write_data_to_file")
    print("6.  magnitude_of_the_velocity_before_hitting_the_ground")
    print("7.  projectile_to_hit_the_incline_plane")

#What user picked out from menu
    User_item = int(input("What menu item do you want?: " ))
    while(User_item < 0 or User_item >  8 ):
        print("I am sorry, that is an invalid value.")
        User_item = int(input("What menu item do you want?: " ))

#What user picked inital_angle
    inital_angle = float(input("What is the initial angle after take off (0 to 90)? :"))
    while(inital_angle < 0 or inital_angle > 90  ):
        print("I am sorry, that is an invalid value.")

#What user picked for Velocity
    inital_velocity = float(input("What is the initial velocity after take off :"))
    while(inital_velocity < 0):
        print("I am sorry, that is an invalid value.")

#What user picked for Height
    inital_height = float(input("What is the initial height after take off :"))
    while(inital_height < 0):
        print("I am sorry, that is an invalid value.")

#What user picked inital_angle
    angle_of_incline = float(input("What is the initial angle after take off (0 to 90)? :"))
    while(angle_of_incline < 0 or angle_of_incline > 90  ):
        print("I am sorry, that is an invalid value.")


#Calculation of x and y directoins
    inital_velocity_x_dirrection = inital_velocity*math.cos(inital_angle)
    inital_velocity_y_dirrection = inital_velocity*math.sin(inital_angle)

#Calculation for Distance_traveled_in_the_x_direction
    if User_item == 1:
        distance_x = Distance_traveled_in_the_x_direction(inital_velocity_y_dirrection,gravity,inital_height,inital_velocity_x_dirrection)
        x = np.arange(1,distance_x)
        y = inital_height * x
        plt.title("Distance_traveled_in_the_x_direction")
        plt.xlabel("distance_x")
        plt.ylabel("inital_height")
        plt.plot(x,y)
        plt.show()
        print (format(distance_x, '.2') ,"m")

#Calculation max_height
    elif User_item == 2:
        max_h = max_height(inital_velocity_y_dirrection,gravity,inital_height)
        x = np.arange(1,max_h)
        y = inital_height * x
        plt.title("max_height")
        plt.xlabel("max_h")
        plt.ylabel("inital_height")
        plt.plot(x,y)
        plt.show()
        print (format(max_h, '.2'), "m" )

#Calculation How_long_the_projectile_was_in_the_air
    elif User_item == 3:
        air_t = How_long_the_projectile_was_in_the_air(inital_velocity_y_dirrection,gravity,inital_height)
        x = np.arange(1,air_t)
        y = inital_height * x
        plt.title("How_long_the_projectile_was_in_the_air")
        plt.xlabel("air_t")
        plt.ylabel("inital_height")
        plt.plot(x,y)
        plt.show()
        print (format(air_t, '.2'), "s" )

#Calls load_file
    elif User_item == 4:
        load_file()

#Calls write_data_to_file
    elif User_item == 5:
        write_data_to_file()

#Calculation magnitude_of_the_velocity_before_hitting_the_ground
    elif User_item == 6:
        mag_v = magnitude_of_the_velocity_before_hitting_the_ground(inital_velocity_x_dirrection,inital_velocity_y_dirrection,gravity,inital_height)
        x = np.arange(1,mag_v)
        y = inital_height * x
        plt.title("magnitude_of_the_velocity_before_hitting_the_ground")
        plt.xlabel("mag_v")
        plt.ylabel("inital_height")
        plt.plot(x,y)
        plt.show()
        print (format(mag_v, '.2'), "s" )

#Calculation projectile_to_hit_the_incline_plane
    elif User_item == 7:
        projectile_to_hit_the_incline_plane_calc= projectile_to_hit_the_incline_plane(gravity ,angle_of_incline, inital_angle, inital_velocity)
        x = np.arange(1,projectile_to_hit_the_incline_plane_calc)
        y = inital_angle * x
        plt.title("projectile_to_hit_the_incline_plane")
        plt.xlabel("projectile_to_hit_the_incline_plane_calc")
        plt.ylabel("inital_angle")
        plt.plot(x,y)
        plt.show()
        print (format(projectile_to_hit_the_incline_plane_calc, '.2'), "s" )

#Exit
    elif User_item == 0:
        print("Exiting")
        break
    else:
        print("Your selection was not valid")


#nice good bye message
print("Have a great day!")
