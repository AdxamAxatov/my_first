def next_not_3(x: int, y: int) -> int:
    a = x * y
    if a % 3 != 0:
        return a
    else:
        a % 3 == 0
        a += 1
        return a

# print(next_not_3(9, 2))



def correct_jumbled_text(text, words):
    """Corrects jumbled words in a text given a list of correct words.

    Args:
        text: A string containing jumbled words.
        words: A list of correct words in any order.

    Returns:
        A string with corrected words.
    """

    words_set = set(words)  # Create a set for faster lookup
    words_dict = {}  # Create a dictionary to store words with first and last letters

    for word in words:
        words_dict[word[0] + word[-1]] = word
    corrected_text = []
    for word in text.split():
        if word[0] + word[-1] in words_dict:
            corrected_text.append(words_dict[word[0] + word[-1]])
        else:
            corrected_text.append(word)  # If word not found, keep original

    return " ".join(corrected_text)


# hi =correct_jumbled_text("Somoene watns to colelct corcert wodrs", ["correct", "someone", "words", "to", "collect", "wants"])
# print(hi)


def correct_jumbled_text_alphabets(text, words):
    """Corrects jumbled words in a text given a list of correct words.

    Args:
        text: A string containing jumbled words.
        words: A list of correct words in any order.

    Returns:
        A string with corrected words.
    """

    words_set = set(words)
    corrected_text = []

    for word in text.split():
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                candidate_word = word[:i] + word[j:]
                if candidate_word in words_set:
                    corrected_text.append(candidate_word)
                    break
            else:
                corrected_text.append(word)  # If no match, keep original

    return " ".join(corrected_text)

# hi =correct_jumbled_text("Somoene watns to colelct wrogn wodrs", ["wrong", "someone", "words", "to", "collect", "wants"])
# print(hi)



def latest_time(time_str):
    """
    Finds the latest possible time from a given 24-hour format time string with '?' characters.

    Args:
        time_str: A string representing a 24-hour format time with '?' characters.

    Returns:
        A string representing the latest possible time.
    """

    hours, minutes = time_str.split(":")

    def replace_question_marks(time_part):
        if time_part[0] == "?":
            if time_part == "??":
                return "23"

            elif int(time_part[1]) <= 3:
                return f"2{time_part[1]}"

            elif 3 < int(time_part[1]):
                return f"1{time_part[1]}"

        else:
            return time_part

    hours = replace_question_marks(hours)

    def replace(minute_part):
        if minute_part[0] == "?":
            if minute_part == "??":
                return "59"
            else:
                return f"5{minute_part[1]}"
        
        else:
            return minute_part
    minutes = replace(minutes)
    
    return f"{hours}:{minutes}"


time_str = "23:??"
# print(latest_time(time_str))  
time_str = "?6:??"
# print(latest_time(time_str)) 






def compress(word: str) -> str:
    if not word:
        return ""

    compressed_string = ""
    count = 1

    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed_string += str(count) + word[i - 1]
            count = 1


    compressed_string += str(count) + word[-1]
    return compressed_string


compres = "abbcccdddd"
# print(compress(compres))
compres = "ddffffee"
# print(compress(compres))





def get_longest_word( s: str) -> str:
    splitted = s.split(" ")
    longest_word = ""
    for i in splitted:
        if len(i) > len(longest_word):
            longest_word = i

    return longest_word


longest = get_longest_word('Python is simple and effective!')
# print(longest)




def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if left < right and s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# print(is_palindrome('racecar'))  
# print(is_palindrome('nottona'))  
# print(is_palindrome("A man, a plan, a canal: Panama"))  






def swap_quotes(string):

    new_string = ""
    for char in string:
        if char == "'":
            new_string += '"'
        elif char == '"':
            new_string += "'"
        else:
            new_string += char
    return new_string


input_string = "This is a 'string' with \"double\" quotes."
output_string = swap_quotes(input_string)
# print(output_string)  





