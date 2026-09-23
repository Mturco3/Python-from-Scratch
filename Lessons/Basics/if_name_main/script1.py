if __name__ == "__main__":
    print("Hello from script1.py"
          "This will be executed only if script1.py is called directly")
else:
    print("Hello from script1.py, I was imported as a module!"
          "This will be executed only if script1.py is imported")
    
def func1():
    print("func1 is called from script1.py")