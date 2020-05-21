if __name__ == '__main__':
    with open('./1_sample_input.txt', 'r') as f:
        lines = f.readlines()
        nums = list()
        for l in lines:
            nums.append(int(l[:-1]))
            print(l[:-1])
        print(nums)
