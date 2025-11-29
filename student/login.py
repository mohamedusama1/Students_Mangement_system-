from customtkinter import *
from tkinter import *
from PIL import Image
from tkinter import messagebox
import sqlite3

class LoginClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1100x600+100+50")
        self.root.title("Login")
        self.root.configure(background="#F2E6FF")
        self.root.resizable(width=False, height=False)
        ########switch fr###############
        login_frame = CTkFrame(root,width=1080,height=550,fg_color="#FFFFFF",bg_color='gray')
        sign_up_frame = CTkFrame(root,width=1080,height=550,fg_color="#FFFFFF",bg_color='gray')

        for frame in (login_frame,sign_up_frame):
            frame.place(x=10,y=20)

        def show_frame(frame):
            frame.tkraise()
        show_frame(login_frame)
        ############LOGO##############
        img = CTkImage(Image.open('images/login.png'), size=(490, 400))
        img_lbl = CTkLabel(login_frame,text='',image=img,fg_color="#F6F2FF")  # ← تعديل قيمة فقط
        img_lbl.place(x=10,y=70)

        ###########frame###############
        frame = CTkFrame(
            login_frame,
            width=520,
            height=500,
            fg_color="#FBF6FF",
            bg_color='gray',
            border_width=2,
            corner_radius=30,
            border_color="#C9A8FF"
        )
        frame.place(x=520,y=20)
        up_text_lbl = CTkLabel(
            frame,
            text='Login Page',
            corner_radius=10,
            fg_color="#FBF6FF",
            width=200,
            height=30,
            text_color="#4A3A6A",
            font=('arial', 20, 'bold')
        )

        up_text_lbl.place(x=160,y=50)
        lbl = CTkLabel(
            frame,
            text='Login To Continue',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 18, 'bold')

        )
        lbl.place(x=30,y=110)
        labl = CTkLabel(
            frame,
            text='Not a Member?',
            width=150,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')

        )
        labl.place(x=30, y=150)
        ################label&Entry#############
        lbl_user = CTkLabel(
            frame,
            text='Enter Your Username',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_user.place(x=25, y=200)
        user_en = CTkEntry(
            frame,
            width=350,
            height=35,
            font=('carier', 14, 'bold'),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        user_en.place(x=50, y=230)
        lbl_pass = CTkLabel(
            frame,
            text='Enter Your Password',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_pass.place(x=25, y=280)
        pass_en = CTkEntry(
            frame,
            width=350,
            height=35,
            font=('carier', 14, 'bold'),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        pass_en.place(x=50, y=310)
        #########buttons########
        forgot_pass_btn = CTkButton(
            frame,
            text='Forgot Password',
            width=150,
            height=20,
            fg_color="transparent",
            font=('arial', 14, 'bold'),
            text_color="#4A3A6A",
            bg_color="transparent",
            hover_color="#E7D6FF",
            command=lambda:forget_password()
        )
        forgot_pass_btn.place(x=150, y=360)
        sign_up_btn = CTkButton(
            frame,
            text='Sign Up Page',
            width=100,
            height=20,
            fg_color="transparent",
            font=('arial', 16, 'bold'),
            text_color="#4A3A6A",
            bg_color="transparent",
            hover_color="#E7D6FF",
            command=lambda: show_frame(sign_up_frame)
        )
        sign_up_btn.place(x=160, y=150)
        login_btn = CTkButton(
            frame,
            text='Login',
            width=150,
            height=20,
            fg_color="transparent",
            font=('arial', 16, 'bold'),
            text_color="#4A3A6A",
            bg_color="transparent",
            hover_color="#E7D6FF",
            border_color="#C9A8FF",
            border_width=2,
            corner_radius=20,
            border_spacing=20
        )
        login_btn.place(x=155, y=400)
        ########### forget password page #########
        def forget_password():
            win = Toplevel()
            win.geometry("400x400+680+150")
            win.title("Forget Password")
            win.config(bg='#F2E6FF')
            win.resizable(width=False, height=False)
            #########label & entry #############
            lbl_up = CTkLabel(
                win,
                text='Update Your Password',
                width=200,
                height=25,
                text_color="#4A3A6A",
                font=('arial', 16, 'bold')

            )
            lbl_up.place(x=50, y=70)
            lbl_username = CTkLabel(
                win,
                text='Enter the Username',

                height=25,
                text_color="#4A3A6A",
                font=('arial', 14)

            )
            lbl_username.place(x=50, y=110)
            username_en = CTkEntry(
                win,
                width=300,
                height=35,
                font=('arial', 14),
                border_width=1,
                border_color="#B49AF2",

            )
            username_en.place(x=50, y=140)


            lbl_pass = CTkLabel(
                win,
                text='Enter the New Password',

                height=25,
                text_color="#4A3A6A",
                font=('arial', 14)

            )
            lbl_pass.place(x=50, y=180)
            pass_en = CTkEntry(
                win,
                width=300,
                height=35,
                font=('arial', 14),
                border_width=1,
                border_color="#B49AF2",

            )
            pass_en.place(x=50, y=210)
            update_pass_btn = CTkButton(
                win,
                text='Update Password',
                width=180,
                height=10,
                fg_color="transparent",
                font=('arial', 14, 'bold'),
                text_color="#4A3A6A",
                bg_color="transparent",
                hover_color="#E7D6FF",
                border_color="#C9A8FF",
                border_width=2,
                corner_radius=20,
                border_spacing=15
            )
            update_pass_btn.place(x=110, y=270)

        ################ sign up page #################
        ############### VARIABLES ##############
        name = StringVar()
        username = StringVar()
        password = StringVar()
        confirm_password = StringVar()

        def rec_id():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute('''
            WITH RECURSIVE cte AS (
            SELECT ROW_NUMBER() OVER (ORDER BY ID) AS new_id, ID
            FROM Account
            )
            UPDATE Account
                         SET ID = (SELECT new_id FROM cte WHERE cte.ID = Account.ID)

            ''')

        def clear():
            name.set('')
            username.set('')
            password.set('')
            confirm_password.set('')

        ##########################
        def sign_up():
            if  name.get() == '' or username.get() == '' or password.get() == '' or confirm_password.get() == '':
                messagebox.showerror('error','please fill all fields')
            elif password.get() != confirm_password.get():
                messagebox.showerror('error','passwords do not match')
            else:
                try:
                    con = sqlite3.connect('school.db')
                    cur = con.cursor()
                    cur.execute('INSERT INTO Account(name,username,password) VALUES(?,?,?)',
                                (name.get(),username.get(),password.get()) )
                    con.commit()
                    con.close()
                    rec_id()
                    messagebox.showinfo('success','account created successfully')
                    clear()
                except Exception as es:
                    messagebox.showerror('error','Something went wrong')


        ############ LOGO ############33
        img = CTkImage(Image.open('images/login.png'), size=(490, 400))
        img_lbl = CTkLabel(sign_up_frame,text='',image=img,fg_color="#F6F2FF")  # ← تعديل قيمة فقط
        img_lbl.place(x=10,y=70)
        ############## frame ##########
        signup_frame = CTkFrame(
            sign_up_frame,
            width=520,
            height=500,
            fg_color="#FBF6FF",
            bg_color='gray',
            border_width=2,
            corner_radius=30,
            border_color="#C9A8FF"
        )
        signup_frame.place(x=520,y=20)

        up_text_lbl = CTkLabel(
            signup_frame,
            text='Sign Up Page',
            corner_radius=10,
            fg_color="#FBF6FF",
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 20, 'bold')
        )
        up_text_lbl.place(x=150,y=20)



        lbl = CTkLabel(
            signup_frame,
            text='Create New User',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 16, 'bold')

        )
        lbl.place(x=20,y=65)
        labl = CTkLabel(
            signup_frame,
            text='Already a Member?',
            width=150,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')

        )
        labl.place(x=70, y=90)

        ############### Label + entry #############

        lbl_name = CTkLabel(
            signup_frame,
            text='Enter Your Name',
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_name.place(x=75, y=120)
        name_en = CTkEntry(
            signup_frame,
            textvariable=name,
            width=350,
            height=35,
            font=('carier', 14),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        name_en.place(x=75, y=150)



        lbl_user = CTkLabel(
            signup_frame,
            text='Enter Your Username',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_user.place(x=50, y=190)
        user_en = CTkEntry(
            signup_frame,
            textvariable=username,
            width=350,
            height=35,
            font=('carier', 14, 'bold'),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        user_en.place(x=75, y=220)

        lbl_pass = CTkLabel(
            signup_frame,
            text='Enter Your Password',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_pass.place(x=50, y=260)
        pass_en = CTkEntry(
            signup_frame,
            textvariable=password,
            width=350,
            height=35,
            font=('carier', 14, 'bold'),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        pass_en.place(x=75, y=290)


        lbl_confirm_pass = CTkLabel(
            signup_frame,
            text='Enter The Confirm Password',
            width=200,
            height=25,
            text_color="#4A3A6A",
            font=('arial', 14, 'bold')
        )
        lbl_confirm_pass.place(x=65, y=330)
        confirm_pass_en = CTkEntry(
            signup_frame,
            textvariable=confirm_password,
            width=350,
            height=35,
            font=('carier', 14, 'bold'),
            border_width=1,
            border_color="#B49AF2",
            justify="center"
        )
        confirm_pass_en.place(x=75, y=360)
        ############### buttons ##################3
        login_btn = CTkButton(
            signup_frame,
            text='Login Page',
            width=100,
            height=20,
            fg_color="transparent",
            font=('arial', 16, 'bold'),
            text_color="#4A3A6A",
            bg_color="transparent",
            hover_color="#E7D6FF",
            command=lambda: show_frame(login_frame)
        )
        login_btn.place(x=210, y=90)
        signup_btn = CTkButton(
            signup_frame,
            text='Sign Up',
            width=150,
            height=20,
            fg_color="transparent",
            font=('arial', 16, 'bold'),
            text_color="#4A3A6A",
            bg_color="transparent",
            hover_color="#E7D6FF",
            border_color="#C9A8FF",
            border_width=2,
            corner_radius=20,
            border_spacing=20,
            command=sign_up
        )
        signup_btn.place(x=155, y=410)
        #

if __name__ == "__main__":
    root = Tk()
    LoginClass(root)
    root.mainloop()
