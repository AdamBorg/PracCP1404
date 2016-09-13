"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():

    score = float(input("Enter score: "))
    print(score_sorter(score))


def score_sorter(score):
    if score < 0:
        report = "Invalid score"
    elif score > 100:
        report = "Invalid score"
    elif score > 90:
        report = "Excellent"
    elif score >= 50:
        report = "Passable"
    else:
        report = "Bad"

    return report

main()