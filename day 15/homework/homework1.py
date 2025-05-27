numbers = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]
even_sum = sum(num for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)