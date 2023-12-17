import tkinter as tk
import mysql.connector


class Page1(tk.Frame):
    def __init__(self, root, show_main_menu):
        super().__init__(root, width=400, height=300)
        label = tk.Label(self, text="Page 1", font=('Helvetica', 18))
        label.pack(pady=20)

        back_button = tk.Button(self, text="Back to Main Menu", command=show_main_menu)
        back_button.pack(pady=10)



def insert_data():
    name = name_entry.get()
    matric_no = matric_entry.get()
    semester = semester_entry.get()

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="your_username",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="your_database"  # Replace with your database name
    )

    mycursor = mydb.cursor()

    # Insert data into the table
    sql = "INSERT INTO students (name, matric_no, semester) VALUES (%s, %s, %s)"
    val = (name, matric_no, semester)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    # Clear the entry fields after insertion
    name_entry.delete(0, tk.END)
    matric_entry.delete(0, tk.END)
    semester_entry.delete(0, tk.END)

    mycursor.close()
    mydb.close()

frame = tk.Frame(Page1)
frame.pack(padx=20, pady=20)

# Labels and Entry fields
tk.Label(frame, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Matric No:").grid(row=1, column=0)
matric_entry = tk.Entry(frame)
matric_entry.grid(row=1, column=1)

tk.Label(frame, text="Semester:").grid(row=2, column=0)
semester_entry = tk.Entry(frame)
semester_entry.grid(row=2, column=1)

# Submit button
submit_button = tk.Button(frame, text="Submit", command=insert_data)
submit_button.grid(row=3, columnspan=2, pady=10)

Page1.mainloop()