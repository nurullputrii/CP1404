"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():

    score = float(input("Enter score: "))
    score_result(score)


def score_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Pass")
        else:
            print("Bad")
main()


