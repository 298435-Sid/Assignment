def hollow_triangle(height):
    for i in range(1, height + 1):
        if i == 1:
            print("*")
        elif i == height:
            print("*" * (2 * height - 1))
        else:
            spaces_inside = 2 * i - 3
            print("*" + " " * spaces_inside + "*")

hollow_triangle(5)