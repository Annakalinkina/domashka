from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79171234567"),
    Smartphone("Samsung", "Galaxy S21", "+79271234567"),
    Smartphone("Xiaomi", "Mi 11", "+79371234567"),
    Smartphone("Huawei", "P40 Pro", "+79871234567"),
    Smartphone("Google", "Pixel 6", "+79271234567"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")