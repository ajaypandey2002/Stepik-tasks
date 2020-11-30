#1000$ for first buy and +120 for every item after 1
def get_shipping_cost(quantity):
	if quantity == 1:
		return 1000
	else:
		return (quantity - 1)*120 + 1000


print(get_shipping_cost(3))
