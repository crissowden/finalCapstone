import math

# investment - to calculate the amount of interest you'll earn on your investment
# bond - to calculate the amount you'll have to pay on a home loan
# enter either 'investment or 'bond' from the menu above to proceed

print(" Investment - to calculate the amount of interest you'll earn on your investment \n Bond - to calculate the amount you'll have to pay on a home loan \n Enter either 'investment or 'bond' from the menu above to proceed ") 
user_choice = input("Please enter your choice : ")
lower_choice = user_choice.lower()

if lower_choice == "investment" : #first control statement for investment

    user_amount = int(input("Please input the amount you wish to deposit : "))
    print(user_amount)
    user_interest = int(input("Thank you, now input the interest rate : "))
    interest_rate = user_interest / 100
    user_duration = int(input("Please confirm the number of years you would like to invest : "))
    interest_type = str(input("Please confirm if you would like to apply simple or compound interest : "))
    interest = interest_type.lower()
    
    # r = user_interest
    # p = user_amount
    # t = user_duration

    # creating a second control statement for the two types of interest
    if interest == "simple" :  
            print(user_amount * (1 + interest_rate * user_duration)) # formula provided : A = P (1 + r * t)

    elif interest == "compound" :
            print(user_amount * math.pow((1 + interest_rate),user_duration)) # formula provided : A = P * math.pow((1 + r), t)

    else : print("Error: Please input either simple or compound only") # in case user error entering simple or compound

# Question for reviewer please - when I tested the error, I then needed to re-input all the previous values. \n
# in your feedback could you suggest a way I could loop back so users just need to input the interest_type rather\n
# needing to start from the begining (sorry I know this isn't part of the Task) 

# repayment formula provided : repayment = (i * P)/(1 - (1 + i)**(-n))
# P = value of house
# i = interest rate
# n = number of months

elif lower_choice == "bond" : # second control flow statement for bond
    user_value = int(input("Please enter value of the house : "))
    user_bond_int = int(input( "Please input the interest rate : "))
    bond_int_annual = user_bond_int / 100
    bond_int_month = bond_int_annual / 12
    num_months = int(input("Please input the term of the bond in months : "))
    repayment = (bond_int_month * user_value)/(1 - (1 + bond_int_month) **(- num_months)) # use formular to calc repayment and print
    print(repayment)

else : print("Error: Please input either 'Bond' or 'Investment' only!") # third control statement for user input error
