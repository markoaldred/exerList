#command user interface
import database
from os import system, name
from tabulate import tabulate
import pandas as pd 
from sqlalchemy.sql import func

#clears python screen
def clear():
	# for windows
	if name == 'nt':
		_ = system('cls')
	#for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

def checklist_menu():
	query = database.session.query(database.Checklist).all()
	clear()
	c1 = []
	c2 = []
	for entry in query:
		c1.append(entry.item_no)
		c2.append(entry.name)
	df = pd.DataFrame({'Item_No' : c1,
						'Checklist_Description' : c2})
	print((tabulate(df, headers='keys', tablefmt='psql')))
	actions('nedru')
	i = input('Action: ')
	if i == 'n':
		new_name = input('Checklist Name: ')
		next_item=database.next_item_no(database.Checklist)
		database.Checklist.add_item(item_no=next_item, name=new_name)
		checklist_menu()
	if i == 'r':
		checklist_no = int(input('Item No: '))
		id_no = database.Checklist.find_id(item_no=checklist_no)
		new_name = input ('New Checklist Name: ')
		database.Checklist.update_item(id=id_no, name=new_name)
		checklist_menu()
	if i == 'd':
		checklist_no = int(input('Item No: '))
		id_no = database.Checklist.find_id(item_no=checklist_no)
		database.Checklist.delete_item(id=id_no)
		checklist_menu()
	if i == 'e':
		checklist_no = int(input('Item No: '))
		id_no = database.Checklist.find_id(item_no=checklist_no)
		task_menu(id_no)

def task_menu(checklist_id):
	query = database.session.query(database.Task).filter(checklist_id==checklist_id).all()
	clear()
	c1 = []
	c2 = []
	for entry in query:
		c1.append(entry.id)
		c2.append(entry.description)
	df = pd.DataFrame({'id' : c1,
						'description' : c2})
	print((tabulate(df, headers='keys', tablefmt='psql')))
	actions('ndeb')
	i = input('Action: ')
	if i == 'n':
		new_name = input('Task: ')
		#next_item=database.next_item_no(database.Checklist)
		database.Task.add_item(checklist_id=checklist_id, description=new_name)
		task_menu(checklist_id)
	if i == 'e':
		item_no = int(input('id: '))
		id_no = database.Task.find_id(id=item_no)
		new_name =input('Rename Task: ')
		database.Task.update_item(id=id_no, description=new_name)
		task_menu(checklist_id)
	if i == 'd':
		item_no = int(input('id: '))
		id_no = database.Task.find_id(id=item_no)
		database.Task.delete_item(id=id_no)
		task_menu(checklist_id)
	if i == 'b':
		checklist_menu()

def actions(menu_items):
	actions = {'n':'new', 'e': 'edit', 'd':'delete', 'r':'rename', 'u':'use', 'b':'back'}
	print('_______________________________________\n')

	for item in menu_items:
		print((item + " - " + actions[item]))
	print('_______________________________________\n')

checklist_menu()