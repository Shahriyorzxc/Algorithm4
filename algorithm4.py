#1!
def arrBetween(num1, num2, arr,):
    result = []
    for x in arr:
        if num1 < x < num2:
            result.append(x)
    return result

print(arrBetween(3,8, [1,5,95,0,4,7]))
print(arrBetween(1,10, [1,10,25,8,11,6]))
print(arrBetween(7,32, [1,2,3,78]))

#2!
def incrementItems(arr):
    result = []
    for x in arr:
        result.append(x+1)
    return result

print(incrementItems([1,2,3]))
print(incrementItems([2,4,6,8]))
print(incrementItems([-1,-2,-3,-4]))

#3!
def calcAge(age_years):
    return age_years * 365

print(calcAge(65))
print(calcAge(0))
print(calcAge(20))

#4!
def is_in_range(num, range_dict):
   return range_dict["min"] <= num <= range_dict["max"]

print(is_in_range(4,{"min": 0, "max": 5})) #True
print(is_in_range(4, {"min": 4, "max": 10})) #True
print(is_in_range(4, {"min": 6, "max": 5})) #False
print(is_in_range(5, {"min": 5, "max": 5})) #True




