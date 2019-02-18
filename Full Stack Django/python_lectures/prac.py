smallest = None
for i in [9,2,5,74,45]:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i
print(smallest)
