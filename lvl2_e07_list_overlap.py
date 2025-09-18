"""
List Overlap

Write a function that takes two lists and returns a new list that contains 
only the elements that are common between them (without duplicates).
"""
def list_overlap(list_1, list_2):
    """
    Takes 2 lists.
    Returns the list of overlapping (common) elements
    """
    overlap = []
    for item_1 in list_1:
        if list_2.count(item_1) and not overlap.count(item_1):
            overlap.append(item_1)

    return overlap

def list_overlap_as_sets(list_1, list_2):
    """
    Takes 2 lists.
    Returns the list of overlapping (common) elements
    Use set intersection
    """
    return list(set(list_1).intersection(set(list_2)))


lista_1 = [1,2,3,4,5,6]
lista_2 = [4,5,6,7,8,4,5,9,4]

print(f"Lista 1: {lista_1}")
print(f"Lista 2: {lista_2}")
print(f"Overlap (intersección): {list_overlap(lista_1, lista_2)}")
print(f"Overlap (intersección) usando set: {list_overlap_as_sets(lista_1, lista_2)}")
