def get_numbers():
    i = float(input("How many numbers would you like to enter ?\n~ "))
    a = int(i)
    N_arr = []
    for j in range(a):
        numbers = float(input(f"Enter Your {j+1} number:\n~ "))
        j +=1
        N_arr.append(numbers)
    return N_arr


def Find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range (1, len(arr)):
        if arr[i] < smallest:
            smallest = arr [i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    New_arr =[]
    for i in range (len(arr)):
        smallest = Find_smallest(arr)
        New_arr.append(arr.pop(smallest))
    return New_arr

sorted_list=selection_sort(get_numbers())
print(sorted_list)
num = float(input("Choose a number in your list:\n~"))

def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low<= high:
        mid=(low+high)//2
        guess=list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

result=binary_search(sorted_list,num)
if result == None:
    print("Your Number is not present in the list")
else:
    print(f"Your Number is a the {result} position ")



































# mess='~'
# j=0
# a=1
# arr = []
# i =int(input(f"how many numbers would you like to enter ?\n{mess} "))
# for j in range(i):
#     numbers = int(input(f"Enter Your {a} number\n{mess}"))
#     j += 1
#     a +=1
#     arr.append(numbers)
# def Find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
# def selection_sort(arr):
#     NewArr=[]
#     for i in range(len(arr)):
#         smallest = Find_smallest(arr)
#         NewArr.append(arr.pop(smallest))
#     return NewArr
# NewArr=selection_sort(arr)
# print(NewArr)
# number = int(input("Choose a number in the list that you gave :\n"))
# def binary_search(list,item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = (low + high)//2
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
# result=binary_search(NewArr,number)
# if result == None:
#     print("Your number is not present in the list")
# else:
#     print(f"Your number is at the position {result} ")







# arr = []
# i = int(input("How many numbers would you like to enter? "))
# for j in range(i):
#     number = int(input(f"Enter number {j+1}: "))
#     arr.append(number)
#
# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = find_smallest(arr)
#         new_arr.append(arr.pop(smallest))
#     return new_arr
#
# sorted_arr = selection_sort(arr)
# print(sorted_arr)
#
# number = int(input("Choose a number in the list: "))
#
# def binary_search(arr, item):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = arr[mid]
#         if guess == item:
#             return mid
#         elif guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# result = binary_search(sorted_arr, number)
# if result == None:
#     print("Your number is not present in the list")
# else:
#     print(f"Your number is at the position {result} ")
