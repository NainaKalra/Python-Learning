"""
My first Python program on macOS
"""
def greet_user():
    name = input("What's your name? ")
    print(f"Hello, {name}! Welcome to Python on macOS!")

def system_info():
    
    import sys
    import platform
    print(f"Python version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.machine()}")
if __name__ == "__main__":
    greet_user()
    print("\nSystem Information:")
system_info()