def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Fill the first row and column
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    # Fill the rest of the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]


str1 = "kitten"
str2 = "sitting"
distance = levenshtein_distance(str1, str2)
# print(f"Levenshtein distance between '{str1}' and '{str2}': {distance}")







from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    str_set = set(str_list)
    str_list = list(str_set)
    str_list.sort()
    return str_list


# print(sort_unique_elements(('red', 'white', 'black', 'red', 'green', 'black')))





# from typing import Union, List

# ListType = List[Union[int, str]]


# def get_fizzbuzz_list(n: int) -> ListType:
#     result = []
#     for num in range(1, n + 1):
#       if num % 15 == 0:
#         result.append("FizzBuzz")
#       elif num % 3 == 0:
#         result.append("Fizz")
#       elif num % 5 == 0:
#         result.append("Buzz")
#       else:
#         result.append(num) 
  
#     return result

# n = 16
# fizzbuzz_list = get_fizzbuzz_list(n)
# print(fizzbuzz_list)



# def foo(nums):

#     if not nums:
#         return []

#     total_product = 1
#     for num in nums:
#         total_product *= num

#     result = []
#     for num in nums:
#         result.append(total_product // num)

#     return result


# nums = [3, 2, 1]
# result = foo(nums)
# print(result)  







# inputs = ['000', '001', '010', '011', '100', '101']

# shift_register_size = 4

# def shift_register_simulation(inputs, seconds, shift_register_size):
#     register = [0] * shift_register_size
#     time = 0
#     result = []

#     for input_value in inputs:
#         bits = [int(bit) for bit in input_value]

#         for bit in bits:
#             register.pop(0)
#             register.append(bit)

#             if time in seconds:
#                 result.append(register[2])

#             time += 1

#     return result

# seconds_to_check = [7, 9, 12, 14]

# output_bits = shift_register_simulation(inputs, seconds_to_check, shift_register_size)

# print("State of  C-element at the time: ", output_bits)




# numbers = [1, 2, 3, 2, 1, 2, 4, 5, 4, 3, 2, 1, 1]
 
# frequency_dict = {}
 
# for num in numbers:
#     if num in frequency_dict:
#         frequency_dict[num] += 1
#     else:
#         frequency_dict[num] = 1
 
# # print("Frequency dictionary:")
# # print(frequency_dict)



# glass = [
#     ['H', 'H', 'W', 'O'],
#     ['W', 'W', 'O', 'W'],
#     ['H', 'H', 'O', 'O']
# ]
# density_chart = {'O': 0.80, 'A': 0.87, 'W': 1.00, 'H': 1.36}
 
# flattened_glass = []
# for row in glass:
#     for item in row:
#         flattened_glass.append(item)
 
# for i in range(len(flattened_glass)):
#     for j in range(i + 1, len(flattened_glass)):
#         if density_chart[flattened_glass[i]] > density_chart[flattened_glass[j]]:
#             flattened_glass[i], flattened_glass[j] = flattened_glass[j], flattened_glass[i]
# rows = len(glass)
# cols = len(glass[0])
 
# sorted_glass = []
# index = 0
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(flattened_glass[index])
#         index += 1
#     sorted_glass.append(row)
 
# for row in sorted_glass:
    # print(row)






# matrix = []
# while True:
#     line = input().strip()
#     if line == "end":
#         break
#     row = [int(item) for item in line.split()]
#     matrix.append(row)
 
# rows = len(matrix)
# cols = len(matrix[0])
# result = [[0] * cols for _ in range(rows)]
 
# for i in range(rows):
#     for j in range(cols):
#         total_sum = 0
#         total_sum += matrix[i - 1][j] if i > 0 else matrix[rows - 1][j]
#         total_sum += matrix[(i + 1) % rows][j]
#         total_sum += matrix[i][j - 1] if j > 0 else matrix[i][cols - 1]
#         total_sum += matrix[i][(j + 1) % cols]
 
