## locations of files with non-taxable items (books, food, medicines)
books = "untaxable_items/books.txt"
food = "untaxable_items/food.txt"
medicines = "untaxable_items/medicines.txt"
categories = [books,food,medicines]


## list which will be populated with nontaxable items
list_of_stuff = [""]
for category in categories:
    f = open(category)
    message = f.read()
    new_list = message.split("\n")
    list_of_stuff.extend(new_list)

## remove empty elements in the list
for x in list_of_stuff:
    if x == '':
        list_of_stuff.remove(x)
