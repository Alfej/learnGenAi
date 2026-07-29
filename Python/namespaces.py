#  Namespace is a space that holds a collection of identifiers (names) and their corresponding objects. In Python, namespaces are implemented as dictionaries that map names to objects. There are several types of namespaces in Python, including:
#  1. Built-in Namespace: Contains built-in functions and exceptions.
#  2. Global Namespace: Contains variables defined at the top level of a module.
#  3. Local Namespace: Contains variables defined within a function.
#  4. Enclosing Namespace: Contains variables defined in the enclosing function (if any).

#  Scope refers to the region of a program where a namespace is directly accessible. In Python, there are four types of scopes:

# LEGB Rule: values within a namespace can be accessed using the LEGB rule, which stands for Local, Enclosing, Global, and Built-in. The LEGB rule defines the order in which Python searches for a name in different namespaces:
#  1. Local Scope: The innermost scope, which is searched first.
#  2. Enclosing Scope: The scope of any enclosing functions, which is searched next.
#  3. Global Scope: The scope of the module, which is searched after the enclosing scope.
#  4. Built-in Scope: The outermost scope, which is searched last.

a = 10 # Global variable

def outer_function():
    b = 20 # Enclosing variable

    def inner_function():
        c = 30 # Local variable
        print("Local variable:", c)
        nonlocal b # To modify the enclosing variable, we need to use the nonlocal keyword
        b += 10 # Modifying the enclosing variable
        print("Enclosing variable:", b) # Accessing enclosing variable we can only read it, we cannot modify it unless we use the nonlocal keyword

        global a # To modify the global variable, we need to use the global keyword
        a += 10 # Modifying the global variable
        print("Global variable:", a) # Accessing global variable we can only read it, we cannot modify it unless we use the global keyword

    inner_function()
    print("b:", b) # Accessing enclosing variable we can only read it, we cannot modify it unless we use the nonlocal keyword
    
outer_function()
print("a:", a) # Accessing global variable we can only read it, we cannot modify it unless we use the global keyword



# built-in namespace
print("Built-in variables:", dir(__builtins__))

# if you create a variable with the same name as a built-in function, it will shadow the built-in function in the local scope. For example:
l=[1,2,3]
 
def max():
    print("This is my function")

max(l) # This will call the local max function due to LEGB rule, which will result in a TypeError since the local max function does not accept any arguments. To avoid this, you can use the built-in max function by using the built-in namespace like this:
print("Max value:", __builtins__.max(l)) # This will call the built-in