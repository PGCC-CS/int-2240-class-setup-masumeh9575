def calculaterAverage(grade1, grade2, grade3):
    total = grade1 + grade2 + grade3
    average = total / 3
    return round(average, 2)

def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def getAcademicStanding(letter):
    if letter == "A":
        return "Excellent"
    elif letter == "B":
        return "Good"
    elif letter == "C":
        return "Satisfactory"
    elif letter == "D":
        return "Needs Improvement"
    else :
        return "Failing "

def main():
    grade1 = float(input("Type your first score: "))
    grade2 = float(input("Type your second score: "))
    grade3 = float(input("And your last score: "))

    if (grade1 < 0 or grade1 > 100 or
            grade2 < 0 or grade2 > 100 or
            grade2 < 0 or grade2 > 100 or
            grade3 < 0 or grade3 > 100):
        print("Error: Scores must be between 0 and 100.")
        return

    average = calculaterAverage(grade1, grade2, grade3)
    letter = getLetterGrade(average)
    standing = getAcademicStanding(letter)

    print("Average score:", average)
    print("Letter grade:", letter)
    print("Academic Standing:", standing)


if __name__ == "__main__":
    main()
