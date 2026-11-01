import csv

#Define the function to get number of students, and write their info to grades.csv.
def write_grades():
    while True:
        try:
            #Get num of students and check for negative/invalid type
            num_students = int(input("Enter number of students to be graded: "))
            if num_students <= 0: print("Invalid: enter a positive integer")
            else: break
        except ValueError: (print("Invalid: enter a positive integer"))

    #Define the header for the csv file.
    header = ["First name", "Last name", "Exam 1", "Exam 2", "Exam 3"]

    #Open the grades.csv file in write mode.
    with open("grades.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        #This line establishes the for loop that allows the user to
        #write student info for 3 exams, for as many students needed.
        for i in range(num_students):
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")

            #Create an empty list to store the grades, later written to grades.csv.
            grades = []
            for r in range(1,4):
                while True:
                    try:
                        exam = int(input(f"Enter score for exam {r}: "))
                        grades.append(exam)
                        break
                    except ValueError: (print("Invalid: enter a positive integer"))
            #Finally write all the collected data to its corresponding row in the table.
            writer.writerow([first_name, last_name, grades[0], grades[1], grades[2]])

#Define the function to read grades.csv and print it in a spreadsheet format.
def read_grades():
        try:
            #Open the grades.csv file in read mode.
            with open("grades.csv", mode="r") as file:
                reader = csv.reader(file)

                #Defines the spacing for each data column
                default_row = "{:<20} {:<20} {:<10} {:<10} {:<10}"

                for index, row in enumerate(reader):
                    if not row: continue
                    print(default_row.format(*row))
                    if index == 0: print("=" * 75)
        except FileNotFoundError: (print("File not found."))
        print("=" * 75)


if __name__ == "__main__":
    write_grades()
    read_grades()
