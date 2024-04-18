from tkinter import *

def click(event):
    global scvalue
    text= event.widget.cget("text")
    
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value= eval(screen.get())
        scvalue.set(value)
        screen.update()
            
            
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
    
    

root=Tk()
root.geometry("400x700")
root.title("Calculator")


scvalue= StringVar()
scvalue.set("")
screen= Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f= Frame(root, bg="grey")
b= Button(f, text="9", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="8", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="7", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f, text="6", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="5", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="4", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f, text="3", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="2", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="1", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f, text="0", padx=5, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="-", padx=5, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="*", padx=5, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f, text="/", padx=2, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="%", padx=1, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="=", padx=1, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root, bg="grey")
b= Button(f, text="C", padx=0, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text=".", padx=0, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text="00", padx=0, pady=1, font="lucida 35 bold")
b.pack(side=LEFT, padx=6, pady=5)
b.bind("<Button-1>", click)

f.pack()

root.mainloop()

