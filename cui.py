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
	print(tabulate(df, headers='keys', tablefmt='psql'))
	actions('NEDRU')
	i = input('Action: ')
	if i == 'N':
		new_name = input('Checklist Name: ')
		database.Checklist.add_item(item_no=database.next_item_no(database.Checklist), name=new_name)

def actions(menu_items):
	actions = {'N':'New', 'E': 'Edit', 'D':'Delete', 'R':'Rename', 'U':'Use'}
	print('_______________________________________\n')

	for item in menu_items:
		print(item + " - " + actions[item])
	print('_______________________________________\n')

checklist_menu()