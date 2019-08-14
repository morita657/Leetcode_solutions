def main(numbers):
    output = [0 for _ in range(len(numbers))]
    for i in range(len(numbers)):
        nums = numbers[:i] + [numbers[i] + 1] + numbers[i + 1:]
        calc = 1
        for j in range(len(numbers)):
            calc *= nums[j]
        output.append(calc)
    return max(output)


print(main([1, 2, 3]))
print(main([1, 3, 2, 1, 1, 3]))
print(main([1000, 999, 998, 997, 996, 995]))
print(main([1, 1, 1, 1]))
