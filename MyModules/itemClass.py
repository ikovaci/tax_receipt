class Items:
    ## class for all the items

    def __init__(self, number, imported, name, price, item_type, tax):
        self.number = number
        self.name = name
        self.price = price
        self.imported = imported
        self.item_type = item_type
        self.tax = tax
    ##  alternative to print in terminal
    def displayItem(self):
        print(self.number, self.name, end="")
        print(": ",end="")
        print("{:.2f}".format(self.price))
