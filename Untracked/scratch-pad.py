"""
Practicing using algorithms
"""
# Sorting algorithm
def sort_algo(sort_this):
    for i in range(len(sort_this) -  1):
        index_smallest = i
        for j in range(i+1, len(sort_this)):
            if sort_this[j] < sort_this[index_smallest]:
                index_smallest = j
        temp = sort_this[i]
        sort_this[i] = sort_this[index_smallest]
        sort_this[index_smallest] = temp
    return sort_this

sort_this = [14, 3, 78, 52, 4, 9, 12, 10, 8, 33, 56, 27]

print(sort_algo(sort_this))