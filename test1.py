# def bin_seach(arr,ele):
#     low = 0
#     high = len(arr) - 1
#     while low<=high:
#         mid = (low+high)//2
#         if arr[mid] == x:
#             return mid
#         elif x<arr[mid]:
#             high = mid-1
#         else:
#             low = mid+1
#     return "not found"        

# arr = [11,22,33,44,55,76,87,98,189]
# x = 11
# res = bin_seach(arr,x)
# print(res)

# arr = [11,22,33,44,55,76,87,98,189]
# l = [x for x in arr if x%2==0]
# print(l)
# def mu_2(x):
#     return x*x


# l1 = [1,2,3,4,5,6,7]
# sq = map(mu_2, l1)

# for i in sq:
#     print(i)

# res = lambda x,y,z: x+2*y+3*z
# res1 = res(3,2,1)
# print(res1)
# nm = input()
# res = nm[::-1]
# if nm==res:
#     print("y")
# else:
#     print("no")   
# n = int(input()) 
# prev2 = 0
# prev = 1
# for i in range(2,n+1):
#     curr = prev+prev2
#     prev2 = prev
#     prev = curr
    
# print(prev)    

 