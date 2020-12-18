'''
Pricing strategy:
Constant price (e.g. 20 per orange)
Linear pricing strategy: a linear equation of inventory level 
(e.g. price = -0.75*current_inventory + 30)
'''

def constant_price(constant_price):
    return constant_price


def linear_price(a,b,c,inventory,freshness):
    return a*inventory+b+c*freshness
