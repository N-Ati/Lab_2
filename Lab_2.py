def main():
    print("ET0735 (DevOps for AIoT - Lab 2 - Introduction to Python)")
    display_main_menu() 
    num_list = get_user_input()

    average = calc_average(num_list)
    print("Average Temperature: " + str(average))
    
    min_max = find_min_max(num_list)
    print("Minimum Temperature: " + str(min_max[0])) #access minimum value, index 0
    print("Maximum Temperature: " + str(min_max[1])) #access maximum value, index 1

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    print("Please input numbers")
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

def sort_temp():
    print("sort_temp")

def calc_median_temp():
    print ("calc_median_temp")

if __name__=="__main__":
    main()