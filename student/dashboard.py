from customtkinter import *
from tkinter import *
from PIL import Image,ImageOps
from time import strftime
import adminpage
import studentspage


class DashboardClass():
    def __init__(self,root):
        self.root = root
        self.root.geometry('1200x690+100+5')
        self.root.title('Dashboard Page')
        self.root.config(bg='#F9F5FF')
        self.root.resizable(False,False)
        def date():
            date_1 = strftime('%I:%M:%S %p \t %A \t %b/%d/%Y')
            date_lbl.config(text=date_1)
            date_lbl.after(1000,date)
        ##############COLOR###########3
        def get_colored_icon(path, size, color):
            img = Image.open(path).convert("RGBA")
            colored_image = Image.new("RGBA", img.size, color)
            colored_image.putalpha(img.getchannel("A"))
            return CTkImage(colored_image, size=size)

        ################### Up Frame ######################
        frame = CTkFrame(
            root,
            width=1197,
            height=615,
            bg_color='#F9F5FF',
            fg_color='#FFFFFF',
            border_color='#CBB3FF',
            border_width=2
        )
        frame.place(x=1, y=72)

        menu_frame = CTkFrame(
            frame,
            width=200,
            height=608,
            fg_color='#F6F0FF',
            bg_color='#FFFFFF',
            border_color='#CBB3FF',
            border_width=2
        )
        menu_frame.place(x=3, y=3)

        def hide_line():
            home_line.config(bg="#EBDFFF")
            note_line.config(bg="#EBDFFF")
            ser_line.config(bg="#EBDFFF")
            stat_line.config(bg="#EBDFFF")

        def delete_pages():
            for frame in page_frame.winfo_children():
                frame.destroy()

        def line(lb,page):
            hide_line()
            lb.config(bg="#6A4FBF")
            delete_pages()
            page()

        ###################### Buttons ###################3
        icon_color = "#4A2E8C"

        # --- HOME ---
        home_img = get_colored_icon('images/home_icon.png', size=(38, 38), color=icon_color)
        self.home_btn = CTkButton(
            menu_frame,
            text='HOME',
            width=180,
            height=50,
            fg_color='#FFFFFF',
            bg_color='#F6F0FF',
            font=('Arial', 20, 'bold'),
            border_color='#CBB3FF',
            border_width=2,
            border_spacing=10,
            hover_color='#F0E8FF',
            image=home_img,
            corner_radius=8,
            text_color=icon_color,
            command=lambda:line(lb=home_line,page=home_page)
        )
        self.home_btn.place(x=15, y=100)

        home_line = Label(menu_frame, text='', bg=icon_color)
        home_line.place(x=3, y=105, width=6, height=40)

        # --- NOTE ---
        note_img = get_colored_icon('images/note.png', size=(42, 42), color=icon_color)
        self.note_btn = CTkButton(
            menu_frame,
            text='NOTE',
            width=180,
            height=50,
            fg_color='#FFFFFF',
            bg_color='#F6F0FF',
            font=('Arial', 20, 'bold'),
            border_color='#CBB3FF',
            border_width=2,
            border_spacing=10,
            hover_color='#F0E8FF',
            image=note_img,
            corner_radius=8,
            text_color=icon_color,
            command=lambda:line(lb=note_line,page=note_page)
        )
        self.note_btn.place(x=15, y=180)

        note_line = Label(menu_frame, text='', bg="#EBDFFF")
        note_line.place(x=3, y=185, width=6, height=40)

        # --- SERVICES ---
        ser_img = get_colored_icon('images/services_icon.png', size=(38, 38), color=icon_color)
        self.ser_btn = CTkButton(
            menu_frame,
            text='SERVICES',
            width=180,
            height=50,
            fg_color='#FFFFFF',
            bg_color='#F6F0FF',
            font=('Arial', 20, 'bold'),
            border_color='#CBB3FF',
            border_width=2,
            border_spacing=10,
            hover_color='#F0E8FF',
            image=ser_img,
            corner_radius=8,
            text_color=icon_color,
            command=lambda: line(lb=ser_line,page=ser_page)
        )
        self.ser_btn.place(x=15, y=260)

        ser_line = Label(menu_frame, text='', bg="#EBDFFF")
        ser_line.place(x=3, y=265, width=6, height=40)

        # --- STATISTICS ---
        stat_img = get_colored_icon('images/ll.png', size=(40, 40), color=icon_color)
        self.stat_btn = CTkButton(
            menu_frame,
            text='STATISTICS',
            width=180,
            height=50,
            fg_color='#FFFFFF',
            bg_color='#F6F0FF',
            font=('Arial', 20, 'bold'),
            border_color='#CBB3FF',
            border_width=2,
            border_spacing=10,
            hover_color='#F0E8FF',
            image=stat_img,
            corner_radius=8,
            text_color=icon_color,
            command=lambda: line(lb=stat_line,page=stat_page)
        )
        self.stat_btn.place(x=15, y=340)

        stat_line = Label(menu_frame, text='', bg="#EBDFFF")
        stat_line.place(x=3, y=345, width=6, height=40)

        # --- CLOSE ---
        close_img = get_colored_icon('images/close.png', size=(28, 28), color=icon_color)
        self.close_btn = CTkButton(
            menu_frame,
            text='CLOSE',
            width=180,
            height=50,
            fg_color='#FFFFFF',
            bg_color='#F6F0FF',
            font=('Arial', 20, 'bold'),
            border_color='#CBB3FF',
            border_width=2,
            border_spacing=10,
            hover_color='#F0E8FF',
            image=close_img,
            corner_radius=8,
            text_color=icon_color
        )
        self.close_btn.place(x=15, y=420)

        ###################### Head Frame ##################3
        up_frame = CTkFrame(
            root,
            width=1199,
            height=70,
            bg_color='#F9F5FF',
            fg_color= '#FFFFFF',
            border_color= '#CBB3FF',
            border_width= 2,
        )
        up_frame.place(x=1,y=1)
        text_lbl = Label(
            up_frame
            ,text='Modern School',
            font=('carier',18,'bold'),
            bg='#FFFFFF',
            fg='#4A2E8C',
                         )
        text_lbl.place(x=30,y=5,width=200,height=60)
        date_lbl = Label(
            up_frame
            ,text='Modern School',
            font=('carier',18,'bold'),
            bg='#FFFFFF',
            fg='#4A2E8C',
                         )
        date_lbl.place(x=590,y=5,width=570,height=60)
        date()

        ################# Page Frame #################3333
        def home_page():
            home_frame = CTkFrame(
                page_frame,
                width=975,
                height=600,
                bg_color='#FBF7FF',
                fg_color='#FBF7FF',
            )
            home_frame.place(x=1, y=1)
            # --- STUDENTS ---
            stu_img = CTkImage(Image.open('images/stu.png'), size=(100, 100))
            student_btn = CTkButton(
                home_frame, text='STUDENTS', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=stu_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30,command=open_students_page
            )
            student_btn.place(x=50, y=80)

            # --- TEACHERS ---
            te_img = CTkImage(Image.open('images/tech.png'), size=(100, 100))
            teachers_btn = CTkButton(
                home_frame, text='TEACHERS', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=te_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30
            )
            teachers_btn.place(x=360, y=80)

            # --- EMPLOYEE ---
            emp_img = CTkImage(Image.open('images/emp.png'), size=(100, 100))
            emp_btn = CTkButton(
                home_frame, text='EMPLOYEE', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=emp_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30
            )
            emp_btn.place(x=670, y=80)

            # --- ACCOUNTING ---
            acc_img = CTkImage(Image.open('images/cou.png'), size=(100, 100))
            accounting_btn = CTkButton(
                home_frame, text='ACCOUNTING', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=acc_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30
            )
            accounting_btn.place(x=50, y=330)

            # --- EXAM ---
            e_img = CTkImage(Image.open('images/exam.png'), size=(100, 100))
            exam_btn = CTkButton(
                home_frame, text='EXAM', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=e_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30
            )
            exam_btn.place(x=360, y=330)

            # --- ADMIN ---
            admin_img = CTkImage(Image.open('images/adminl.png'), size=(100, 100))
            admin_btn = CTkButton(
                home_frame, text='ADMIN', width=250, height=200,
                bg_color='#FBF7FF', fg_color='#FBF7FF',
                font=('Arial', 30, 'bold'),
                border_color='#CBB3FF', border_width=5,
                image=admin_img, compound='top',
                border_spacing=20, hover_color='#F0E8FF', corner_radius=30,
                command=open_admin_page
            )
            admin_btn.place(x=670, y=330)

        def note_page():
            note_frame = CTkFrame(
                page_frame,
                width=975,
                height=600,
                bg_color='#FBF7FF',
                fg_color='#FBF7FF',
            )
            note_frame.place(x=1, y=1)
            lbl = Label(
                note_frame,
                text='Note Page'

            )
            lbl.pack()

        page_frame = CTkFrame(
         frame,
            width=980,
            height=605,
            bg_color='#FBF7FF',
            fg_color= '#FBF7FF',
        )
        page_frame.place(x=210,y=5)


        def ser_page():
            ser_frame = CTkFrame(
                page_frame,
                width=975,
                height=600,
                bg_color='#FBF7FF',
                fg_color='#FBF7FF',
            )
            ser_frame.place(x=1, y=1)
            lbl = Label(
                ser_frame,
                text='SERVICES Page'

            )
            lbl.pack()
        def stat_page():
            stat_frame = CTkFrame(
                page_frame,
                width=975,
                height=600,
                bg_color='#FBF7FF',
                fg_color='#FBF7FF',
            )
            stat_frame.place(x=1, y=1)
            lbl = Label(
                stat_frame,
                text='STATISTICS Page'

            )
            lbl.pack()

            ############# import Pages ############3
        def open_admin_page():
            win = Toplevel()
            adminpage.AdminClass(win)
            root.withdraw()
            win.deiconify()
        def open_students_page():
            win = Toplevel()
            studentspage.StudentsClass(win)
            root.withdraw()
            win.deiconify()


        page_frame = CTkFrame(
            frame,
            width=980,
            height=605,
            bg_color='#F9F5FF',
            fg_color='#FFFFFF',
        )
        page_frame.place(x=210, y=5)
        home_page()


if __name__ == '__main__':

    root = Tk()
    DashboardClass(root)
    root.mainloop()
