#Student Practice-

def practice_1_basic_exceptions():
    """
    Practice identifying and handling common exceptions
    """
    print("\n" + "="*50)
    print("EXERCISE 1: Handle the Exceptions")
    print("="*50)


    # TODO 1: Fix division by zero
    def safe_divide(a, b):
        """Return a/b or None if division by zero"""
        try:
            return a / b
        except ZeroDivisionError:
            return None


    # Test your function
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")


    # TODO 2: Fix list index error
    def safe_get_item(lst, index):
        """Get item at index or return 'Not found'"""
        try:
            return lst[index]
        except IndexError:
            return "not found"


    # Test your function
    my_list = [1, 2, 3]
    print(f"Item at index 1: {safe_get_item(my_list, 1)}")
    print(f"Item at index 10: {safe_get_item(my_list, 10)}")

    # TODO 3: Handle multiple exceptions
    def convert_to_number(value):
        """Convert string to int or float, return None if impossible"""
        try:
            # Integer conversion first
            return int(value)
        except (ValueError, TypeError):
            # If int fails, try float
            try:
                return float(value)
            except (ValueError, TypeError):
                return None


    # Test conversions
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = convert_to_number(val)
        print(f"Converting '{val}': {result}")



# Run the practice
practice_1_basic_exceptions()

def practice_2_exception_hierarchy():
    """
    Practice with exception hierarchy
    """
    print("\n" + "="*50)
    print("EXERCISE 2: Exception Hierarchy")
    print("="*50)

    # TODO 1: Catch multiple related exceptions efficiently
    def access_data(data_structure, key):
        """
        Access data[key] whether data is list or dict.
        Return None if key doesn't exist.
        """
        try:
            return data_structure[key]
        except (IndexError, KeyError, TypeError):
            # These errors happen when:
            # if index doesn't exist (IndexError)
            # if the dictionary key doesn't exist (KeyError)
            # if the key type is invalid (TypeError)
            return None

    # Test with different data structures
    test_list = [10, 20, 30]
    test_dict = {"a": 1, "b": 2}

    print(f"List[1]: {access_data(test_list, 1)}")
    print(f"List[10]: {access_data(test_list, 10)}")
    print(f"Dict['a']: {access_data(test_dict, 'a')}")
    print(f"Dict['z']: {access_data(test_dict, 'z')}")


    # TODO 2: Order exception handlers correctly
    def parse_value(value):
        """
        Try to parse value as int, then float, then return as string.
        """
        try:
            # first converting to int
            return int(value)
        except (ValueError, TypeError):
            # If int fails, try float
            try:
                return float(value)
            except (ValueError, TypeError):
                # If float fails, return as string
                return str(value)

    # Test parsing
    test_values = ["42", "3.14", "hello", None]
    for val in test_values:
        result = parse_value(val)
        print(f"Parsing '{val}': {result} (type: {type(result).__name__})")


# Run the practice
practice_2_exception_hierarchy()


# Practice 3
def practice_3_complete_pattern():
    """
    Practice with try-except-else-finally
    """
    print("\n" + "="*50)
    print("EXERCISE 3: Complete Exception Pattern")
    print("="*50)

    # ----------------------------------------------------------
    # TODO 1: File processor with complete error handling
    # ----------------------------------------------------------

    def process_file(filename):
        """
        Read file, process content, ensure file is closed.
        Return processed content or None.
        """
        file = None
        try:
            file = open(filename, "r")   # OPEN FILE
        except FileNotFoundError:
            return "Error: File not found"
        except PermissionError:
            return "Error: Permission denied"
        else:
            # PROCESS FILE CONTENT (only if opened successfully)
            content = file.read()
            return content.upper()  # example processing
        finally:
            # ALWAYS close file if opened
            if file is not None:
                file.close()

    # Test with different scenarios
    test_files = ["exists.txt", "missing.txt", "/root/file"]
    for filename in test_files:
        result = process_file(filename)
        print(f"Processing '{filename}': {result}")

    # ----------------------------------------------------------
    # TODO 2: Resource manager
    # ----------------------------------------------------------

    class ResourceManager:
        def __init__(self, name):
            self.name = name
            self.resource = None

        def acquire(self):
            """Acquire resource - might fail."""
            import random
            if random.choice([True, False]):  # 50% chance to fail
                raise RuntimeError(f"Failed to acquire {self.name}")
            self.resource = f"{self.name} Connection"
            print(f"[ACQUIRED] {self.resource}")

        def release(self):
            """Release resource - must always happen."""
            if self.resource:
                print(f"[RELEASED] {self.resource}")
            else:
                print(f"[RELEASED] No resource to release")
            self.resource = None

        def use(self):
            """Use resource - only if acquired."""
            if not self.resource:
                raise RuntimeError("Cannot use resource before acquiring it!")
            print(f"[USING] {self.resource}")

    # Test resource management
    rm = ResourceManager("Database")

    # Using full try–except–else–finally pattern
    try:
        rm.acquire()
    except RuntimeError as e:
        print("Acquire Error:", e)
    else:
        try:
            rm.use()
        except RuntimeError as e:
            print("Use Error:", e)
    finally:
        rm.release()


# Run the practice
practice_3_complete_pattern()
