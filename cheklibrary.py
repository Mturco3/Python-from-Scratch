library = input("Enter the library name: ")

try:
    __import__(library)
    print(f'The library "{library}" is installed.')
except ImportError:
    print(f'"{library}" not installed.')