#         result[i][j] = total_sum
 
# for row in result:
    # print(" ".join(map(str, row)))




# n = int(input().strip())
# matrix = [[0] * n for _ in range(n)]
 
# top, bottom, left, right = 0, n - 1, 0, n - 1
# direction = 0  # 0: right, 1: down, 2: left, 3: up
# num = 1
 
# while num <= n * n:
#     if direction == 0:  # Moving right
#         for i in range(left, right + 1):
#             matrix[top][i] = num
#             num += 1
#         top += 1
#     elif direction == 1:  # Moving down
#         for i in range(top, bottom + 1):
#             matrix[i][right] = num
#             num += 1
#         right -= 1
#     elif direction == 2:  # Moving left
#         for i in range(right, left - 1, -1):
#             matrix[bottom][i] = num
#             num += 1
#         bottom -= 1
#     elif direction == 3:  # Moving up
#         for i in range(bottom, top - 1, -1):
#             matrix[i][left] = num
#             num += 1
#         left += 1
 
#     direction = (direction + 1) % 4
 
# for row in matrix:
#     print(" ".join(map(str, row)))





# def get_tuple(num: int):
#     string = str(num)
#     listed = []
#     for i in string:
#         integer = int(i)
#         listed.append(integer)
#     converted = tuple(listed)
#     return converted


# print(get_tuple(87178291199))



# def get_pairs(lst: list):
#     pairs = []
#     for i in range(len(lst) - 1):
#         pair = (lst[i], lst[i + 1])
#         pairs.append(pair)
#     return pairs


# print(get_pairs([1, 2, 3, 8, 9]))
# print(get_pairs(['need', 'to', 'sleep', 'more']))



# def get_dict(s: str):
#     char_freq = {}
#     for char in s.lower():
#         char_freq[char] = char_freq.get(char, 0) + 1
#     return char_freq 

# print(get_dict('Oh, it is python'))




# from typing import Any, Dict, List, Set

# def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
#     dct = {}
#     for i in lst:
#         for k, v in i.items():
#             dct[v] = dct.get(k, v)
#     sett = set(dct)
#     return sett 

# print(check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))





# def multiplication_table(row_start, row_end, column_start, column_end):
#     table = []
#     for row in range(row_start, row_end + 1):
#         row_list = []
#         for col in range(column_start, column_end + 1):
#             product = row * col
#             row_list.append(product)
#         table.append(row_list)

#     print(table)

# row_start = 2
# row_end = 4
# column_start = 3
# column_end = 7
# multiplication_table(row_start, row_end, column_start, column_end)


# # Function to find the Checksum of Sent Message
# def findChecksum(SentMessage, k):

# 	# Dividing sent message in packets of k bits.
# 	c1 = SentMessage[0:k]
# 	c2 = SentMessage[k:2*k]
# 	c3 = SentMessage[2*k:3*k]
# 	c4 = SentMessage[3*k:4*k]

# 	# Calculating the binary sum of packets
# 	Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

# 	# Adding the overflow bits
# 	if(len(Sum) > k):
# 		x = len(Sum)-k
# 		Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
# 	if(len(Sum) < k):
# 		Sum = '0'*(k-len(Sum))+Sum

# 	# Calculating the complement of sum
# 	Checksum = ''
# 	for i in Sum:
# 		if(i == '1'):
# 			Checksum += '0'
# 		else:
# 			Checksum += '1'
# 	return Checksum

# # Function to find the Complement of binary addition of
# # k bit packets of the Received Message + Checksum
# def checkReceiverChecksum(ReceivedMessage, k, Checksum):

# 	# Dividing sent message in packets of k bits.
# 	c1 = ReceivedMessage[0:k]
# 	c2 = ReceivedMessage[k:2*k]
# 	c3 = ReceivedMessage[2*k:3*k]
# 	c4 = ReceivedMessage[3*k:4*k]

