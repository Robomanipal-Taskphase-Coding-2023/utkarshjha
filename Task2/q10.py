def encoded_string(encoded):
    parts = encoded.split('000')

    if len(parts) >= 3:
        first_name = parts[0]
        last_name = parts[1]
        user_id = parts[2]

        result_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "id": user_id
        }

        return result_dict
    else:
        return {"error": "Invalid input format"}

encoded_str = input("Enter the string: ")
decoded_string = encoded_string(encoded_str)
print(decoded_string)
