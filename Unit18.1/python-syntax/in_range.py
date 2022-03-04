def in_range(nums, lowest, highest):

    for num in nums:
        if num >= lowest and num <= highest:
            print(num)


    # YOUR CODE HERE


print(in_range([10, 20, 30, 40, 50], 15, 30))            
