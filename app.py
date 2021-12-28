from tkinter import *

import subprocess

class App():
    def __init__(self,app):
        self.app=app
        self.app.geometry("400x200")
        self.app.title("Pip GUI")

        #Main Frame
        mainFrame=Frame(background='black',bd=5,relief=SOLID)
        mainFrame.pack(expand=True,fill=BOTH)
        
        lbl=Label(mainFrame,text="Pip GUI",background='black',foreground='white',bd=5,relief=SUNKEN,font=("cascadia code",13,"bold")).pack(side=TOP,fill=X)

        module_lbl=Label(mainFrame,text="Module:",background="black",foreground="white",font=("cascadia code",13,"bold"))
        module_lbl.place(x=60,y=60)
        self.module_txt=Entry(mainFrame,background='black',foreground='white',insertbackground='white',bd=3,relief=SUNKEN)
        self.module_txt.place(x=200,y=65)
        
        install_btn=Button(mainFrame,text="Install",background="black",foreground="white",command=self.install_module,bd=3,relief=SUNKEN,font=("cascadia code",12,"bold"))
        install_btn.place(x=160,y=130)
    def install_module(self):
        result=subprocess.run(["pip","install",f"{self.module_txt.get()}"],capture_output=True)
        if result.stdout == None:
            print("No output")
        if result.stderr == None:
            print("No error")    
        print(f"{self.module_txt.get()} installed")
            
app=Tk()
constructor=App(app)
app.mainloop()        