# ===================================
# Global Variable
# ===================================

name = "Shruti"

def show_name():
    print(name)

show_name()

# ====================================
# Local Variable
# ====================================

def greet():
    message = "Hello"
    print(message)

greet()

# Accessing local variable outside function
# this would cause error

# =============================================
# Local and Global variable with same NAME
# =============================================

value = 100

def test_scope():
    value = 50
    print("Local Value: ", value)

test_scope()
print("Global Value: ", value)