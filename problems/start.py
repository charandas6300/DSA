# print("helloworld")
# n=int(input())

# if n%2 == 0:
#     print("even")
#     if n==2:
#         print("2eve")
#     else:
#         print(n)    
# else:
#     print("odd")    
# n=1
# m=int(input("enter m"))
# while n<m:
#     print(n)
#     n+=1

# prime

# n=int(input())
# d=2
# flag = 10
# while d<n:
#     if n%d==0:
#         flag=11
        
#     d=d+1
    
    
# if flag == 11:
#     print("not")
# else:
#     print("yep")

# print prime

# n=int(input())
# k=2
# while k<=n:
#     d=2
#     flag = False
#     while d<k:
#          if k%d==0:
#            flag=True
#          d=d+1
#     if flag == False:
#         print(k)
#     k=k+1


# n=int(input())
# k=2
# while k<n:
#     d=2
#     flag=False
#     while d<k:
#         if k%d==0:
#             flag=True
#         d=d+1

#     if flag==True:
#         print(k)

#     k=k+1     

#patterns
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         c=n
#         print(c,end='')
#         j=j+1
#     print()
#     i=i+1    

#print patterns
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print((n-j)+1,end='')
#         j=j+1
#     print("")
#     i=i+1

##############

# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while i>=j:
#         print((i+1),end='')
#         j=j+1
#     print("")
#     i=i+1  

#####################
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     p=i
#     while j<=i:
#         print(p,end='')
#         j=j+1
#         p=p+1
#     print("")
#     i=i+1
########################
# n=int(input())
# i=1
# p=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(p,end="")
#         p=p+1
#         j=j+1
#     print("")
#     i=i+1    
 
 ##########################
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         charP=chr(ord('A')+j-1)
#         print(charP,end="")
#         j=j+1
#     print("")
#     i=i+1


###inverted patterns
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         print("*",end="")
#         j=j+1
#     print("")
#     i=i+1
###################3#
# n=int(input())
# i=1
# while i<=n:
#     j=1
#     while j<=n-i+1:
#         print(j,end="")
#         j=j+1
#     print("")
#     i=i+1
#####################
# n=int(input())
# i=1
# while i<=n:
#     spaces=1
#     while spaces<=n-i:
#         print(" ",end="")
#         spaces=spaces+1
#     stars=1
#     while stars<=i:
#         print("*",end="")
#         stars=stars+1
#     print()
#     i=i+1
########################
# n= int(input())
# arr = (int(i) for i in input().split())
# sum = 0
# for x in arr:
#     sum = sum + x
    
# print(sum)
####
# arr = [2,3]
# print(sum(arr))
# arr = []
# n = int(input())
# for i in range(0,n):
#     dt = int(input())
#     arr.append(dt)
 
    
# arr.sort(reverse=True)
# print(arr)   
# for j in (0,len(arr)):
#     # if(arr[j]==arr[j+1]):
#     #     arr[j]=arr[j+1]
#     # else:
    
#     #     print("out")
# r = arr[j+1]
# print(r)  
# #########################           
# arr = []
# n = int(input())
# for i in range(0,n):
#     dt=int(input())
#     arr.append(dt)

# arr.sort()
# print(arr)
# for j in arr:
#     r=len(arr)%2
#     if(r==0):
#         p=len(arr)
#         print((arr[r]+(arr[r]-1))/2)
#         break
#     else:
#         print(arr[r])
#         break
#######################
a = {1:2,'list':[1,2],3:5}
a.pop('list')
a['list'] = [3,5]
print(a['list'])