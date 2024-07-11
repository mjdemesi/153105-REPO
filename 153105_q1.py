# Patient management system

def add_patient(patients):
    """Adds a new patient to the list."""
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}
    patients.append(patient)
    print(f"Patient {name} added successfully.\n")

def display_patients(patients):
    """Displays all patients."""
    if not patients:
        print("No patients to display.\n")
        return
    for patient in patients:
        print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
    print()

def search_patient(patients):
    """Searches for a patient by name and displays their details if found."""
    name = input("Enter patient's name to search: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            print(f"Found patient: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            return
    print(f"No patient found with the name {name}.\n")

def remove_patient(patients):
    """Removes a patient by name."""
    name = input("Enter patient's name to remove: ")
    for patient in patients:
        if patient['name'].lower() == name.lower():
            patients.remove(patient)
            print(f"Patient {name} removed successfully.\n")
            return
    print(f"No patient found with the name {name}.\n")

def main():
    patients = []
    while True:
        print("Hospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            search_patient(patients)
        elif choice == '4':
            remove_patient(patients)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
