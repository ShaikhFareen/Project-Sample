height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")
bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)
print(bmi_as_int)

height = input("Enter your height in m:")
weight = input("Enter your weight in kg:")
weight = int(weight)
height = float(height)
bmi = weight / (height * height)
print(bmi)
