from Tkinter import *
import tkMessageBox, pickle, ttk, os

class win1(Tk):
    new=None
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        lab1=Label(self,text='Welcome to',font=('Comic Sans MS',35),fg='red',width=13)
        lab1.pack()
        lab2=Label(self,text='Music Library',font=('Comic Sans MS',50,'bold'),fg='#994483',width=13)
        lab2.pack()
        lab1=Label(self,text='Creators---                    ',font=('Times',35,'bold'),fg='green',width=17,justify='right')
        lab1.pack()
        lab1=Label(self,text='        Kshitiz Gehlot(XII A)',font=('Verdana',30),fg='lightgreen',width=23)
        lab1.pack()
        lab1=Label(self,text='        Pratham Jain(XII A)',font=('Verdana',30),fg='lightgreen',width=23)
        lab1.pack()
        bottom=Frame()
        bottom.pack()
        but=Button(bottom,text='NEW USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=24,cursor='hand2',
                   activebackground='#86cc64',command=self.open1)
        but.pack(side='left')
        but=Button(bottom,text='EXISTING USER',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=24
                   ,cursor='hand2',
                   activebackground='#86cc64',command=self.open2)
        but.pack(side='right')

    def open1(self,*arg):
        self.destroy()
        win2().mainloop()

    def open2(self,*arg):
        self.destroy()
        root=Tk()
        clas=login(root)
        win1.new=clas.user
        existing(win1.new).mainloop()

