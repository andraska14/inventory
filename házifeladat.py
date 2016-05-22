# -*- coding: utf-8 -*-


def add_to_inventory(inv, added_items):
	for key in added_items:
		if key in inv:
			inv[key]=int(inv[key])+1
		else:
			inv[key]=1
	return inv
def display_inventory(inv):
	print("Inventory:")
	db=0
	for key in inv.items():
		print (str(key[1]) + " " + str(key[0]))
		db=db + int(key[1])
	print ("Total number of items: "+ str(db))

'''loot=["rope" , "ruby"]
inv={"rope":3}
inv= add_to_inventory(inv, loot)
display_inventory(inv)'''
