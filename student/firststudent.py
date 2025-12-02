from customtkinter import*
from tkinter import *
from PIL import Image
from time import strftime
import dashboard
import studentspage

class FirstStudentClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x690+100+5')
        self.root.title('First Students Page')
        self.root.config(bg='white')
        self.root.resizable(False,False)
        def date():
            date_1 = strftime('%I:%M:%S %p \t %A \t %b/%d/%Y')
            date_lbl.config(text=date_1)
            date_lbl.after(1000, date)

        ###################### head frame ####################
        up_frame = CTkFrame(
            root,
            width=1199,
            height=70,
            fg_color='#F7F3FF',  # Lavender light
            border_color='#D9A7FF',  # Purple border
            border_width=2,
        )
        up_frame.place(x=1, y=1)

        text_lbl = Label(
            up_frame,
            text='Students Page',
            font=('corier', 18, 'bold'),
            bg='#F7F3FF',
            fg='#6A4FA3'  # Purple deep
        )
        text_lbl.place(x=150, y=5, width=200, height=60)

        date_lbl = Label(
            up_frame,
            font=('corier', 18, 'bold'),
            bg='#F7F3FF',
            fg='#D97FA6'  # Soft pink
        )
        date_lbl.place(x=590, y=5, width=570, height=60)

        date()

        ############## back button ####################
        def back():
            win= Toplevel()
            studentspage.StudentsClass(win)
            root.withdraw()
            win.deiconify()
       
        back_btn = CTkButton(
            up_frame,
            text='←',
            width=100,
            height=68,
            fg_color='#DDEBFF',  # Light baby blue
            text_color='#4F6CA8',  # Blue for clarity
            bg_color='#F7F3FF',
            font=('corier', 18, 'bold'),
            border_color='#4F6CA8',
            border_width=2,
            corner_radius=10,command=back
        
        )
        back_btn.place(x=2, y=2)
         ################### Up Frame #############333
        head_frame = CTkFrame(
            root,
            width=1197,
            height=615,
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
            border_color='#D9A7FF',
            border_width=2
        )
        head_frame.place(x=1, y=72)
       
          

if __name__ == "__main__":
    root = Tk()
    FirstStudentClass(root)
    root.mainloop()