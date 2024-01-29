import pulp

# Model initialization
model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

# Definition of variables
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Quantity of lemonade
fruit_juice = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')  # Quantity of fruit juice

# Objective function (Maximization of production)
model += lemonade + fruit_juice, "Total Production"

# Adding constraints
# Resources: Water, Sugar, Lemon Juice, Fruit Puree
model += 2 * lemonade + 1 * fruit_juice <= 100  # Constraint for water
model += 1 * lemonade <= 50  # Constraint for sugar
model += 1 * lemonade <= 30  # Constraint for lemon juice
model += 1 * fruit_juice <= 40  # Constraint for fruit puree

# Solving the model
model.solve()

# Displaying results
print("Quantity of lemonade:", lemonade.varValue)
print("Quantity of fruit juice:", fruit_juice.varValue)
