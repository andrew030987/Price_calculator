from tkinter import *

window = Tk()
window.title("SD Electro")
window.geometry("800x300")

def count1():
    t1.delete("1.0", "end")
    t2.delete("1.0", "end")

    percent1 = 1 + (float(e2_val.get())/100)
    total = float(e1_val.get()) * quantity1.get()
    price = (total * percent1 + float(e3_val.get()) + float(e4_val.get()) + float(e5_val.get()))/ total
    kf = price * float(e1_val.get())
    t1.insert(END, price)
    t2.insert(END, kf)
#####
b1 = Button(window, text="Посчитать", font=("Arial Bold", 12), command=count1)
b1.grid(row=9, column=2, rowspan=3)


l1 = Label(window, text = "Цена за 1 шт", font=("Arial Bold", 12))
l1.grid(row=0, column=0, ipadx=10,ipady=6)

l2 = Label(window, text = "Количество", font=("Arial Bold", 12))
l2.grid(row=1, column=0)


e1_val = StringVar()
e1=Entry(window, textvariable=e1_val, font=("Arial Bold", 12))
e1.focus()
e1.grid(row=0, column=1)


quantity1 = IntVar()
q1=Entry(window, textvariable=quantity1, font=("Arial Bold", 12))
q1.grid(row=1, column=1)
#############################################################

l3 = Label(window, text = "Ставка таможни (процент)", font=("Arial Bold", 12))
l3.grid(row=0, column=3)

l4 = Label(window, text = "Логистика", font=("Arial Bold", 12))
l4.grid(row=1, column=3)

l5 = Label(window, text = "Таможенный платеж", font=("Arial Bold", 12))
l5.grid(row=2, column=3)

l6 = Label(window, text = "Иные расходы", font=("Arial Bold", 12))
l6.grid(row=3, column=3)

e2_val = IntVar()
e2=Entry(window, textvariable=e2_val, font=("Arial Bold", 12))
e2.grid(row=0, column=4)

e3_val = IntVar()
e3=Entry(window, textvariable=e3_val, font=("Arial Bold", 12))
e3.grid(row=1, column=4)

e4_val = IntVar()
e4=Entry(window, textvariable=e4_val, font=("Arial Bold", 12))
e4.grid(row=2, column=4)

e5_val = IntVar()
e5=Entry(window, textvariable=e5_val, font=("Arial Bold", 12))
e5.grid(row=3, column=4)

#####################################################

empty_l = Label(window, text="")
empty_l.grid(row=8, column=3)

l7 = Label(window, text = "Входной коэффициент", font=("Arial Bold", 12))
l7.grid(row=9, column=3)

l8 = Label(window, text = "Входная цена", font=("Arial Bold", 12))
l8.grid(row=10, column=3)


t1=Text(window, height=1, width=10, font=("Arial Bold", 12))
t1.grid(row=9, column=4)

t2=Text(window, height=1, width=10, font=("Arial Bold", 12))
t2.grid(row=10, column=4)

window.mainloop()