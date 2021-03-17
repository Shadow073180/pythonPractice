

# Given a list with pairs, sort on the first element.
def sort_list_with_pairs_on_first_element(collection):
    collection.sort(key=lambda x:x[0])
    print(collection)


# Now sort on the second element
def sort_list_with_pairs_on_second_element(collection):
    collection.sort(key=lambda x: x[1])
    print(collection)