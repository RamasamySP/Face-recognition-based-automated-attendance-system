from cgi import print_arguments
from fileinput import filename
from tkinter import messagebox, ttk
from tkinter import*
from PIL import Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class mail_attendance :
    def __init__(self,root) :
        self.root = root
        self.root.geometry("1530x820+0+0")
        self.root.title("Mail")

        img = Image.open(r"images\back.jpg")
        img = img.resize((1530, 820), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x = 0, y = 0, width = 1530, height = 820)
        title_lbl = Label(bg_img, text = "Mailing Attendance ", font=("times new roman",35, "bold" ), bg = "navyblue", fg = "white")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 50 )

        self.email = StringVar()
        self.subject = StringVar()

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x = 500, y = 245, width = 530, height = 330)

        mail_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text = "Send Attendance ", font=("times new roman", 12, "bold"))
        mail_frame.place(x = 7, y = 10, width=500, height= 300)

        # Subject
        subject_label = Label(mail_frame, text="Subject :", font=("times new roman", 12, "bold"))
        subject_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        subject_entry = ttk.Entry(mail_frame, textvariable=self.subject,width=40, font=("times new roman", 12, "bold"))
        subject_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Email entry
        email_label = Label(mail_frame, text="Email id :", font=("times new roman", 12, "bold"))
        email_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(mail_frame, textvariable=self.email,width=40, font=("times new roman", 12, "bold"))
        email_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Buttons frame
        btn_frame = Frame(mail_frame, bd=2, relief=RIDGE)
        btn_frame.place(x = 150, y = 200, width=170, height=35)

        send_btn = Button(btn_frame, text="Send", command=self.send_email, width=18, font=("times new roman", 12, "bold"), bg = "navyblue", fg ="white")
        send_btn.grid(row=0, column=0)


    def send_email(self):
        try :
            fromaddr = "spramasamy2@gmail.com"
            toaddr = self.email.get()
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = self.subject.get()    
            filename = "attendance.csv"
            attachment = open(r"C:\Users\spram\Desktop\Face Recognition based automated Attendance system\attendance.csv", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
            msg.attach(p)

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr, "---- ---- ---- ----")
            text = msg.as_string()
            s.sendmail(fromaddr, toaddr, text)
            s.quit()
            messagebox.showinfo("Success","Email Sent Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)
            

            


if __name__ == "__main__" :
    root = Tk()
    obj = mail_attendance(root)
    root.mainloop()
