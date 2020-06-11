from tkinter import *
from tkinter import ttk
root = Tk()

#State variables

#Create and grid the outer content frame
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
c.columnconfigure(0, weight=1)
c.columnconfigure(2, weight=1)
c.rowconfigure(1, weight=1)

#create widgets
checklists_listbox = Listbox(c, height=5)
checklists_label = ttk.Label(c, text="Checklists")
tags_listbox = ttk.Treeview(c, height=5)
tags_label = ttk.Label(c, text="Tags")

'''
btn_new_checklist = Button(c, text="New")
btn_del_checklist = Button(c, text="Delete")
btn_new_tag = Button(c, text="New")
btn_del_tag = Button(c, text="Delete")
'''

#grid all widgets
checklists_listbox.grid(column=2, row=1, padx=20, pady=(0, 20), sticky=(N,S,E,W), columnspan=2)
checklists_label.grid(column=2, row=0, padx=20, sticky=(E,W,S), columnspan=2)
tags_listbox.grid(column=0, row=1, padx=20, pady=(0,20),sticky=(N,S,E,W), columnspan=2)
tags_label.grid(column=0, row=0, padx=20, sticky=(E,W,S), columnspan=2)
'''
btn_new_checklist.grid(column=0, row=2, padx=20, pady=10, sticky=(N,W,S))
btn_del_checklist.grid(column=1, row=2, padx=20, pady=10, sticky=(N,W,S))
btn_new_tag.grid(column=3, row=2, padx=20, pady=10, sticky=(N,W,S))
btn_del_tag.grid(column=4, row=2, padx=20, pady=10, sticky=(N,W,S))
'''

#Create Checklists right click menu
m = Menu(root, tearoff=0)
#Adding options to the menu
m.add_command(label="New")
m.add_command(label="Delete")
m.add_separator()
m.add_command(label="Duplicate")

#Create Pop up Event at current mouse position
def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

#Use right mouse trigger to trigger do_popup event
tags_listbox.bind("<Button-3>", do_popup)
checklists_listbox.bind("<Button-3>", do_popup)

root.mainloop()