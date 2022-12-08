from tkinter import *
from tkinter import messagebox
import ast

pen = Tk()
pen.title("Kayıt Ol")
pen.geometry("925x500+300+200")
pen.configure(bg="#ffffff")
pen.resizable(False,False)

def singup():
    username = user.get()
    password=code.get()
    conform_password=conform_code.get()

    if password==conform_password:
        try:
            dosya = open("data.txt", "r+")
            d=dosya.read()

            r = ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            dosya.truncate(0)
            dosya.close()
            dosya = open("data.txt","w")
            w=dosya.write(str(r))
            messagebox.showinfo("Kayıt","Başarılı !")
        except:
            dosya = open("data.txt","w")
            pp=str({"\nUsername":"password"})
            dosya.write(pp)
            dosya.close()
    else:
        messagebox.showerror("Hata!!!","Hatalı Bilgiler")



img = PhotoImage(file="11.png")
Label(pen,image=img,border=0,bg="white").place(x=50,y=90)

frame = Frame(pen,width=350, height=390,bg="#ffffff")
frame.place(x=480,y=50)

heading = Label(frame,text="Kayıt Ol", fg="#57a1f8",bg="white",font=('Microsoft Yahei UI Light', 23 , 'bold'))
heading.place(x=100,y=5)




#-----------------------------#

def on_enter(e):
    user.delete(0,"end")
def on_leave(e):
    if user.get()=="":
        user.insert(0,"Kullanıcı Adı")

user = Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0, "Kullanıcı Adı")
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=107)



#-----------------------------#

def on_enter(e):
    code.delete(0,"end")
def on_leave(e):
    if code.get()=="":
        code.insert(0,"Şifre")

code = Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0, "Şifre")
code.bind("<FocusIn>",on_enter)
code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=177)




#-----------------------------#

def on_enter(e):
    conform_code.delete(0,"end")
def on_leave(e):
    if conform_code.get()=="":
        conform_code.insert(0,"Şifreni Doğrula")

conform_code = Entry(frame,width=25,fg="black",border=0,bg="white",font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0, "Şifreni Doğrula")
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind("<FocusOut>",on_leave)

Frame(frame,width=295,height=2,bg="black").place(x=25,y=247)

#-----------------------------#

Button(frame,width=39,pady=7,text="Kayıt Ol",bg="#57a1f8",fg="white",border=0,command=singup).place(x=35,y=280)
label=Label(frame,text="Bir Hesaba Sahibim",fg="black",bg="white",font=("Microsoft YaHei UI Light",9))
label.place(x=90,y=340)

singin=Button(frame,width=6,text="Kayıt Ol",border=0,bg="white",cursor="hand2",fg="#57a1f8")
singin.place(x=200,y=340)
pen.mainloop()