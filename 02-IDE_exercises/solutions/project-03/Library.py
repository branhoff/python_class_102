 # Author: Brandon Hoffman
 # Date: 1/20/2021
 # Description: Library simulator involving multiple classes


class LibraryItem:
    """
    Parent class for Book, Album, and Movie classes
    """

    def __init__(self, library_item_id, title):
        """
        inits an library_item_id and title
        sets _location to "ON_SHELF"
        All other variables set to None
        """
        self._library_item_id = library_item_id
        self._title = title

        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_library_item_id(self):
        """
        gets library item value
        """
        return self._library_item_id

    def get_title(self):
        """
        gets title value
        """
        return self._title
    
    def get_location(self):
        """
        gets location value
        """
        return self._location

    def get_checked_out_by(self):
        """
        gets checked_out_by value
        """
        return self._checked_out_by

    def get_requested_by(self):
        """
        gets requested_by value
        """
        return self._requested_by

    def get_date_checked_out(self):
        """
        gets date_checked_out value
        """
        return self._date_checked_out

    def set_location(self, location):
        """
        gets location value
        """
        self._location = location

    def set_checked_out_by(self, patron):
        """
        gets checked_out_by value
        """
        self._checked_out_by = patron

    def set_requested_by(self, patron):
        """
        gets requested_by value
        """
        self._requested_by = patron

    def set_date_checked_out(self, date):
        """
        gets date_checked_out value
        """
        self._date_checked_out = date

class Book(LibraryItem):
    """
    class inherits from LibraryItem parent class
    """

    def __init__(self, _library_item_id, _title, author):
        """
        inherits _library_item_id, _title from parent class
        intializes author value
        """
        super().__init__(_library_item_id, _title)
        self._author = author

    def get_author(self):
        """
        gets author value
        """
        return self._author
    
    def get_check_out_length(self):
        """
        returns the integer 21 to represent length of days to be checked out
        """
        return 21



class Album(LibraryItem):
    """
    class inherits from LibraryItem parent class
    """

    def __init__(self, _library_item_id, _title, artist):
        """
        inherits _library_item_id, _title from parent class
        intializes artist value
        """
        super().__init__(_library_item_id, _title)
        self._artist = artist

    def get_artist(self):
        """
        gets artist value
        """
        return self._artist

    def get_check_out_length(self):
        """
        returns the integer 14 to represent length of days to be checked out
        """
        return 14


class Movie(LibraryItem):
    """
    class inherits from LibraryItem parent class
    """

    def __init__(self, _library_item_id, _title, director):
        """
        inherits _library_item_id, _title from parent class
        intializes director value
        """
        super().__init__(_library_item_id, _title)
        self._director = director

    def get_director(self):
        """
        gets director value
        """
        return self._director

    def get_check_out_length(self):
        """
        returns the integer 7 to represent length of days to be checked out
        """
        return 7

class Patron:
    """
    Models person who checks out items from the Library
    """
    
    def __init__(self, patron_id, name):
        """
        inits a patron_id and name from required arguments
        inits empty dictionary for checked_out_items
        inits fine_amount to 0
        """
        self._patron_id = patron_id
        self._name = name

        self._checked_out_items = {}
        self._fine_amount = 0

    def get_patron_id(self):
        """
        gets patron_id
        """
        return self._patron_id

    def get_fine_amount(self):
        """
        gets find_amount
        """
        return self._fine_amount

    def get_checked_out_items(self):
        """
        gets checked_out_items
        """
        return self._checked_out_items

    def add_library_item(self, library_item):
        """
        adds library item to checked_out_items dict
        library_item_id is key and library_item object is value
        """
        id_ = library_item.get_library_item_id
        self._checked_out_items[id_] = library_item
        

    def remove_library_item(self, library_item):
        """
        pops library_item from checked_out_items dict
        """
        id_ = library_item.get_library_item_id
        self._checked_out_items.pop(id_, None)

    def amend_fine(self, journal_entry):
        """
        adds journal_entry to fine field
        """
        self._fine_amount += journal_entry



