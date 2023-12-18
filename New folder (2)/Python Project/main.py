from tkinter import *

from tkinter import ttk
from tkinter import messagebox
import pymysql

#####################Functions

def login_window():
    root.destroy()
    import login

def clear():
    entryEmail.delete(0, END)
    entrycontact.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryfirstname.delete(0, END)
    entrylastname.delete(0, END)
    entryAnswer.delete(0, END)
    comboquestion.current(0)
    check.set(0)

def register():
    if entryfirstname.get()=='' or entrylastname.get=='' or entryEmail.get()==''or entrycontact.get()==''\
        or entrypassword.get()=='' or entryconfirmpassword.get()=='' or comboquestion.get()=='Select' or\
            entryAnswer.get()=='':
        messagebox.showerror('Error','All Fields Are Required')

    elif entrypassword.get()!=entryconfirmpassword.get():
        messagebox.showerror('Error','Password Mismatch')

    elif check.get()==0:
        messagebox.showerror('Error','Please agree to our terms and condtions')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='root',database='register')
            cur=con.cursor()
            cur.execute('select * from student where email=%s',entryEmail.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror('Error','User Already Exists')

            else:
                cur.execute('insert into student (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)',
                            (entryfirstname.get(), entrylastname.get(), entrycontact.get(), entryEmail.get(),
                             comboquestion.get(),entryAnswer.get(), entrypassword.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Sucess','Registration is successful')
                clear()
                root.destroy()
                import login

        except Exception as e:
            messagebox.showerror('error',f'Error due to {e}')
#####################GUI

root=Tk()

root.geometry('1350x710')
root.title('Registration Form')
bgimage=PhotoImage(file='images/bg.png')
bgLabel=Label(root,image=bgimage)
bgLabel.place(x=0,y=0)

registerFrame=Frame(root,width=650,height=650)
registerFrame.place(x=630,y=30)

titleLabel=Label(registerFrame,text="Registration Form",font=('arial',22,'bold'),fg='gold')
titleLabel.place(x=28,y=5)

firstnameLabel=Label(registerFrame,text='First Name',font=('times new roman',18,'bold'),fg='gray20')
firstnameLabel.place(x=20,y=80)
entryfirstname=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entryfirstname.place(x=20,y=115)

lastnameLabel=Label(registerFrame,text='Last Name',font=('times new roman',18,'bold'),fg='gray20')
lastnameLabel.place(x=370,y=80)
entrylastname=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entrylastname.place(x=370,y=115)

contactLabel=Label(registerFrame,text='Contact',font=('times new roman',18,'bold'),fg='gray20')
contactLabel.place(x=20,y=200)
entrycontact=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entrycontact.place(x=20,y=235)

emailLabel=Label(registerFrame,text='Email',font=('times new roman',18,'bold'),fg='gray20')
emailLabel.place(x=370,y=200)
entryEmail=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entryEmail.place(x=379,y=235)

questionLabel=Label(registerFrame,text='Security Question',font=('times new Roman',18,'bold'),fg='gray20')
questionLabel.place(x=20,y=320)

comboquestion=ttk.Combobox(registerFrame,font=('times new roman',16),state='readonly')
comboquestion['values']=('Select','Your First Name?','Your Birth Place?','Your Best Friend?',
                         'Your Favourite Teacher?','Your Favourite Hobby?')

comboquestion.place(x=20,y=350)
comboquestion.current(0)



answerLabel=Label(registerFrame,text='Answer',font=('times new Roman',18,'bold'),fg='gray20')
answerLabel.place(x=370,y=320)
entryAnswer=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entryAnswer.place(x=379,y=350)

passwordLabel=Label(registerFrame,text='Password',font=('times new Roman',18,'bold'),fg='gray20')
passwordLabel.place(x=20,y=440)
entrypassword=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entrypassword.place(x=20,y=475)

confirmpasswordLabel=Label(registerFrame,text='Confirm Password',font=('times new Roman',18,'bold'),fg='gray20')
confirmpasswordLabel.place(x=370,y=440)
entryconfirmpassword=Entry(registerFrame,font=('times new roman',18),bg='lightgray')
entryconfirmpassword.place(x=370,y=475)

check=IntVar()
checkButton= Checkbutton(registerFrame, text='I Agree All The Terms & Conditions',  onvalue=1,
                          offvalue=0,variable=check, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=20, y=530)

buttonimage=PhotoImage(file='images/button.png')
registerButton=Button(registerFrame,image=buttonimage,bd=0,cursor='hand2',command=register)
registerButton.place(x=250,y=580)

loginimage=PhotoImage(file='images/login.png')
loginButton=Button(root,image=loginimage,bd=0,bg='gold',cursor='hand2',command=login_window)
loginButton.place(x=240,y=330)








root.mainloop()