# 	# Calculating the binary sum of packets + checksum
# 	ReceiverSum = bin(int(c1, 2)+int(c2, 2)+int(Checksum, 2) +
# 					int(c3, 2)+int(c4, 2)+int(Checksum, 2))[2:]

# 	# Adding the overflow bits
# 	if(len(ReceiverSum) > k):
# 		x = len(ReceiverSum)-k
# 		ReceiverSum = bin(int(ReceiverSum[0:x], 2)+int(ReceiverSum[x:], 2))[2:]

# 	# Calculating the complement of sum
# 	ReceiverChecksum = ''
# 	for i in ReceiverSum:
# 		if(i == '1'):
# 			ReceiverChecksum += '0'
# 		else:
# 			ReceiverChecksum += '1'
# 	return ReceiverChecksum

# # 00000001000000100000010000001000
# # 10000001011000100001000100001000
# # 10011001001101110110001101100100
# # 10101111000011111011001010010011


# # Driver Code
# SentMessage = "10101111000011111011001010010011"
# k = 8
# #ReceivedMessage = "10000101011000111001010011101101"
# ReceivedMessage = "10101111000011111011001010010011"
# # Calling the findChecksum() function
# Checksum = findChecksum(SentMessage, k)

# # Calling the checkReceiverChecksum() function
# ReceiverChecksum = checkReceiverChecksum(ReceivedMessage, k, Checksum)

# # Printing Checksum
# print("SENDER SIDE CHECKSUM: ", Checksum)
# print("RECEIVER SIDE CHECKSUM: ", ReceiverChecksum)
# finalsum=bin(int(Checksum,2)+int(ReceiverChecksum,2))[2:]

# # Finding the sum of checksum and received checksum
# finalcomp=''
# for i in finalsum:
# 	if(i == '1'):
# 		finalcomp += '0'
# 	else:
# 		finalcomp += '1'

# # If sum = 0, No error is detected
# if(int(finalcomp,2) == 0):
# 	print("Receiver Checksum is equal to 0. Therefore,")
# 	print("STATUS: ACCEPTED")
	
# # Otherwise, Error is detected
# else:
# 	print("Receiver Checksum is not equal to 0. Therefore,")
# 	print("STATUS: ERROR DETECTED")





# a = [-4, 4, 5, -1, -2, 4, 7, -9]
# # print(list(map(abs, a))) 



# number = [0, 3, 2, 0, 1, 0, 0, 4, 5]
# no_zero = []
# zero = []

# for num in number:
#     if num != 0:
#         no_zero.append(num)
#     else:
#         zero.append(num)

# no_zero.reverse()
# result = no_zero + zero
# print(result) 



# fixed = []
# appended = []
# half_append = []
# # user = int(input('enter the number of loop: '))

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# appended.append(nums[:user])
# half_append.append(nums[user:])

# appends_added = half_append + appended
# for i in appends_added:
#     for j in i:
#         fixed.append(j)
# print(fixed)



# def move_zeros_to_end(numbers):
#   output = numbers.copy()  
#   left, right = 0, len(output) - 1

#   while left < right:
#     if output[left] == 0:
#       while left < right and output[right] == 0:
#         right -= 1
#       output[left], output[right] = output[right], output[left]
#     left += 1

#   return output

# number = [0, 3, 2, 0, 1, 0, 0, 4, 5]
# result = move_zeros_to_end(number)
# print(result) 




# abs(int)
# nums = [-4, 4, 5, -1, 2, 6, -9]
# for i in range(len(nums)):
#     nums[i] = nums[i] ** 2
#     nums[i] = abs(nums[i] ** 2)
# print(sorted(nums))



# nums = [0, 3, 5, 2, 0, 0, 6, 9]
# nums = list(filter(lambda a: a != 0, nums)) + list(filter(lambda a: a == 0, nums))
# print(nums)

