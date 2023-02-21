from easy import treasure, water_1, water_2

name = input("Введіть свій нік: ")
print("ви вибрали нкнейм ", name)

print("Виберіть складність")

complexity = {
    1: "легкий",
    2: "середній",
    3: "складний"
}

print(complexity)

while True:
    try:
        level = int(input("Введіть число: "))
                
        if level in complexity:
            break
        else:
            raise Exception()
    except:
        print("зробіть вибір")


if level == 1:
    print("Ви вибрали легкий рівень")
    treasure()
    water_1()
    water_2()
elif level == 2:
    print("Ви вибрали середній рівень")
elif level == 3:
    print("Ви вибрали складний рівень")