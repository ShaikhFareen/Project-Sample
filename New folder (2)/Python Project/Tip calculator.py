#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("WELCOME TO TIP CALCULATOR")
bill=float(input("What was the total bill?$"))
tip=int(input("How much tip will you loke to give 10,12 or 15 ?"))
people=int(input("How many people to split the bill ?"))
tip_in_percent=bill/100
total_tip_amount=bill*tip_in_percent
total_bill=bill*total_tip_amount
person_per_bill=total_bill/people
final_amount=round(person_per_bill,2)
print(f"Each Person should pay : ${final_amount}")