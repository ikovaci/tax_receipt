'''
ROUNDING AMBIGUITY!
Here we assume total tax (import only 5%, sales only 10%, both 15%) and
round the tax before adding it to the main price

ROUNDING ISSUES!
problem states to round to the nearest 0.05, but last example (output 3,
last line) is rounded to the nearest UPPER 0.05 (0.5625 is rounded to 0.60
instead of nearest 0.55). There are two round_tax functions: first rounds UP
if tax > 0. But second rounds to the nearest 0.05 (and it only affects
output3 last line) and total.
'''




## always ROUND UP (explanation in readme.txt, issue/assumption 1),
## tax > 0 will always be rounded to the nearest UPPER 0.05
def round_tax (a, rounding = 0.05):
    b =  a // rounding
    if b > 0:
        return round(b * rounding + rounding, 2)
    else:
        return 0

#### rounds to the nearest 0.05 mathematically
#### avoids banker's rounding in python 3 (example: round(1.25,1) = 1.2)
##def round_tax (a, rounding = 0.05):
##    b =  a // rounding
##    rest = round(a % rounding,3)
##    if rest < rounding/2:
##        return round(b * rounding, 2)
##    else:
##        return round(b * rounding + rounding, 2)


## calculate tax, round per round_tax beore adding to principal
def item_tax(base, tax = 10): ## tax in %
    calc_tax = tax / 100
    return round_tax(base * calc_tax)
