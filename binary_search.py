import time
mess = '~'
a = 1
j = 0
arr=[]
warning="ENTER YOUR NUMBER IN AN ASCENDING ORDER"
for x in range(5):
    print(mess,warning)
    time.sleep(0.5)


i = int(input(f'How many numbers would you like to add to the list ?\n{mess}'))

for j in range(i):

    numbers = int(input(f"enter your {a} number :\n{mess}"))
    j += 1
    arr.append(numbers)

number = int(input(f"choose a number in the list of numbers that you gave:\n{arr}\n{mess}"))


def binary_search(list,item):

    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
result=binary_search(arr,number)
if result == None:
    print("Your number is not present in the list")
else:
    print(f"your number is at the {result} position")
