import tkinter as tk
from tkinter import messagebox

def bmi():
    try:
        w = float(e1.get())
        h = float(e2.get())
        index = w / (h*h)
        messagebox.showinfo('your BMi', f'{index:2f}')
    except:
        messagebox.showerror('Faild!')
root = tk.Tk()

l1 = tk.Label(root, text='Weight')
l1.grid(row=0, column=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)

l2 = tk.Label(root, text='Height')
l2.grid(row=1, column=0)
e2 = tk.Entry(root)
e2.grid(row=1, column=1)


frame = tk.Frame(root)
frame.grid(row=2, column=0, columnspan=2)

b1 = tk.Button(frame, text='BMI', command=bmi)
b1.grid(row=0, column=0)

b2 = tk.Button(frame, text='Cancel', command=root.destroy)
b2.grid(row=0, column=0)

root.mainloop()