#@@@@@@@@@@@@@@@@@@@@@@@@@
# Simple Text Editor  
# Taposh Dutta Roy
#@@@@@@@@@@@@@@@@@@@@@@@@@
import sys
from Tkinter import *
import tkMessageBox
import string
from ScrolledText import *


elements = ["1","2","3","4","5"]

#Functions
def die ():
     sys.exit(0)

def die1 (event):
  global v,periods
	print periods[v.get()][0]
	sys.exit(0)

def callee():
	print "I was called; few are Chosen!"

def about():
	response=tkMessageBox.askyesno("tkMenu","This is tkMenu.py, version 0")
	print response

root = Tk()
bar = Menu(root)

filem = Menu(bar)
filem.add_command(label ="Open..", command =callee)
filem.add_command(label ="New..", command =callee)
filem.add_command(label ="Save..", command =callee)
filem.add_command(label ="Save as..", command =callee)
filem.add_separator()
filem.add_command(label ="Exit..", command = die)

helpm = Menu(bar)
helpm.add_command(label ="Index..", command =callee)
helpm.add_separator()
helpm.add_command(label ="About..", command =about)

bar.add_cascade(label="File",menu=filem)
bar.add_cascade(label="Help",menu=helpm)


v = IntVar()
v.set(2)

periods = [
	("Kin",0),
	("qKin",1),
	("wKin",2),
	("rKin",3),
	("tKin",4),
	("yKin",5),
	]

if len(sys.argv) > 1:
	indicator = 0
	filler =X
	expander=1
else :
	indicator = 1
	filler =NONE
	expander=0

for t,m in periods :
	b = Radiobutton(root,text =t,variable=v,value =m,indicatoron=indicator)
	if indicator == 1 :
		b.pack(anchor =W)
	else :
		b.pack(expand=expander,fill=filler)

def reader(s):
	f = string.atoi(s)
	f = f-32
	c = f/9
	c = c*5
	labelx["text"] = "Degrees Fahrenheit:  %s" % (s)
	label["text"] = "Degrees Celcius:  %d" % (int(c))
scale1 = Scale(root,orient =HORIZONTAL)
scale1.pack()
scale2 = Scale(root,orient =VERTICAL,from_=-40,to=212,command=reader)
scale2.pack()
#canvas = Canvas(root)
#canvas["height"] = 30
#canvas["width"] = 30
#canvas["borderwidth"]=1
#canvas["relief"]=RAISED
#canvas.pack()
checkbutton = Checkbutton(root)
checkbutton["text"] = "Checkbutton"
checkbutton.pack()
labelx = Label(root)
labelx ["height"] =1
labelx ["text"] = "Degrees Fahrenheit"
#labelx["borderwidth"] =1
labelx.pack(anchor=W)
label = Label(root)
label["text"] ="Degrees Celcius"
#label["borderwidth"] =1
label["relief"] = SOLID
label.pack(anchor=W)
entry = Entry(root)
entry.insert(0,"Entry")
entry.pack()
#listbox = Listbox(root)
#for i in elements:
#	listbox.insert(0,i)
#listbox.pack()
root.config(menu=bar)

f = Frame(root)
f.pack(expand=1,fill=BOTH)
button = Button(f,width =25)
button["text"] = "Quit!"
button.bind("<Button-1>", die1)
button.pack()
t = ScrolledText(f,background="white")
t.pack()
root.mainloop()
