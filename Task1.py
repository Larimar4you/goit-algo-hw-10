import pulp

model = pulp.LpProblem("Drink_Production_Optimization", pulp.LpMaximize)

lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Integer")


model += lemonade + juice, "Maximize_total_products"

# Обмеження ресурсів
model += 2 * lemonade + 1 * juice <= 100, "Water_constraint"
model += lemonade <= 50, "Sugar_constraint"
model += lemonade <= 30, "Lemon_juice_constraint"
model += 2 * juice <= 40, "Fruit_puree_constraint"


model.solve()


print("Status:", pulp.LpStatus[model.status])
print("Lemonade produced:", lemonade.varValue)
print("Fruit juice produced:", juice.varValue)
print("Total products:", lemonade.varValue + juice.varValue)

"""
Lemonade produced: 30.0
Fruit juice produced: 20.0
Total products: 50.0
"""
