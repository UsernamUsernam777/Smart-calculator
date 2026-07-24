from customtkinter import CTk, CTkButton, CTkEntry, CTkLabel
from pypower.GUI import CustomTk
from string import digits
from datetime import datetime
from os import path, mkdir, startfile
#main window
main = CTk()
main.title('Smart Calculator')
main.geometry('821x764+363+94')
#operation and result entries
operation = CTkEntry(main, font=('google sans17pt', 60), width=700, placeholder_text='operation')
operation.pack(pady=70)
result = CTkEntry(main, font=('google sans17pt', 50), width=700, placeholder_text='result')
result.pack(pady=10)
#calculations and validation
error = CTkLabel(main, text='Error!', font=('google sans17pt', 60), text_color='red')
def show_error():
    error.pack(pady=50)
    error.after(1000, error.pack_forget)
def calculate():
    #validate
    allowed = '/*-+()' + digits
    op = operation.get().strip()
    for c in op:
        if c not in allowed or len(op) > 35:
            show_error()
            return
    try:
        result.delete(0, 'end')
        result.insert(0, str(eval(op)))
    except Exception:
        show_error()
#calculation button
calculation_btn = CTkButton(main, text='Calculate', font=('google sans17pt', 60), command=calculate)
calculation_btn.pack(pady=20)
#save
file_path = r"C:\ProgramData\Smart Calculator\Calculator.txt"
if not path.exists(file_path):
    mkdir(path.dirname(file_path))
    with open(file_path, 'x') as f:
        pass
def save():
    if result.get().strip() and operation.get().strip():
        data = f"""Date: {datetime.now().strftime('%Y/%M/%d %H:%M:%S')}
Operation: {operation.get()}
Result: {result.get()}\n\n"""
        with open(file_path, 'a') as f:
            f.write(data)
CTkButton(main, text='Save', command=save, font=('google sans17pt', 60)).pack(pady=20)
#some features
CustomTk.exit_esc(main)
CustomTk.change_mode(main).place(x=0, y=0)
CTkButton(main, text='open data file', font=('arial', 30), command=lambda:startfile(file_path)).place(x=160, y=0)
main.mainloop()
