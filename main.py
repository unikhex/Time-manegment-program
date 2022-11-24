import tkinter
from tkinter import *
# theimports used in this code

root= Tk()
root.title("GET THESE DONE")
root.geometry("400x650+400+100") #size
root.resizable(False,False)#not resizible so that the icons dont move away(makes the app look ugly)
#root is our window object(this is mostly for me to know where to write the code, knowing the borders)

btn = Button(root,text="Open Calender",command=open).pack
task_list=[]

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert( END, task)
# this is the function that saves the writte input and adds it onto a list that will be viewed on screen
# it saves the input in a separate file


def deleteTask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete( ANCHOR)
# deletes inputs that we are already finished with(makes it so that completed tasks can be deleted)            


def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()
    
        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END ,task)
    except:
        file=open('tasklist.txt','w')

        file.close()
# this function reads and writes  what is on the file that we are using depending on the situation before(if there was something written on the file before it will read it and displays it and if not it saves your input into the file then displays it)

#icon
Image_icon=PhotoImage(file="Images/task.png")
root.iconphoto(False,Image_icon)

#top bar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root,image= TopImage).pack()

dockImage=PhotoImage(file="Images/dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="Images/task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)

heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b")
heading.place(x=130,y=20)

#main
frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry= Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()


button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",fg="#fff",bd=0,command=addTask)
button.place(x=300,y=0)

#listbox
frame1=Frame(root,bd=3,width=700,heigh=12880,bg="#32405b")
frame1.pack(pady=(160,0))

listbox= Listbox(frame1,font=('arial',12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT , fill=BOTH, padx=2)
scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT   ,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
# The scroll

openTaskFile()

#delete
Delete_icon=PhotoImage(file="Images/delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)
#The above are mostly how the app looks like, which colours it has and which buttons it has.


root.mainloop()
