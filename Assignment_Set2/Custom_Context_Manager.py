class DatabaseConnection:
    def __enter__(self):
        print("Connecting to Database...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print("Error:", exc_value)
        print("Closing Database Connection safely.")
        return True  

with DatabaseConnection():
    print("Processing data...")
    raise Exception("something went wrong")