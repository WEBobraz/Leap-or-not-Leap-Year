# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} Year is Leap')
        else:
            print(f'{year} Year is Not Leap')
    else:
        print(f'{year} Year is Leap')
else:
    print(f'{year} Year is Not Leap')

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))