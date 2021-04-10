import tkinter as tk
import tkinter.ttk as ttk
import time

root = tk.Tk()

note = ttk.Notebook(root)
note.grid(row=0, column=0)
# ##########################
patients = ttk.Frame(note)
note.add(patients, text='patients')
timers = ttk.Frame(note)
note.add(timers, text="Timers")
# ###########################################################
lf1 = tk.LabelFrame(patients, text="patient 1")
lf1.grid(row=0, column=0)

tk.Label(lf1, text='Name').grid(row=0, column=0)
tk.Label(lf1, text='Time').grid(row=1, column=0)
name1 = tk.StringVar()
time1 = tk.StringVar()
tk.Entry(lf1, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf1, textvariable=time1).grid(row=0, column=1)
# ###########################################################
lf2 = tk.LabelFrame(patients, text="patient 2")
lf2.grid(row=1, column=0)

tk.Label(lf2, text='Name').grid(row=0, column=0)
tk.Label(lf2, text='Time').grid(row=1, column=0)
name2 = tk.StringVar()
time2 = tk.StringVar()
tk.Entry(lf2, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf2, textvariable=time1).grid(row=1, column=1)
# ###########################################################
lf3 = tk.LabelFrame(patients, text="patient 3")
lf3.grid(row=2, column=0)

tk.Label(lf3, text='Name').grid(row=0, column=0)
tk.Label(lf3, text='Time').grid(row=1, column=0)
name3 = tk.StringVar()
time3 = tk.StringVar()
tk.Entry(lf3, textvariable=name1).grid(row=0, column=1)
tk.Entry(lf3, textvariable=time1).grid(row=1, column=1)

name3 = tk.StringVar()
time3 = tk.StringVar()
# ###########################################################
j1 = tk.LabelFrame(timers)
j1.grid(row=0, column=0)
j1.set('Patient1')
tk.Label(j1, text='patient 1').grid(row=0, column=0)
# ###########################################################
j2 = tk.LabelFrame(timers)
j2.grid(row=0, column=1)

tk.Label(j2, text='patient 2').grid(row=0, column=0)
# ###########################################################
j3 = tk.LabelFrame(timers)
j3.grid(row=0, column=2)

tk.Label(j3, text='patient 3').grid(row=0, column=0)



root.mainloop()
