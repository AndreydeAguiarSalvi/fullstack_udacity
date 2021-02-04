import sqlite3
connection = sqlite3.connect('restaurantmenu.db')
c = connection.cursor()

c.execute('''
	CREATE TABLE restaurant
		(id INTEGER PRIMARY KEY ASC, name varchar(100) NOT NULL)
	''')

c.execute('''
	CREATE TABLE menu_item
		(id INTEGER PRIMARY KEY ASC, name varchar(100), price varchar(100),
		descriprion varchar(250) NOT NULL, restaurant_id INTEGER NOT NULL,
		FOREIGN KEY(restaurant_id) references restaurant(ID))
	''')

connection.commit()
connection.close()
