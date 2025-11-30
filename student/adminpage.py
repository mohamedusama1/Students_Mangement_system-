from customtkinter import *
from tkinter import *
from PIL import Image
from time import strftime
import sqlite3

from django.utils.termcolors import foreground

import dashboard
from tkinter import ttk, messagebox


class AdminClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x690+100+5")
        self.root.title('Admin Page')
        self.root.config(bg='white')
        self.root.resizable(width=False, height=False)

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
            text='Admin Page',
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
            win = Toplevel()
            dashboard.DashboardClass(win)
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
            corner_radius=10,
            command=back
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

        text_lbl = Label(
            head_frame,
            text='WELCOME TO \n Admin Page',
            font=('corier', 25, 'bold'),
            bg='#FFFFFF',
            fg='#D97FA6'
        )
        text_lbl.place(x=20, y=50, width=300, height=100)
        ############### LOGO IMG #############3
        logo_img = CTkImage(Image.open('images/admin.png'), size=(250, 250))
        img_lbl = CTkLabel(
            head_frame,
            text='',
            image=logo_img,
            fg_color='transparent',
        )
        img_lbl.place(x=350, y=20)

        img_lbl.place(x=350, y=20)
        ################# VAR #################33
        id = StringVar()
        name = StringVar()
        username = StringVar()
        password = StringVar()

        ############### Labels + Entry ######################
        lbl_id = CTkLabel(
            head_frame, text='ID',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_id.place(x=80, y=300)

        en_id = CTkEntry(
            head_frame,
            justify='center',
            textvariable=id,
            width=50,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_id.place(x=200, y=300)

        lbl_name = CTkLabel(
            head_frame, text='New Account Name',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_name.place(x=20, y=340)

        en_name = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=name,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_name.place(x=20, y=370)
        lbl_username = CTkLabel(
            head_frame, text='USERNAME',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_username.place(x=20, y=410)

        en_username = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=username,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_username.place(x=20, y=440)

        lbl_pass = CTkLabel(
            head_frame, text='New Account Password',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_pass.place(x=20, y=480)

        en_pass = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=password,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_pass.place(x=20, y=510)

        #################Buttons####################
        def clear():
            id.set('')
            name.set('')
            username.set('')
            password.set('')

        def delete():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            op = messagebox.askyesno('confirm', 'Are you sure you want to delete this account?')
            if op:
                try:
                    cur.execute("DELETE FROM Account WHERE ID = ?", (id.get(),))
                    con.commit()
                    rec_id()
                    messagebox.showinfo('Delete', 'Account deleted')
                    show()
                    clear()
                except Exception as ex:
                    messagebox.showerror('Error', f'error {ex}')
                finally:
                    con.close()
            else:
                messagebox.showinfo('Canceled', 'Account not deleted')
                con.close()

        clear_button = CTkButton(
            head_frame,
            text='Clear',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8,
            width=100,
            height=40,
            command=clear
        )
        clear_button.place(x=20, y=560)

        delete_button = CTkButton(
            head_frame,
            text='Delete',
            fg_color='#FFE4E8',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#C94763',
            hover_color='#FFD3DB',
            border_color='#F5A9B8',
            border_width=2,
            corner_radius=8,
            width=100,
            height=40,
            command=delete
        )
        delete_button.place(x=150, y=560)

        ##################### new account treeview ##############
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
            con.commit()
            con.close()

        def show():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute('SELECT * FROM Account')
                rows = cur.fetchall()
                new_account_tree.delete(*new_account_tree.get_children())
                global count
                count = 0
                for row in rows:
                    # new_account_tree.insert('', 'end', values=row)
                    if count % 2 == 0:
                        new_account_tree.insert(parent='', index='end', iid=count,
                                                values=(row[0], row[1], row[2], row[3]), tags=('evenrow'))
                    else:
                        new_account_tree.insert(parent='', index='end', iid=count,
                                                values=(row[0], row[1], row[2], row[3]), tags=('oddrow'))
                    count += 1


            except Exception as ex:
                messagebox.showerror('Error', f'error{str(ex)}')

        def get_data(ev):

            n = new_account_tree.focus()
            f = (new_account_tree.item(n))
            row = f['values']

            id.set(row[0])
            name.set(row[1])
            username.set(row[2])
            password.set(row[3])

            var_id_admin.set(row[0])
            var_name_admin.set(row[1])
            var_username_admin.set(row[2])
            var_password_admin.set(row[3])

        new_account_tree_f = Frame(head_frame, bg='#FFFFFF')
        new_account_tree_f.place(x=280, y=330, width=420, height=250)

        new_account_style = ttk.Style()
        new_account_style.theme_use('clam')

        # --- إعدادات جسم الجدول (البيانات) ---
        new_account_style.configure(
            'Treeview',
            bg='white',
            rowheight=25,
            fieldbackground='white',
            font=('corier', 11, 'bold'),
            fg='#4A4A4A'
        )

        new_account_style.configure(
            'Treeview.Heading',
            background='#D97FA6',  # Soft pink header
            font=('corier', 15, 'bold'),
            foreground='white',
            relief='flat'
        )
        # تفعيل لون العنوان عند التحويم
        new_account_style.map('Treeview.Heading', background=[('active', '#E06D82')])

        scroll_new_account_tree = Scrollbar(new_account_tree_f)
        scroll_new_account_tree.pack(side=RIGHT, fill=Y)

        new_account_tree = ttk.Treeview(new_account_tree_f, yscrollcommand=scroll_new_account_tree.set,
                                        style='Treeview')
        new_account_tree.place(x=0, y=0, width=403, height=250)

        scroll_new_account_tree.config(command=new_account_tree.yview)

        new_account_tree['columns'] = ('ID', 'name', 'username', 'password')

        new_account_tree.column('#0', width=0, stretch=NO)
        new_account_tree.column('ID', anchor=W, width=40)
        new_account_tree.column('name', anchor=W, width=100)
        new_account_tree.column('username', anchor=W, width=100)
        new_account_tree.column('password', anchor=W, width=100)

        new_account_tree.heading('#0', text='', anchor=W)
        new_account_tree.heading('ID', text='ID', anchor='center')
        new_account_tree.heading('name', text='Name', anchor='center')
        new_account_tree.heading('username', text='Username', anchor='center')
        new_account_tree.heading('password', text='Password', anchor='center')
        # new_account_tree.bind('<ButtonRelease>', get_data)
        new_account_tree.bind("<ButtonRelease-1>", get_data)

        new_account_tree.tag_configure('evenrow', background='#FFFFFF')
        new_account_tree.tag_configure('oddrow', background='#EEF6FF')

        # ================admin=============================
        def rec_admin_id():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute('''
            WITH RECURSIVE cte AS (
                SELECT ROW_NUMBER() OVER (ORDER BY admin_ID) AS new_id, admin_ID
                FROM Admin
            )
            UPDATE Admin
            SET admin_ID = (SELECT new_id FROM cte WHERE cte.admin_ID = Admin.admin_ID)
            ''')
            con.commit()
            con.close()

        def add():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            if (var_name_admin.get() == "" or var_name_admin.get() == "" or var_password_admin.get() == ""):
                messagebox.showerror("error", "please enter all date")
            else:
                cur.execute("INSERT INTO Admin(admin_name,admin_username,admin_password) values(?,?,?)", (
                    var_name_admin.get(),
                    var_username_admin.get(),
                    var_password_admin.get(),
                ))
                messagebox.showinfo("success", "add successfully")
            con.commit()
            con.close()
            rec_admin_id()
            show_admin()
            clear_admin()

        def show_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            try:
                cur.execute('SELECT * FROM Admin')
                rows = cur.fetchall()
                admin_tree.delete(*admin_tree.get_children())
                global count
                count = 0
                for row in rows:
                    if count % 2 == 0:
                        admin_tree.insert(parent='', index='end', iid=count,
                                          values=(row[0], row[1], row[2], row[3]), tags=('evenrow'))
                    else:
                        admin_tree.insert(parent='', index='end', iid=count,
                                          values=(row[0], row[1], row[2], row[3]), tags=('oddrow'))
                    count += 1

            except Exception as ex:
                messagebox.showerror('Error', f'error{str(ex)}')
            finally:
                con.close()



        def clear_admin():
            var_id_admin.set("")
            var_name_admin.set("")
            var_password_admin.set("")
            var_username_admin.set("")

        def get_admin_date(ev):
            n = admin_tree.focus()
            f = (admin_tree.item(n))
            row = f['values']

            var_id_admin.set(row[0])
            var_name_admin.set(row[1])
            var_username_admin.set(row[2])
            var_password_admin.set(row[3])

        def update_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            cur.execute("""
            UPDATE Admin SET admin_name=?, admin_username=?, admin_password=? 
            WHERE admin_ID=?""", (
                var_name_admin.get(),
                var_username_admin.get(),
                var_password_admin.get(),
                var_id_admin.get(),
            ))
            con.commit()
            con.close()
            rec_admin_id()
            messagebox.showinfo("success", "update successfully")
            show_admin()
            clear_admin()

        def delete_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()
            op = messagebox.askyesno("confirm", "do you really want to delete")
            if op:
                cur.execute("DELETE FROM Admin WHERE admin_ID=?", (var_id_admin.get(),))
                con.commit()
                con.close()
                rec_admin_id()
                messagebox.showinfo("success", "delete successfully")
                show_admin()
                clear_admin()

            else:
                messagebox.showinfo("cancle", "delete cancel")
                con.close()

        def upgrade_to_admin():
            con = sqlite3.connect('school.db')
            cur = con.cursor()

            if id.get() == "":
                messagebox.showerror("error", "please select a new account to upgrade")
                return

            cur.execute("SELECT * FROM Account WHERE ID=?", (id.get(),))
            data = cur.fetchone()

            if data:
                cur.execute("INSERT INTO Admin(admin_name,admin_username,admin_password) VALUES(?,?,?)", (
                    data[1],
                    data[2],
                    data[3]
                ))
                cur.execute("DELETE FROM Account WHERE ID=?", (id.get(),))
                con.commit()
                rec_id()
                messagebox.showinfo("success", "upgrade successfully")
                show()
                clear()

            else:
                messagebox.showerror("error", "no new account")
            con.close()
            rec_admin_id()
            show_admin()
            clear_admin()

        # =================
        var_id_admin = StringVar()
        var_name_admin = StringVar()
        var_username_admin = StringVar()
        var_password_admin = StringVar()
        ############### Labels + Entry ######################
        lbl_admin_id = CTkLabel(
            head_frame, text='ID',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_admin_id.place(x=790, y=50)

        en_admin_id = CTkEntry(
            head_frame,
            justify='center',
            textvariable=var_id_admin,
            width=50,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_admin_id.place(x=910, y=50)

        lbl_admin_name = CTkLabel(
            head_frame, text=' Admin Name',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_admin_name.place(x=750, y=90)

        en_admin_name = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=var_name_admin,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_admin_name.place(x=730, y=120)
        lbl_admin_username = CTkLabel(
            head_frame, text=' admin USERNAME',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_admin_username.place(x=750, y=170)

        en_admin_username = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=var_username_admin,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_admin_username.place(x=730, y=200)

        lbl_admin_pass = CTkLabel(
            head_frame, text='New Account Password',
            font=('corier', 14, 'bold'),
            fg_color='transparent',
            text_color='#5A4FA3',
            height=25,
            width=200,
            bg_color='#F7F3FF'
        )
        lbl_admin_pass.place(x=750, y=240)

        en_admin_pass = CTkEntry(
            head_frame,
            justify='center',
            width=230,
            textvariable=var_password_admin,
            height=35,
            font=('corier', 14, 'bold'),
            border_width=1,
            border_color='#C9B7FF',
            bg_color='#F7F3FF',
            fg_color='#FFFFFF',
        )
        en_admin_pass.place(x=730, y=270)
        # ==================================buttons==============
        add_button = CTkButton(
            head_frame,
            text='Add',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8, command=add,
            width=100,
            height=40,
        )
        add_button.place(x=1020, y=50)
        clear_button = CTkButton(
            head_frame,
            text='Clear',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8, command=clear_admin,
            width=100,
            height=40,
        )
        clear_button.place(x=1020, y=100)
        update_button = CTkButton(
            head_frame,
            text='Update',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8, command=update_admin,
            width=100,
            height=40,
        )
        update_button.place(x=1020, y=150)
        delete_button = CTkButton(
            head_frame,
            text='Delete',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8, command=delete_admin,
            width=100,
            height=40,
        )
        delete_button.place(x=1020, y=200)
        upgrade_button = CTkButton(
            head_frame,
            text='Upgrade to admin',
            fg_color='#E7EDFF',
            bg_color='#EEF3FF',
            font=('arial', 16, 'bold'),
            text_color='#5A4FA3',
            hover_color='#D9E3FF',
            border_color='#C7BAFF',
            border_width=2,
            corner_radius=8, command=upgrade_to_admin,
            width=100,
            height=40,
        )
        upgrade_button.place(x=1000, y=250)
        # ==================admin treeview============
        admin_tree_f = Frame(head_frame, bg='#FFFFFF')
        admin_tree_f.place(x=730, y=330, width=420, height=250)

        admin_style = ttk.Style()
        admin_style.theme_use('clam')

        # --- إعدادات جسم الجدول (البيانات) ---
        admin_style.configure(
            'Treeview',
            bg='white',
            rowheight=25,
            fieldbackground='white',
            font=('corier', 11, 'bold'),
            fg='#4A4A4A'
        )

        admin_style.configure(
            'Treeview.Heading',
            background='#D97FA6',  # Soft pink header
            font=('corier', 15, 'bold'),
            foreground='white',
            relief='flat'
        )
        # تفعيل لون العنوان عند التحويم
        new_account_style.map('Treeview.Heading', background=[('active', '#E06D82')])

        scroll_admin_tree = Scrollbar(admin_tree_f)
        scroll_admin_tree.pack(side=RIGHT, fill=Y)

        admin_tree = ttk.Treeview(admin_tree_f, yscrollcommand=scroll_admin_tree.set,
                                  style='Treeview')
        admin_tree.place(x=0, y=0, width=403, height=250)

        scroll_admin_tree.config(command=admin_tree.yview)

        admin_tree['columns'] = ('admin_ID', 'admin_name', 'admin_username', 'admin_password')

        admin_tree.column('#0', width=0, stretch=NO)
        admin_tree.column('admin_ID', anchor=W, width=40)
        admin_tree.column('admin_name', anchor=W, width=100)
        admin_tree.column('admin_username', anchor=W, width=70)
        admin_tree.column('admin_password', anchor=W, width=70)

        admin_tree.heading('#0', text='', anchor=W)
        admin_tree.heading('admin_ID', text='ID', anchor='center')
        admin_tree.heading('admin_name', text='admin Name', anchor='center')
        admin_tree.heading('admin_username', text='Username', anchor='center')
        admin_tree.heading('admin_password', text='Password', anchor='center')
        admin_tree.bind("<ButtonRelease-1>", get_admin_date)

        admin_tree.tag_configure('evenrow', background='#FFFFFF')
        admin_tree.tag_configure('oddrow', background='#EEF6FF')
        # load data initially
        show()
        show_admin()


if __name__ == '__main__':
    root = Tk()
    AdminClass(root)
    root.mainloop()
