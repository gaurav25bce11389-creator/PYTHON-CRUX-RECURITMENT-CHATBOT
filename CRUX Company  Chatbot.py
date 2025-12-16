# CRUX Company recuritment chatbot
Department=["Data analyst","IT coordinator","Cybersecurity specialist","Backend developer","Support specialist",
            "Cloud engineer","Fullstack developer","Project manager","DevOps engineer","Help Desk Analyst"]

Selected_Department=[]

print("Hello\n","Welcome to CRUX recuritment chat\n")

def Candidate_name():
    Name=input("Enter the name of candidate:")
    print("Hello",Name)
if not Candidate_name:
    print("Name cannot be empty")
def Candidate_age():
    Age=int(input("Enter age of candidate:"))
    if Age >=25:
        print("You are eligible to apply in this company")
    else:
        print("Your age is not as per the company policy")
def Candidate_qualification(user_input):
    qualification_map={
        "Btech AI/ML":"01",
        "Btech CLOUD COMPUTING":"02",
        "Btech cybersecurity":"03",
        "Btech CSE":"04"
    }
    user_input=input("Enter your qualification:").strip().upper
    if user_input in qualification_map:
        print("Qualification recognized!")
        return True,qualification_map[user_input]
    else:
        print("Sorry! The entered qualification is not recognined.")
        return False,None
def Check_Department():
    list(Department,"Available department for recuritment")
def select_Department():
    if not Department:
        print("No Department is available.\n")
        return
    try:
        selection = int(input("Select Department number:"))
    except:
        print("Invalid input. Please enter a number.\n")
        return
    Department_index = selection - 1
    if 0 <= Department_index < len(Department):
        item_to_borrow = Department.pop(Department_index)
        
        Selected_Department.append(item_to_borrow)
        print("Department selected.\n")
    else:
        print("That Department number does not match any available Department.\n")
def main():
    while True:
        print(" CRUX company catbot")
        print("1.Candidate_name")
        print("2.Candidate_age")
        print("3.Candidate_qualification")
        print("4.Check Department")
        print("5.Select Department")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            Candidate_name()
        elif choice == "2":
            Candidate_age()
        elif choice == "3":
            Candidate_qualification('user_input')
        elif choice == "4":
            Check_Department()
        elif choice == "5":
            list(select_Department, "Selected position")
        elif choice == "6":
            print("\nThank you!.")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()
print("Always available in need")