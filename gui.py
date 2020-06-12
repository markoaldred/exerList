from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title('Checklists')
#root.iconbitmap('exerlist.ico')
root.geometry("400x700")

#State variables [testing diff]

#Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
c.columnconfigure(0, weight=1)
c.rowconfigure(1, weight=1)

#create widgets
checklists_listbox = Listbox(c, height=5)
#checklists_label = ttk.Label(c, text="Checklists")

#grid all widgets
checklists_listbox.grid(column=0, row=1, padx=20, pady=(0,20), sticky=(N,S,E,W))
#checklists_label.grid(column=0, row=0, padx=20, pady=(20,0), sticky=(N,E,W,S))

# Add list of items to listbox
my_list = ["One", "Two", "Three"]

for item in my_list:
	checklists_listbox.insert(0, item)

def delete():
	checklists_listbox.delete(ANCHOR)
	my_label.config(text='')

def select():
	my_label.config(text=checklists_listbox.get(ANCHOR))

def new():
	checklists_listbox.insert(END, entry.get())
	top.destroy()

def new_popup():
	global entry
	global top
	top = Toplevel()
	top.title('New Item')
	lbl = Label(top, text="Enter new checklist name:")
	lbl.grid(column=0,row=0, padx=10, sticky=(W))
	entry = Entry(top, width=50)
	entry.grid(column=0, row=1, padx=10, sticky=(W))
	entry.focus()
	btn = Button(top, text="OK", command=new)
	btn.grid(column=0, row=2, padx=10, pady=10, sticky=(W), ipadx=139)

def delete_all():
	checklists_listbox.delete(0, END)


global my_label
my_label = Label(c, text='')
my_label.grid(column=0, row =2, pady=20)

#Create Checklists right click menu
m = Menu(root, tearoff=0)
#Adding options to the menu
m.add_command(label="Open")
m.add_command(label="New", command=new_popup)
m.add_command(label="Delete", command=delete)
m.add_command(label="Clear All", command=delete_all)
m.add_command(label="Rename")
m.add_command(label="Select", command=select)

#Create Pop up Event at current mouse position
def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

#Use right mouse trigger to trigger do_popup event
checklists_listbox.bind("<Button-3>", do_popup)

root.mainloop()