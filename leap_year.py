# year = input('Enter a year:')
# year = int(year)

# year=int(input('enter a year:'))

# if year % 4 == 0:
#     print(year,'is a leap year')
# elif year % 100 == 0:
#     print(year,'is not a leap year')

# elif year % 400 :
#     print(year,'is a leap year')

# else:
#     print(year,'is not a leap year')


# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


# Leap year হবে যদি:

# 👉 (৪ দিয়ে ভাগ যায় AND ১০০ দিয়ে ভাগ না যায়)
# OR
# 👉 ৪০০ দিয়ে ভাগ যায়

# 100 diye bag gele 400 diyeo jete hobe

year = int(input("enter a year:"))
# if year % 4 == 0 :
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('yes')
#         else:
#             print('no')

#     else:
#         print('yes')

# else:
#     print('no')


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes")
        else:
            print("no")
    else:
        print("yes")

else:
    print("no")
