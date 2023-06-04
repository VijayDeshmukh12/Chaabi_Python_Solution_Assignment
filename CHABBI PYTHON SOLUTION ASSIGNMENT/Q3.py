def sort_list_of_dicts(list_of_dicts, key):
    sorted_list = sorted(list_of_dicts, key=lambda x: x[key])
    return sorted_list

# Example usage
input_list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
sorted_list_by_fruit = sort_list_of_dicts(input_list, "fruit")
print(sorted_list_by_fruit)

sorted_list_by_color = sort_list_of_dicts(input_list, "color")
print(sorted_list_by_color)
