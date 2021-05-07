"""Task 2

Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock."""

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

def price_calc(stock_dict, price_dict):
    stock_sum = 0
    for key in stock_dict:
        item_sum = price_dict[key] * stock_dict[key]
        stock_sum += item_sum
    return ('%.0f' % stock_sum)

print(f'The total sum of stock: {price_calc(stock, prices)}')
