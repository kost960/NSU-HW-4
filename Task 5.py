catch = input("Введите уловы рыбаков: ")
nums = catch.split(" ")
n = int(nums[0])
k = int(nums[1])
if n < k:
    print(n)
else:
    print(k)