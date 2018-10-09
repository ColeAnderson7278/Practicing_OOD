from core import *


def main():
    # test_wheel = Wheel(26, 1.5)
    # test_gear = Gear(52, 11, test_wheel)
    # print(test_gear.gear_inches())
    bike = Bicycle("M", "red")
    print(bike.size)
    print(bike.tape_color)


if __name__ == '__main__':
    main()
