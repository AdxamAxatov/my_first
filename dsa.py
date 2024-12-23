def binary_search(list, main_item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        mid_list = list[mid]
        if mid_list == main_item:
            return mid
        else: 
            if mid_list < main_item:
                low = mid + 1
            else:
                high = mid - 1

# search = binary_search([1, 3, 5, 6, 8, 9, 12], 1)
# print(search)


# Recap
# • Binary search is a lot faster than simple search.
# • O(log n) is faster than O(n), but it gets a lot faster once the list of
# items you’re searching through grows.
# • Algorithm speed isn’t measured in seconds.
# • Algorithm times are measured in terms of growth of an algorithm.
# • Algorithm times are written in Big O notation.














































































































