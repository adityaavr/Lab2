import statistics
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    txt = input("User Input: ")
    x = txt.split(",")
    print("User input: " + str(x))
    numbers = [float(n) for n in x]
    return numbers


def calc_average_temperature(numbers):
    avg = sum(numbers) / len(numbers)
    print("Average temperature: " + str(avg))

def calc_min_max_temperature(numbers):
    min_temp = min(numbers)
    max_temp = max(numbers)
    print("Lowest temperature: " + str(min_temp))
    print("Highest temperature: " + str(max_temp))
    numbers.sort(reverse=False)
    print(numbers)

def calc_median_temperature(numbers):
    median = statistics.median(numbers)
    print("The median temperature is " + str(median))






display_main_menu()
numbers = get_user_input()
calc_average_temperature(numbers)
calc_min_max_temperature(numbers)
calc_median_temperature(numbers)
