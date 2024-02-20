# countdown
def countdown(n):
    return list(range(n,-1,-1))
result=countdown(5)
print(result)

# print and return 
def print_and_return(nums):
    value = nums[0]
    print(value)
    return nums[1]
result = print_and_return([1, 2])
print("Returned value:", result) 

# first plus length 
def first_plus_length(list) :
    return list[0] + len(list)
result = first_plus_length([2,3,4,5,6,7])
print(result)

# This Length, That Value 
def this_length_that_value(size,value) :
    return [value]*size
result=this_length_that_value(8,5)
print(result)

