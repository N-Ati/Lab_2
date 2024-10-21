def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    BMI = weight / (height * height)
    print("Your BMI is = " + str(BMI))

    if BMI < 18.5:
        print("Weight Classification: Underweight")
    elif 18.5 <= BMI <= 25.0:
        print("Weight Classification: Normal Weight")
    elif BMI > 25.0:
        print("Weight Classification: Overweight")

calculate_bmi(weight=57, height=1.73)

