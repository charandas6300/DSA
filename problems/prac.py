# name = input()
# age = int(input())
# print(f"The name of the person is {name} and the age is {age}.")
# i = 0
# for i in range(5):
#     a = i
# print(a) 
#------------------------------------------------------------------------------------------
# import queue   
# import collections
# queue = collections.deque()
# while not queue:
#     queue.appendleft(10)
#     queue.appendleft(20)
#     queue.appendleft(20)
#     queue.appendleft(40)

# print(queue)
# print(queue.__sizeof__)
# import queue
# import time
# q = queue.PriorityQueue()

# q.put(20)
# q.put(30)
# q.put(10)
# q.put(60)
# q.put(50)

# print(q)

# p=[]
# while not q.empty():
#     r=q.get()
#     print(r)
#     p.append(r)

# print(p)        

# strat =time.time()
# while not q.empty():
#     res = q.get()
#     print(res)
# end = time.time()
# print(f"{end - strat:.4f}")    
#444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         list1 = []
#         for num in nums:
#             if num not in list1:
#                 list1.append(num)
#             else:   
#                 list1.append(num) 
#                 c = num
#                 break   
           
       
#         for i in list1:
#             if list1[i] != c:
#                 print(c)
#                 del(list1[i])
#             return list1    
        
#         print(list1)
#         # return len(list1)

# # Create an instance of the Solution class
# solution = Solution()

# # Call the removeDuplicates method on the instance
# result = solution.removeDuplicates([3, 2, 2, 3])

# # print(result)  # Output: 5

s=input("string")
dici = {'I' : 1 , 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
sum = 0
for i in s:
    if s[i] in dici.keys():
        sum += dici.values(s[i])
print(sum)        