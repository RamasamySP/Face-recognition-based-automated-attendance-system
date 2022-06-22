from asyncore import read
from multiprocessing import allow_connection_pickling
from sqlite3 import Cursor
from sre_parse import State
from tkinter import*
from tkinter import ttk
from tkinter.tix import Select
from turtle import update, width, window_width
from PIL import Image, ImageTk
from click import command
from matplotlib.pyplot import text
from numpy import pad
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x820+0+0")
        self.root.title("Deep Learning Based Automated Attendence System")

        #**********Variables***************
        self.var_dep = StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
     

        #Background
        img3 = Image.open(r"images\back.jpg")
        img3 = img3.resize((1530,820), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 0, width = 1530, height = 820)

        title_lbl = Label(bg_img, text = "Student Register System", font=("times new roman",35, "bold" ), bg = "navyblue", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 50 )

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x = 10, y = 60, width = 1500, height = 600)

        #Left label Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text = "Student Information", font=("times new roman", 12, "bold"))
        Left_frame.place(x = 5, y = 10, width=730, height=570)


        #Current Course
        current_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text = "Student Register Form", font=("times new roman", 12, "bold"))
        current_frame.place(x = 5, y = 20, width=720, height=150)

        # Department 
        dep_label = Label(current_frame, text = "Department", font=("times new roman", 12, "bold"))
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(current_frame, textvariable=self.var_dep,font=("times new roman", 12, "bold"),state="readonly", width=17)
        dep_combo["values"] = ("Select Department", "CSE", "ECE", "EEE", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)     

        # Course 
        course_label = Label(current_frame, text = "Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_frame, textvariable=self.var_course,font=("times new roman", 12, "bold"), state="readonly", width=17)
        course_combo["values"] = ("Select Course", "BE", "B.tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2,pady=10,sticky=W)

        #Year
        year_label = Label(current_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo=ttk.Combobox(current_frame, textvariable=self.var_year,font=("times new roman", 12, "bold"), state="readonly", width=17)
        year_combo["values"]=("Select Year", "2018-22", "2019-23", "2020-24", "2021-25")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)


        # Semester
        semester_label = Label(current_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_frame, textvariable=self.var_semester,font=("times new roman", 12, "bold"), state="readonly", width=17)
        semester_combo["values"]=("Select Semester", "Odd-Semester", "Even-Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text = "Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x = 5, y = 210, width=720, height=300)

        #Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 12, "bold"))
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.va_std_id,width=20, font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 12, "bold"))
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name,width=20, font=("times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Section:", font=("times new roman", 12, "bold"))
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        #class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div,width = 20, font=("times new roman", 12, "bold"))
        #class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        div_combo=ttk.Combobox(class_student_frame, textvariable=self.var_div,font=("times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"]=("Select Division", "A", "B")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 12, "bold"))
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll,width=20, font=("times new roman", 12, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"))
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        #gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender,width=20, font=("times new roman", 12, "bold"))
        #gender_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        gender_combo=ttk.Combobox(class_student_frame, textvariable=self.var_gender,font=("times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"]=("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)


        # DOB
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 12, "bold"))
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob,width=20, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 12, "bold"))
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email,width=20, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone_no
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 12, "bold"))
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone,width=20, font=("times new roman", 12, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 12, "bold"))
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address,width=20, font=("times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher
        Teacher_label = Label(class_student_frame, text="Teacher's Name:", font=("times new roman", 12, "bold"))
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher,width=20, font=("times new roman", 12, "bold"))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        self.var_radio1=StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1 ,text="Photo Sample collected", value="Yes")
        radiobtn1.grid(row=5, column=0)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # Buttons frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x = 0, y = 200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save",command=self.add_data ,width=18, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data,width=19, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=19, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,width=19, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x = 0, y = 235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo Sample", command=self.generate_dataset,width=38, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=39, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        update_photo_btn.grid(row=0, column=1)     
           


        #Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text = "Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x = 750, y = 10, width=720, height=580)


        #------------Searching System---------------------
        search_frame = LabelFrame(Right_frame, bd=2, relief=RIDGE, text = "Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x = 5, y = 25, width=710, height=70)

        search_label = Label(search_frame, text = "Search By:", font=("times new roman", 15, "bold"), bg = "black", fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"]=("Select", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        search_btn.grid(row=0, column=3, padx=4)

        showall_btn = Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        showall_btn.grid(row=0, column=4)


        # Table Frame
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x = 5, y = 180, width=710, height=325)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "roll", "div", "gender" ,"dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll NO")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


#****************Function declaration****************

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.va_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get() ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Saved Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)


#******************Fetch Data*******************
    def fetch_data(self):
        conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


#*******************Update data***************
    def get_cursor(self, event="") :
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]), self.var_course.set(data[1]), self.var_year.set(data[2]), self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]), self.var_std_name.set(data[5]), self.var_div.set(data[6]), self.var_roll.set(data[7]), self.var_gender.set(data[8]),
        self.var_dob.set(data[9]), self.var_email.set(data[10]), self.var_phone.set(data[11]), self.var_address.set(data[12]), self.var_teacher.set(data[13]), self.var_radio1.set(data[14])


#*******************Update Function********************
    def update_data(self) :
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        else :
            try :
                Update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if Update > 0 :
                    conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.va_std_id.get() ))
                else :
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Details updated succesfully!", parent= self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            
#****************Delete Function********************        
    def delete_data(self) :
        if self.va_std_id.get() == "" :
            messagebox.showerror("Error", "Student ID is Required!", parent=self.root)
        else :
            try :
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student's details?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.va_std_id.get(),)
                    my_cursor.execute(sql, val)
                else :
                    if not delete :
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Student Details deleted successfully", parent = self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            
        
#*******************Reset Function***************
    def reset_data(self) :
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


#*************************Generate data set, Take Photo Sample*******************************
    def generate_dataset(self) :
        if self.var_dep.get() == "Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required", parent=self.root)
        else :
            try :
                conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult :
                    id += 1
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_div.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get(), self.va_std_id.get()==id+1 ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #****************Load Predefined data on face frontals from opencv*************************

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img) :
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    #Scaling Factor = 1.3, Minimum Neighbor = 5

                    for (x,y,w,h) in faces :
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None :
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." +str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100 :
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generation of Dataset Completed!")

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)



if __name__ == "__main__" :
    root = Tk()
    obj = Student(root)
    root.mainloop()