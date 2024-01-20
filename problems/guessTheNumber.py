import random

def guessing(x):
    random_num = random.randint(1,x)
    guess = 0
    while(guess != random_num):
        guess = int(input(f"guess a number btw 1 and {x}:"))
        print(guess)
        if guess < random_num:
            print("guessed number is low")
        elif guess > random_num:
            print("guess is greater than random number")
    print(f"you got the number {random_num}")       
################################################################################################
# def comp_guess(y):
#     random_num = random.randint(1,y)
#     correct = int(input())
#     while(random_num != correct):
#         if random_num < correct:
#             o = random_num+1
#             random_num = random.randint(o ,y)
#             print(f"random num is {random_num}")
#         elif random_num > correct:
#             j = random_num-1
#             random_num = random.randint(0 , j)
#             print(f"random num is {random_num}")    
#     print(f"correct is {random_num}")
# # n = int(input())
# # guessing(n)
# comp_guess(50)
######################################################################################################
def comp_guess(x):
    low = 0
    high = x
    random_num = random.randint(1,x)
    print(random_num)
    
    while random_num != 0:
        user = input("low: l, high:h, correct:c")
        if user == "l":
            low = random_num + 1
            random_num = random.randint(low,high)
            print(random_num)
        elif user == "h":
            high = random_num - 1
            random_num = random.randint(low,high)
            print(random_num)
        elif user == "c":
            break
    print(f"you got it {random_num}")            

comp_guess(1000)