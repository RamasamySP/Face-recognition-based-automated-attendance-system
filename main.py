from importlib.util import set_loader
from tkinter import*
from tkinter import ttk
from turtle import width
from PIL import Image, ImageTk
from student import Student
import os
from attendance import Attendance
import cv2
from unicodedata import name
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
from mail import mail_attendance

class Face_reco:
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x820+0+0")
        self.root.title("Face Recognition Based Automated Attendence System")
        
        
        #Background
        img3 = Image.open(r"images\back_1.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 0, width = 1530, height = 820)

        title_lbl = Label(bg_img, text = "Face Recognition Based Automated Attendance System", font=("times new roman",35, "bold" ), bg = "navyblue", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 50 )

        #Student Register button
        img4 = Image.open(r"images\student.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image = self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x = 200, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Student Register", command=self.student_details,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 200, y = 300, width = 220, height = 40)

        #Face Detection button
        img5 = Image.open(r"images\face_detection.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image = self.photoimg5, command= self.face_recognition, cursor="hand2")
        b1.place(x = 600, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Face Detection", command= self.face_recognition,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 600, y = 300, width = 220, height = 40)

        #Attendance button
        img6 = Image.open(r"images\attendance.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image = self.photoimg6, cursor="hand2", command=self.attendace_data)
        b1.place(x = 1000, y = 100, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Attendance", command=self.attendace_data,cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 1000, y = 300, width = 220, height = 40)

        
        #Train Face button
        img8 = Image.open(r"images\train.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image = self.photoimg8, command=self.train_classifier, cursor="hand2")
        b1.place(x = 200, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Train Data", command=self.train_classifier, cursor="hand2", font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 200, y = 580, width = 220, height = 40)

        #Photos button
        img9 = Image.open(r"images\photoimg.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image = self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x = 600, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Photo", cursor="hand2", command=self.open_img,font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 600, y = 580, width = 220, height = 40)


        #Mail button
        img11 = Image.open(r"images\mail.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image = self.photoimg11, cursor="hand2", command=self.mailing)
        b1.place(x = 1000, y = 380, width = 220, height = 220)

        b_1 = Button(bg_img, text = "Mail", cursor="hand2", command=self.mailing, font=("times new roman",15, "bold" ), bg = "darkblue", fg = "white")
        b_1.place(x = 1000, y = 580, width = 220, height = 40)

    def open_img(self) :
        os.startfile("data")

    #********************** Functions buttons*********************
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)



    def attendace_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window) 

    def mailing(self) :
        self.new_window = Toplevel(self.root)
        self.app = mail_attendance(self.new_window)

    def train_classifier(self) :
        data_dir = ('data')
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path :
            img = Image.open(image).convert('L')  #Gray scale image
            imageNp=np.array(img, 'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        #************** Train the Classifier and Save ****************************
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Completed!")




        #*****************Attendance*************************
    def mark_attendance(self, i, r, n, d) :
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList :
                entry = line.split((",")) 
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)) :
                now = datetime.now()
                d1 = now.strftime("%d-%m-%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


    #*****************Face Recognition **********************

    def face_recognition(self) :
        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf) :
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord = []
            for(x,y,w,h) in features  :
                cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0), 3)
                id,predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100* (1-predict/300)))

                conn = mysql.connector.connect(host = "localhost", username="root", password="ram",database="face_recognization")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=" +str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Roll from student where Student_id=" +str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dep from student where Student_id=" +str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=" +str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)


                if confidence > 77 :
                    cv2.putText(img, f"ID:{i}",(x,y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Roll:{r}",(x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Name:{n}",(x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    cv2.putText(img, f"Department:{d}",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    self.mark_attendance(i,r,n,d)
                else :
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown Face",(x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    coord=[x,y,w,y]
            return coord
            
        def recognize(img, clf, faceCascade) :
            coord=draw_boundary(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True :
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__" :
    root = Tk()
    obj = Face_reco(root)
    root.mainloop()