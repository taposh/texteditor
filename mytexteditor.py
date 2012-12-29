#@@@@@@@@@@@@@@@@@@@@@@@@@
# Simple Text Editor  
# Taposh Dutta Roy
#@@@@@@@@@@@@@@@@@@@@@@@@@
import sys
from Tkinter import *
import tkMessageBox
import string
from ScrolledText import *
from tkFileDialog import *
import fileinput

##################
#Initializations
#################
root = None
t1=[]
##################
#Functions
##################
def die ():
     sys.exit(0)

def openfile():
  global st
	pl = END
	oname = askopenfilename(filetypes=[("Python files","*.py")])
	if oname:
		for line in fileinput.input(oname):
			self.st.insert(pl, line)
			self.t.title(sname)
def savefile():
	sname = asksaveasfilename()
	if sname :
		ofp = open(sname,"w")
		ofp.write(st.get(1.0,END))
		ofp.flush()
		ofp.close()
		self.t.title(sname)

def callee():
	print "I was called; few are Chosen!"

def about():
	response=tkMessageBox.askyesno("tkMenu","This is tkMenu.py, version 0")
	print response

def newwin():
	global root
	t1.append(editor(root))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# CLASS EDITOR
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class editor:
	def __init__(self,rt):
		if rt == None:
			self.t = Tk(rt)
		else:
			self.t = Toplevel(rt)
		self.t.title("Taposh's Editor %d" %len(t1))
		self.bar = Menu(rt)

		self.filem = Menu(self.bar)
		self.filem.add_command(label ="Open..", command =openfile)
		self.filem.add_command(label ="New..", command =newwin)
		self.filem.add_command(label ="Save..", command =savefile)
		self.filem.add_command(label ="Save as..", command =savefile)
		self.filem.add_separator()
		self.filem.add_command(label ="Exit..", command = die)
		self.helpm = Menu(bar)
		self.helpm.add_command(label ="Index..", command =callee)
		self.helpm.add_separator()
		self.helpm.add_command(label ="About..", command =about)
		self.bar.add_cascade(label="File",menu=filem)
		self.bar.add_cascade(label="Help",menu=helpm)
		self.t.config(menu=bar)
		self.f = Frame(self.t,width=512)
		self.f.pack(expand=1,fill=BOTH)

		self.st = ScrolledText(self.f,background="white")
		self.st.pack(side=LEFT, fill=BOTH, expand=1)

if __name__ == "__main__" :
	root = None
	t1.append(editor(root))
	root = t1[0].t
	root.mainloop()				
