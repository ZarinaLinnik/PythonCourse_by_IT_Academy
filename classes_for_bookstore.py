import re
import decimal

decimal.getcontext().prec = 2


class Book:

    def __init__(self, title, author, isbn, price):
        self.__title = title
        self.__author = author
        self.__set_isbn(isbn)
        self.price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def __set_isbn(self, isbn):
        while True:
            if len(str(isbn)) != 13 or not isinstance(isbn, int):
                print('it must have 13 digits! \ntry again!')
                try:
                    isbn = int(input())
                except ValueError:
                    print('it must be an integer and', end=' ')
            else:
                self.__isbn = isbn
                break

    title = property(get_title)
    author = property(get_author)
    isbn = property(get_isbn)


class EBook(Book):

    def __init__(self, title, author, isbn, price, format_, file_size, download_link):
        super().__init__(title, author, isbn, price)
        self.format_and_file_size = (format_, file_size)
        self.set_download_link(download_link)

    def get_download_link(self):
        return self.__download_link

    def set_download_link(self, download_link):
        while True:
            if re.search("^https://", download_link):
                self.__download_link = download_link
                break
            else:
                download_link = input("Give another link that starts with 'https://'. \n")

    download_link = property(get_download_link, set_download_link)


class PhysicalBook(Book):

    def __init__(self, title, author, isbn, price, weight, in_stock=True):
        super().__init__(title, author, isbn, price)
        self.__weight = weight
        self.__in_stock = in_stock

    def get_status(self):
        return self.__in_stock

    def update_status(self, in_stock):
        self.__in_stock = in_stock

    def get_weight(self):
        return self.__weight

    in_stock = property(get_status, update_status)
    weight = property(get_weight)


class Customer:

    class __ShoppingCart:

        def __init__(self):
            self.cart = {}

        def add_book(self, *books):
            for book in books:
                if isinstance(book, EBook) and book.title in self.cart:
                    continue
                if isinstance(book, PhysicalBook):
                    if book.in_stock and book.title in self.cart:
                        self.cart[book.title][1] += 1
                    elif book.in_stock:
                        self.cart[book.title] = [book.price, 1]
                elif isinstance(book, Book) and book.title in self.cart:
                    self.cart[book.title][1] += 1
                else:
                    self.cart[book.title] = [book.price, 1]

        def remove_book(self, book):
            self.cart.pop(book.title)

        def total_price(self):
            full_price = 0
            for book in self.cart:
                full_price = self.cart[book][0] * self.cart[book][1]
            return full_price

    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.cart = Customer.__ShoppingCart()

    def pay_for_it(self):
        Order.give_info(self.name, self.cart.total_price(), self.cart.cart)


class PremiumCustomer(Customer):
    def __init__(self, name, email, address, membership_status, discount_rate):
        super().__init__(name, email, address)
        self.membership_status = membership_status
        self.discount_rate = decimal.Decimal(f'{discount_rate}')

    def discount_to_your_cart(self):
        if self.cart.cart:
            price_without_discount = decimal.Decimal(f'{self.cart.total_price()}')
            final_price = float(price_without_discount - price_without_discount * self.discount_rate)
            return final_price
        else:
            return 'Now you have no books that you would buy. Find somthing you would like and put it in your cart'


class Order:

    __order_of_customers = []
    __total_order_price = 0
    __order_of_books = []

    @staticmethod
    def give_info(name, price, cart_with_books):
        Order.__order_of_customers.append(name)
        Order.__total_order_price += price
        ([Order.__order_of_books.extend([book for _ in range(cart_with_books[book][1])]) for book in cart_with_books])

    @staticmethod
    def get_customer_order():
        return Order.__order_of_customers

    @staticmethod
    def get_order_total_price():
        return Order.__total_order_price

    @staticmethod
    def get_books_order():
        return Order.__order_of_books


e_paws = EBook('My Life In His Paws', 'Wendy Hillings', 1234567891634, 15, \
               'PDF', 10, "https://www.goodreads.com/book/show/29244831-my-life-in-his-paws")
#
ph_paws1 = PhysicalBook('My Life In His Paws', 'Wendy Hillings', 1234567891234, 25, \
                       150)
ph_paws1.in_stock = False
#
ph_paws2 = PhysicalBook('My Life In His Paws', 'Wendy Hillings', 1234567893454, 45, \
                       200)
ennead = EBook('Ennead', 'Mojito', 1234567891267, 30, \
               'ePub', 30, "https://www.tappytoon.com/en/book/ennead")
my_book = Book('Book', 'Author', 1234567890213, 100)
very_expensive_book = Book('ExpensiveBook', 'RealAuthor', 1234444490213, 437)

print('e_paws:', e_paws.title, e_paws.author, e_paws.isbn, e_paws.price, \
      e_paws.format_and_file_size, e_paws.download_link, sep='; ')
print('ph_paws1:', ph_paws1.title, ph_paws1.author, ph_paws1.isbn, ph_paws1.price, \
      ph_paws1.weight, ph_paws1.in_stock, sep='; ')
print('ph_paws2:', ph_paws2.title, ph_paws2.author, ph_paws2.isbn, ph_paws2.price, \
      ph_paws2.weight, ph_paws2.in_stock, sep='; ')
print('ennead:', ennead.title, ennead.author, ennead.isbn, ennead.price, \
      ennead.format_and_file_size, ennead.download_link, sep='; ')

cust1 = Customer('Zarin', '123@gmail.com', 'Tower Square, 11')
cust2 = Customer('Alin', 'al23@gmail.com', 'Big Ban, 11')

cust1.cart.add_book(e_paws, e_paws, ennead)  # {'My Life In His Paws': [15, 1], 'Ennead': [30, 1]}
cust2.cart.add_book(ph_paws1, ph_paws2, ph_paws2, my_book, my_book)  # {'My Life In His Paws': [45, 2], 'Book': [100, 2]}
cust1.cart.remove_book(ennead)
cust2.cart.remove_book(my_book)
print(cust1.cart.cart, cust1.cart.total_price())  # {'My Life In His Paws': [15, 1]} 15
print(cust2.cart.cart, cust2.cart.total_price())  # {'My Life In His Paws': [45, 2]} 90

premium_customer1 = PremiumCustomer('Alana', 'evil@gmail.com', 'Hell', 'BigDaddy', 0.9)
premium_customer1.cart.add_book(e_paws, ennead, ph_paws2)
print('Your price with the discount is', premium_customer1.discount_to_your_cart(), \
      '. If it was without your great discount it would be', premium_customer1.cart.total_price())

premium_customer2 = PremiumCustomer('Elan', 'kind@gmail.com', 'Paradise', 'MassiveMommy', 0.35)
premium_customer2.cart.add_book(very_expensive_book)
premium_customer2.discount_to_your_cart()
print('Your price with the discount is', premium_customer2.discount_to_your_cart(), \
      '. If it was without your great discount it would be', premium_customer2.cart.total_price())


cust2.pay_for_it()
cust1.pay_for_it()
premium_customer2.pay_for_it()
premium_customer1.pay_for_it()

print(Order.get_customer_order(), cust2.name, cust1.name, premium_customer2.name, premium_customer1.name)
print(Order.get_books_order(), cust2.cart.cart, cust1.cart.cart, premium_customer2.cart.cart, premium_customer1.cart.cart)
print(Order.get_order_total_price(), cust2.cart.total_price(), cust1.cart.total_price(), \
      premium_customer2.cart.total_price(), premium_customer1.cart.total_price())
