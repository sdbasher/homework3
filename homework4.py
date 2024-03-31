name = input("Enter your name: ")
age = input("Enter your age: ")

if not age.isdigit():
    print("Помилка, повторіть введення")
elif 0 < int(age) <= 9:
    print("Привіт, шкет", name)
elif 9 < int(age) < 17:
    print("Як справи?", name)
elif 17 < int(age) < 100:
    print("Що бажаєте?", name)
else:
    print(name, "ви брешете - у наш час стільки не живуть...")
