def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/height**2
    print(bmi)
    if bmi<18.5:
<<<<<<< HEAD
        rslt = -1

    elif 18.5<=bmi<=25.0:
        rslt = 0

    elif bmi>=25.0:
        rslt = 1

    print(rslt)
    return rslt

=======
        x = -1
        print(x)
    elif 18.5<=bmi<=25.0:
        y = 0
        print(y)
    elif bmi>=25.0:
        z = 1
        print(z)
>>>>>>> 06b4db110b94e344d23c76c1565160917d181fc8
calculate_bmi(weight=57, height=1.73)

