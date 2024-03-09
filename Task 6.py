score = input("Введите счёт (через :): ")
nums = score.split(":")
n = int(nums[0])
k = int(nums[1])
if n < k:
    print(2)
elif n > k:
    print(1)
else:
    print(0)