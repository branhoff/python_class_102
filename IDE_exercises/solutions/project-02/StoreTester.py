# Author: Brandon Hoffman
# Date: 1/12/2021
# Description: unittest for Store.py

import unittest
from Store import Product, Customer, Store, InvalidCheckoutError

class StoreTester(unittest.TestCase):
    """
    unit tests for Store.py
    """

    def test_product(self):
        """
        tests thte basic functionality of the Product class
        """
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        self.assertEqual(p1.get_product_id(), "889")
        self.assertEqual(p1.get_title(), "Rodent of unusual size")
        self.assertEqual(p1.get_description(), "when a rodent of the usual size just won't do")
        self.assertEqual(p1.get_price(), 33.45)
        self.assertEqual(p1.get_quantity_available(), 8)

        p1.decrease_quantity()

        self.assertEqual(p1.get_quantity_available(), 7)

    def test_customer(self):
        """
        tests the basic functionality of the Customer class
        """
        c1 = Customer("Yinsheng", "QWF", False)

        self.assertEqual(c1.get_name(), "Yinsheng")
        self.assertEqual(c1.get_customer_id(), "QWF")
        self.assertFalse(c1.is_premium_member())

        c1.add_product_to_cart("101")
        c1.add_product_to_cart("889")

        self.assertDictEqual(c1.get_cart(), {"889": 1, "101": 1})

        c1.add_product_to_cart("101")
        c1.add_product_to_cart("889")

        self.assertDictEqual(c1.get_cart(), {"101": 2, "889": 2})

        c1.empty_cart()

        self.assertEqual(c1.get_cart(), {})

    def test_store_get_product_from_id(self):
        """
        tests the basic functionality of the Store method get_product_from_id()
        """
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("755", "Plunger", "dislodge clogs", 15.00, 3)
        p3 = Product("1000", "key-chain", "hold your keys", 0.99, 35)

        myStore = Store() 
        
        myStore.add_product(p1)
        myStore.add_product(p2)
        myStore.add_product(p3)

        self.assertEqual(myStore.get_product_from_id("889"), p1)
        self.assertEqual(myStore.get_product_from_id("755"), p2)
        self.assertEqual(myStore.get_product_from_id("1000"), p3)
        self.assertEqual(myStore.get_product_from_id("10"), None)


    def test_store_get_member_from_id(self):
        """
        tests the basic functionality of the Store method get_member_from_id()
        """
        c1 = Customer("Yinsheng", "QWF", False)
        c2 = Customer("Alan", "ABC", True)
        c3 = Customer("Kirk", "EEF", True)

        myStore = Store()

        myStore.add_member(c1)
        myStore.add_member(c2)
        myStore.add_member(c3)

        self.assertEqual(myStore.get_member_from_id("QWF"), c1)
        self.assertEqual(myStore.get_member_from_id("ABC"), c2)
        self.assertEqual(myStore.get_member_from_id("EEF"), c3)
        self.assertEqual(myStore.get_member_from_id("DLL"), None)
        
    
    def test_store_product_search(self):
        """
        tests the basic functionality of the Store method product_search()
        """
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("755", "Plunger", "dislodge clogs", 15.00, 3)
        p3 = Product("1000", "key-chain", "hold your keys", 0.99, 35)
        p4 = Product("88", "rat trap", "traps rodents", 3.99, 50)
        p5 = Product("001", "mouse pad", "not a RODENT's house", 9.95, 20)

        myStore = Store() 
        
        myStore.add_product(p1)
        myStore.add_product(p3)
        myStore.add_product(p4)
        myStore.add_product(p2)
        myStore.add_product(p5)

        self.assertEqual(myStore.product_search("RoDeNt"), ["001", "88", "889"])

    def test_store_add_product_to_member_cart(self):
        """
        tests the basic functionality of the Store method add_product_to_member_cart()
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
        
        self.assertEqual(myStore.add_product_to_member_cart("8", "QF"), "product ID not found")
        self.assertEqual(myStore.add_product_to_member_cart("88", "QF"), "member ID not found")
        self.assertEqual(myStore.add_product_to_member_cart("88", "QWF"), "product added to cart")
        self.assertEqual(myStore.add_product_to_member_cart("002", "QWF"), "product out of stock")
        self.assertEqual(myStore.add_product_to_member_cart("755", "QWF"), "product added to cart")
        self.assertEqual(myStore.add_product_to_member_cart("755", "QWF"), "product added to cart")

    def test_assert_raises_InvalidCheckoutError(self):
        """
        tests the basic functionality of the InvalidCheckoutError class and its appropriate use in the checkout_member()
        method
        """
        with self.assertRaises(InvalidCheckoutError):
            c1 = Customer("Yinsheng", "QWF", False)
            myStore = Store() 
            myStore.add_member(c1)
            myStore.check_out_member("NOTAVALIDCUSTID")

        with self.assertRaises(InvalidCheckoutError):
            myStore = Store() 
            myStore.check_out_member("NOTAVALIDCUSTID")

    def test_checkout_sum(self):
        """
        tests basic functionality of the Store method check_out_member()
        """
        p1 = Product("889", "Rodent of unusual size", "when a rodent of the usual size just won't do", 33.45, 8)
        p2 = Product("755", "Plunger", "dislodge clogs", 15.00, 1)
        p3 = Product("1000", "key-chain", "hold your keys", 0.99, 35)
        p4 = Product("88", "rat trap", "traps rodents", 3.99, 50)
        p5 = Product("001", "mouse pad", "not a RODENT's house", 9.95, 20)
        p6 = Product("002", "remote conrol", "you and your signficant other will fight for it", 14.50, 0)

        c1 = Customer("Yinsheng", "QWF", True)
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
        myStore.add_product_to_member_cart("889", "QWF")
        myStore.add_product_to_member_cart("755", "QWF")
        myStore.add_product_to_member_cart("755", "QWF")
        myStore.add_product_to_member_cart("1000", "QWF")
        myStore.add_product_to_member_cart("001", "QWF")
        myStore.add_product_to_member_cart("002", "QWF")
        myStore.add_product_to_member_cart("002", "QWF")

        self.assertAlmostEqual(myStore.check_out_member("QWF"), 96.83)

if __name__ == '__main__':
    unittest.main()
