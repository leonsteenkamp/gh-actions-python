# A little test program
# Leon Steenkamp
# 2022-08-22
#
"""A Test Application
"""

def add(first, second):
    """Addition function
    Function that add two numbers
    """
    return first + second


def main():
    """Main function
    """
    one = 5
    two = 5
    print(f"{one} + {two} = {add(one,two)}")


if __name__ == "__main__":
    main()
