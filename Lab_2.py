def main():
    print("ET0735 (DevOps for AIoT - Lab 2 - Introduction to Python)")
    display_main_menu() 

    num_list = get_user_input()

    average = calc_average(num_list)
    print("Average Temperature: " + str(average))
    
    min_max = find_min_max(num_list)
    print("Minimum Temperature: " + str(min_max[0])) #access minimum value, index 0
    print("Maximum Temperature: " + str(min_max[1])) #access maximum value, index 1

    median_temp = calc_median_temp(num_list)
    print("Median Temperature: " + str(median_temp))

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    input_list = user_input.split(",")
    float_list = [float(num) for num in input_list]
    return float_list


def calc_average(temp):
    avg = sum(temp) / len(temp) # sum of inputs / length of list
    return avg

def find_min_max(temp):
    min_temp = min(temp)
    max_temp = max(temp)
    
    return [min_temp, max_temp] #return as integer list

def calc_median_temp(temp):
    temp.sort()
    n = len(temp)
    if n % 2 == 0:
        median = (temp[n//2 - 1] + temp[n//2]) / 2
    else:
        median = temp[n//2]
    return median
    

if __name__=="__main__":
    main()