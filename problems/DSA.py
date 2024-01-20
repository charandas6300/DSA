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
#####################################################
        