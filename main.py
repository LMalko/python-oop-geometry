import sys
import os
import time
from geometry import *


def check_if_positive(*args):
    ''' Prevent program from breaking if negative number.'''
    for i in args:
        if i <= 0:
            print("Negative number.")
            return False
    return True


def add_shape_to_table(shapes_list_table, shape):

    area = '{:^10.10}'.format('{:.2f}'.format(shape.area))
    perimeter = '{:^10.10}'.format('{:.2f}'.format(shape.perimeter))

    shape_details = ['{:^19}'.format(shape.__class__.__name__),
                     '{:^55}'.format(shape.__str__()),
                     perimeter,
                     '{:^16}'.format(shape.get_perimeter_formula()[shape.__class__.__name__]),
                     area,
                     '{:^23}'.format(shape.get_area_formula()[shape.__class__.__name__])]

    shapes_list_table.append(shape_details)

    return shapes_list_table


def add_shape(shapes_list, shapes_list_table):

    os.system("cls")
    shapes_supported = '''1. CIRCLE, 2. TRIANGLE, 3. EQUILATERALTRIANGLE, 4. RECTANGLE, 5. SQUARE,
                  6. REGULARPENTAGON, 7. SECTOR, 8. PARALLEOGRAM'''

    while True:
        available_options = ("1", "2", "3", "4", "5", "6", "7", "8")
        print("Shapes supported: " + shapes_supported)
        shape_choice = input("\n\nWhat's Your choice? ")
        if shape_choice not in available_options:
            os.system("cls")
            print("Select properly.")
            time.sleep(2)
            os.system("cls")
            continue
        else:
            break

    if shape_choice == "1":
        while True:
            radius = float(input("Radius: "))
            if check_if_positive(radius):
                break
        new_CIRCLE = Circle(radius)

        shapes_list.add_shape(new_CIRCLE)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_CIRCLE)

        govern_instance(shapes_list, shapes_list_table)

    if shape_choice == "2":
        while True:
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            if check_if_positive(a, b, c):
                break
        new_TRIANGLE = Triangle(a, b, c)

        shapes_list.add_shape(new_TRIANGLE)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_TRIANGLE)

        govern_instance(shapes_list, shapes_list_table)
        
    if shape_choice == "3":
        while True:
            a = float(input("a: "))
            if check_if_positive(a):
                break
        new_EQUILATERALTRIANGLE = EquilateralTriangle(a)

        shapes_list.add_shape(new_EQUILATERALTRIANGLE)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_EQUILATERALTRIANGLE)

        govern_instance(shapes_list, shapes_list_table)
    if shape_choice == "4":
        while True:
            a = float(input("a: "))
            b = float(input("b: "))
            if check_if_positive(a, b):
                break
        new_RECTANGLE = Rectangle(a, b)

        shapes_list.add_shape(new_RECTANGLE)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_RECTANGLE)

        govern_instance(shapes_list, shapes_list_table)
    if shape_choice == "5":
        while True:
            a = float(input("a: "))
            if check_if_positive(a):
                break
        new_SQUARE = Square(a)

        shapes_list.add_shape(new_SQUARE)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_SQUARE)

        govern_instance(shapes_list, shapes_list_table)
    if shape_choice == "6":
        while True:
            a = float(input("a: "))
            if check_if_positive(a):
                break
        new_REGULARPENTAGON = RegularPentagon(a)

        shapes_list.add_shape(new_REGULARPENTAGON)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_REGULARPENTAGON)

        govern_instance(shapes_list, shapes_list_table)
    if shape_choice == "7":
        while True:
            radius = float(input("Radius: "))
            arc_length = float(input("Arc_length: "))
            if check_if_positive(radius, arc_length):
                break
        new_SECTOR = Sector(radius, arc_length)

        shapes_list.add_shape(new_SECTOR)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_SECTOR)

        govern_instance(shapes_list, shapes_list_table)
    if shape_choice == "8":
        while True:
            base = float(input("Base: "))
            height = float(input("Height: "))
            side = float(input("Side: "))
            if check_if_positive(base, height, side):
                break
        new_PARALLEOGRAM = Paralleogram(base, height, side)

        shapes_list.add_shape(new_PARALLEOGRAM)
        shapes_list_table = add_shape_to_table(shapes_list_table, new_PARALLEOGRAM)

        govern_instance(shapes_list, shapes_list_table)


def menu():
    ''' Display menu.'''
    print("\n\nLearn Geometry.")
    print("  What do you want to do?")
    print("  (1) Add new shape.")
    print("  (2) Show all shapes")
    print("  (3) Show shape with the largest perimeter")
    print("  (4) Show shape with the largest area")
    print("  (5) Show formulas")
    print("  (6) Clear list, start again.")
    print("  (7) Save to file")##############
    print("  (0) Quit\n\n")


def govern_instance(shapes_list, shapes_list_table):
    ''' Seperate new list instance.'''

    os.system("cls")
    while True:
        menu()
        option = input("Your choice is: ")

        available_choices = ("1", "2", "3", "4", "5", "6", "7", "0")
        if option not in available_choices:
            os.system("cls")
            exit = input("\n\n\nNo such choice, try again.")
            os.system("cls")
            continue

        if option == "1":
            add_shape(shapes_list, shapes_list_table)

        if option == "2":
            os.system("cls")

            line_number = 0
            table_length = 154
            adjusted_column_names = "||ID\t\tSHAPE\t\t\t\t\t__str__\t\t\t\tPERIMETER\tFORMULA\t\tAREA\t\tFORMULA\t\t||"
            print("@" * table_length)
            print(adjusted_column_names)
            for i in shapes_list_table:
                print("||" + str('{:03d}'.format(line_number)) + ". " + "||" + "||".join(i) + "||")
                line_number += 1
            print("@" * table_length)

            exit = input("\n\n\nPress anything to exit.")
            os.system("cls")

        if option == "3":
            os.system("cls")
            print(shapes_list.get_largest_shape_by_perimeter())

            exit = input("\n\n\nPress anything to exit.")
            os.system("cls")

        if option == "4":
            os.system("cls")
            print(shapes_list.get_largest_shape_by_area())

            exit = input("\n\n\nPress anything to exit.")
            os.system("cls")

        if option == "5":
            os.system("cls")

            areas = Shape.get_area_formula()
            perimeters = Shape.get_perimeter_formula()

            print("AREAS:")
            for key, value in areas.items():
                print(key, ": ", value)

            print("\n\nPERIMETERS:")
            for key, value in perimeters.items():
                print(key, ": ", value)

            exit = input("\n\n\nPress anything to exit.")
            os.system("cls")

        if option == "6":
            main()

        if option == "7":
            pass

        if option == "0":
            quit()
        

def main():
    os.system("cls")
    # object containing all shapes added by the user
    shapes_list = ShapeList()
    shapes_list_table = []

    govern_instance(shapes_list, shapes_list_table)


if __name__ == "__main__":
    main()