# count = 0
# for i, num in enumerate(nums):
#     if num == 0:
#         count += 1
#         continue
#     nums[i], nums[i-count] = nums[i-count], nums[i]
# print(nums)



def reverse(nums: list[int], i, j):
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

def rotate(nums: list[int], k: int):
    k = k % len(nums)
    reverse(nums, 0, len(nums)-1)
# [1,2,3,4,5,6,7]
# [7,2,3,4,5,6,1]
# [7,6,3,4,5,2,1]
# [7,6,5,4,3,2,1]
    reverse(nums, 0, k-1)
# [5,6,7,4,3,2,1]
    reverse(nums, k, len(nums)-1)
# [5,6,7,4,3,2,1]
# [5,6,7,1,3,2,4]
# [5,6,7,1,2,3,4]
    return nums

# nums = [1,2,3,4,5,6,7] # nums = [5,6,7,1,2,3,4]
# print(rotate(nums=nums, k=3))



def square(num):
    dct = {}
    for i in range(1, num + 1):
        dct[i] = i * i 

    return dct

# print(square(5))



def union(*args) -> set:
    result = set()
    for i in args:
        if args:
            result = result.union(i)

    return result

# print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))

def intersect(*args) -> set:
    result = set(args[0])
    for i in args[1:]:
        if args:
            result = result.intersection(i)

    return result

# print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))


# print(2**32)
# print(58503978996815 % 2**32)
# print(60878229962 % 2**32)
# print(60878229962 % 4294967296)

def hi():
    print(2**32)
    return 60878229962 > 2**32-1
# print(hi())
# print(ord('A'))



def hash_function(text):
    h = 0
    for char in text:
        h = (31 * h + ord(char)) % (2**32)
    return h

# text = "Algorithm"
# hash_value = hash_function(text)
# print(hex(hash_value)) 
# print(hash_value)  



def decimal_to_hexadecimal(decimal_num):
  if decimal_num == 0:
    return '0'

  hex_digits = []
  while decimal_num > 0:
    remainder = decimal_num % 16
    hex_digits.append(hex(remainder)[2:].upper())
    decimal_num //= 16

  hex_digits.reverse()
  return ''.join(hex_digits)

# decimal_number = 100000100000111010000011000011010000000110000011000011000000001010000011000010110000001110000011000010100000100100000110000100100000101100000110000100000000110100000110000011100000111100000110000011000001000100000110000010100000100110000011000001000000010101000001100000010000001100100000110000000100000110110000011
# hexadecimal_number = decimal_to_hexadecimal(decimal_number)
# # print(hexadecimal_number)  




def binary_to_hex(binary_str):
    # Ensure the binary string length is a multiple of 4
    while len(binary_str) % 4 != 0:
        binary_str = '0' + binary_str

    # Convert each 4-bit chunk to its hexadecimal equivalent
    hex_str = ''
    for i in range(0, len(binary_str), 4):
        chunk = binary_str[i:i+4]
        hex_str += hex(int(chunk, 2))[2:]  # Remove the '0x' prefix

    return hex_str.upper()

binary_input = "10000010000011101000001100001110100000110000111010000011000011101000001100001110100000110000111010000011000011101000001100001110100000110000111010000011000011101000001100001110100000110000111010000011000011101000001100001110100000110000111010000010"
hex_output = binary_to_hex(binary_input)
# print(hex_output)

def check():
    hi = '820E830E830E830E830E830E830E830E830E830E830E830E830E830E830E82'
    ye = '820E830E830E830E830E830E830E830E830E830E830E830E830E830E830E82'
    return hi == ye

# print(check())



import math

