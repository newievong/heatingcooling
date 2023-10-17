def heating_cooling(actual_temp, desired_temp):
    while actual_temp != desired_temp:
        if actual_temp > desired_temp:
            print("Run A/C")
            actual_temp = actual_temp - 1
            print(actual_temp)

        elif actual_temp < desired_temp:
            print("Run Heat")
            actual_temp = actual_temp + 1
            print(actual_temp)

    else:
        print("Standby")

actual_temp = int(input("Enter the actual temperature: "))
desired_temp = int(input("Enter the desired temperature: "))

