import tkinter as tk


counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter))
    label.after(1000, count)
  count()
 
 
master = tk.Tk()
master.title("Counting Seconds")
label = tk.Label(master, fg="black")
label.pack()
counter_label(label)
master.mainloop()
