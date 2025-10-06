# Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Additionally, abstractions should not depend on details. Details should depend on abstractions. 

# example without DIP
class SQLDatabase:  # Low-level module
    def connect(self):
        return "Connected to SQL Database"

class MongoDB:     # Low-level module
    def connect(self):
        return "Connected to MongoDB"
    
class DataFetcher:   # High-level module
    def __init__(self):
        self.sql_db = SQLDatabase()  # Direct dependency on low-level module
        self.mongo_db = MongoDB()    # Direct dependency on low-level module
    
    def fetch_data_sql(self):
        return self.sql_db.connect()

    def fetch_data_mongo(self):
        return self.mongo_db.connect()


# Problem: if we introduce a new database, we need to modify the DataFetcher class.
# Solution with DIP
from abc import ABC, abstractmethod
class Database(ABC):  # Abstraction
    @abstractmethod
    def connect(self):
        pass

class SQLDatabase(Database):  # Low-level module
    def connect(self):
        return "Connected to SQL Database"
    
class MongoDB(Database):     # Low-level module
    def connect(self):
        return "Connected to MongoDB"

class DataFetcher:   # High-level module
    def __init__(self, database: Database):  # Dependency on abstraction
        self.database = database
    
    def fetch_data(self):
        return self.database.connect()

# Now, if we want to use a different database, we can simply pass it to the DataFetcher without modifying its code.
sql_fetcher = DataFetcher(SQLDatabase())
print(sql_fetcher.fetch_data())  # Output: Connected to SQL Database
mongo_fetcher = DataFetcher(MongoDB())
print(mongo_fetcher.fetch_data())  # Output: Connected to MongoDB