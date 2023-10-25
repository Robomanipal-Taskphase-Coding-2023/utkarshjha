def generate_square_dictionary(n):
    square_dict = {i: i * i for i in range(1, n + 1)}
    return square_dict

n = int(input("Enter an integral number (n): "))
result_dict = generate_square_dictionary(n)

print("The dictionary is:")
for key, value in result_dict.items():
    print(f"{key}: {value}")
