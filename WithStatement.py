#The with statement calls __enter__() and __exit(). Thus, it can open and close a file automatically.

class WithStatementTestClass:
    def __init__(self):
        print("WithStatementTestClass object created.")

    '''
    This is called by with.
    '''
    def __enter__(self):
        print("__enter__ method called")
        return self

    '''
    This is called by with.
    '''
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_type: {}".format(exc_type))
        print("exc_val: {}".format(exc_val))
        print("traceback: {}".format(exc_tb))

    '''
    This is called by the format method.
    '''
    def __repr__(self):
        return "This is the WithStatementTestClass object"

#This if statement says is this being run directly by python or is it being imported.
#You use this because sometimes you only want to run code if it is the main file.
if __name__ == "__main__":
    with WithStatementTestClass() as object:
        print("Processing objects: {}".format(object))

    print("\nIndentation block is left")
