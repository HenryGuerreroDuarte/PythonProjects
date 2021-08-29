#Henry Guerrero-Duarte 918600766
#assignment_2


####################Code#############################

##Variables names
# p_t percent test
# l_t letter test
# p_a perecnt assignments
# l_a Letter assignment
# p_o perecnt overall
# l_o letter asignments
# m_o message overall
# t_a test assigned
# a_a assignmentes assigned

accumalator_assignment = 0
accumalator_test  = 0

#Opening screen
print("CS309 Gradebook!")
#input validation for Assignments
a_a= int(input("How many assignments were assigned: " ))
while ( a_a < 0):
    print("I am sorry, that is an invalid value.")
    a_a= int(input("How many assignments were assigned: " ))


#input validation for Tests
t_a= int(input("How many tests were assigned: " ))
while ( t_a < 0 ):
    print("I am sorry, that is an invalid value.")
    t_a= int(input("How many tests were assigned: " ))


#input validfoation and accumalating scores for assigment scores
for assignment_score in range(0, a_a):
    assignment_score= int(input("What was your score on Assignment : "))
    while ( (assignment_score > 25) or (assignment_score < 0) ):
        print("I am sorry, that is an invalid value.")
        assignment_score= int(input("What was your score on Assignment : " ))
    accumalator_assignment += assignment_score


#input validfoation and accumalating scores for tests scores
for test_score in range(0, t_a):
    test_score= float(input("What was your score on Test : "))
    while ( (test_score > 90) or (test_score < 0) ):
        print("I am sorry, that is an invalid value.")
        test_score= int(input("What was your score on Test : " ))
    accumalator_test += test_score




#Calculations for perecnt of test
p_t = accumalator_test/(80*t_a)
#If statement for what the person gets for test score
if p_t >= .90:
  l_t= "A"
elif p_t >= .80:
  l_t = "B"
elif p_t >= .70:
  l_t = "C"
elif p_t >= .60:
  l_t = "D"
elif p_t < .60:
  l_t = "F"

#Calculations for perecnt of assignment
p_a = accumalator_assignment/(20*a_a)
#If statement for what the person gets for assigment score
if p_a >= .90:
  l_a = "A"
elif p_a >= .80:
  l_a = "B"
elif p_a >= .70:
  l_a = "C"
elif p_a >= .60:
  l_a = "D"
elif p_a < .60:
  l_a = "F"

#Calculations for overall class
p_o = (accumalator_test+ accumalator_assignment)/((20*a_a)+(80*t_a))
#If statement for what the person gets for overall score
if p_o >= .90:
  l_o = "A"
  m_o = "Fantastic Job!"
elif p_o >= .80:
  l_o = "B"
  m_o = "Good Job!"
elif p_o >= .70:
  l_o = "C"
  m_o = "Good Try!"
elif p_o >= .60:
  l_o = "D"
  m_o = "Time to study harder!"
elif p_o < .60:
  l_o = "F"
  m_o = "Please see the professor for help."

#What to print out at the end for outputs
print("Your scores are below")
print("Item             Perecnt Letter Grade")
print("Test          ", format(p_t,'.2%'), l_t)
print("Assignment    ", format(p_a,'.2%'), l_a)
print("Overall       ", format(p_o,'.2%'), l_o)
print(m_o)

###############End Code################################

#############Scoring
#Program ran:
#Correct Output:
#Documentation:
#Requirements Met:
#Total:
