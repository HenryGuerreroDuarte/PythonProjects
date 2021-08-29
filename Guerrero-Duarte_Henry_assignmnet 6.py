"""CS309 Python Assignment Template
This template is to be used with all assignments. Failure to use this template
will result in max grade of half credit. To use this template replace lines beginning
with a "#" with the indicated information. Your code will go in the code section.
Save this file with in the form lastname_firstname_assignmnet#.py before submitting to iLearn
For example if I (Sonny Sevin) was submitting assignmnet 1, the file name wouled be: sevin_sonny_assignment1.py."""

#Henry Guerrero-Duarte sfsu_id 918600766
#assignment_6


####################Code#############################

#Henry Guerrero-Duarte 918600766
#assignment_6


    #check_out_items = {
           # 'item' : ['Apples' , 'Eggs' , 'Bread' , 'Peppers' , 'Tissues' , 'Cookies'],
           # 'inventory' : [10 , 12, 5 , 3 , 1 , 15],
           # 'price' : [0.70, 3.00 , 4.25 , 0.50 , 2.0 , 3.00]}

#Opening screen with user inputs
print("What Items did your bring for your order? :")
input_apples = int(input("How many Apples? : " ))
input_eggs = int(input("How many Eggs? : " ))
input_bread = int(input("How many Bread? : " ))
input_peppers = int(input("How many Peppers? : " ))
input_tissues = int(input("How many Tissues? : " ))
input_cookies = int(input("How many Cookies? : " ))

#Checking if any of the inputs are negitive numbers
while ( (input_apples or input_eggs or input_bread or input_peppers or input_tissues or input_cookies)  < 0):
    print("I am sorry, that is an invalid value.")
    print("What Items did your bring for your order? :")
    input_apples = int(input("How many Apples? : " ))
    input_eggs = int(input("How many Eggs? : " ))
    input_bread = int(input("How many Bread? : " ))
    input_peppers = int(input("How many Peppers? : " ))
    input_tissues = int(input("How many Tissues? : " ))
    input_cookies = int(input("How many Cookies? : " ))


#Goes to directory, if the person is asking more then requested replaced
Apple_dir ={'inventory' : 10 , 'price' : 0.70 }
if input_apples <= Apple_dir['inventory']:
    app_cost= input_apples* Apple_dir['price']
else:
    print("We dont have that many Apple     , so were going to give you what we have in stock")
    input_apples = Apple_dir['inventory']
    app_cost= Apple_dir['inventory'] * Apple_dir['price']

#Goes to directory, if the person is asking more then requested replaced
Eggs_dir ={'inventory' : 12 , 'price' : 3.00 }
if input_eggs <= Eggs_dir['inventory']:
    egg_cost= input_eggs* Eggs_dir['price']
else:
    print("We dont have that many Eggs      , so were going to give you what we have in stock")
    input_eggs = Eggs_dir['inventory']
    egg_cost= Eggs_dir['inventory'] * Eggs_dir['price']

#Goes to directory, if the person is asking more then requested replaced
Bread_dir ={'inventory' : 5 , 'price' : 4.25 }
if input_bread <= Bread_dir['inventory']:
    bre_cost= input_bread* Bread_dir['price']
else:
    print("We dont have that many Bread       , so were going to give you what we have in stock")
    input_bread = Bread_dir['inventory']
    bre_cost= Bread_dir['inventory'] * Bread_dir['price']

#Goes to directory, if the person is asking more then requested replaced
Peppers_dir ={'inventory' : 3 , 'price' : 0.50 }
if input_peppers <= Peppers_dir['inventory']:
    pep_cost= input_peppers* Peppers_dir['price']
else:
    print("We dont have that many Peppers     , so were going to give you what we have in stock")
    input_peppers = Peppers_dir['inventory']
    pep_cost= Peppers_dir['inventory'] * Peppers_dir['price']

#Goes to directory, if the person is asking more then requested replaced
Tissues_dir ={'inventory' : 1 , 'price' : 2.00 }
if input_tissues <= Tissues_dir['inventory']:
    tis_cost= input_tissues* Tissues_dir['price']
else:
    print("We dont have that many Tissues     , so were going to give you what we have in stock")
    input_tissues = Tissues_dir['inventory']
    tis_cost= Tissues_dir['inventory'] * Tissues_dir['price']

#Goes to directory, if the person is asking more then requested replaced
Cookies_dir ={'inventory' : 15 , 'price' : 3.00 }
if input_cookies <= Cookies_dir['inventory']:
    coo_cost= input_cookies* Cookies_dir['price']
else:
    print("We dont have that many Cookies      , so were going to give you what we have in stock!!!!")
    input_cookies = Cookies_dir['inventory']
    coo_cost= Cookies_dir['inventory'] * Cookies_dir['price']

#Calculation of the final cost
total_cost = app_cost + egg_cost + bre_cost + pep_cost + tis_cost + coo_cost

#Final output screen
print("Customer Reciept")
print("Item          Quantity     Cost"   )
print("")
print("Apple        ",input_apples,"      $",format(app_cost,'.3'))
print("Eggs        ",input_eggs,"      $",format(egg_cost,'.3'))
print("Bread        ",input_bread,"      $",format(bre_cost,'.3'))
print("Peppers        ",input_peppers,"      $",format(pep_cost,'.3'))
print("Tissues        ",input_tissues,"      $",format(tis_cost,'.3'))
print("Cookies       ",input_cookies,"      $",format(coo_cost,'.3'))
print("Total:, $", total_cost)
x = input("press space to continou")


###############End Code################################

#############Scoring
#Program ran:
#Correct Output:
#Documentation:
#Requirements Met:
#Total:
