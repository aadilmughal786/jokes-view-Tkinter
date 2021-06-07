from tkinter import *
from random import randint
from jokes_list import *
#-------------------[ main window ]----------------------------
root = Tk()
root.title("Jokes view")
root.resizable(0,0)
count = 1
hindi = "hjoke"
english = "ejoke"
flag = english
#---------------------------[ functions ]------------------------------

def prev():
    global count
    global  flag
    if count==1:
        return 0
    else:
        count-=1
        labKey["text"] = f"{flag} No.{count}"
        labvalue["text"] = listt[f"{flag}{count}"]


def random_():
    global count
    global  flag
    count = randint(1,len(listt)//2)
    labKey["text"] = f"{flag} No.{count}"
    labvalue["text"] = listt[f"{flag}{count}"]

def next():
    global  flag
    global count
    if count==(len(listt)//2):
        return 0
    else:
        count+=1
        labKey["text"] = f"{flag} No.{count}"
        labvalue["text"] = listt[f"{flag}{count}"]

def switch(choice):
    global  flag
    flag = choice
    labKey["text"] = f"Joke No.{count}"
    labvalue["text"] = listt[f"{flag}{count}"]

#---------------------------[ row -1 ]------------------------------
lab0 = Label(root,width = 6,height = 2)
lab0.grid(row = 0,column = 0,sticky = "ewns")

labKey = Label(root)
labKey.grid(row = 0,column = 1,sticky = "ewns",pady =20)

btnhindi = Button(root,text = "HINDI",command = lambda:switch(hindi))
btnhindi.grid(row = 0,column = 3,sticky = "ewns",pady =20 )

btnenglish = Button(root,text = "ENGLISH",command = lambda:switch(english))
btnenglish.grid(row = 0,column = 5,sticky = "ewns",pady =20 )

lab0 = Label(root,width = 6)
lab0.grid(row = 0,column = 6,sticky = "ewns")
#-----------------------------[ row - 2 ]-----------------------------------

labvalue = Label(root,bd = 2,relief = "solid",width = 35,height = 10,text = listt["ejoke1"],font = "bold 20")
labvalue.grid(row = 1,column = 1,sticky = "ewns",columnspan  = 5)

#-----------------------------[ row - 2 ]-----------------------------------
lab0 = Label(root,height = 1)
lab0.grid(row = 2,column =0,sticky = "ewns")

btnpre = Button(root,text = "🢘",command = prev)
btnpre.grid(row = 3,column = 1,sticky = "ewns")
btnrand = Button(root,text = "RANDOM",font = "bold",command = random_)
btnrand.grid(row = 3,column = 3,sticky = "ewns")
btnnext = Button(root,text = "🢚",command = next)
btnnext.grid(row = 3,column = 5,sticky = "ewns")

lab0 = Label(root,height = 1)
lab0.grid(row = 4,column =0,sticky = "ewns")


#---------------------------------------------------------------------
labKey["text"] = "Joke No.1"
#-----------------------------[ event loop ]----------------------------------

root.mainloop()