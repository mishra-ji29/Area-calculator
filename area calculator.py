# noinspection NonAsciiCharacters
π = 22 / 7

# ////////////////////////////////////////////Dealing with area////////////////////////////////////////////////////////

while True:
    option = input("Which operation\nperimeter, area, volume:\n")

    if option == "area":

        option1 = input("Circle, Triangle, Parallelogram, Trapezium:\n")

        # Triangle

        if option1 == "triangle":
            height = float(input("Enter height:\n"))
            base = float(input("Enter base:\n"))
            area = 0.5 * base * height
            print("area of triangle =", area)
            area = height * base * 0.5

            # Parallelogram

        elif option1 == "parallelogram":
            length = float(input("Enter the length:\n"))
            breadth = float(input("Enter the breadth:\n"))
            area1 = length * breadth
            print("area of parallelogram =", area1)
            if length == breadth:
                print("It is a square/rhombus")

                # Circle

        elif option1 == "circle":
            radius = float(input("Enter radius:\n"))
            area_of_circle = π * radius ** 2
            print("Area of circle =", area_of_circle)

            # Trapezium

        elif option1 == "trapezium":
            DB2S = float(input("Enter distance between two sides:\n"))
            PS1 = float(input("Enter parallel side 1:\n"))
            PS2 = float(input("Enter parallel side2:\n"))
            area_of_trapezium = 0.5 * (PS1 + PS2) * DB2S
            print("Area of Trapezium =", area_of_trapezium)

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Dealing with perimeter///////////////////////////////////////////////////////

    elif option == "perimeter":

        option1 = input("Triangle, Circle, Parallelogram:\n")

        # Triangle

        if option1 == "triangle":

            side1 = int(input("enter side 1:\n"))
            side2 = int(input("enter side 3:\n"))
            side3 = int(input("enter side 2:\n"))
            perimeter_of_triangle = side1 + side2 + side3
            print("perimeter =", perimeter_of_triangle)
            # Equality
            if side1 == side2 and side1 == side3:
                print("It is an eqalitral triangle")

        # Circle

        elif option1 == "circle":
            radius = float(input("Enter radius"))
            circumference_of_circle = 2 * π * radius
            print("circumference of circle =", circumference_of_circle)

            # Parallelogram

        elif option1 == "parallelogram":
            length = float(input("Enter the length:\n"))
            breadth = float(input("Enter the breadth:\n"))
            perimeter_of_parallelogram = length * breadth
            print("perimeter of parallelogram = ", perimeter_of_parallelogram)
            if length == breadth:
                print("It is a rhombus/square")
            else:
                print('It is a parallelogram/rectangle')

                # Trapezium

        elif option1 == "trapezium":
            NPS1 = float(input("Enter other side 1:\n"))
            NPS2 = float(input("Enter other side 2:\n"))
            PS1 = float(input("Enter parallel side 1:\n"))
            PS2 = float(input("Enter parallel side2:\n"))
            POT = PS1 + PS2 + NPS1 + NPS2
            print("Perimeter of Trapezium =", POT)

    # ////////////////////////////////////////////Dealing with volume//////////////////////////////////////////////////

    elif option == "volume":

        option1 = input("Cube, Cuboid, Cylinder, Sphere, Hemisphere. Cone:\n")

        # Cone

        if option1 == "cone":
            r = float(input("Enter radius:\n"))
            h = float(input("Enter height:\n"))
            VOC = 1 / 3 * π * h * r ** 2
            print("Volume of cone =", VOC)

        # Sphere

        elif option1 == "sphere":
            r1 = float(input("Enter radius:\n"))
            VOS = 4 / 3 * π * r1 ** 3
            print("Volume of sphere = ", VOS)

            # Hemisphere

        elif option1 == "hemisphere":
            r2 = float(input("Enter radius:\n"))
            VOHS = 2 / 3 * π * r2 ** 3
            print("Volume of hemisphere = ", VOHS)

            # Cylinder

        elif option1 == "cylinder":
            r3 = float(input("Enter radius:\n"))
            h1 = float(input("Enter height:\n"))
            VOCY = π * r3 ** 2 * h1
            print("Volume of cylinder = ", VOCY)

            # Cube

        elif option1 == "cube":
            s = float(input("Enter side of cube:\n"))
            VOCU = s ** 3
            print("Volume of cube = ", VOCU)

            # Cuboid

        elif option1 == "cuboid":
            l1 = float(input("Enter length of cuboid:\n"))
            b1 = float(input("Enter breadth of cuboid:\n"))
            h2 = float(input("Enter height of cuboid:\n"))
            VOCO = l1 * b1 * h2
            print("Volume of cuboid = ", VOCO)

            # samapt

    else:
        print("Invalid input")

    again = input("Do you want to calculate anything again??\n")

    if again == "yes":
        print()
        continue

    else:
        print("Thank you")
        break
