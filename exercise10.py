# Given
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# Define a function, with two list as a parameter
# this function should return a new list
# loop through the first list to get all the odd numbers
# loop trough the second list to get all the even numbers
# return the modified new list

def combine_list(lst1, lst2):
    result = []
    for num in lst1:
        if num % 2 != 0:
            result.append(num)
    
    for num in lst2:
        if num % 2 == 0:
            result.append(num)

    return result


print(combine_list(lst1=list1, lst2=list2))
