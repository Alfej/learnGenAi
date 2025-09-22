# Open close principle:
    # A class should be open for extension but closed for modification.

# class product:

#     def __init__(self,Name,Value):
#         self.Name = Name
#         self.Value = Value

# #  Below we have devided each of the responsibility in each different class
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

# class ShopingClassPrinter():
#     def __init__(self,obj:ShoppingCart):
#         self.cart = obj
    
#     def printInvoice(self):
#         for product in self.cart.products:
#             print(f"{product.Name } -> {product.Value}")

# class ShopingCartDB():
#     def __init__(self,obj:ShoppingCart):
#         self.cart = obj
#     def AddToDB(self):
#         print("Adding data to DB")
    
# if __name__=="__main__":
#     p1 = product("Laptop",50000)
#     p2 = product("Mouse",100)

#     cart = ShoppingCart()
#     cart.addProduct(p1)
#     cart.addProduct(p2)

#     cart.calculateTotal()
    
#     printer = ShopingClassPrinter(cart)
#     printer.printInvoice()

#     dbStorage = ShopingCartDB(cart)
#     dbStorage.AddToDB()

# Problem:
    #  If we want to add a new feature like adding data to file and mongoDB
    #  we will have to modify the ShoppingCartDB class which is against the Open close principle.

from abc import ABC,abstractmethod

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
class Storage(ABC):
    @abstractmethod
    def AddToDB(self):
        pass

class ShopingSQl(Storage):
    def __init__(self,obj:ShoppingCart):
        self.cart = obj
    def AddToDB(self):
        print("Adding data to DB")

class shoppingFiles(Storage):
    def  __init__(self,obj:ShoppingCart):
        self.cart = obj
    
    def AddToDB(self):
        print("Adding data to File")

class shoppingMongoDB(Storage):
    def  __init__(self,obj:ShoppingCart):
        self.cart = obj
    
    def AddToDB(self):
        print("Adding data to MongoDB")
    
if __name__=="__main__":
    p1 = product("Laptop",50000)
    p2 = product("Mouse",100)

    cart = ShoppingCart()
    cart.addProduct(p1)
    cart.addProduct(p2)

    cart.calculateTotal()
    
    printer = ShopingClassPrinter(cart)
    printer.printInvoice()

    dbStorage = ShopingSQl(cart)
    dbStorage.AddToDB()

    dbStorage = shoppingFiles(cart)
    dbStorage.AddToDB()
    
    dbStorage = shoppingMongoDB(cart)
    dbStorage.AddToDB()
