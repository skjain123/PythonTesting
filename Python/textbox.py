from tkinter import *

master = Tk()
S = Scrollbar(master)
T = Text(master, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
stufzz = "yuy"
exit_out = Button(master, text="quit", command=master.destroy)
exit_out.pack()
T.insert(END, stufzz)
mainloop()
