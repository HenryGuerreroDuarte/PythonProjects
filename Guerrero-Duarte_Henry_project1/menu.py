###Guerrero_Duarte, Henry, 918600766
#This is the file where you will put the menu for your project

#imports
import math

#global constants
gravity = 9.8

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

#What user picked out from menu
    User_item = int(input("What menu item do you want?: " ))
    while(User_item < 0 or User_item > 5  ):
        print("I am sorry, that is an invalid value.")
        User_item = int(input("What menu item do you want?: " ))

#What user picked out from menu
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

#Calculation of x and y directoins
    inital_velocity_x_dirrection = inital_velocity*math.cos(inital_angle)
    inital_velocity_y_dirrection = inital_velocity*math.sin(inital_angle)

#Calculation for Distance_traveled_in_the_x_direction
    if User_item == 1:
        distance_x = float(Distance_traveled_in_the_x_direction(inital_velocity_y_dirrection,gravity,inital_height,inital_velocity_x_dirrection))
        print (format(distance_x, '.2') ,"m")

#Calculation max_height
    elif User_item == 2:
        max_h =  float(max_height(inital_velocity_y_dirrection,gravity,inital_height))
        print (format(max_h, '.2'), "m" )

#Calculation How_long_the_projectile_was_in_the_air
    elif User_item == 3:
        air_t = float(How_long_the_projectile_was_in_the_air(inital_velocity_y_dirrection,gravity,inital_height))
        print (format(air_t, '.2'), "s" )

#Calls load_file
    elif User_item == 4:
        load_file()

#Calls write_data_to_file
    elif User_item == 5:
        write_data_to_file()

#Exit
    elif User_item == 0:
        print("Exiting")
        break
    else:
        print("Your selection was not valid")


#nice good bye message
print("Have a great day!")
