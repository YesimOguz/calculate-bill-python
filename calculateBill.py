# this is a program to calculate the total amount to be paid by customer in a restourant
# get the price of the meal
# ask the user to chose the type of tip to give(18%,20%,25%)
# base on the tip calculate the total bill

meal_cost = int(input('please enter the price of the meal: ' ))
percentage_of_tip = input("""what tip percentage would you prefer
a. 18%
b. 20%
c. 25%
 """ )

#meal_cost=2000(if we dont get it from user)
if percentage_of_tip == 'a':
    tip = 0.18*meal_cost
elif percentage_of_tip == 'b':
    tip = 0.2*meal_cost
elif percentage_of_tip == 'c':
    tip = 0.25*meal_cost

total_bill = meal_cost + tip
print(f'the total cost of meal is {total_bill}')



    
    




