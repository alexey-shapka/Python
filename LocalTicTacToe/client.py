import socket
from tkinter import *
from tkinter import messagebox

ipserv='localhost'


def getup():
    global labelnameopponent
    try:
        while True:

            sock = socket.socket()
            sock.connect((ipserv, 9090))
            sock.send('up'.encode())
            data = str(sock.recv(1024).decode())
            sock.close()
            if data == 'wait':
                root.update()
                continue
            else:
                newdata = data.split()

                if int(newdata[1])<2:
                    messagebox.showinfo("Leave", "Your opponent left the game.")
                    forget()
                    login()
                    break

                else:
                    labelnameopponent['text'] = "Opponent: "+ str(newdata[2])
                    root.update()

                    for i in range(len(newdata[0])):
                        if data[i]=='1':
                            buttons[i].config(text = 'X')
                            buttons[i].config(bg = '#bf00ff')
                        elif data[i]=='2':
                            buttons[i].config(text = 'O')
                            buttons[i].config(bg = '#ff96f9')
                        elif data[i] == '0':
                            buttons[i].config(text = '')
                            buttons[i].config(bg="#cecece")
                    root.update()
    except:
        pass


def other(data):
    if data == 'Other':
        messagebox.showinfo("Turn", "Other player turns!")

    elif data == 'wait':
        messagebox.showinfo("Wait", "Wait for another player connect.")

def paint(ris,data):
    global player
    global ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8
    if data == "1":
        ris.config(text = 'X')
        ris.config(bg = '#bf00ff')
        player=1
    elif data == "2":
        ris.config(text = 'O')
        ris.config(bg = '#ff96f9')
        player=2
    elif data == 'error':
        messagebox.showinfo("Error", "This field already taken.\n"
                          "Choose another one.")
    elif data == 'win':
        if player==1:
            ris.config(text = 'X')
            ris.config(bg = '#bf00ff')
            messagebox.showinfo("Complete!","You win!")
        elif player==2:
            ris.config(text = 'O')
            ris.config(bg = '#ff96f9')
            messagebox.showinfo("Complete!","You win!")

def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def senddata(n):
    try:
        global buttons
        global ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8
        sock = socket.socket()
        sock.connect((ipserv, 9090))
        if n==1:
            sock.send("1".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris0,XO)
            sock.close()

        elif n==2:
            sock.send("2".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris1,XO)
            sock.close()
        elif n==3:
            sock.send("3".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris2,XO)
            sock.close()
        elif n==4:
            sock.send("4".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris3,XO)
            sock.close()
        elif n==5:
            sock.send("5".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris4,XO)
            sock.close()
        elif n==6:
            sock.send("6".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris5,XO)
            sock.close()
        elif n==7:
            sock.send("7".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris6,XO)
            sock.close()
        elif n==8:
            sock.send("8".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris7,XO)
            sock.close()
        elif n==9:
            sock.send("9".encode())
            data = sock.recv(1024)
            XO=str(data.decode())
            other(XO)
            paint(ris8,XO)
            sock.close()

        elif n=='reset':
            sock.send("reset".encode())
            for b in buttons:
                b.config(bg="#cecece",text = '')
            sock.close()

        elif n=='author':
            messagebox.showinfo("Author", "Shapka Alexey")

        elif n == 'records':
            sock.send("records".encode())
            data = str(sock.recv(1024).decode())
            record = data.split()

            def sort_col(i):
                return i[2]

            for i in range(int(len(record)/3)):
                record[i*3+1]=int(record[i*3+1])
                record[i*3+2]=float(record[i*3+2])

            newrecord = chunkIt(record,int(len(record)/3))

            newrecord.sort(key=sort_col, reverse=True)


            record_window = Toplevel(bg="#cecece")
            record_window.geometry("320x290+"+str(int(screen_width/2+270/2))+"+"+str(int(screen_height/2-238/2)))
            record_window.title("Records")
            record_window.resizable(False, False)

            def myfunction(event):
                canvas.configure(scrollregion=canvas.bbox("all"),width=275,height=260)

            myframe=Frame(record_window,relief=GROOVE,width=50,height=100,bd=1)
            myframe.place(x=10,y=10)
            canvas=Canvas(myframe)
            frame=Frame(canvas)
            myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
            canvas.configure(yscrollcommand=myscrollbar.set)

            myscrollbar.pack(side="right",fill="y")
            canvas.pack(side="left")
            canvas.create_window((0,0),window=frame,anchor='nw')
            frame.bind("<Configure>",myfunction)

            Label(frame,text="Name", width=8, fg="#3a3a3a", font=("Lato", 14),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=0,column=0)
            Label(frame,text="Winrate", width=8, fg="#3a3a3a", font=("Lato", 14),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=0,column=1)
            Label(frame,text="Wins", width=8, fg="#3a3a3a", font=("Lato", 14),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=0,column=2)

            for i in range(len(newrecord)):
                Label(frame,text=str(newrecord[i][0]), width=9, fg="#3a3a3a", font=("Lato", 13),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=i+1,column=0)
                Label(frame,text=str(newrecord[i][2])+"%", width=9, fg="#3a3a3a", font=("Lato", 13),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=i+1,column=1)
                Label(frame,text=str(newrecord[i][1]), width=9, fg="#3a3a3a", font=("Lato", 13),  activebackground="#FFFFFF", relief="flat", cursor="hand2").grid(row=i+1,column=2)


    except(ConnectionRefusedError):
        messagebox.showinfo("Error","Connection error.\nTry later.")



