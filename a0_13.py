"""Из папки Projects на рабочем столе вычитываем задаваемый csv файл"""

import pandas as pd

def get_df_from_csv(ticker):
    try:
        df = pd.read_csv(r'C:\Users\Влад\Desktop\Projects/' + ticker + '.csv')
    except FileNotFoundError:
        print("File doesn't exist")
    else:
        return df

nifty = get_df_from_csv('^NSEI')

print(nifty)

# import pandas as pd
#
# df = pd.DataFrame({"col_1":[-5,-2,1,4,6],"col_2":[2,3,-1,4,7]})
#
# df.style.background_gradient()
# print(df)
#
# df.style.background_gradient(cmap='plazma')
# print(df)

# a = [4, 10, 5, 4, 5, 6]
#
# if (list_sum := sum(a)) > 30:
#     print(f"Сумма больше 30 и равна : {list_sum}")
#
# class Database:
#     def __init__(self, connection_string):
#         connection_string.self = connection_string
#
#     def connect(self):
#         # Connect to the database using the connection string
#         pass
#
# class UserService:
#     def __init__(self, db: Database):
#         self.db = db
#
#     def get_user(self, user_id):
#         # Query the database for the user using the db instance
#         pass
#
# # In the client code , we can create an instance of UserService and inject the dependencies using the constructor
# db = Database("my-connection-string")
# service = UserService(db)


class Animal:
    def make_noise(self):
        print("Making noise...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

    def make_noise(self):
        super().make_noise() # Access the make_noise() method
        # from the parent class
        self.bark() # Call the bark() method from thr subclass

dog = Dog()
dog.make_noise()
# Making noise...
# Barking...
# ______________________________________________________________________
