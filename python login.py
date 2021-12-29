# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 12:05:12 2021

@author: Simon
"""

from tkinter import*
import tkinter.messagebox
import mysql.connector

#connecting to db

connectiondb=mysql.connector.connect(host="localhost",user="root",passwd="Ikondani#1",database="logindb")
cursordb=connectiondb.cursor()


def login():
    global root2
    root2=Toplevel(root)
    root2.title("Account login")
    root2.geometry("450x300")
    root2.config(bg="white")
        
    global username_verification
    global password_verification
    Label(root2,text='Please enter your account details',bd=5,font=('arial',12,'bold'),relief="groove",fg="white",bg="blue",width=300).pack()
    username_verification=StringVar()
    password_verification=StringVar()
        
    Label(root2,text="").pack()
    Label(root2,text="Username",fg="black",font=('arial',12,'bold')).pack()
    Entry(root2,textvariable=username_verification).pack()
    Label(root2,text="").pack()
    Label(root2, text="Password",fg="black",font=('arial',12,'bold')).pack()
    Entry(root2,textvariable=password_verification,show="*").pack()
    Label(root2,text="").pack()
    Button(root2,text="Login",bg="blue",fg="white",relief="groove",font=('arial',12,'bold'),command=login_verification).pack()
    Label(root2, text= "")
    
def logged_destroy():
    logged_message.destroy()
    root2.destroy()
    
def failed_destroy():
    failed_message.destroy()
    
def logged():
    global logged_message
    logged_message=Toplevel(root2)
    logged_message.title("WELCOME")
    logged_message.geometry("500x100")
    Label(logged_message,text="logged in succesfully ......welcome{}".format(username_verification.get()),fg="green",font="bold").pack()
    Label(logged_message,text= "").pack()
    Button(logged_message,text="LOGOUT",bg="blue",fg="white",relief="groove",font=('arial',12,'bold'),command=logged_destroy).pack()
    
def failed():
    global failed_message
    failed_message=Toplevel(root2)
    failed_message.title("Invalid message")
    failed_message.geometry("500x100")
    Label(failed_message,text="Invalid username or password",fg="red",font="bold").pack()
    Label(failed_message,text="").pack()
    Button(failed_message,text="ok",bg="blue",fg="white",relief="groove",font=('arial',12,'bold'),command=failed_destroy).pack()
    
def login_verification():
    user_verification=username_verification.get()
    pass_verification=password_verification.get()
    sql= "select*from usertable where username=%s and password=%s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results=cursordb.fetchall()
    
    if results:
        for i in results:
            logged()
            break
        else:
            failed()
            
def Exit():
    wayOut=tkinter.messagebox.askyesno("Login System","Do you want to exit the system?")
    if wayOut & gt==0:
        root.destroy()
        
        return
    
def main_display():
    global root
    root=Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("600x600")
    Label(root,text="WELCOME TO LOGIN SYSTEM",bd=20,font=('arial',20,'bold'),relief="groove",fg="white",bg="blue",width=400).pack()
    Label(root,text="").pack()
    Button(root,text="LOG IN",height="1",width="20",bd=8,font=('arial',12,'bold'),relief="groove",fg="white",bg="blue",command=login).pack()
    Label(root,text="").pack()
    Button(root,text="EXIT",height="1",width="20",bd=8,font=('arial',12,'bold'),relief="groove",fg="white",bg="blue",command=Exit).pack()
    Label(root,text="").pack()
    
main_display()
root.mainloop()
    
    