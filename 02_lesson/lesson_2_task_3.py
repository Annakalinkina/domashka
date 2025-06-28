def square(side):
    area = side ** 2
    return area
if __name__ == "__main__":
    side_length = 4
    area_result = square(side_length)
    print(f"Площадь квадрата со стороной {side_length}: {area_result}")