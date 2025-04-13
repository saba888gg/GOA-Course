nums = [1, 2, 4, 18]
def join_integers(numbers):
    result = ""
    for num in numbers:
        result += str(num)
    return result
print(join_integers(nums))