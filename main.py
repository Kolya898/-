def c_e_d(number):
    if number % 2 == 0:
        return "парне"
    else:
        return "непарне"

try:
    num = int(input("Введіть число: "))
    result = c_e_d(num)
    print(f"Введене число {num} є {result}.")
except ValueError:
    print("Будь ласка, введіть ціле число.")