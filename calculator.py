from tkinter import *

def numericbtn(num):
    value=e.get()
    e.delete(0,END)
    e.insert(0,str(value)+str(num))

screen=Tk()
screen.title("Calculator")

e=Entry(screen, width="15",font="arial 25 bold",border="23px",background="grey",fg="black")

e.grid(row=0,column=0,columnspan="4")

btnp=Button(screen,text="%",padx="30",pady="30",bd="5")
btnce=Button(screen,text="CE",padx="30",pady="30",bd="5")
btnc=Button(screen,text="C",padx="30",pady="30",bd="5")
btnx=Button(screen,text="X",padx="30",pady="30",bd="5")

btna=Button(screen,text="1/x",padx="23",pady="30",bd="5")
btns=Button(screen,text="x^2",padx="23",pady="30",bd="5")
btnb=Button(screen,text="",padx="30",pady="30",bd="5")
btnd=Button(screen,text="/",padx="30",pady="30",bd="5")

btn7=Button(screen,text="7",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("7"))
btn8=Button(screen,text="8",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("8"))
btn9=Button(screen,text="9",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("9"))
btnm=Button(screen,text="*",padx="30",pady="30",bd="5")

btn4=Button(screen,text="4",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("4"))
btn5=Button(screen,text="5",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("5"))
btn6=Button(screen,text="6",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("6"))
btnsub=Button(screen,text="-",padx="30",pady="30",bd="5")

btn1=Button(screen,text="1",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("1"))
btn2=Button(screen,text="2",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("2"))
btn3=Button(screen,text="3",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("3"))
btnadd=Button(screen,text="+",padx="30",pady="30",bd="5")

btnas=Button(screen,text="+/-",padx="23",pady="30",bd="5",bg="white")
btnz=Button(screen,text="0",padx="30",pady="30",bd="5",bg="white",command=lambda: numericbtn("0"))
btndot=Button(screen,text=".",padx="30",pady="30",bd="5",bg="white")
btneq=Button(screen,text="=",padx="30",pady="30",bd="5",bg="blue")


btnp.grid (row="1",column="0")
btnce.grid (row="1",column="1")
btnc.grid (row="1",column="2")
btnx.grid (row="1",column="3")

btna.grid (row="2",column="0")
btns.grid (row="2",column="1")
btnb.grid (row="2",column="2")
btnd.grid (row="2",column="3")

btn7.grid (row="3",column="0")
btn8.grid (row="3",column="1")
btn9.grid (row="3",column="2")
btnm.grid (row="3",column="3")

btn4.grid (row="4",column="0")
btn5.grid (row="4",column="1")
btn6.grid (row="4",column="2")
btnsub.grid(row="4",column="3")

btn1.grid (row="5",column="0")
btn2.grid (row="5",column="1")
btn3.grid (row="5",column="2")
btnadd.grid(row="5",column="3")

btnas.grid (row="6",column="0")
btndot.grid (row="6",column="1")
btnz.grid (row="6",column="2")
btneq.grid(row="6",column="3")


mainloop()
