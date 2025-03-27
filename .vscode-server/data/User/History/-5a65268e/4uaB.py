import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the program name
    total = sum(int(arg) for arg in argv)  # Sum of all arguments as integers
    print(total)
