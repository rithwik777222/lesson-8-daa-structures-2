x  = {1,2,2,3,4,4,4}
print("set:",x)

x.add(5)
print("updated:",x)

set1 = x
set2 = {2,4,4,6}

print("\nset1",set1)
print("set2",set2)
print("difference:")
print(set1.difference(set2))
print("symmetric difference")
print(set1.symmetric_difference(set2))