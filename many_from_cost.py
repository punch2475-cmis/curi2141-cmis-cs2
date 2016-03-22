def cost_tax(d,e):
    return d+(d*(e/100))
def dutch_pay(g,h):
    return g/h
def discount_cost(i,j):
    return i-(i*(j/100))
def discount_and_tax(k,l,n):
    return k-(k*(l/100))+(k*(n/100))
def output(CostWithTax,DutchPay,CostWithDiscount,CostWithDiscountAndTax):
    out="""
Hello
Here are the results for the information you inserted:
The cost with tax : {}
Here is how much each person should pay : {}
This is the cost with the discount : {}
This is the cost with tax and discount : {}
""".format(CostWithTax,DutchPay,CostWithDiscount,CostWithDiscountAndTax)
    return out

#input
def main ():
    print "INFORMATION: If you do not need some of this information, do not type zero. Type any number. It will not function if the number zero is typed."
    amount=raw_input("How much is the total amount? >>> ")
    person=raw_input("How many people are there? >>> ")
    tax=raw_input("Type the percentage for tax >>> ")
    discount=raw_input("Type the percentage of discount>>> ")
    
    #processing
    CostWithTax = cost_tax(float(amount),float(tax))
    DutchPay = dutch_pay(float(amount),float(person))
    CostWithDiscount = discount_cost(float(amount),float(discount))
    CostWithDiscountAndTax = discount_and_tax(float(amount),float(discount),float(tax))
    #output
    out=output(CostWithTax,DutchPay,CostWithDiscount,CostWithDiscountAndTax)
    print out

main()
