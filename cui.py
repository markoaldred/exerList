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
	if i == 'r':
		checklist_no = int(input('Item No: '))
		new_name = input ('New Checklist Name: ')
		
		database.Checklist.update_item(item_no=checklist_no, name=new_name)

def actions(menu_items):
	actions = {'n':'new', 'e': 'edit', 'd':'delete', 'r':'rename', 'u':'use'}
	print('_______________________________________\n')

	for item in menu_items:
		print((item + " - " + actions[item]))
	print('_______________________________________\n')

checklist_menu()