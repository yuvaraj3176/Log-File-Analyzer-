# 🚀 Log File Analyzer – Flask Web Application

A **Flask-based Log File Analyzer** designed for IT Operations automation.  
This application processes large server log files, identifies HTTP errors, generates actionable insights, and visualizes error distributions using charts.

---

## 📌 Project Overview

In large-scale IT infrastructures, servers generate massive log files daily.  
Manually analyzing these logs is time-consuming and error-prone.

This project automates log analysis by:
- Parsing large log files efficiently
- Detecting and counting HTTP error codes
- Identifying top IP addresses causing errors
- Generating visual reports through a web interface

---

## 🛠 Tech Stack

- **Backend:** Python, Flask  
- **Data Processing:** Pandas  
- **Visualization:** Matplotlib  
- **Frontend:** HTML5, CSS3 (animated UI)  
- **Logging:** Python `logging` module  
- **Version Control:** Git & GitHub  

---

## ✨ Features

✔ Handles large log files (50,000+ lines)  
✔ Gracefully skips malformed or corrupted log entries  
✔ Counts HTTP error codes (404, 500, 403, etc.)  
✔ Displays top 5 IP addresses generating errors  
✔ Generates error distribution charts  
✔ Auto-opens web app URL in browser  
✔ Clean, responsive, animated dashboard UI  
✔ Modular and maintainable code structure  


yaml
Copy code

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
bash
git clone https://github.com/yuvaraj3176/Log-File-Analyzer-.git
cd Log-File-Analyzer-
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy code
python app.py
✔ The application URL will be printed in the terminal
✔ Browser opens automatically at:

cpp
Copy code
http://127.0.0.1:5000/
📊 Application Workflow
User clicks Start Log Analysis

Log file is generated (if not present)

Logs are parsed using Regular Expressions

Errors are filtered and aggregated using Pandas

Charts are generated using Matplotlib

Results are displayed on a dashboard UI

🧪 Error Handling & Reliability
Malformed log entries are skipped safely

Application never crashes due to bad data

All execution details are logged for auditing

Charts are generated only when valid error data exists

🎓 Learning Outcomes
Parsing and analyzing large files in Python

Using regular expressions for pattern matching

Applying Pandas for data aggregation

Creating visualizations with Matplotlib

Implementing exception handling

Building modular Flask applications

Applying logging for debugging and monitoring


<img width="1920" height="1080" alt="Screenshot 2026-01-22 160220" src="https://github.com/user-attachments/assets/7166272f-d842-4969-b00b-f4daf608ab2b" />

<img width="1920" height="1080" alt="Screenshot 2026-01-22 160248" src="https://github.com/user-attachments/assets/8b74046c-926b-4ff0-8415-4d07e80a24f5" />

<img width="1920" height="1080" alt="Screenshot 2026-01-22 160311" src="https://github.com/user-attachments/assets/dfba603b-bf16-4ed4-aa34-c056302638fd" />

<img width="1920" height="1080" alt="Screenshot 2026-01-22 160332" src="https://github.com/user-attachments/assets/0c1d1d0c-1734-4409-b549-9090287337af" />
