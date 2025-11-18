
Nested_list = eval(input())

flattend= []
for row in Nested_list:
    for value in row:
        flattend.append(value)

print(flattend)
