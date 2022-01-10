customer = {
    "name" : "Pratik Pawar",
    "age": 20,
    "BFF": "smit patel",
    "is_varified": True
}
print(customer["name"])
# always use "" in .get method
print(customer.get("birthday"))
print(customer.get("birthday", "jan 6 1999"))

#adding a term
customer["name"] = "nana kaka"
customer["age"] = 28
print(customer["name"])
print(customer["age"])