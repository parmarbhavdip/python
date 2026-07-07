'''Create a program that checks how compatible two people are for marriage based on their zodiac signs.

Ask for the male's birth day (example: 15)
Ask for the male's birth month (example: 3 for March)
Ask for the female's birth day (example: 22)
Ask for the female's birth month (example: 7 for July)'''

male_day = int(input("Enter the male's birth day: "))
male_month = int(input("Enter the male's birth month: "))
female_day = int(input("Enter the female's birth day: "))
female_month = int(input("Enter the female's birth month: "))

def get_zodiac_sign(day, month):
     if (month == 3 and day >= 21) or (month == 4 and day <= 19):
          return "Aries"
     elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
          return "Taurus"
     elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
          return "Gemini"
     elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
          return "Cancer"
     elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
          return "Leo"
     elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
          return "Virgo"
     elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
          return "Libra"
     elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
          return "Scorpio"
     elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
          return "Sagittarius"
     elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
          return "Capricorn"
     elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
          return "Aquarius"
     elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
          return "Pisces"
     else:
          