def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / height ** 2
    print(bmi)
    if bmi < 18.5:
        print("Under Weight")
        print(int(-1))
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        print(int(0))
        return 0
    elif bmi > 25.0:
        print("Over Weight")
        print(int(1))
        return 1

calculate_bmi(weight=57, height=1.73)
