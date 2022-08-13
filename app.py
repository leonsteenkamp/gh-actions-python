# A little test program
# Leon Steenkamp
# 2022-08-22
#

def add(a, b):
    """Addition function
    Function that add two numbers
    """
    return (a + b)


def main():
    k = 5
    m = 5
    print(f"{k} + {m} = {add(k,m)}")


if __name__ == "__main__":
    main()
