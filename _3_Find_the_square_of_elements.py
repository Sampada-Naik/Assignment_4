number = int(input("Enter the number of elements in list: "))
lst = []
for i in range(0,number):
    element = int(input())
    lst.append(element)

print(lst)

square = lambda num : num*num

final_result = map(square,lst)

print("\nSquare of the elements of the list:")
print(list(final_result))