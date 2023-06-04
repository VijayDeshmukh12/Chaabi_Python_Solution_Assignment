def get_sublist_with_every_second_element(lst, start_index, end_index):
    sub_list = lst[start_index+1:end_index:2]
    return sub_list

# Example usage
input_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9
sub_list = get_sublist_with_every_second_element(input_list, start_index, end_index)
print(sub_list)
