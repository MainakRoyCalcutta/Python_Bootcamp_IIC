from tkinter import *
import socket

window = Tk()

frame1 = Frame(master=window, bg="cyan")
frame1.pack(fill=BOTH, side=LEFT, expand=False)

window.title("HOST")
s = socket.socket()
host = socket.gethostname()
print(host)
label2 = Label(master=frame1, text="Your connection server is starting on: " + f"{host}", bg="red")
label2.grid(row=0, column=0, sticky=W)
port = 1025

s.bind((host, port))

label3 = Label(master=frame1, text="Server is ready to accept", bg="blue")
label3.grid(row=1, column=0, sticky=W)
s.listen(1)
connection, addr = s.accept()
print(addr)
label4 = Label(master=frame1, text="Connection established to address: " + f"{addr}", bg="green")
label4.grid(row=2, column=0, sticky=W)

_ = StringVar()

entry1 = Entry(master=frame1, textvariable=_)
entry1.grid(row=3, column=0, sticky=W)


def send():
    global j, k
    rn = j

    x = str(_.get())
    label5 = Label(master=frame1, text=x)
    label5.grid(row=rn, column=0, sticky=W)
    message = x
    message = message.encode()
    connection.send(message)
    entry1.delete(0, END)

    j = j + 2
    """
    cn = k
    incoming_message = connection.recv(1025)
    incoming_message = incoming_message.decode()
    label6 = Label(master=frame1, text=incoming_message)
    label6.grid(row=cn, column=1, sticky=E)
    k = k + 2
    """


j = 4
k = 5

button1 = Button(master=frame1, text="SEND", command=send)
button1.grid(row=3, column=1, sticky=E)

window.mainloop()
