from tkinter import *

window = Tk()

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

def weight_converter():
    try:
        print(e2_value.get())
        gram = float(e2_value.get())*1000
        pound = float(e2_value.get())*2.20462
        ounce = float(e2_value.get())*35.274
    except:
        print("Warning: blank, do nothing")

b1 = Button(window, text = "Excute", command = km_to_miles)
b1.grid(row = 0, column = 0)

b2 = Button(window, text = "Convert", command = weight_converter)
b2.grid(row = 1, column = 0)


e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

e2_value = StringVar()
e2 = Entry(window, textvariable = e1_value)
e2.grid(row = 1, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 0, column = 2)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 2)
t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 3)
t4 = Text(window, height = 1, width = 20)
t4.grid(row = 1, column = 2)

window.mainloop()