class Library:
    """
    models library that records LibraryItems in holdings and Patrons in members
    """
    
    def __init__(self):
        """
        inits current_date to 1
        inits holdings to empty dict for storing LibraryItems later
        inits members to empty dict for storing Patrons later
        """
        self._current_date = 1
        self._holdings = {}
        self._members = {}

    def add_library_item(self, library_item):
        """
        adds library_item_id:LibraryItem to holdings
        """
        id_ = library_item.get_library_item_id()
        self._holdings[id_] = library_item 

    def add_patron(self, patron):
        """
        adds patron_id:Patron to members
        """
        id_ = patron.get_patron_id()
        self._members[id_] = patron

    def get_library_item_from_id(self, id_):
        """
        returns LibraryItem value from id_ key
        returns None if KeyError
        """
        try:
            return self._holdings[id_]

        except KeyError:
            return None

    def get_patron_from_id(self, id_):
        """
        returns Patron value from id_ key
        returns None if KeyError
        """
        try:
            return self._members[id_]

        except KeyError:
            return None

    def check_out_library_item(self, patron_id, library_item_id):
        """
        checks out LibraryItem if patron in members, library_item in holdings and not already CHECKED_OUT
        """
        patron = self.get_patron_from_id(patron_id)
        if patron == None:
            return "patron not found"

        library_item = self.get_library_item_from_id(library_item_id)
        if library_item == None:
            return "item not found"

        if library_item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if library_item.get_location() == "ON_HOLD_SHELF":
            return "item on hold by other patron"

        library_item.set_checked_out_by(patron)
        patron.add_library_item(library_item)
        library_item.set_location("CHECKED_OUT")
        library_item.set_date_checked_out(self._current_date)
        if library_item.get_requested_by() == patron_id:
            library_item.set_requested_by(None)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """
        returns LibraryItem to Library by updating location and removes item from Patron's checked out dict
        """
        library_item = self.get_library_item_from_id(library_item_id)
        if library_item_id == None:
            return "item not found"

        if library_item.get_location() != "CHECKED_OUT":
            return "item already in library"

        patron = library_item.get_checked_out_by()
        patron.remove_library_item(library_item)

        if library_item.get_requested_by != None:
            library_item.set_location("ON_HOLD_SHELF")
        
        else:
            library_item.set_location("ON_SHELF")

        return "request successful"

    def request_library_item(self, patron_id, library_item_id):
        """
        Puts LibraryItem on hold if not already on hold for Patron
        """
        patron = self.get_patron_from_id(patron_id)
        if patron == None:
            return "patron not found"

        library_item = self.get_library_item_from_id(library_item_id)
        if library_item == None:
            return "item not found"

        if library_item.get_requested_by() != None:
            return "item already on hold"

        library_item.set_requested_by(patron)
        if library_item.get_location() == "ON_SHELF":
            library_item.set_location("ON_HOLD_SHELF")

        return "request successful"

    def pay_fine(self, patron_id, amount_paid):
        """
        takes amount given and flips sign and uses patron amend fine method to update fine
        """
        patron = self.get_patron_from_id(patron_id)
        if patron == None:
            return "patron not found"

        patron.amend_fine(-amount_paid)

    def increment_current_date(self):
        """
        increments current_date value by 1 and then amends find by 10 cents for all outstanding items for each relevant Patron
        """
        self._current_date += 1
        
        for patron in self._members.values():
            for lib_item in patron.get_checked_out_items().values():
                check_out_limit = lib_item.get_check_out_length()
                date_checked_out = lib_item.get_date_checked_out()
                check_out_days = self._current_date - date_checked_out 
                if check_out_days > check_out_limit:
                    patron.amend_fine(.10)
        

def main():
    """
    basic test provided by README
    """

    b1 = Book("345", "Phantom Tollbooth", "Juster")
    a1 = Album("456", "...And His Orchestra", "The Fastbacks")
    a2 = Album("457", "...And His Orchestra", "The Fastbacks")
    m1 = Movie("567", "Laputa", "Miyazaki")

    p1 = Patron("abc", "Felicity")
    p2 = Patron("bcd", "Waldo")

    lib = Library()
    lib.add_library_item(b1)
    lib.add_library_item(a1)
    lib.add_library_item(a2)
    lib.add_patron(p1)
    lib.add_patron(p2)
    
    lib.check_out_library_item("bcd", "456")
    lib.check_out_library_item("bcd", "457")

    loc = a1.get_location()
    lib.request_library_item("abc", "456")
    for _i in range(57):
        lib.increment_current_date()   # 57 days pass

    p2_fine = p2.get_fine_amount()
    lib.pay_fine("bcd", p2_fine)
    p2_fine = p2.get_fine_amount()
    print(p2_fine)
    lib.return_library_item("456")

if __name__ == "__main__":
    main()