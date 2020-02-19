import random


def generation_arr():
    return [random.randint(0,100) for _ in range(5)]


def sum_of_arr(arr):
    sum_of_arr=0
    for i in arr:
        sum_of_arr+=i
    return sum_of_arr


if __name__ == '__main__':
    calculate_arr = []
    max_arr = []
    arr_1 = generation_arr()
    calculate_arr.append(arr_1)
    arr_2 = generation_arr()
    calculate_arr.append(arr_2)
    arr_3 = generation_arr()
    calculate_arr.append(arr_3)
    arr_4 = generation_arr()
    calculate_arr.append(arr_4)
    arr_5 = generation_arr()
    calculate_arr.append(arr_5)
    arr_6 = generation_arr()
    calculate_arr.append(arr_6)
    arr_7 = generation_arr()
    calculate_arr.append(arr_7)
    arr_8 = generation_arr()
    calculate_arr.append(arr_8)
    arr_9 = generation_arr()
    calculate_arr.append(arr_9)
    arr_10 = generation_arr()
    calculate_arr.append(arr_10)
    for arr in calculate_arr:
        print(arr)
        print(sum_of_arr(arr))
    number = 0
    max_sum = 0
    max_number = 0
    for i in calculate_arr:
        number +=1
        if sum_of_arr(i) > max_sum:
            max_sum = sum_of_arr(i)
            max_arr = i
            max_number = number
    print("")
    print(max_number)
    print(max_sum)
    print(max_arr)