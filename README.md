# 🎓 College Management System (Python CLI Project)

A simple yet functional **College Management System** built in **Python**, designed to manage student records and class timetables efficiently through a command-line interface. Data is stored in a plain text file, making it beginner-friendly and portable.

---

## 📌 Features

- ✅ Add Student Records  
- ✏️ Update Student Information  
- 🔍 View All Students  
- ❌ Delete Student Data  
- 🗓️ Create & View Timetable  
- 💾 Text-based persistent storage  
- 👨‍💻 Easy to modify and extend  

---

## 💡 Technologies Used

- **Python 3.x**
- **Text File Storage** (`details.txt`)
- No external libraries required

---

## 🛠️ How to Use

### 1. 🔄 Clone the Repository

```bash
git clone https://github.com/Ajuu1801/College-Management-System.git
cd College-Management-System
```

### 2. ▶️ Run the Application

```bash
python college_system.py
```

---

## 📂 Project Structure

```
College-Management-System/
│
├── college_system.py        # Main application logic
├── details.txt              # Data file (auto-created if not present)
├── README.md                # Documentation (you are reading it!)
```

---

## 🖼️ Example Usage

### 🧑 Add Student
```
Enter Students Name: Aditi
Enter Roll Number: 102
Enter Student Course: BCA
Enter Batch: 2024
✅ Account Created Successfully
```

### 🗓️ Add Timetable
```
Enter Serial Number: 1
Enter Subject Name: Python
Enter Teacher Name: Mr. Sharma
Enter Lecture Time: 10:00AM
✅ Timetable created successfully
```

### 📋 View Timetable
```
Serial No    Subject                 Teacher         Lecture Time
--------------------------------------------------------------
1            Python Programming      Mr. Sharma      10:00AM
```

---

## 📁 Data Format (in `details.txt`)

Each line stores either student info or timetable:

### 👨‍🎓 Student Format:
```
<name>,<roll_number>,<course>,<batch>
```
Example:
```
Rahul,101,BCA,2024
```

### 🗓️ Timetable Format:
```
<serial>,<subject>,<teacher>,<lecture_time>
```
Example:
```
1,Python,Mr. Sharma,10:00AM
```

> 💡 You can optionally separate student and timetable data into different files (e.g., `students.txt`, `timetable.txt`) for cleaner handling.

---

## 🔍 Main Menu Options

| Option | Description                    |
|--------|--------------------------------|
| 1      | Add Student Record             |
| 2      | Update Student Record          |
| 3      | View Student Record            |
| 4      | Delete Student Record          |
| 5      | Create TimeTable               |
| 6      | Display TimeTable              |
| 7      | Update TimeTable *(Coming Soon)* |
| 8      | Exit Program                   |

---

## 📈 Future Enhancements

- 🔐 Admin Login Authentication
- 💳 Fees Management System
- 🧠 Search and Filter Options
- 🖼️ GUI using Tkinter / PyQt
- 📊 Generate Reports in CSV / PDF
- 🗄️ Migrate to MySQL / SQLite for large datasets

---

## 🤝 Contributing

Contributions are welcome!

- 📩 Fork the repo
- 🛠️ Create your feature branch
- 📤 Commit your changes
- 📥 Submit a pull request

---

## 👨‍💻 Author

Developed with ❤️ by [Ajay Gawas](https://github.com/Ajuu1801)

📫 **Contact**: *ajaygawasc@gmail.com*

---

## 🪪 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for more information.

---

## 🙌 Support

If this project helped you, leave a ⭐ star on GitHub.  
Thank you for using the College Management System!

