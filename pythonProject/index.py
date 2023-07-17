from tkinter import *
import pymysql

# print(dir()) ## Find all the attributes 

##function To get the quiz page
def getQuiz(record):
    print(record)
    messagebox.showinfo('show info',"Welcome to Home page")
    guiWindow = Tk()
    guiWindow.geometry("1000x400")
    guiWindow.title("Jithon Sujit")
    class myQuiz:
        def __init__(self):
            self.quesNumber =0;
            self.displayTitle()
            self.displayQuestion()
            self.optSelected = IntVar() 
            self.options = self.radioButton()
            self.displayButton()
            self.button()
            self.dataSize= len(question)
            x = len(question)
            self.rightAns = 0
        def _displayResult(self):
            wrongCount = self.dataSize -self.rightAns
            rightAns = f"Correct :{self.rightAns}"
            wrongAns = f"Wrong : {self.wrongCount}"
            the_score = int(self.rightAns/self.dataSize * 100)
            the_result = f"Score : {the_score}"
            mb.showinfo("Result ",f"{the_result}\n {rightAns} \n {wrongAns}")
            def checkAnswer(self,quesNumber):
                if self.optSelected.get()==answer[quesNumber]:return true
        def nextButton(self):
            if(self.checkAnswer(self.quesNumber)):self.rightAns+=1
            self.quesNumber+=1
            if self.quesNumber == self.dataSize:
                self._displayResult()
                guiWindow.destroy()
            else:
                self.displayQuestion()
                self.displayOptions() 

        def buttons(self):
            next_button = Button(guiWindow,text="Next",
            command=self.nextButton,
            width=10,
            bg="blue",
            fg="white",
            font=("ariel",16,"bold"))
            next_button.place(x=350,y=380)
            
            quit_button = Button(guiWindow,text="Quit",
            command=guiWindow.destroy,
            width=10,
            bg="blue",
            fg="white",
            font=("ariel",16,"bold"))
            quit_button.place(x = 500,y=380)
        
        def displayOptions(self):
            val = 0
            self.optSelected = set(0)
            for opt in opts[self.quesNumber]:
                self.options[val]['text'] = opt
                val+=1
        def displayQuestion(self):
            quesNumber = Label(guiWindow,
            text = question[self.quesNumber],
            witdh=60,
            font=('ariel',16,'bold'),anchor='w')
            quesNumber.place(x=70,y=100)        
        def displayTitle(self):
            myTitle

##function to handle the login details
def Login():
    x = user_name.get()
    y = user_password.get()
    # print(x,"->",y)
    connObj = pymysql.connect(host="localhost",user="root",password="")
    curObj = connObj.cursor()
    curObj.execute('use cs_py_project');
    query = f'select uid,password from student where uid="{x}" or password="{y}";'
    curObj.execute(query)
    record = curObj.fetchall()
    # print(record)
    Exit();
    getQuiz(record);



##Function to exit the window
def Exit():
   win.destroy()