class win2(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        self.lab1=Label(text='ENTER YOUR DETAILS FOR NEW ID',font=('Times',17,'bold'),fg='#15633b')
        self.lab1.grid(row=1,column=1,columnspan=2)
        
        self.lab2=Label(text='Username',font=('Times',17),fg='#14b863')
        self.lab2.grid(row=2,column=1)
        self.txt1=Entry(bd=4,width=20,font=('Verdana',12))
        self.txt1.grid(row=2,column=2)
        
        
        self.lab3=Label(text='Password',font=('Times',17),fg='#14b863')
        self.lab3.grid(row=3,column=1)
        self.txt2=Entry(bd=5,width=20,font=('Verdana',12),show='*')
        self.txt2.grid(row=3,column=2)
        
        self.lab4=Label(text='Contact No.',font=('Times',17),fg='#14b863')
        self.lab4.grid(row=4,column=1)
        self.txt3=Entry(bd=5,width=20,font=('Verdana',12))
        self.txt3.grid(row=4,column=2)
        
        self.lab5=Label(text='City',font=('Times',17),fg='#14b863')
        self.lab5.grid(row=5,column=1)
        self.txt4=Entry(bd=5,width=20,font=('Verdana',12))
        self.txt4.grid(row=5,column=2)
        
        self.lab6=Label(text='Email',font=('Times',17),fg='#14b863')
        self.lab6.grid(row=6,column=1)
        self.txt5=Entry(bd=5,width=20,font=('Verdana',12))
        self.txt5.grid(row=6,column=2)
        
        self.txt1.bind('<Return>',self.call2)
        self.txt2.bind('<Return>',self.call3)
        self.txt3.bind('<Return>',self.call4)
        self.txt4.bind('<Return>',self.call5)
        self.txt5.bind('<Return>',self.call6)

        self.but=Button(self,text='BACK',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=15,cursor='hand2',
                   activebackground='#86cc64',command=self.back)
        self.but.grid(row=7,column=1)
        self.but=Button(self,text='DONE',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=15,cursor='hand2',
                   activebackground='#86cc64',command=self.done)
        self.but.grid(row=7,column=2)
        self.txt1.focus_set()

        
    def call2(self,*arg):
        return self.txt2.focus_set()

    def call3(self,*arg):
        return self.txt3.focus_set()

    def call4(self,*arg):
        return self.txt4.focus_set()

    def call5(self,*arg):
        return self.txt5.focus_set()

    def call6(self,*arg):
        return self.but.invoke()

    def done(self,*arg):
        self.user=self.txt1.get()
        if self.user=='':
            return tkMessageBox.showinfo('Error','Enter a username')
        self.password=self.txt2.get()
        if self.password=='':
            return tkMessageBox.showinfo('Error','Enter a password')
        self.contact=self.txt3.get()
        if self.contact=='':
            return tkMessageBox.showinfo('Error','Enter a contact')
        try:
            tmp=self.contact
            int(tmp)
        except ValueError:
            return tkMessageBox.showinfo('Error','Contact No. Should Be Integer')
        self.city=self.txt4.get()
        if self.user=='':
            return tkMessageBox.showinfo('Error','Enter a city')
        self.email=self.txt5.get()
        if self.user=='':
            return tkMessageBox.showinfo('Error','Enter an email')
        f=open('users.log','rb')
        while True:
            try:
                user=pickle.load(f)
                if user.name==self.user:
                    return tkMessageBox.showinfo('Error','Username Already Exists')

            except EOFError:
                f.close()
                break
            
        f=open('users.log','ab')
        new=new_file(name=self.user, password=self.password, contact=self.contact, city=self.city, email=self.email)
        pickle.dump(new,f)
        f.close()
        self.back()
    
    def back(self):
        self.destroy()
        win1()

class song_select(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        self.flag=0
        self.selected_songs=[]
        f=open('user_songs.dat','rb')
        fn=open('tmp.dat','ab')
        while True:
            try:
                d=pickle.load(f)
                for key in d:
                    if key==win1.new:
                            self.selected_songs=d[win1.new]
                    else:
                        pickle.dump(d,fn)
            except EOFError:
                break
        f.close()
        fn.close()
        os.remove('user_songs.dat')
        os.rename('tmp.dat','user_songs.dat')
    
        f=open('songs.dat','rb')
        self.data=pickle.load(f)
        f.close()

        self.selected_movie=StringVar(self)
        self.selected_movie.set('Choose a movie')
        
        self.top_tab=Frame()
        self.top_tab.pack()
        
        
        self.content1()
        

    def content1(self):
        self.cont2=Frame()
        self.cont2.pack()
        self.cont=Frame()
        self.cont.pack()
        
        self.drop=ttk.Combobox(self.cont2,values=self.data.keys(),textvariable=self.selected_movie,font=('Times',15),width=40,
                      cursor='hand2',state='readonly')
        self.but=Button(self.cont2,text='OK',font=('times',12,'bold'),fg='#436632',bg='#abcdef',cursor='hand2',width=6,
                   activebackground='#86cc64',command=self.content2)
        self.but.pack(side='right')
        self.drop.pack(side='left')
        
        self.lab=Label(self.cont,text='Choose A\nMovie\nTo Continue\n(You Can Select\nSongs From\nMultiple Movies)',
                       font=('Courier',30,'bold'),fg='#792834',width=18)
        self.lab.pack(side='top')
        self.but=Button(self.cont,text='BACK',font=('times',20,'bold'),fg='#436632',bg='#abcdef',cursor='hand2',width=15,
                   activebackground='#86cc64',command=self.back)
        self.but.pack(side='left')
        if self.flag==1:
            self.but2=Button(self.cont,text='DONE',font=('times',20,'bold'),fg='#436632',bg='#abcdef',cursor='hand2',
                             width=15,activebackground='#86cc64',command=self.callback2)
            self.but2.pack(side='right')
        

    def content2(self):
        self.cont.destroy()
        self.cont2.destroy()
        self.flag=1
        self.cont=Frame()
        self.cont.pack()

        self.movie=self.selected_movie.get()
        self.songs=self.data[self.movie]
        self.info=Label(self.cont,text='Select the Songs',font=('Courier',23,'bold'),fg='#792834')
        self.info.pack()
        self.list=Listbox(self.cont,selectmode='multiple',font=('times',20,'bold'),cursor='hand2',bd=5)
        self.list.pack()

        for i in range(len(self.songs)):
            self.list.insert(i,self.songs[i])
            if self.songs[i] in self.selected_songs:
                self.list.selection_set(i)
                self.selected_songs.remove(self.songs[i])
        self.but2=Button(self.cont,text='NEXT',font=('times',20,'bold'),fg='#436632',bg='#abcdef',cursor='hand2',width=25,
                   activebackground='#86cc64',command=self.callback)
        self.but2.pack(side='bottom')

    def callback(self):
        self.tpl=self.list.curselection()
        for pos in self.tpl:
            self.selected_songs.append(self.songs[pos])
        self.cont.destroy()
        self.content1()

    def back(self):
        self.destroy()
        self.selection={win1.new:self.selected_songs}
        f=open('user_songs.dat','ab')
        pickle.dump(self.selection,f)
        f.close()
        existing(win1.new).mainloop()
        

    def callback2(self):
        self.back()

        


class new_file(object):
    def __init__(self ,name ,password ,city ,email ,contact):
        self.name=name
        self.password=password
        self.city=city
        self.email=email
        self.contact=contact

class login():
    def __init__(self,root):
        self.users={}
        self.root=root
        f=open('users.log','rb')
        while True:
            try:
                user=pickle.load(f)
                self.users[user.name]=user.password

            except EOFError:
                f.close
                break

        self.cont=Frame(self.root)
        self.cont.pack()
        self.name=StringVar()
        self.pasw=StringVar()
        self.head=Label(self.cont,text='LOGIN',font=('Times',45,'bold'),fg='#546775')
        self.head.grid(row=1,column=1,columnspan=2)
        self.lab1=Label(self.cont,text='USERNAME',font=('Courier',15,'bold'),fg='#792834')
        self.lab1.grid(row=2,column=1)
        self.ent1=Entry(self.cont,bd=5,font=('Courier',15,'bold'),textvariable=self.name
                        )
        self.ent1.grid(row=2,column=2)
        self.ent1.focus_set()
        self.lab2=Label(self.cont,text='PASSWORD',font=('Courier',15,'bold'),fg='#792834')
        self.lab2.grid(row=3,column=1)
        self.ent2=Entry(self.cont,bd=5,font=('Courier',15,'bold'),show='*',textvariable=self.pasw)
        self.ent2.grid(row=3,column=2)
        self.but=Button(self.cont,text='Login',font=('Courier',25,'bold'),fg='cyan',command=self.callback)
        self.but.grid(row=4,column=1,columnspan=2)

        self.ent1.bind('<Return>',self.move1)
        self.ent2.bind('<Return>',self.move2)
        self.root.mainloop()


    def move1(self,*arg):
        return self.ent2.focus_set()

    def move2(self,*arg):
        return self.but.invoke()

    def callback(self):
        complete=False
        for user in self.users:
            if self.name.get()==user and self.pasw.get()==self.users[user]:
                complete=True
                self.root.destroy()
                self.user=user
                return
        if not complete:
            com=tkMessageBox.askyesno(title='Wrong Password',message='WRONG PASSWORD!!!!  Do you want to retry?')
            if com:
                self.ent2.delete(0,END)
            else:
                self.root.destroy()
                win1.win1()

class existing(Tk):
    def __init__(self,name,*arg):
        Tk.__init__(self,*arg)
        self.name=name
        lab1=Label(self,text='Welcome',font=('Comic Sans MS',50),fg='red',width=13)
        lab1.pack()
        lab2=Label(self,text='Mr.'+name,font=('Comic Sans MS',50,'bold'),fg='#994483',width=13)
        lab2.pack()
        bottom=Frame()
        bottom.pack()
        but=Button(bottom,text='Song Select',font=('Courier',20,'bold'),fg='#436632',bg='#abcdef',width=20,cursor='hand2',
                   activebackground='#86cc64',command=self.open1)
        but.grid(row=1,column=1)
        but=Button(bottom,text='Modify Details',font=('Courier',20,'bold'),fg='#436632',bg='#abcdef',width=20,cursor='hand2',
                   activebackground='#86cc64',command=self.open2)
        but.grid(row=1,column=2)
        but=Button(bottom,text='Delete User',font=('Courier',20,'bold'),fg='#436632',bg='#abcdef',width=20,cursor='hand2',
                   activebackground='#86cc64',command=self.open3)
        but.grid(row=2,column=1)
        but=Button(bottom,text='View selected songs',font=('Courier',20,'bold'),fg='#436632',bg='#abcdef',width=20,cursor='hand2',
                   activebackground='#86cc64',command=self.open4)
        but.grid(row=2,column=2)
        but=Button(bottom,text='Back',font=('Courier',20,'bold'),fg='#436632',bg='#bbcdef',width=12,cursor='hand2',
                   activebackground='#86cc64',command=self.back)
        but.grid(row=3,column=1,columnspan=2)

    def open1(self,*arg):
        self.destroy()
        song_select().mainloop()

    def open2(self,*arg):
        self.destroy()
        change(self.name).mainloop()

    def open3(self,*arg):
        self.destroy()
        f=open('users.log','rb')
        fn=open('temp.log','wb')
        while True:
            try:
                user=pickle.load(f)
                if new!=user.name:
                    pickle.dump(user,fn)

            except EOFError:
                f.close()
                fn.close()
                break
        os.remove('users.log')
        os.rename('temp.log','users.log')
        win1().mainloop()

    def open4(self,*arg):
        self.destroy()
        show().mainloop()

    def back(self):
        self.destroy()
        win1().mainloop()

    


class change(Tk):
    def __init__(self,new,*arg):
        if new==None:
            return
        Tk.__init__(self,*arg)
        f=open('users.log','rb')
        self.new=new
        self.name=StringVar()
        self.pasw=StringVar()
        self.contact=StringVar()
        self.city=StringVar()
        self.email=StringVar()
        while True:
            try:
                user=pickle.load(f)
                if new==user.name:
                    self.name.set(user.name)
                    self.pasw.set(user.password)
                    self.contact.set(user.contact)
                    self.city.set(user.city)
                    self.email.set(user.email)
                    

            except EOFError:
                f.close()
                break
        
        self.lab1=Label(text='UPDATE YOUR DETAILS U WANT TO CHANGE',font=('Times',17,'bold'),fg='#15633b')
        self.lab1.grid(row=1,column=1,columnspan=2)
        
        self.lab2=Label(text='Username',font=('Times',17),fg='#14b863')
        self.lab2.grid(row=2,column=1)
        self.txt1=Entry(bd=4,width=20,font=('Verdana',12),textvariable=self.name)
        self.txt1.grid(row=2,column=2)
        
        self.lab3=Label(text='Password',font=('Times',17),fg='#14b863')
        self.lab3.grid(row=3,column=1)
        self.txt2=Entry(bd=5,width=20,font=('Verdana',12),textvariable=self.pasw)
        self.txt2.grid(row=3,column=2)
        
        self.lab4=Label(text='Contact No.',font=('Times',17),fg='#14b863')
        self.lab4.grid(row=4,column=1)
        self.txt3=Entry(bd=5,width=20,font=('Verdana',12),textvariable=self.contact)
        self.txt3.grid(row=4,column=2)
        
        self.lab5=Label(text='City',font=('Times',17),fg='#14b863')
        self.lab5.grid(row=5,column=1)
        self.txt4=Entry(bd=5,width=20,font=('Verdana',12),textvariable=self.city)
        self.txt4.grid(row=5,column=2)

        self.lab6=Label(text='Email',font=('Times',17),fg='#14b863')
        self.lab6.grid(row=6,column=1)
        self.txt5=Entry(bd=5,width=20,font=('Verdana',12),textvariable=self.email)
        self.txt5.grid(row=6,column=2)
        
        self.txt1.bind('<Return>',self.call2)
        self.txt2.bind('<Return>',self.call3)
        self.txt3.bind('<Return>',self.call4)
        self.txt4.bind('<Return>',self.call5)
        self.txt5.bind('<Return>',self.call6)
        self.but=Button(self,text='BACK',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=15,cursor='hand2',
                   activebackground='#86cc64',command=self.back)
        self.but.grid(row=7,column=1)

        self.but=Button(self,text='DONE',font=('Courier',15,'bold'),fg='#436632',bg='#abcdef',width=15,cursor='hand2',
                   activebackground='#86cc64',command=self.callback)
        self.but.grid(row=7,column=2)

        
    def call2(self,*arg):
        return self.txt2.focus_set()

    def call3(self,*arg):
        return self.txt3.focus_set()

    def call4(self,*arg):
        return self.txt4.focus_set()

    def call5(self,*arg):
        return self.txt5.focus_set()

    def call6(self,*arg):
        return self.but.invoke()

    def callback(self,*arg):
        f=open('users.log','rb')
        fn=open('temp.log','wb')
        while True:
            try:
                user=pickle.load(f)
                if self.new==user.name:
                    name=self.name.get()
                    pas=self.pasw.get()
                    contact=self.contact.get()
                    email=self.email.get()
                    city=self.city.get()
                    user=new_file(name ,pas ,city ,email ,contact)
                pickle.dump(user,fn)

            except EOFError:
                f.close()
                fn.close()
                break
        os.remove('users.log')
        os.rename('temp.log','users.log')
        self.back()

    def back(self):
        self.destroy()
        existing(win1.new).mainloop()
        
class show(Tk):
    def __init__(self,*arg):
        Tk.__init__(self,*arg)
        f=open('user_songs.dat','rb')
        self.selected_songs=[]
        while True:
            try:
                d=pickle.load(f)
                for key in d:
                    if key==win1.new:
                            self.selected_songs=d[win1.new]
            except EOFError:
                break
        f.close()
        self.info=Label(self,text='Here are your songs',font=('Courier',23,'bold'),fg='#792834')
        self.info.pack()
        self.frame=Frame()
        self.frame.pack()
        self.sc=Scrollbar(self.frame)
        self.sc.pack(side=RIGHT,fill=Y)
        self.list=Listbox(self.frame,font=('times',20,'bold'),cursor='hand2',bd=5,height=10,yscrollcommand=self.sc.set)
        self.list.pack(side=LEFT,fill=BOTH)

        for i in self.selected_songs:
            self.list.insert(END, i)
        self.sc.config(command=self.list.yview)
        self.but2=Button(self,text='BACK',font=('times',20,'bold'),fg='#436632',bg='#abcdef',cursor='hand2',width=25,
                   activebackground='#86cc64',command=self.callback)
        self.but2.pack()

    def callback(self):
        self.destroy()
        existing(win1.new).mainloop()

app=win1()
app.mainloop()
