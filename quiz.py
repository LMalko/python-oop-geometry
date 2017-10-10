from geometry import *
import random


def random_shape():
    reasonable_range = 500
    random_number1 = float(random.choice(range(reasonable_range)))
    random_number2 = float(random.choice(range(reasonable_range)))
    random_number3 = float(random.choice(range(reasonable_range)))

    shape_object_choices = [Circle(random_number1),
                            EquilateralTriangle(random_number1),
                            Rectangle(random_number1, random_number2),
                            Square(random_number1),
                            RegularPentagon(random_number1),
                            Sector(random_number1, random_number2),
                            Paralleogram(random_number1, random_number2, random_number3)]
    return random.choice(shape_object_choices)


def start():
    print("Welcome to quiz")
    print("Your assignment: Calculate area and perimeter of:\n\n")
    shape_random_choice = random_shape()
    print(shape_random_choice)
    area = '{:.0f}'.format(shape_random_choice.get_area())
    perimeter = '{:.0f}'.format(shape_random_choice.get_perimeter())
    user_guess_area = input("\n\nArea = ")
    user_guess_area = input("\n\nPerimeter = ")
    print("\nCorrect answers:")
    print(area)
    print(perimeter)
    finish = input("Press anything to continue")


if __name__ == "__main__":
    start()
