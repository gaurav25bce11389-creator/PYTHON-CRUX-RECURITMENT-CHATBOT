#CRUX Recruitment Chatbot
Departments = [
    "Data Analyst", "IT Coordinator", "Cybersecurity Specialist",
    "Backend Developer", "Support Specialist", "Cloud Engineer",
    "Full Stack Developer", "Project Manager", "DevOps Engineer",
    "Help Desk Analyst"
]

selected_departments = []

print("\nHello!")
print("Welcome to the CRUX Company Recruitment Chatbot\n")
def candidate_name():
    while True:
        name = input("Please enter the candidate's name: ").strip()
        if name:
            print("\nWelcome, " + name + "!")
            return name
        else:
            print("Name cannot be empty. Please try again.")
def candidate_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age >= 25:
                print("Great! You are eligible to apply.\n")
                return age
            else:
                print("Sorry, you must be at least 25 years old to apply.\n")
                return None
        except ValueError:
            print("Invalid input. Please enter your age in numbers only.")
def candidate_qualification():
    qualification_codes = {
        "BTECH AI/ML": "01",
        "BTECH CLOUD COMPUTING": "02",
        "BTECH CYBERSECURITY": "03",
        "BTECH CSE": "04"
    }
    print("\nAvailable Qualifications:")
    for qualification in qualification_codes:
        print("- " + qualification)

    user_input = input("\nEnter your qualification: ").strip().upper()

    if user_input in qualification_codes:
        print("Qualification verified successfully")
        return True, user_input, qualification_codes[user_input]
    else:
        print("Sorry! This qualification is not recognized")
        return False, None, None
def view_Departments():
    if not Departments:
        print("Currently, no departments are available for selection.")
        return

    print("\nDepartments Available for Recruitment:")
    index = 1
    for dept in Departments:
        print(str(index) + ". " + dept)
        index += 1
def select_Department():
    if not Departments:
        print("No departments available to choose from.\n")
        return

    view_Departments()

    while True:
        try:
            choice = int(input("\nSelect a department number: "))
            index = choice - 1

            if index >= 0 and index < len(Departments):
                selected = Departments.pop(index)
                selected_departments.append(selected)

                print("\nYou have successfully selected: " + selected)
                print("Your selected department(s):", selected_departments)
                return
            else:
                print("Invalid department number. Please try again.")
        except:
            print("Please enter a valid number.")
def main():
    candidate_name = None
    candidate_age = None
    qualification_verified = False

    while True:
        print("\n CRUX Chatbot")
        print("1. Enter Candidate Name")
        print("2. Enter Candidate Age")
        print("3. Enter Candidate Qualification")
        print("4. View Available Departments")
        print("5. Select Department")
        print("6. Exit")
        option = input("Please choose an option (1-6): ")

        if option == "1":
            candidate_name = candidate_name()
        elif option == "2":
            candidate_age = candidate_age()
        elif option == "3":
            status, qual_name, qual_code = candidate_qualification()
            if status:
                qualification_verified = True
                print("Qualification:", qual_name, "| Code:", qual_code)
        elif option == "4":
            view_Departments()
        elif option == "5":
            select_Department()
        elif option == "6":
            print("\nThank you for using the CRUX Recruitment Chatbot!")
            print("We are always available when you need us.")
            break
    else:
            print("error")
if __name__ == "__main__":
    main()