def permutation_ratio(n, r1, r2):
  """
  Calculates the ratio of permutations P(n, r1) / P(n, r2).

  Args:
    n: Total number of objects.
    r1: Number of objects taken in the numerator.
    r2: Number of objects taken in the denominator.

  Returns:
    The calculated ratio.
  """

  if r1 > n or r2 > n or r1 < r2:
    raise ValueError("Invalid input: r1 must be less than or equal to n, r2 must be less than or equal to n, and r1 must be greater than or equal to r2.")

  numerator = math.factorial(n) / math.factorial(n - r1)
  denominator = math.factorial(n) / math.factorial(n - r2)

  return numerator / denominator

# Calculate the ratio for the given values
# n = 100
# r1 = 85
# r2 = 83

# ratio = permutation_ratio(n, r1, r2)
# print(f"The ratio P({n},{r1}) / P({n},{r2}) is {int(ratio)}")




def evaluate_expression(n, m):
    """
    Evaluates the expression (n! - m!) / m!

    Args:
        n (int): The larger factorial number.
        m (int): The smaller factorial number.

    Returns:
        float: The evaluated result.
    """

    numerator = n * (n - 1)
    denominator = m

    result = numerator / denominator
    return result

# n = 56
# m = 55

# result = evaluate_expression(n, m)
# print(f"The result is: {result:.2f}")




from typing import Dict
# from collections import defaultdict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:           
    # return dictt 
    # result = defaultdict(int)    
    result = {}
    for d in args:
        for key, value in d.items():
            # result[key] += value    
            result[key] = result.get(key, 0) + value

    return dict(result)

# dict_1 = {'a': 100, 'b': 200}
# dict_2 = {'a': 200, 'c': 300}
# dict_3 = {'a': 300, 'd': 100}

# combined_dict = combine_dicts(dict_1, dict_2, dict_3)
# print(combined_dict)  




from numbers import Number
from typing import Callable


def operation_factory(operation: str) -> Callable[[Number, Number], Number]:
    if operation == 'add':
        return lambda a, b: a + b
    elif operation == 'subtract':
        return lambda a, b: a - b
    elif operation =='multiply':
        return lambda a, b: a * b
    elif operation == 'divide':
        return lambda a, b: a / b if b != 0 else ValueError("Division by zero") 

def perform_operation(operation: str, a: Number, b: Number) -> Number:
    return operation_factory(operation)(a, b)


# print(perform_operation("multiply", 5, 3))
# print(perform_operation("divide", 3, 0))
# print(perform_operation("subtract", 5, 3))
# print(perform_operation("add", 5, 3))



# def sum_of_digits(num: int): 
#     if num < 10:
#         return num
#     else:
#         return num % 10 + sum_of_digits(num // 10)
    

# print(sum_of_digits(12345))





def marshal(obj):
    if isinstance(obj, int):
        return f"i:{obj}"
    elif isinstance(obj, bool):
        return f"b:{str(obj).lower()}"  # Convert True/False to true/false
    elif isinstance(obj, str):
        return f"s:{obj}" 
    elif isinstance(obj, list):
        return f"l:[{','.join(marshal(item) for item in obj)}]" 
    elif isinstance(obj, tuple): 
        return f"t:({','.join(marshal(item) for item in obj)})" 
    elif isinstance(obj, dict):
        return f"d:{{{','.join(f'{marshal(key)}:{marshal(value)}' for key, value in obj.items())}}}" 
    else:
        raise TypeError(f"Unsupported type: {type(obj)}")
    
# print(marshal({"key": "value", "number": 123}))


