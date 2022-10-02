number = int(input("Enter the number of elements in list: "))
lst = []
for i in range(0,number):
    element = int(input())
    lst.append(element)

print(lst)

triple = lambda num : num+num+num

final_result = map(triple,lst)

print("\nTriple of list numbers:")
print(list(final_result))