##Function for new user registration page
def newUser():
    win1 = Tk()
    win1.title("Signup | User")
    win1.configure(
        bg="#20262E"
    )
    win1.geometry('700x600')
    win1.maxsize(700,700)
    win1.minsize(700,700)

    Label(win1,text = "Register Here",
    font=("Bell MT",20),
    bg="#579BB1",
    fg="white",
    width="43",
    height="2").place(x=0,y=0)

    l1 = Label(win1,text = "Enter first name",
    font=("Bell MT",16),
    bg="#579BB1",
    fg="white",
    width="20",
    height="2")
    l1.place(x=50,y=100)

    first_name=Entry(win1,
    font=("Bell MT",16),
    bg="white",
    fg="black",width="20")
    first_name.place(x=350,y=110)

    Label(win1,text = "Enter Last Name:",
    font=("Bell MT",16),
    bg="#579BB1",
    fg="white",
    width="20",
    height="2").place(x=50,y=170)

    last_name = Entry(win1,
    font=('Bell MT',16),
    bg="white",
    fg="black",
    width="20")
    last_name.place(x=350,y=180)
    
    Label(win1,text = "Enter User Id:",
    font=("Bell MT",16),
    bg="#579BB1",
    fg="white",
    width="20",
    height="2").place(x=50,y=240)

    uid = Entry(win1,
    font=('Bell MT',16),
    bg="white",
    fg="black",
    width="20")
    uid.place(x=350,y=250)

    Label(win1,text = "Enter password:",
    font=("Bell MT",16),
    bg="#579BB1",
    fg="white",
    width="20",
    height="2").place(x=50,y=310)

    password = Entry(win1,
    font=('Bell MT',16),
    bg="white",
    fg="black",
    width="20")
    password.place(x=350,y=320)

    Label(win1,text = "Gender:",
    font=("Bell MT",16),
    bg="#579BB1",
    fg="white",
    width="20",
    height="2").place(x=50,y=380)

    gender=Entry(win1,
    font=("Bell MT",16),
    bg="white",
    fg="black",width="20")
    gender.place(x=350,y=390);
    # r1 = Radiobutton(win1,
    # text="Male",
    # value="Male",
    # bg="#20262E",
    # fg="white")

    # r2 = Radiobutton(win1,
    # text="Female",
    # value="Female",
    # bg="#20262E",
    # fg="white")

    # r3 = Radiobutton(win1,
    # text="Other",
    # value="Other",
    # bg="#20262E",
    # fg="white")

    # r1.place(x=350,y=390)
    # r2.place(x=450,y=390)
    # r3.place(x=550,y=390)


    def ExitPage():
        win1.destroy();
    exitBtn = Button(win1,
    text = "Exit",
    font=("Bell MT",10),
    bg="#E90064",
    fg="white",
    width="15",
    height="2",
    command=ExitPage)
    exitBtn.place(x=450,y=450) 


    ## Submit the data to the DB
    def SubmitData():
        fname = first_name.get()
        lname = last_name.get()
        userid= uid.get()
        passWord = password.get();
        gen = gender.get();
        # print(fname," ",lanme," ",userid,"  ",passWord)
        connObj = pymysql.connect(host="localhost",user="root",password="");
        curObj = connObj.cursor()
        curObj.execute('use cs_py_project');
        query ='insert into student (fname,lname,uid,password,gender)values("{fname}","{lname}","{uid}","{Pass}","{gender}");'.format(fname=fname,lname=lname,uid=userid,Pass=passWord,gender=gen)
        # print(query)
        curObj.execute(query)
        curObj.execute('commit')
        curObj.close()
        connObj.close()
        win1.destroy()
    
    
    ## Submit Button
    submit = Button(win1,
    text = "submit",
    font=("Bell MT",10),
    bg="#54B435",
    fg="white",
    width="15",
    height="2",
    command=SubmitData)
    submit.place(x=250,y=450) 

    win1.mainloop()   




#Create a window
win = Tk() #Win is a object of TK() class

win.title("Home Page")
win.configure(bg="#20262E")

#set size of the window
win.geometry('700x600')


#create a lebel
Label(win,text = "Please Login Here",
    font=("Bell MT",20),
    bg="#579BB1",
    fg="white",
    width="43",
    height="2").grid(row=1,column=1)

Label(win,
    text = "Enter User Id / Regno",
    font=("Bell MT",16),
    bg="#143F6B",
    fg="white",
    width="20",
    height="2").place(x=20,y=100)
user_name=Entry(win,
    font=("Bell MT",16),
    bg="white",
    fg="black",width="20")
user_name.place(x=300,y=110)    


Label(win,
    text = "Enter Password",
    font=("Bell MT",16),
    bg="#143F6B",
    fg="white",
    width="20",height="2").place(x=20,y=200)
user_password = Entry(win,
    font=("Bell MT",16),
    bg="white",
    fg="black",
    width="20",
    show="*")
user_password.place(x=300,y=220)    
Button(win,
    text = "New Register/sign up",
    font=("Bell MT",10),
    bg="#E90064",
    fg="white",
    width="15",
    height="2",
    command=newUser).place(x=100,y=280)  

Button(win,
    text = "Login",
    font=("Bell MT",16)
    ,bg="#54B435",
    fg="white",
    width="10",
    height="1",
    command=Login).place(x=250,y=280)
Button(win,
    text = "Exit",
    font=("Bell MT",16),
    bg="#E90064",
    fg="white",
    width="10",
    height="1",
    command=Exit).place(x=400,y=280)






win.mainloop()