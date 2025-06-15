import os

student_file = "students.txt"
timetable_file = "timetable.txt"

# 1. Add Student
def addstudent():
    print("\n")
    stname = input("Enter Student's Name: ")
    stRoll = input("Enter Roll Number: ")
    stcourse = input("Enter Student Course: ")
    stBatch = input("Enter Batch: ")

    with open(student_file, "a") as f:
        f.write(f"{stname},{stRoll},{stcourse},{stBatch}\n")

    print("✅ Student Record Created Successfully\n")

# 2. Update Student
def updatestudent():
    print("\n")
    searchRoll = input("Enter Roll no of student to update: ")

    newName = input("Enter New Name: ")
    newRoll = input("Enter New Roll Number: ")
    newCourse = input("Enter New Course: ")
    newBatch = input("Enter New Batch: ")

    if not os.path.exists(student_file):
        print("No student record found.")
        return

    updated_lines = []
    found = False

    with open(student_file, "r") as f:
        for line in f:
            stn, strol, stcour, stbat = line.strip().split(",")
            if strol == searchRoll:
                found = True
                updated_lines.append(f"{newName},{newRoll},{newCourse},{newBatch}\n")
            else:
                updated_lines.append(line)

    if not found:
        print("❌ Student not found.\n")
        return

    with open(student_file, "w") as f:
        f.writelines(updated_lines)

    print("✅ Student Record Updated Successfully\n")

# 3. View Students
def viewstudent():
    print("\n")
    if not os.path.exists(student_file):
        print("No student records found.")
        return

    print("{:<15} {:<10} {:<10} {:<10}".format("Name", "Roll No", "Course", "Batch"))
    print("-" * 50)
    with open(student_file, "r") as f:
        for line in f:
            stn, strol, stcour, stbat = line.strip().split(",")
            print(f"{stn:<15} {strol:<10} {stcour:<10} {stbat:<10}")
    print("\n")

# 4. Delete Student
def deletestudent():
    print("\n")
    searchRoll = input("Enter Roll no to delete record: ")

    if not os.path.exists(student_file):
        print("No student records found.")
        return

    updated_lines = []
    found = False

    with open(student_file, "r") as f:
        for line in f:
            stn, strol, stcour, stbat = line.strip().split(",")
            if strol == searchRoll:
                found = True
                print("✅ Student record deleted.\n")
                continue
            updated_lines.append(line)

    if not found:
        print("❌ Student not found.\n")
        return

    with open(student_file, "w") as f:
        f.writelines(updated_lines)

# 5. Create Timetable
def createTimetable():
    srno = input("Enter Serial Number: ")
    subj = input("Enter Subject Name: ")
    teac = input("Enter Teacher Name: ")
    letime = input("Enter Lecture Time: ")

    with open(timetable_file, "a") as f:
        f.write(f"{srno},{subj},{teac},{letime}\n")

    print("✅ Timetable Entry Created Successfully\n")

# 6. View Timetable
def timetableshow():
    print("\n")
    if not os.path.exists(timetable_file):
        print("No timetable file found.")
        return

    print("{:<10} {:<20} {:<15} {:<10}".format("Sr.No", "Subject", "Teacher", "Time"))
    print("-" * 60)
    with open(timetable_file, "r") as f:
        for line in f:
            srn, sub, tea, let = line.strip().split(",")
            print(f"{srn:<10} {sub:<20} {tea:<15} {let:<10}")
    print("\n")

# Main Menu
while True:
    print("🧑‍🎓 Welcome to College Management System")
    print("1️⃣  Add Student Record")
    print("2️⃣  Update Student Record")
    print("3️⃣  View Student Record")
    print("4️⃣  Delete Student Record")
    print("5️⃣  Create Timetable")
    print("6️⃣  View Timetable")
    print("7️⃣  Exit")

    choice = input("Enter Option: ")

    if choice == "1":
        addstudent()
    elif choice == "2":
        updatestudent()
    elif choice == "3":
        viewstudent()
    elif choice == "4":
        deletestudent()
    elif choice == "5":
        createTimetable()
    elif choice == "6":
        timetableshow()
    elif choice == "7":
        print("👋 Thank You! Exiting...")
        break
    else:
        print("❌ Invalid Option. Try again.\n")