def Exit(event):
    try:
        sock = socket.socket()
        sock.connect((ipserv, 9090))
        sock.send("exit".encode())
        sock.close()
        root.destroy()
    except(ConnectionRefusedError):
        root.destroy()



root = Tk()
root.title("Tic-tac-toe")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry("233x305+"+str(int(screen_width/2-233/2))+"+"+str(int(screen_height/2-238/2)))
root.resizable(False, False)
menu_bar = Menu(root)
root.configure(menu=menu_bar)

def forget():

    global ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8
    global label0, label1, labelname, labelnameopponent

    ris0.place_forget()
    ris1.place_forget()
    ris2.place_forget()
    ris3.place_forget()
    ris4.place_forget()
    ris5.place_forget()
    ris6.place_forget()
    ris7.place_forget()
    ris8.place_forget()

    label0.place_forget()
    label1.place_forget()
    labelname.place_forget()
    labelnameopponent.place_forget()

    root.unbind(1)
    root.unbind(2)
    root.unbind(3)
    root.unbind(4)
    root.unbind(5)
    root.unbind(6)
    root.unbind(7)
    root.unbind(8)
    root.unbind(9)

    root.unbind('<Escape>')
    root.unbind('<n>')
    root.unbind('<r>')
    root.unbind('<a>')

    menu_bar.delete("New game")
    menu_bar.delete("Statistics")
    menu_bar.delete("Author")
    menu_bar.delete("Exit")

    pass


