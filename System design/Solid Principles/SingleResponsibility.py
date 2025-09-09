# Single responsibility principle
# Class should have only one reason to change 
# Class should do only one task
# ex. TV remote it handles only TV

# from below exaples you will feel like Single responsibility means single methos per class but thats not true, You can add number of methods but each method in a class be having one responsibility only means they should work on a similar kind of a class, system 

# example : Violating the SRP

# class product:

#     def __init__(self,Name,Value):
#         self.Name = Name
#         self.Value = Value

# #  this class is violating the Single responsibility principle as it have 3 responsibility of calculating total printing the Invoice and saving data to DB
# class ShoppingCart:
#     def __init__(self):
#         self.products = []

#     def addProduct(self,product):
#         self.products.append(product)

#     def calculateTotal(self):
#         total=0
#         for product in self.products:
#             total+=product.Value
        
#         print("Total: ",total)

#     def printInvoice(self):
#         for product in self.products:
#             print(f"{product.Name } -> {product.Value}")

#     def AddToDB(self):
#         print("Adding data to DB")
    
# if __name__=="__main__":
#     p1 = product("Laptop",50000)
#     p2 = product("Mouse",100)

#     cart = ShoppingCart()
#     cart.addProduct(p1)
#     cart.addProduct(p2)

#     cart.calculateTotal()
#     cart.printInvoice()
#     cart.AddToDB()


# Exaple where we are following the Single Responsibility principle.

class product:

    def __init__(self,Name,Value):
        self.Name = Name
        self.Value = Value

#  Below we have devided each of the responsibility in each different class
class ShoppingCart:
    def __init__(self):
        self.products = []

    def addProduct(self,product):
        self.products.append(product)

    def calculateTotal(self):
        total=0
        for product in self.products:
            total+=product.Value
        
        print("Total: ",total)

class ShopingClassPrinter():
    def __init__(self,obj:ShoppingCart):
        self.cart = obj
    
    def printInvoice(self):
        for product in self.cart.products:
            print(f"{product.Name } -> {product.Value}")

class ShopingCartDB():
    def __init__(self,obj:ShoppingCart):
        self.cart = obj
    def AddToDB(self):
        print("Adding data to DB")
    
if __name__=="__main__":
    p1 = product("Laptop",50000)
    p2 = product("Mouse",100)

    cart = ShoppingCart()
    cart.addProduct(p1)
    cart.addProduct(p2)

    cart.calculateTotal()
    
    printer = ShopingClassPrinter(cart)
    printer.printInvoice()

    dbStorage = ShopingCartDB(cart)
    dbStorage.AddToDB()
