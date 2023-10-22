def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0+')
    
    first_name = parts[0]
    last_name = parts[1]
    user_id = parts[2]
    
    result_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "id": user_id
    }
    
    return result_dict
