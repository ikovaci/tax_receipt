# tax_receipt
Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions. When I purchase items I receive a receipt which lists the name of all the items and
their price (including tax), finishing with the total cost of the items, and the total amounts of sales taxes paid. The rounding rules for sales tax
are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax. Write an application that prints out the receipt details for these shopping baskets...
### INPUT:
Input 1:
> 1 book at 12.49
> 
> 1 music CD at 14.99
> 
> 1 chocolate bar at 0.85
> 
Input 2:

> 1 imported box of chocolates at 10.00
> 
> 1 imported bottle of perfume at 47.50
> 
Input 3:

> 1 imported bottle of perfume at 27.99
> 
> 1 bottle of perfume at 18.99
> 
> 1 packet of headache pills at 9.75
> 

> 1 box of imported chocolates at 11.25
> 
### OUTPUT
Output 1:

> 1 book: 12.49
> 
> 1 music CD: 16.49
> 
> 1 chocolate bar: 0.85
> 
> Sales Taxes: 1.50
> 
> Total: 29.83
> 
Output 2:

> 1 imported box of chocolates: 10.50
> 
> 1 imported bottle of perfume: 54.65
> 
> Sales Taxes: 7.65
> 
> Total: 65.15
> 
Output 3:

> 1 imported bottle of perfume: 32.19
> 
> 1 bottle of perfume: 20.89
> 
> 1 packet of headache pills: 9.75
> 
> 1 imported box of chocolates: 11.85
> 
> Sales Taxes: 6.70
> 
> Total: 74.68

### Issues/assumptions:

Loads "/data/input/input_*.txt", saves in "/data/output/output_*.txt",
counts number of files, but they have to be named by increasing integers 
starting from 1.


1. Rounding issue in example (input3 last line) is ambiguous -- text says to
round to nearest 0.05 but last example rounds up: price is 11.25, imported 
food, 5% tax is 0.5625 which rounds to 0.55 (as is <0.575), making item price 
11.80 (vs 11.85), Sales Taxes 6.65 (vs 6.70), and Total 74.63 (vs 74.68 as in 
example). Solution is to ROUND UP (for example, 0.021 -> 0.05 instead 0.00).
For rounding to nearest instead of up, uncomment the other round_tax function in
MyModules/tax_rules.py 

2. Rounding ambiguous -- do we round only the sales tax, or duty, or both after 
adding up, or do we round the total after everything was calculated? Assume we 
calculate total taxes (sales + duty where applicable), rounding up to upper
0.05 (explained in issue 1), then adding to the principal.

3. Input/output 3, last line -- "box of imported chocolates" and "imported box
of chocolates" aren't the same. Assume that word "imported" in the line means
added 5% duty tax regardless of its position in item name.

4. Assumes names of untaxable items are one word as is. Words can be loaded
into untaxable_items/ files, one word per line. Doesn't differentiate
between categories, simply marks item as untaxable if name matches any word.

5. Assumes no empty lines in input or untaxable files.
