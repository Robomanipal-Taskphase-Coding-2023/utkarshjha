result = []

for num in range(2000, 3201):
    
    if num % 7 == 0 and num % 5 != 0:
    
        result.append(str(num))

# Join the list of strings with commas and print the result
result_str = ','.join(result)
print(result_str)