def unmarshal(serialized_obj):
    if serialized_obj.startswith("i:"):
        return int(serialized_obj[2:])
    elif serialized_obj.startswith("b:"):
        return serialized_obj[2:] == "true"
    elif serialized_obj.startswith("s:"):
        return serialized_obj[2:]
    elif serialized_obj.startswith("l:"):
        start = serialized_obj.find("[") + 1
        end = serialized_obj.find("]")
        return [unmarshal(item) for item in serialized_obj[start:end].split(",")]
    elif serialized_obj.startswith("t:"):
        start = serialized_obj.find("(") + 1
        end = serialized_obj.find(")")
        return tuple(unmarshal(item) for item in serialized_obj[start:end].split(","))
    elif serialized_obj.startswith("d:"):
        print(1)
        start = serialized_obj.find("{") + 1
        end = serialized_obj.find("}")
        result = {}
        pairs = serialized_obj[start:end].split(",") 
        for pair in pairs:
            key_end = pair.find(":")
            key = unmarshal(pair[:key_end])
            value = unmarshal(pair[key_end + 1:])
            result[key] = value
        return result
    else:
        raise ValueError("Invalid serialized object")
    
# print(unmarshal('i:42'))
# print(unmarshal('d:{s:key:s:value,s:number:i:123}'))





from typing import Any

# Escape special characters in strings
def escape_string(s: str) -> str:
    return s.replace("\\", "\\\\").replace(":", "\\:").replace(",", "\\,")

# Unescape special characters in strings
def unescape_string(s: str) -> str:
    return s.replace("\\,", ",").replace("\\:", ":").replace("\\\\", "\\")

def marshal(obj: Any) -> str:
    """Convert a Python data structure into a custom string format."""
    if isinstance(obj, int):
        return f"i:{obj}"
    elif isinstance(obj, bool):
        return f"b:{str(obj).lower()}"
    elif isinstance(obj, str):
        return f"s:{escape_string(obj)}"
    elif isinstance(obj, list):
        return f"l:[{','.join(marshal(item) for item in obj)}]"
    elif isinstance(obj, tuple):
        return f"t:({','.join(marshal(item) for item in obj)})"
    elif isinstance(obj, dict):
        return f"d:{{{','.join(f'{marshal(key)}:{marshal(value)}' for key, value in obj.items())}}}"
    else:
        raise TypeError(f"Unsupported type: {type(obj)}")

def unmarshal(serialized_obj: str) -> Any:
    """Parse the custom string format back into the original Python data structure."""
    def parse_nested(data: str, start_char: str, end_char: str) -> list:
        """Helper to parse nested structures like lists, tuples, or dicts."""
        stack, result, current = [], [], ""
        for char in data:
            if char == start_char:
                stack.append(char)
                current += char
            elif char == end_char:
                stack.pop()
                current += char
            elif char == "," and not stack:
                result.append(current)
                current = ""
            else:
                current += char
        if current:
            result.append(current)
        return result

    if serialized_obj.startswith("i:"):
        return int(serialized_obj[2:])
    elif serialized_obj.startswith("b:"):
        return serialized_obj[2:] == "true"
    elif serialized_obj.startswith("s:"):
        return unescape_string(serialized_obj[2:])
    elif serialized_obj.startswith("l:"):
        inner = serialized_obj[3:-1]  # Strip 'l:[' and ']'
        if not inner:
            return []
        items = parse_nested(inner, "[", "]")
        return [unmarshal(item) for item in items]
    elif serialized_obj.startswith("t:"):
        inner = serialized_obj[3:-1]  # Strip 't:(' and ')'
        if not inner:
            return ()
        items = parse_nested(inner, "(", ")")
        return tuple(unmarshal(item) for item in items)
    elif serialized_obj.startswith("d:"):
        inner = serialized_obj[3:-1]  # Strip 'd:{' and '}'
        if not inner:
            return {}
        pairs = parse_nested(inner, "{", "}")
        result = {}
        for pair in pairs:
            # Find the key-value delimiter safely
            key, value = split_key_value(pair)
            result[unmarshal(key)] = unmarshal(value)
        return result
    else:
        raise ValueError(f"Invalid serialized object: {serialized_obj}")

def split_key_value(pair: str) -> tuple:
    """Safely split a key-value pair at the correct colon."""
    stack = 0
    for i, char in enumerate(pair):
        if char in "{[(":
            stack += 1
        elif char in "}])":
            stack -= 1
        elif char == ":" and stack == 0:
            return pair[:i], pair[i + 1:]
    raise ValueError(f"Malformed key-value pair: {pair}")


# print(unmarshal('d:{s:key:s:value,s:number:i:123}'))
# print(unmarshal('i:42'))



from numbers import Number
from typing import Dict, Union, List, Any

# Type aliases
RawDataRecord = Dict[Any, Union[Number, str, None]]
FilteredDataRecord = Dict[Any, Union[Number, str]]


def temp_map(mapped_data):
    """Convert all 'value' fields to float, setting to 0 if conversion fails."""
    result = []
    for record in mapped_data:
        new_record = record.copy()  # Avoid modifying input
        try:
            new_record["value"] = float(str(new_record["value"]).strip())
        except (ValueError, TypeError):
            new_record["value"] = 0
        result.append(new_record)
    return result


def temp_filter(raw_data):
    """Filter records where 'metric' is 'temp' and 'value' is valid."""
    filtered_data = []
    for record in raw_data:
        # Ensure 'metric' is 'temp' and 'value' exists
        if record.get("metric") == "temp" and record.get("value") is not None:
            try:
                float(str(record["value"]).strip())  # Ensure value is numeric
                filtered_data.append(record)
            except (ValueError, TypeError):
                continue
    return filtered_data


def temp_reduce(mapped_data, default: Number) -> Number:
    """Calculate the average temperature from mapped data."""
    total = 0
    count = 0
    for record in mapped_data:
        total += record["value"]
        count += 1
    return total / count if count > 0 else default


def validate_and_calculate(raw_data, default: Number = 0) -> Number:
    """
    Process raw data:
    1. Filter invalid records.
    2. Map 'value' to float.
    3. Reduce to calculate average temperature.
    """
    return temp_reduce(temp_map(temp_filter(raw_data)), default)



raw_data = [
    {"key": 1, "timestamp": 1234567, "metric": "temp", "value": "+12"},
    {"key": 2, "timestamp": None, "metric": "temp", "value": "+10"},
    {"key": 3, "timestamp": 1234569, "metric": "temp", "value": 11},
    {"key": "4", "timestamp": 1234570, "metric": "", "value": "88"},
]
print(validate_and_calculate(raw_data))  




from numbers import Number
from typing import Dict, Union, List, Any


RawDataRecord = Dict[Any, Union[Number, str, None]]
FilteredDataRecord = Dict[Any, Union[Number, str]]


def temp_map(mapped_data):
    """Convert all 'value' fields to float, setting to 0 if conversion fails."""
    for record in mapped_data:
        try:
            record["value"] = float(record["value"])
        except (ValueError, TypeError):
            record["value"] = 0
    return mapped_data


def temp_filter(raw_data):
    """Filter records where 'metric' is 'temp' and 'value' is valid."""
    filtered_data = []
    for record in raw_data:        
        if record.get("metric") == "temp" and record.get("value") is not None:
            try:
                float(record["value"])  
                filtered_data.append(record)
            except (ValueError, TypeError):
                continue
    return filtered_data


def temp_reduce(mapped_data, default: Number):
    """Calculate the average temperature from mapped data."""
    total = 0
    count = 0
    for record in mapped_data:
        total += record["value"]
        count += 1
    return total / count if count > 0 else default


def validate_and_calculate(raw_data, default: Number = 0) -> Number:
    return temp_reduce(temp_map(temp_filter(raw_data)), default)


raw_data = [
    {"key": 1, "timestamp": 1234567, "metric": "temp", "value": "+12"},
    {"key": 2, "timestamp": None, "metric": "temp", "value": "+10"},
    {"key": 3, "timestamp": 1234569, "metric": "temp", "value": 11},
    {"key": "4", "timestamp": 1234570, "metric": "", "value": "88"},
]
print(validate_and_calculate(raw_data)) 