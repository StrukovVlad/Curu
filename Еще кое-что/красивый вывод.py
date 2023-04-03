price_list = {
    "Coffe": 2.5,
    "Tea": 1.8,
    "Chocolate bar": 1.75,
    "Laptop": 1_500,
    "Small car": 12_000,
}

for item, price in price_list.items():
    print(f"{item if len(item) > 3 else '---':15} ${price:10,.2f}")

# Coffe           $      2.50
# ---             $      1.80
# Chocolate bar   $      1.75
# Laptop          $  1,500.00
# Small car       $ 12,000.00