def create():
    global buttons
    global ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8

    global label0, label1, labelname , labelnameopponent
    global entry0, entry1
    global submitbutton


    logpas = str("con "+entry0.get())+ " " + str(entry1.get())
    try:
        sock = socket.socket()
        sock.connect((ipserv, 9090))
        sock.send(logpas.encode())
        data = str(sock.recv(1024).decode())

        if data == 'go' or data == 'create':
            if data == 'go':
                messagebox.showinfo("Log in", "Success!")
            elif data == 'create':
                messagebox.showinfo("Check in", "User successfully created!")

            labelname = Label(root, text="You: "+entry0.get(), width=21, font=("Lato", 15), bg="#d6d6d6", fg="#3a3a3a")
            labelname.place(x=0,y=0)

            labelnameopponent = Label(root, text="Opponent: ", width=21, font=("Lato", 15), bg="#d6d6d6", fg="#e02121")
            labelnameopponent.place(x=0,y=276)



            ris0 = Button(root, width=10, height=5, bg="#cecece", command=lambda:senddata(1))

            ris0.place(x=0, y=30)
            ris1 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(2))

            ris1.place(x=81, y=30)
            ris2 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(3))

            ris2.place(x=162, y=30)

            ris3 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(4))

            ris3.place(x=0, y=111)
            ris4 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(5))

            ris4.place(x=81, y=111)
            ris5 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(6))

            ris5.place(x=162, y=111)

            ris6 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(7))

            ris6.place(x=0, y=192)
            ris7 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(8))
            ris7.place(x=81, y=192)

            ris8 = Button(root, width=10, height=5, bg="#cecece",command=lambda:senddata(9))
            ris8.place(x=162, y=192)


            menu_bar.add_command(label="New game", command = lambda:senddata('reset'))
            menu_bar.add_command(label="Statistics", command = lambda:senddata('records'))
            menu_bar.add_command(label="Author", command = lambda:senddata('author'))
            menu_bar.add_command(label="Exit", command = lambda:Exit(event='click'))


            buttons = [ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8]

            root.bind(1, lambda *ignore:senddata(1))
            root.bind(2, lambda *ignore:senddata(2))
            root.bind(3, lambda *ignore:senddata(3))
            root.bind(4, lambda *ignore:senddata(4))
            root.bind(5, lambda *ignore:senddata(5))
            root.bind(6, lambda *ignore:senddata(6))
            root.bind(7, lambda *ignore:senddata(7))
            root.bind(8, lambda *ignore:senddata(8))
            root.bind(9, lambda *ignore:senddata(9))
            root.bind('<Escape>', Exit)
            root.bind('<n>', lambda *ignore:senddata("reset"))
            root.bind('<r>', lambda *ignore:senddata("records"))
            root.bind('<a>', lambda *ignore:senddata("author"))


            label0.place_forget()
            label1.place_forget()
            entry0.place_forget()
            entry1.place_forget()
            submitbutton.place_forget()

            root.update()
            getup()

        else:
            messagebox.showinfo("Sign in", "Incorrect login or password")
        sock.close()
    except:
        messagebox.showinfo("Error","Connection error.\nTry later.")


def login():

    global label0, label1, entry0,entry1,submitbutton
    label0 = Label(root, text="Enter your name", width=19, font=("Lato", 15), bg="#d6d6d6", fg="#3a3a3a")
    label0.place(x=10,y=10)
    entry0 = Entry(root, width=19, font=("Lato", 15), cursor="hand2", bg="#F0F0F0", fg="#3a3a3a")
    entry0.place(x=10,y=50)
    label1 = Label(root, text="Enter your password", width=19, font=("Lato", 15), bg="#d6d6d6", fg="#3a3a3a")
    label1.place(x=10,y=100)
    entry1 = Entry(root, width=19, font=("Lato", 15), cursor="hand2", bg="#F0F0F0", fg="#3a3a3a")
    entry1.place(x=10,y=150)
    submitbutton = Button(root, text="Sign in", width=20, fg="#3a3a3a", font=("Lato", 12),  activebackground="#FFFFFF", relief="flat", cursor="hand2", bg="#969696", command=create)
    submitbutton.place(x=21, y=190)
    logbut.place_forget()
    checkin.place_forget()

logbut = Button(root, text="Log in", width=20, fg="#3a3a3a", font=("Lato", 12),  activebackground="#FFFFFF", relief="flat", cursor="hand2", bg="#969696", command=login)
logbut.place(x=21, y=75)
checkin = Button(root, text="Check in", width=20, fg="#3a3a3a", font=("Lato", 12),  activebackground="#FFFFFF", relief="flat", cursor="hand2", bg="#969696", command=login)
checkin.place(x=21, y=150)

root.mainloop()
