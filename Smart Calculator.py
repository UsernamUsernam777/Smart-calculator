from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel
from pypower.GUI import CustomTk
from pypower.Files import make_if_not_exists
from string import digits
from datetime import datetime
from os import startfile
from re import compile as comp

# some important vars
allowed = '%*()+-/' + digits
invalid_pat = comp(f'[^{allowed}]')

# main window
main = CTk(fg_color='black')
main.title('Smart Calculator')
main.geometry('821x764+363+94')

# operation and result entries
operation = CTkEntry(main, font=('Google sans 17pt semibold', 35), width=700, placeholder_text='operation',
                     fg_color='white', text_color='black')
operation.pack(pady=70)
result = CTkEntry(main, font=('Google sans 17pt semibold', 30), width=700, placeholder_text='result',
                  fg_color='white', text_color='black')
result.pack(pady=10)

# calculations and validation
error = CTkLabel(main, text='Error!', font=('Google sans 17pt semibold', 35), text_color='red')


def show_error():
    error.pack(pady=50)
    error.after(1000, error.pack_forget)


def calculate():
    # validate
    op = operation.get().strip().replace(' ', '')
    if invalid_pat.findall(op) and len(op) > 40:
        show_error()
        return
    try:
        r = str(eval(op))
        result.delete(0, 'end')
        result.insert(0, r)
    except:
        show_error()

# calculation button
calculation_btn = CTkButton(main, text='Calculate', font=('Google sans 17pt semibold', 35),
                            fg_color='#1367e4', text_color='white', command=calculate)
calculation_btn.pack(pady=20)

# save
file_path = r"C:\ProgramData\Smart Calculator\Calculator.txt"
make_if_not_exists(file_path)

# add name
name = CTkEntry(main, font=('Google sans 17pt semibold', 30), width=700, placeholder_text='name (optional)',
                fg_color='white', text_color='black')
name.pack()

# show saving message
a = CTkLabel(main, text='Saved!', font=('Google sans 17pt semibold', 35), text_color='green')

# save
def save():
    if result.get().strip() and operation.get().strip():
        data = f"""Name: {name.get().strip() or '<untitled>'}
Date: {datetime.now().strftime('%Y/%M/%d %H:%M:%S')}
Operation: {operation.get()}
Result: {result.get()}\n\n"""
        with open(file_path, 'a') as f:
            f.write(data)
        a.pack(pady=20)
        a.after(1000, a.pack_forget)

CTkButton(main, text='Save', command=save, font=('Google sans 17pt semibold', 35), fg_color='#1367e4',
          text_color='white').pack(pady=20)

# some features
CustomTk.exit_esc(main)
CustomTk.change_mode(main).place(x=0, y=0)
CTkButton(main, text='open data file', font=('Google sans 17pt semibold', 25), fg_color='#1367e4',
          text_color='white', command=lambda: startfile(file_path)).place(x=160, y=0)
main.mainloop()
