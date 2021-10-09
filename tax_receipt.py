import os ## to read number of files in input
from MyModules import tax_rules, itemClass, untaxable

## locations of input/output files
input_loc = "data/input/"
output_loc = "data/output/"

## scans the input directory and returns number of files in it
list = os.listdir(input_loc)
number_files = len(list)
print("Number of receipts:", number_files)


## populate list with names of untaxable items (described in untaxable.py)
list_of_stuff = untaxable.list_of_stuff


file_counter = 1 ## counter for files
while file_counter <= number_files:

    ## create a new empty output file
    output_file = open(output_loc + "output_" + str(file_counter)+".txt", "w")
    output_file.close()
    ## open newly created file and append values into it
    output_file = open(output_loc + "output_" + str(file_counter)+".txt", "a")


    tax_total = 0 ## to summarise tax total in a file
    value_total = 0 ## to summarise bill total
    ## read input file, split into lines
    input_file = open(input_loc + "input_" + str(file_counter)+".txt", "r")
    message = input_file.read()
    input_file.close()
    lines = message.split("\n")

    n_rows = len(lines)-1 ## counter for rows in a file
    rows_counter = 0
    while rows_counter < n_rows: ## go through rows

        ## split line into list of words
        arr = [x.strip() for x in lines[rows_counter].split(" ")]
        ## to check if 'imported' is on the list
        imported = "no"
        if "imported" in arr: ## scan list for word 'imported'
            imported = "yes"

        ## scan list for untaxable items
        counter_type = 0 ## counter for if item is on list of untaxable items
        for x in list_of_stuff:
            if x in arr:
                counter_type += 1

        ## determine tax rate (taxable vs untaxable items)
        item_tax = 0
        item_type = "untaxable"
        if counter_type == 0:
            item_tax = 10
            item_type = "taxable"

        ## get item name from list (removing first element (no of items) and
        ## last 2 ('at' and price)
        item_name = (arr[1:len(arr)-2])
        item_name = ' '.join(item_name)

        import_tax = 0
        ## to remove "imported" in the middle of string (output3)
        if imported == "yes":
            item_name = item_name.replace("imported ","")
            item_name = "imported " + item_name
            import_tax = 5 ## adding duty if item imported

        tax = import_tax + item_tax ## total tax %


        ## item number (first) and price (last) from list
        item_number = (arr[0])
        item_price = arr[len(arr)-1]

        ## finally join everything
        item1 = itemClass.Items(item_number, imported, item_name, item_price,
                      item_type, tax)

    
        tax_total += tax_rules.item_tax(float(item1.price), tax) ##sum total tax of the bill

        ## calculate item price with tax
        item1.price = float(item1.price) + tax_rules.item_tax(float(item1.price), tax)
        item1.price = round(item1.price,2)
        value_total += item1.price ## value total for the bill

        ## whole line to be printed in output file
        string = str(item1.number) + " " + str(item1.name) + ": " + \
                 "{:.2f}".format(item1.price)
        output_file.write(str(string+"\n"))

        item1.displayItem() ##print in terminal

        rows_counter += 1

    ## tax and bill total to be added to the output file (format with
    ## 2 decimals)
    sales_tax_print = "Sales Taxes: " + "{:.2f}".format(tax_total)
    sales_bill_print = "Total: " + "{:.2f}".format(value_total)
    output_file.write(sales_tax_print + "\n")
    output_file.write(sales_bill_print)

    print(sales_tax_print)##print in terminal
    print(sales_bill_print + "\n")##print in terminal

    output_file.close()
    print("Receipt " + str(file_counter) + " done!\n")
    file_counter += 1

print("Location: " + output_loc)
