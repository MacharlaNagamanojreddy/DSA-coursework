#Attendance tracker program 

def add_attendance(attendance_records, name, date, status):
    if name not in attendance_records:
        attendance_records[name] = {}
    attendance_records[name][date] = status

def view_attendance(attendance_records):
    if not attendance_records:
        print("No attendance records found.")
    else:
        print("Attendance Records:")
        for name, records in attendance_records.items():
            print(f"{name}:")
            for date, status in records.items():
                print(f"  {date}: {status}")

def main():
    attendance_records = {}
    while True:
        print("\nAttendance Tracker")
        print("1. Add Attendance")
        print("2. View Attendance")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            status = input("Enter attendance status (Present/Absent): ")
            add_attendance(attendance_records, name, date, status)
            print("Attendance record added.")
        elif choice == '2':
            view_attendance(attendance_records)
        elif choice == '3':
            print("Exiting Attendance Tracker.")
            break
        else:
            print("Invalid option. Please try again.")
main()  