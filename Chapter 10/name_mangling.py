# Python code to illustrate how mangling works
# With method overriding
# A testing class for identifier
class Testing:
    # Giving Name as an identifier
    def __init__(self, name):
        # Identifier initializing with double underscore
        self.__name = name

    def print_name(self):
        print(self.__name)


t1 = Testing("A small Test")  # Calling variable name with the class
t1.print_name()  # Printing name in the output
# Accessing identifier outside the class
# print(t1.__name)  # will throw an error in the output
# Workaround
print("The name mangled that we are accessing outside the class:", t1._Testing__name)
