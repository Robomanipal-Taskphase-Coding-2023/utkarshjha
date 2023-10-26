def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two numbers"
    
    largest = second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return "There is no second largest element in the list"
    else:
        return second_largest
list = []
n = int(input("Enter list range: "))
for i in range(0, n):
    ele = int(input())
    list.append(ele)
output = second_largest(list)  
print(output)      
