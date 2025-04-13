def filter_by_division(nums, divisor):
    res = []
    for num in nums:
        if num % divisor == 0:
            res.append(num)
    return res

nums = [1, 23, 165, 2, 3, 92, 10, 34, 911]
divisor = 3
print(filter_by_division(nums, divisor))