from tkinter import *

#window
mwindow = Tk()
mwindow.title('Length Converter')

#function for conversion
def conv():
    
    mm = float(val.get())*10
    m = float(val.get())/100
    km = float(val.get())/100000
    inch = float(val.get())/2.54
 
    pr1.delete(1.0, END)
    pr1.insert(END, mm)
    pr2.delete(1.0, END)
    pr2.insert(END, m)
    pr3.delete(1.0, END)
    pr3.insert(END, km)
    pr4.delete(1.0, END)
    pr4.insert(END, inch)
 

#part1
show1 = Label(mwindow, text='Length in Centimeters:')
show1.grid(row=0,column=0)

val = StringVar()
u_in = Entry(mwindow,fg="black" , bg="white", width=15,textvariable=val)
u_in.grid(row=0,column=1)

convbutton = Button(mwindow, text='Convert',fg='white',bg='black',width=6, command =conv)
convbutton.grid(row=0,column=3)



#part2
mm_l = Label(mwindow, text='Millimeter (mm)')
mm_l.grid(row=2,column=0)
pr1 = Text(mwindow, height = 1, width=20)
pr1.grid(row=2,column=1)

m_l = Label(mwindow, text='Meter (m)')
m_l.grid(row=3,column=0)
pr2 = Text(mwindow, height = 1, width=20)
pr2.grid(row=3,column=1)

km_l = Label(mwindow, text='Kilometer (km)')
km_l.grid(row=4,column=0)
pr3 = Text(mwindow, height = 1, width=20)
pr3.grid(row=4,column=1)

in_l = Label(mwindow, text='Inch (IN)')
in_l.grid(row=5,column=0)
pr4 = Text(mwindow, height = 1, width=20)
pr4.grid(row=5,column=1)

mwindow.mainloop()