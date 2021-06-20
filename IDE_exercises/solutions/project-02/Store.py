 # Author: Brandon Hoffman
 # Date: 1/12/2021
 # Description: Class based archicture to represent the backend of an online store simulator. 
 #              It has the following classes: Product, Customer and Store, InvalidCheckoutError. 

class  InvalidCheckoutError(Exception):
    """
    Error to be used for when Customer ID not found in listed members
    """
    pass

class Product:
    """
    models products that will be sold in a store
    """

    def __init__(self, id_, title, description, price, quantity):
        """
        intializes id, title, description, price, and quantity for products
        """
        self._id = id_
        self._title = title
        self._description = description
        self._price = price
        self._quantity = quantity

    def get_product_id(self):
        """
        gets ID value
        """
        return self._id

    def get_title(self):
        """
        gets title value
        """
        return self._title

    def get_description(self):
        """
        gets description value
        """
        return self._description

    def get_price(self):
        """
        gets price value
        """
        return self._price

    def get_quantity_available(self):
        """
        gets quantity value
        """
        return self._quantity

    def decrease_quantity(self):
        """
        decreases quantity value by 1
        """
        if self._quantity > 0:
            self._quantity -= 1

class Customer:
    """
    models Customers that will shop in the Store
    """

    def __init__(self, name, id_, premium_member):
        """
        intializes name, id, and premium_member, and cart values
        """
        self._name = name
        self._id = id_
        self._premium_member = premium_member
    
        self._cart = {}

    def get_name(self):
        """
        gets name value
        """
        return self._name

    def get_customer_id(self):
        """
        gets customer id value
        """
        return self._id

    def get_cart(self):
        """
        gets cart value
        """
        return self._cart

    def is_premium_member(self):
        """
        returns boolean premium member value
        """
        return self._premium_member

    def add_product_to_cart(self, id_):
        """
        tries to take product id as key in cart dictionary and increment value
        except for a Key error in which case it intializes id as key and value as 1

        key: product id
        value: count of product id's
        """
        try:
            self._cart[id_] += 1
        
        except KeyError:
            self._cart[id_] = 1

    def empty_cart(self):
        """
        binds cart to an empty dictionary
        """
        self._cart = {}

class Store:
    """
    models Store with products and customers stored as members
    """
    
    def __init__(self):
        """
        intializes private variables product_inventory and members
        as empty dictionaries
        """
        self._product_inventory = {}
        self._members = {}

    def add_product(self, product):
        """
        takes product object and stores it in product inventory with product_id value as key
        and product object as value
        """
        self._product_inventory[product.get_product_id()] = product

    def add_member(self, customer):
        """
        takes customer object and stores it in members dictionary with
        customer id as key and customer object as value
        """
        self._members[customer.get_customer_id()] = customer

    def get_product_from_id(self, product_id):
        """
        takes a product id and tries to return the value from the product_inventory dictionary
        except for KeyError returns None value
        """
        try:
            return self._product_inventory[product_id]

        except KeyError:
            return None

    def get_member_from_id(self, cust_id):
        """
        takes a customer id and tries to return the value from the members dictionary
        except for KeyError returns None value
        """
        try:
            return self._members[cust_id]

        except KeyError:
            return None

    def product_search(self, search_string_input):
        """
        takes a string argument that compares against
        Product title and descripton values
        returns sorted product ids
        """
        search_string = search_string_input.lower()
        matches = []
        for product in self._product_inventory.values():
            if search_string in product.get_title().lower():
                matches.append(product.get_product_id())

            elif search_string in product.get_description().lower():
                matches.append(product.get_product_id())
        
        matches.sort()

        return matches


    def add_product_to_member_cart(self, product_id, customer_id):
        """
        takes a product id and customer id arguments
        if product id and member id are found in relevant dicts and quanity of product is > 0
        adds product to the relevant member's cart
        returns outcome whether successful or specific reason wasn't successful
        """
        product = self.get_product_from_id(product_id)
        if product == None:
            return "product ID not found"

        customer = self.get_member_from_id(customer_id)
        if customer == None:
            return "member ID not found"

        if product.get_quantity_available() > 0:
            customer.add_product_to_cart(product.get_product_id())
            return "product added to cart"

        else:
            return "product out of stock"


    def check_out_member(self, customer_id):
        """
        takes customer id
        iterates through member cart returns sum of prouct price
        """
        if customer_id not in self._members:
            raise InvalidCheckoutError

        customer = self._members[customer_id]
        charge = 0

        for product_id, no_items in customer.get_cart().items():
            try:
                product = self._product_inventory[product_id]
                
                for _i in range(no_items):
                    if product.get_quantity_available() > 0:
                        charge += product.get_price()
                        product.decrease_quantity()
            
            except KeyError:
                pass
                
        if not customer.is_premium_member():
            charge *= 1.07

        customer.empty_cart()

        return charge

def main():
    """
    runs simulated program using the Product, Customer, and Store Class
    has no return value
    """
    p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
    p2 = Product("755", "Plunger", "dislodge clogs", 15.00, 1)
    p3 = Product("1000", "key-chain", "hold your keys", 0.99, 35)
    p4 = Product("88", "rat trap", "traps rodents", 3.99, 50)
    p5 = Product("001", "mouse pad", "not a RODENT's house", 9.95, 20)
    p6 = Product("002", "remote conrol", "you and your signficant other will fight for it", 14.50, 0)

    c1 = Customer("Yinsheng", "QWF", False)
    myStore = Store() 

    myStore.add_member(c1)
        
    myStore.add_product(p1)
    myStore.add_product(p3)
    myStore.add_product(p4)
    myStore.add_product(p2)
    myStore.add_product(p5)
    myStore.add_product(p6)
        

    myStore.add_product_to_member_cart("88", "QWF")
    myStore.add_product_to_member_cart("002", "QWF")
    myStore.add_product_to_member_cart("889", "QWF")
    myStore.add_product_to_member_cart("755", "QWF")
    myStore.add_product_to_member_cart("755", "QWF")
    myStore.add_product_to_member_cart("1000", "QWF")
    myStore.add_product_to_member_cart("001", "QWF")
    myStore.add_product_to_member_cart("002", "QWF")

    
    try:
        myStore.check_out_member("QWF")

    except InvalidCheckoutError:
        print("Invalid Customer ID: Customer ID not found in listed members")

if __name__ == '__main__':
    main()





