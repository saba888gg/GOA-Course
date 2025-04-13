nums = [1, 2, 3, 4, 5, 6, 7]
def remove_odd_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result
print(remove_odd_numbers([1, 2, 3, 4, 5]))