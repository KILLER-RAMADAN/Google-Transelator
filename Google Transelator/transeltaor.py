import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import googletrans
from googletrans import Translator
import pyperclip
import sys
from tkinter import ttk
from tkinter.ttk import *
import webbrowser





class transeltor(tk.Tk):
    
    
    def translate_text(self):
      try:
        if self.lang_text1_place.get(1.0,"end")=="" or self.compo1.get()=="":
            messagebox.showerror("Google Transelator","Select Transelating Language....")
        else:
         self.gettext=self.lang_text1_place.get(1.0,"end")
         Translate=Translator()
         translate_text_from_text1=Translate.translate(self.gettext,src=self.compo1.get(), dest=self.compo2.get())
         self.lang_text2_place.delete(1.0,"end")
         self.lang_text2_place.insert(1.0,translate_text_from_text1.text)
      except:
          messagebox.showerror("Google Transelator","1)Select Transelating Language\n2)Enter Any Thing To Translate!\n3)Make Sure About Your Connection!!")
    def copy(self):
        if self.lang_text2_place.get(0.0,"end")=="":
            return ""
        else:
         pyperclip.copy(self.lang_text2_place.get(1.0,"end"))
         spam = pyperclip.paste()
         messagebox.showinfo("Google Transelator","copied to clipboard!!!!")
        
    def destroy(self):
        sys.exit()
    
    
    
    def change_label(self):
        label1=self.compo1.get()
        label2=self.compo2.get()
        self.change2_lng_label.configure(text=label2.upper())
        self.change1_lng_label.configure(text=label1.upper())
        self.change1_lng_label.update()
        self.after(1000,self.change_label)
    
    def open_git(self):
        webbrowser.open("https://github.com/KILLER-RAMADAN")
    
    def open_linkedin(self):
        webbrowser.open("https://www.linkedin.com/in/ahmed-ramadan-9b5a32221/")
    
    def open_gmail(self):
        webbrowser.open("https://mail.proton.me/u/0/inbox")
        
  
    
    
    def __init__(self):
        
    
        super().__init__()
       
        self.geometry("1080x420+250+100")
        self.title("Google Transelator")
        self.resizable(0,0)
        self.attributes("-topmost",True)
        self.iconbitmap("images//trans.ico")
        
        self.tras_image=tk.PhotoImage(file="images//timage.png")
        self.gmail_image=tk.PhotoImage(file="images//gmail.png")
        self.git_image=tk.PhotoImage(file="images//github.png")
        self.linkedin_image=tk.PhotoImage(file="images//linkedin.png")
        self.speaker_image=tk.PhotoImage(file="images//speak.png")
        
        self.tras_label=tk.Label(image=self.tras_image,width=0,bd=0)
        self.tras_label.place(x=480,y=10)
        
        
        #  import google language #
        lang=googletrans.LANGUAGES
        
        all_lang=list(lang.values())
        
        all_lang_keys=lang.keys()
        #  import google language #
        #
        #
        # first layout of compo 1 #
        self.select_lng_label1=tk.Label(text="Selected Language",width=25,font=("roboto,14"),relief="solid")
        self.select_lng_label1.place(x=20,y=5)
        
    
        self.compo1=ttk.Combobox(values=all_lang,width=22,font=("roboto,14"))
        self.compo1.place(x=20,y=40)
        self.compo1.set("english")
        
        self.change1_lng_label=tk.Label(text="",width=25,font=("roboto,14"),relief="solid")
        self.change1_lng_label.place(x=20,y=80)
        # first layout of compo 1 #
        #
        #
        # second layout of compo 2 #
        self.select_lng_label2=tk.Label(text="Translation",width=25,font=("roboto,14"),relief="solid")
        self.select_lng_label2.place(x=780,y=5)
        
    
        self.compo2=ttk.Combobox(values=all_lang,width=22,font=("roboto,14"))
        self.compo2.place(x=780,y=40)
        self.compo2.set("english")
        
        self.change2_lng_label=tk.Label(text="",width=25,font=("roboto,14"),relief="solid")
        self.change2_lng_label.place(x=780,y=80)
        # second layout of compo 2 #
        
        
        # first text layout #
        self.frist_frame=tk.Frame(bg="green",bd=5)
        self.frist_frame.place(x=10,y=118,width=440,height=250)
        
        self.lang_text1_place=tk.Text(self.frist_frame,font="roboto,20",relief="groove",wrap="word")
        self.lang_text1_place.place(x=0,y=0,height=240,width=430)
        
        self.scrollpar1=tk.Scrollbar(self.frist_frame)
        self.scrollpar1.pack(side="right",fill="y")
        
        self.scrollpar1.configure(command=self.lang_text1_place.yview)
        self.lang_text1_place.configure(yscrollcommand=self.scrollpar1.set)
        # first text layout #
        
        # second text layout #
        self.second_frame2=tk.Frame(bg="red",bd=5)
        self.second_frame2.place(x=630,y=118,width=440,height=250)
        
        self.lang_text2_place=tk.Text(self.second_frame2,font="roboto,20",relief="groove",wrap="word")
        self.lang_text2_place.place(x=0,y=0,height=240,width=430)
        
        self.scrollpar2=tk.Scrollbar(self.second_frame2)
        self.scrollpar2.pack(side="right",fill="y")
        
        self.scrollpar2.configure(command=self.lang_text2_place.yview)
        self.lang_text2_place.configure(yscrollcommand=self.scrollpar2.set)
        # second text layout #
        
        
        # buttons #
        
        style=Style()

        style.configure("TButton",font=('calibri',20,'bold'),borderwidth="4")
        style.map("TButton",foreground=[('active','!disabled','green')],
        background=[('active','black')])
        
        
        self.trans_button=ttk.Button(text="Translate",command=self.translate_text)
        self.trans_button.place(x=459,y=118)
        
        self.copy_button=ttk.Button(text="Copy",command=self.copy)
        self.copy_button.place(x=459,y=200)
        
        self.exit_button=ttk.Button(text="Exit",command=self.destroy)
        self.exit_button.place(x=459,y=282)
        
        # social buttons #
        
        self.gmail_button=ttk.Button(text="",image=self.gmail_image,command=self.open_gmail)
        self.gmail_button.place(x=720,y=60)
        
        self.git_button=ttk.Button(text="",image=self.git_image,command=self.open_git)
        self.git_button.place(x=720,y=10)
        
        self.link_button=ttk.Button(text="",image=self.linkedin_image,command=self.open_linkedin)
        self.link_button.place(x=670,y=10)
        
        # self.speaker_button=ttk.Button(text="",image=self.speaker_image,command=self.speak)
        # self.speaker_button.place(x=670,y=60)
        
        # social buttons #
        
        
        # buttons #
        
        
        
        # down frame  #
        
        self.down_frame=tk.Frame(width=2000,height=300,bg="#2C3E50")
        self.down_frame.place(x=0,y=370)
        
        self.rights_label=tk.Label(text="All Rights Reserved® By Ahmed Ramadan",bg="#2C3E50",fg="white",font=("arial,20,bold"))
        self.rights_label.place(x=350,y=380)
        
        # down frame  #
        
        self.change_label()
        


app=transeltor()
app.mainloop()
        