"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

# score = float(input("Enter score: "))
# if score < 0:
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     elif score > 50:
#         print("Passable")
#      score > 90:
#         print("Excellent")
# if score < 50:
#     print("Bad")

score = float(input("enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
else:
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Pass")
    else:
        print("Bad")
