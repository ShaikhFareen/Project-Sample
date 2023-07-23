import tkinter
root = tkinter.Tk()
root.title("My Chatbot")

def send():
    send = "You->"+e.get()
    txt.insert(tkinter.END, "n" + send)
    user = e.get().lower()
    if (user=="hello"):
        txt.insert(tkinter.END, '\n' + "Bot->Hi")
    elif(user=="hi" or user=="hii" or user=="hiii"):
        txt.insert(tkinter.END, "\n" + "Bot->Hello")
    elif(e.get()=="how are you"):
        txt.insert(tkinter.END, '\n' + "Bot->Fine! and you")
    elif(user=="fine" or user=="I am good"):
        txt.insert((tkinter.END,'\n'+"Bot->Great! How can I help you today?"))
    else:
        txt.insert(tkinter.END,'\n'+"Bot-> Sorry! I didn't get you.")
    e.delete(0,tkinter.END)
txt=tkinter.Text(root)
txt.grid(row=0,column=0,columnspan=2)
e = tkinter.Entry(root,width=100)
e.grid(row=1,column=0)
send=tkinter.Button(root,text="SEND",command=send).grid(row=1,column=1)
root.mainloop()
