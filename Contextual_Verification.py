from tkinter import *
import urllib.request
from bs4 import BeautifulSoup
import re
import json

def analysis():
    global win1,lbl1,btn1,btn2,btn3,e1,e2
    win.destroy()
    win1=Tk()
    win1.title("Verification")
    win1.geometry("700x300")
    lbl1=Label(win1,text="Enter URL")
    e1=Entry(win1,width=42,font=('Times New Roman',20))
    e2 = Entry(win1, width=42, font=('Times New Roman', 20))
    lbl1.place(relx=0.05,rely=0.1,anchor=W)
    lbl1.config(font=('Times New Roman', 20))
    e1.place(relx=0.07,rely=0.3,anchor=W)
    e2.place(relx=0.07,rely=0.5,anchor=W)
    btn2=Button(win1,text="Verify",width="10",bg="gray89",command=lambda:verify(e1.get(),e2.get()))
    btn2.place(relx=0.25, rely=0.75, anchor=E)
    btn2.config(font=('Times New Roman', 15))
    btn1=Button(win1,text="Clear",width="10",bg="gray89",command=clear)
    btn1.place(relx=0.45, rely=0.75, anchor=E)
    btn1.config(font=('Times New Roman', 15))
    win1.mainloop()


def verify(url,ourl):
       win1.destroy()
       global win2,lbl1,lbl2,lbl3,lbl4,lbl5,lbl6,lbl7,lbl8,lbl9,lbl10,lbl11,btn2
       count=0
       win2=Tk()
       win2.title("Results")
       win2.geometry("500x500")
       lbl1=Label(win2,text="The Results are",font=("Times New Roman", 17, "bold"))
       lbl1.place(relx=0.05, rely=0.1, anchor=W)
       lbl2 = Label(win2, text="Meta Title", font=("Times New Roman", 17, "bold"))
       lbl2.place(relx=0.05, rely=0.25, anchor=W)
       lbl3 = Label(win2, text="Meta Descrption", font=("Times New Roman", 17, "bold"))
       lbl3.place(relx=0.05, rely=0.40, anchor=W)
       lbl4 = Label(win2, text="Keywords", font=("Times New Roman", 17, "bold"))
       lbl4.place(relx=0.05, rely=0.55, anchor=W)
       lbl5 = Label(win2, text="Content", font=("Times New Roman", 17, "bold"))
       lbl5.place(relx=0.05, rely=0.70, anchor=W)
       lbl6 = Label(win2, text="Pass", font=("Times New Roman", 17, "bold"))
       lbl6.place(relx=0.55, rely=0.25, anchor=W)
       lbl7 = Label(win2, text="Pass", font=("Times New Roman", 17, "bold"))
       lbl7.place(relx=0.55, rely=0.40, anchor=W)
       lbl8 = Label(win2, text="Pass", font=("Times New Roman", 17, "bold"))
       lbl8.place(relx=0.55, rely=0.55, anchor=W)
       lbl9 = Label(win2, text="pass", font=("Times New Roman", 17, "bold"))
       lbl9.place(relx=0.55, rely=0.70, anchor=W)
       try:
           html = urllib.request.urlopen(url).read()
           soup = BeautifulSoup(html, 'html.parser')
           html1= urllib.request.urlopen(ourl).read()
           soup1= BeautifulSoup(html1, 'html.parser')
           if (soup.find('meta', attrs={'name': 'keywords'}) == soup1.find('meta', attrs={'name': 'keywords'})):
               lbl8.config(text="Pass")
               count+=10
           else:
               lbl8.config(text="Fail")
               count-=10
               if (soup.find('meta', attrs={'name': 'keywords'}) not in soup1.find('meta', attrs={'name': 'keywords'})):
                   print(soup.find('meta', attrs={'name': 'keywords'}))
           if (soup.find('title') == soup1.find('title')):
               lbl6.config(text="Pass")
               count+=10
           else:
               lbl6.config(text="Fail")
               count-=10
               if (soup.find('title') not in soup1.find('title')):
                   print(soup.find('title'))
           if (soup.find('meta', attrs={'name': 'description'}) == soup1.find('meta', attrs={'name': 'description'})):
               lbl7.config(text="Pass")
               count+=10
           else:
               lbl7.config(text="Fail")
               count-=10
               if (soup.find('meta', attrs={'name': 'description'}) not in soup1.find('meta',attrs={'name': 'description'})):
                   print(soup.find('meta', attrs={'name': 'description'}))

           if (soup.find('meta', attrs={'name': 'description'}) in soup1):
               lbl9.config(text="Pass")
               count += 10
           else:
               lbl9.config(text="Fail")
               count -= 10
               if (soup.find('meta', attrs={'name': 'description'}) not in soup1):
                   print(soup.find('meta', attrs={'name': 'description'}))
           lbl11 = Label(win2, text=count, font=("Times New Roman", 17, "bold"))
           lbl11.place(relx=0.3, rely=0.1, anchor=W)
       except Exception as e:
           print("Error has occured")
           print(e)
       bt2 = Button(win2, text="Thank You....", width="18", bg="gray89",command=Thanks)
       bt2.place(relx=0.25, rely=0.85, anchor=CENTER)
       bt2.config(font=('Times New Roman', 15))
       win2.mainloop()
def Thanks():
    win3=Tk()
    global lbl1
    win3.geometry("350x150")
    lbl1=Label(win3,text="Hope this helped you",font=("Times New Roman", 15, "bold"))
    lbl1.place(relx=0.17, rely=0.3, anchor=W)
    lbl2 = Label(win3, text="Have a Great Day ^^", font=("Times New Roman", 15, "bold"))
    lbl2.place(relx=0.4, rely=0.6, anchor=W)
    win2.destroy()
    win3.mainloop()

def clear():
        e1.delete(0, "end")
        e1.insert(0, "")
        e2.delete(0, "end")
        e2.insert(0, "")
win = Tk()
win.title("Bajaj_Finserv")
win.geometry("550x500")
lbl = Label(win)
img=PhotoImage(file='Bajaj_Finserv_Logo.svg.png')
lbl = Label(win,image=img,width=300,height=150)
lbl.place(relx=0.7, rely=0.2, anchor=CENTER)
lbl.pack()
lbl1=Label(win,text="Welcome")
lbl1.config(font=('Times New Roman', 14, "bold"))
lbl1.place(relx=0.15,rely=0.35,anchor=CENTER)
lbl2=Label(win,text="Our application helps in analysing the URL that you Provide")
lbl2.config(font=('Times New Roman', 14))
lbl2.place(relx=0.55,rely=0.45,anchor=CENTER)
lbl3=Label(win,text="and Verify With the original website")
lbl3.config(font=('Times New Roman', 14))
lbl3.place(relx=0.38,rely=0.55,anchor=CENTER)
bt2 = Button(win, text="Try it Out", width="18", bg="gray89",command=analysis)
bt2.place(relx=0.5, rely=0.8, anchor=CENTER)
bt2.config(font=('Times New Roman', 15))
win.mainloop()
