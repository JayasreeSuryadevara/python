# Given the array nums consisting of 2n elements in the form[x1, x2, ..., xn, y1, y2, ..., yn].
# Return the array in the form[x1, y1, x2, y2, ..., xn, yn].
#
# Example 1:
# Input: nums = [2, 5, 1, 3, 4, 7], n = 3
# Output: [2, 3, 5, 4, 1, 7]
# Explanation: Since x1 = 2, x2 = 5, x3 = 1, y1 = 3, y2 = 4, y3 = 7 then the answer is [2, 3, 5, 4, 1, 7].
#
# Example 2:
# Input: nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
# Output: [1, 4, 2, 3, 3, 2, 4, 1]
#
# Example 3:
# Input: nums = [1, 1, 2, 2], n = 2
# Output: [1, 2, 1, 2]


# Define the function shuffle that takes two arguments
# array of numbers => arr, and no of x values => n
def shuffle(arr, n):
  # initialize i to count x elements 
  # i + n will be the index of y elements

  # print(shuffle([1, 1, 2, 2], 2))
  # [1, 2, 1, 2]

  # arr = [1,1,2,2]
  # n = 2

  i = 0
  # put them into result array
  result = []               # result = []
  while i < n:              # 2 < 2
    result.append(arr[i])   # result = [1, 2, 1]
    result.append(arr[i+n]) # result[1,2, 1, 2]
    i += 1                  # i = i + 1 =>  i = 2
  
  # return the result 
  return result






# as the function returns an array we need to print it to see it
print(shuffle([2, 5, 1, 3, 4, 7], 3))
# [2, 3, 5, 4, 1, 7]
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
# [1, 4, 2, 3, 3, 2, 4, 1]
print(shuffle([1, 1, 2, 2], 2))
# [1, 2, 1, 2]

print(shuffle([1,1,1,1,1,1,2,2,2,2,2,2], 6))