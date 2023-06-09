def switch_dict_keys_values(dictionary):
    return {value: key for key, value in dictionary.items()}

#example
input_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}

switched_dict = switch_dict_keys_values(input_dict)
print(switched_dict)
