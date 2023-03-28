#!/usr/bin/python3
def safe_print_integer(value):
    try:
        check = False;
        int(value)
        print("{:d}".format(value))
        check = True

    except ValueError:
        pass
    finally:
        return check
