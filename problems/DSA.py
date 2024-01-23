# def rotate( arr, n):
#     stack = []
#     ele = arr.pop()
#     for i in range(n-1):
#         stack.append(arr[i])
#     stack.insert(0, ele)
#     print(stack)


# arr = [1,2,3,4,5]
# n = 5
# rotate(arr,n)    
###########################ncr
# def permut(n,r):
#     res = 1
#     for i in range(r):
#         res = res*(n-i)
#         res = res//(i+1)
#     return res

# # ans = permut(10,3)
# # print(int(ans))

# def eleOfN(n):
#     for i in range(n+1):
#         print(permut(n,i))


# # eleOfN(4)

# def elOfN(n):
#     ans = 1
#     print(ans)
#     for i in range(n-1):
#         ans = ans * ((n-1)-i)
#         i+=1
#         ans = ans // i
#         print(ans)    

# elOfN(5)
# nums = [0,1,0,3,12]
# arr = sorted(nums, reverse=True)
# print(arr)
# nums = arr

# print(nums)    

#majority elemnt
# nums = [3,2,3]
# dictnry = {}
# srt_arr = sorted(nums)
# for i in range(len(nums)):
#     if srt_arr[i] not in dictnry.keys():
#         dictnry[srt_arr[i]] = 1
#     elif srt_arr[i] in dictnry.keys():
#         dictnry[srt_arr[i]]+=1
        

# max_key=[]
# max_val = max(dictnry.values())
# print(max_val)
# for key,value in dictnry.items():
#     if max_val == value:
#         max_key.append(key)

# print(max_key)  
digits = "4"
# dictnry = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
# result = [['d', 'e', 'f'], ['g', 'h', 'i']]
# for i in digits:
#     key = int(i)
#     if key in dictnry:
#         result.append(dictnry[key])
#     else:
#         print(0)

# print(result)        
# # final = []
# dictnry = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
# result = []
# for i in digits:
#     key = int(i)
#     if key in dictnry:
#         result.append(dictnry[key])

# final = []        
# if len(result) == 0:
#     print("[]")
# elif len(result) == 1:
#     final = result[0]
# elif len(result) == 2:
#     for ele1 in (result[0]):
#         for ele2 in (result[1]):
#             final.append(str(ele1)+str(ele2))

# print(final)
##########################################
# nums = [5,7,7,8,8,10]
# target = 8        
# res = []
# for j in range(0,len(nums),-1):
#     if target == nums[j]:
#         res.append(j)
#         break
# for i in range(len(nums)):
#     if target == nums[i]:
#         res.append(i)
        


# if res:        
#     print(res)
# else:
#     print([-1,-1])

#######################################Nth root of m
# def NthRoot(n: int, m: int) -> int:
#     low = 1
#     high = m
#     while low<=high:
#         mid = (low+high)//2
#         mid_power = mid**n
#         if mid_power < m:
#             low = mid+1
#             print('1')
#         elif mid_power > m:
#             high = mid-1
#             print('2')
#         elif mid_power == m:
#             return mid
#     return -1  

# n = int(input())
# m = int(input())
# result = NthRoot(n, m)
# print(result)
##############################koko eating bananas
# import math
# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         def max_hours(arr, hour_rate):
#             total_hours = 0
#             n = len(arr)
#             for i in range(n):
#                 total_hours += math.ceil(arr[i]/hour_rate)
#             return total_hours
#         low = 1
#         high = max(piles)
#         while low <= high:
#             mid = (low+high)//2
#             ans = max_hours(piles, mid)
#             if ans > h:
#                 low = mid+1
#             elif ans <= h:
#                 high = mid-1
#         return low
#####################################################search in 2D
# def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix[0])
#         n = len(matrix)
#         low = 0
#         high = m*n -1
#         while low <= high:
#             mid = (low+high)//2
#             row = mid // m
#             col = mid%m
#             if target == matrix[row][col]:
#                 return True
#             elif target < matrix[row][col]:
#                 high = mid-1
#             else:
#                 low = mid+1
#         return False     
################################################strings
#############Reverse in a string

# def reverseWords(s: str) -> str:
#         arr = s.split(' ')
#         arr2 = []
#         print("arr1", arr)
#         for i in range(len(arr)-1,-1,-1):
#             if arr[i] != "":
#                 arr2.append(arr[i])
#         print(arr2)        
#         return " ".join(arr2)   

# ans = reverseWords("a good   example")
# print(ans)        

########################remove outer parenthesis

# def removeOuterParentheses(s: str) -> str:
#     res = []
#     opened = 0
#     for char in s:
#         if char == "(" and opened>0:
#             res.append(char)
#         elif char == ")"  and opened>1:
#             res.append(char)
#         opened += 1 if char == "(" else -1
#     return "".join(res)           

# ans = removeOuterParentheses("(()())(())(()(()))")   
# print(ans)     
###################Roman to Integers
# def romanToInt(self, s: str) -> int:
#     dictn = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
#     total = 0
#     i = 0
#     while i < len(s):
#         if s[i:i+2] in dictn:
#             total+=dictn[s[i:i+2]]
#             i+=2
#         elif s[i] in dictn:
#             total+=dictn[s[i]]
#             i+=1
#     return total            
#################longest palindromic substring
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         count = 0
#         ans = ""
#         if len(s) == 1:
#             return s
#         if len(s) == 2:
#             if s[0] == s[1]:
#                 return s
#             else:
#                 return s[1]        
#         for i in range(len(s)):
#             for j in range(i+1, len(s)+1):
#                 if s[i:j] == s[i:j][::-1]:
#                     if count < len(s[i:j]):
#                         count = len(s[i:j])
#                         ans = s[i:j]
#         return ans
####################################Linked list,delnode
# class Solution:
#     def deleteNode(self, node):
    
#         node.val = node.next.val
#         node.next = node.next.next
##############################LLsearch
# def searchInLinkedList(head, k):
#     n = head
#     while n is not None:
#         if n.data == k:
#             return 1
#         n=n.next    
#     return 0          