#Henry Guerrero-Duarte 918600766
#assignment_1


####################Code#############################

#Variables names 
# t test
# a assignments
# p_t percent test
# l_t letter test
# p_a perecnt assignments
# l_a Letter assignment
# p_o perecnt overall
# l_o letter asignments
# m_o message overall

#Opening screen
print("CS309 Gradebook!")
t= float(input("What was your score on Test 1: "))
a= float(input("What was your score on Assignment 1: "))


#Calculations for perecnt of test
p_t = t/80
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
p_a = a/20
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
p_o = (t+ a)/100
#If statement for what the person gets for overall score
if p_o >= .90:
  l_o = "A"
  m_o = "Fantastic Job!"
elif p_a >= .80:
  l_o = "B"
  m_o = "Good Job!"
elif p_a >= .70:
  l_o = "C"
  m_o = "Good Try!"
elif p_a >= .60:
  l_o = "D"
  m_o = "Time to study harder!"
elif p_a < .60:
  l_o = "F"
  m_o = "Please see the professor for help."

#What to print out at the end for outputs
print("Your scores are below")
print("Item            Perecnt Letter Grade")
print("Test 1         ", format(p_t,'.2%'), l_t)
print("Assignment 1   ", format(p_a,'.2%'), l_a)
print("Overall        ", format(p_o,'.2%'), l_o)
print(m_o)

###############End Code################################

#############Scoring
#Program ran:
#Correct Output:
#Documentation:
#Requirements Met:
#Total:
