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





from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    result = []
    for num in range(1, n + 1):
      if num % 15 == 0:
        result.append("FizzBuzz")
      elif num % 3 == 0:
        result.append("Fizz")
      elif num % 5 == 0:
        result.append("Buzz")
      else:
        result.append(num) 
  
    return result

n = 16
fizzbuzz_list = get_fizzbuzz_list(n)
# print(fizzbuzz_list)



def foo(nums):

    if not nums:
        return []

    total_product = 1
    for num in nums:
        total_product *= num

    result = []
    for num in nums:
        result.append(total_product // num)

    return result


nums = [3, 2, 1]
result = foo(nums)
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





def get_tuple(num: int):
    string = str(num)
    listed = []
    for i in string:
        integer = int(i)
        listed.append(integer)
    converted = tuple(listed)
    return converted


# print(get_tuple(87178291199))



def get_pairs(lst: list):
    pairs = []
    for i in range(len(lst) - 1):
        pair = (lst[i], lst[i + 1])
        pairs.append(pair)
    return pairs


# print(get_pairs([1, 2, 3, 8, 9]))
# print(get_pairs(['need', 'to', 'sleep', 'more']))



def get_dict(s: str):
    char_freq = {}
    for char in s.lower():
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq 

# print(get_dict('Oh, it is python'))




from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    dct = {}
    for i in lst:
        for k, v in i.items():
            dct[v] = dct.get(k, v)
    sett = set(dct)
    return sett 

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





a = [-4, 4, 5, -1, -2, 4, 7, -9]
# print(list(map(abs, a))) 

import numpy 

a = numpy.array([-4, 4, 5, -1, -2, 4, 7, -9])
sorted = numpy.abs(a)
# print(sorted) 
   

number = [0, 3, 2, 0, 1, 0, 0, 4, 5]
no_zero = []
zero = []

for num in number:
    if num != 0:
        no_zero.append(num)
    else:
        zero.append(num)

no_zero.reverse()
result = no_zero + zero
# print(result) 



fixed = []
appended = []
half_append = []
user = int(input('enter the number of loop: '))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

appended.append(nums[:user])
half_append.append(nums[user:])

appends_added = half_append + appended
for i in appends_added:
    for j in i:
        fixed.append(j)
# print(fixed)