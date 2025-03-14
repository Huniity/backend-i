
class User:
    def __init__(self, username: str, password: str, email: str):
        self.username = username
        self.password = password
        self.email = email

    def hidden_user_password(self):
        return "*" * len(self.password)


class RegisterUser:
    def __init__(self):
        self.user_database = {}

    def create_user(self, user):
        new_user = {"Password": user.password,
                    "Email": user.email}

        if user.username in self.user_database:
            print(f"{user.username} - already exists.")
        else:
            print(
                f"\n\n{user.username} | Created with success | Email: {user.email}. | Password: {user.hidden_user_password()} ")
            self.user_database[user.username] = new_user

    def remove_user(self, user):
        if user.username not in self.user_database:
            pass
        else:
            self.user_database.pop(user.username)
            print(f"{user.username} | Deleted with success.")

    def change_user_info(self, user, new_password, new_email):
        if user.username not in self.user_database:
            pass
        else:
            user.email = new_email
            user.password = new_password
            self.user_database[user.username]["Password"] = new_password
            self.user_database[user.username]["Email"] = new_email
            print(
                f"{user.username} | Password changed with success ({user.hidden_user_password()}).")
            print(f"{user.username} | Email changed with success ({new_email}).")


class Product:
    def __init__(self, name: str, category: str, price: float):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"Category: {self.category} | Product: {self.name} (${self.price:.2f})"


class OnlineStore:
    def __init__(self):
        self.stock = {}

    def create_product(self, product, stock=0):
        new_prod = {"Category": product.category,
                    "Price": product.price,
                    "Stock": stock,
                    }

        if product.name in self.stock:
            print(f"{product.name} already exists.")
            self.change_product_stock(product, stock)
            pass
        else:
            self.stock[product.name] = new_prod
            print(product, f"| In stock: {stock}")

    def remove_product(self, product):
        if product.name not in self.stock:
            pass
        else:
            self.stock.pop(product.name)

    def change_product_stock(self, product, update_stock):
        if update_stock < 0:
            print("Your stock can't be negative.")
        else:
            self.stock[product.name]["Stock"] = update_stock
            print(f"{product.name}: New stock is: {update_stock}")

    def store_inventory(self):
        print("\n\n**************| STOCK INVENTORY |**************\n")
        for product, detail in self.stock.items():
            print(f"{product} - {detail["Stock"]} in stock.")


class DiscountedProduct(Product):
    def __init__(self, name: str, category: str, price: float, discount: float):
        super().__init__(name, category, price)
        self.discount = discount

    def discounted_price(self):
        return self.price * (1 - self.discount / 100)

    def __str__(self):
        return (f"Category: {self.category} | Product: {self.name} Was €{self.price:.2f} | Now: €{self.discounted_price():.2f} ({self.discount}% OFF)")


fnac = OnlineStore()
fnac.create_product(Product("MacBook Pro 16", "Tech", 4999.99), 4)
fnac.create_product(Product("Iphone 16 Pro Max", "Tech", 1999.99), 9)
fnac.create_product(DiscountedProduct(
    "iWatch Ultra 2", "Tech", 4999.99, 15), 22)
fnac.create_product(DiscountedProduct(
    "Airpods Gen3", "Tech", 1999.99, 25), 113)
fnac.create_product(Product("Playstation 5", "Gaming", 4999.99), 0)
fnac.change_product_stock(Product("MacBook Pro 16", "Tech", 4999.99), 9)
fnac.remove_product(Product("Laptop", "Tech", 4999.99))
fnac.store_inventory()


admin = RegisterUser()
admin_1 = (User("Huniity", "aVB7!sdE7#aF6*fa", "huniity_1234@google.com"))
admin.create_user(admin_1)
admin.change_user_info(admin_1, "abc123*", "huniity_93@yahoo.com.uk")
admin.remove_user(admin_1)
