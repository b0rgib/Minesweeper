import numpy as np
import random 
from tkinter import *
from tkinter import messagebox
def flag():
    global fl
    if fl==0:
        fl=1
        btn2.config(relief=SUNKEN)
    else:
        fl=0
        btn2.config(relief=RAISED)
def clicked(i,j):
    if fl==0:
        x=np.int(a[i+1,j+1])
        R[i+1,j+1]=1
        if a[i+1,j+1]==0:
            x=''
            for row in range(3):
                for column in range(3):
                    if R[i+row,j+column]==0:
                        clicked(i+row-1,j+column-1)
        elif a[i+1,j+1]==9:
            x='*'
            for row in range(len(a)-1):
                for column in range(len(a[i])-1):
                    buttonList[row][column]['state'] = 'disabled'
            messagebox.showinfo('Minesweeper', 'Вы проиграли!')
        buttonList[i][j].config(text = x, relief=SUNKEN, font='10')
        buttonList[i][j]['state'] = 'disabled'
    else:
        if buttonList[i][j]['text']=='!':
            buttonList[i][j].config(text = '',  font='10')
            R[i+1,j+1]=0
        else:
            buttonList[i][j].config(text = '!',  font='10')
            R[i+1,j+1]=9
    R1=R[1:-1,1:-1]
    a1=a[1:,1:]
    check=1
    for row in range(len(a)-1):
        for column in range(len(a[i])-1):
            if (a1[row,column]==9) & (a1[row,column]-R1[row,column]!=0):
                check=0
    if check==1:
        for row in range(len(a)-1):
            for column in range(len(a[i])-1):
                buttonList[row][column]['state'] = 'disabled'
        messagebox.showinfo('Minesweeper', 'Победа!')
def start():
    lbl.config(text='')
    n1=int(n.get())
    m1=int(m.get())
    global a
    a = np.zeros((n1*m1))
    a[:int(k.get())]=9 
    np.random.shuffle(a)
    a.shape = (n1, m1)
    a=np.column_stack((np.zeros((n1,1)), a))
    a=np.row_stack((np.zeros((1,m1+1)), a))
    global buttonList
    buttonList=[] 
    for i in range(len(a)):
        buttonRow=[]
        for j in range(len(a[i])):
            if a[i,j] == 0:
                a[i,j]=np.sum(a[i-1:i+2,j-1:j+2]==9)
    for i in range(len(a)-1):
        buttonRow=[]
        for j in range(len(a[i])-1):
            button=Button(root, width=2, height=1, command = lambda i=i, j=j: clicked(i,j),font='10')
            button.grid(column=5+i, row=5+j)
            buttonRow.append(button)
        buttonList.append(buttonRow)
    root.geometry('1000x600')
    global R
    R=np.zeros((n1,m1))
    R=np.column_stack((np.ones((n1,1)), R))
    R=np.column_stack((R, np.ones((n1,1))))
    R=np.row_stack((np.ones((1,m1+2)), R))
    R=np.row_stack((R, np.ones((1,m1+2)))) 
root = Tk()
root.title("Minesweeper")
root.geometry('600x400')
fl=0
btn2 = Button(root, text="Мина", command=flag)
btn2.grid(column=99, row=0)  
lbl = Label(root, text='', font=("Arial Bold", 10))  
lbl.grid(column=100, row=0)
lbl1 = Label(root, text='Ширина')  
lbl1.grid(column=0, row=0)  
lbl2 = Label(root, text='Высота')  
lbl2.grid(column=0, row=1)  
lbl3 = Label(root, text='Мины')  
lbl3.grid(column=0, row=2)  
n = Entry(root,width=5)  
n.grid(column=1, row=0)
m = Entry(root,width=5)  
m.grid(column=1, row=1)
k = Entry(root,width=5)  
k.grid(column=1, row=2)
btn1 = Button(root, text="Ввод", command=start)  
btn1.grid(column=3, row=0)
root.mainloop()




