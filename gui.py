from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database

root = Tk()
root.title('Checklists')
#root.iconbitmap('exerlist.ico')
root.geometry("400x700")

#State variables [testing diff]

#Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0)) #
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
#c.columnconfigure(0, weight=1)
#c.rowconfigure(1, weight=1)

#create listbox and scroll bar
checklist_scrollbar = Scrollbar(c, orient=VERTICAL)
#can set listbox SINGLE, MULTIPLE, BROWSE, EXTENDED
checklists_listbox = Listbox(c, yscrollcommand=checklist_scrollbar.set, selectmode=EXTENDED)

#cofigure scrollbar
checklist_scrollbar.config(command=checklists_listbox.yview)


#checklists_label = ttk.Label(c, text="Checklists")

#grid all widgets
#checklists_listbox.grid(column=0, row=1, padx=20, pady=(0,20), sticky=(N,S,E,W))
#checklist_scrollbar.pack(side=RIGHT, fill=Y)
#checklists_listbox.pack(pady=15)
checklist_scrollbar.grid(column=1, row=0, sticky=(N,S))
checklists_listbox.grid(column=0, row=0, ipadx=120, ipady=200)

'''
# Add list of items to listbox
my_list = ["One", "Two", "Three", "abc", "asfkas", "ahakfs", "ahsoufc", "nafbwi"]

for item in my_list:
	checklists_listbox.insert(0, item)
'''

#run the database.py to build the temporary database
database.build_db()
data = database.link_lstbox_db()

for item in data:
	checklists_listbox.insert(item['item_no'], item['name'])
	#print(item['listbox_item'], item['name'])


def delete():
	for item in reversed(checklists_listbox.curselection()):
		checklists_listbox.delete(item)

def select():
	my_label.config(text=checklists_listbox.get(ANCHOR))

def new():
	checklists_listbox.insert(END, entry.get())
	#Database add operation
	next_item = checklists_listbox.size() + 1
	database.Checklist.add_item(item_no=next_item, name=entry.get())
	#Remove the pop-up screen
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


def select_all():
	result = ''
	for item in checklists_listbox.curselection():
			result = result + str(checklists_listbox.get(item)) + '\n'
	my_label.config(text=result)


global my_label
my_label = Label(root, text='')
my_label.grid(column=0, row =2, pady=20)

#Create Checklists right click menu
m = Menu(root, tearoff=0)
#Adding options to the menu
m.add_command(label="Open")
m.add_command(label="New", command=new_popup)
m.add_command(label="Delete", command=delete)
m.add_command(label="Clear All", command=delete_all)
m.add_command(label="Rename")
m.add_command(label="Select", command=select_all)

#Create Pop up Event at current mouse position
def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

#Use right mouse trigger to trigger do_popup event
checklists_listbox.bind("<Button-3>", do_popup)

root.mainloop()