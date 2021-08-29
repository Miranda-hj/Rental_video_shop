
import unittest
from videorentalshop import *

class TestMovie(unittest.TestCase):   
    def test_init(self):
        movie = Movie("Hansel and Gretel",2012)
        self.assertEqual(movie.Movie,'Hansel and Gretel')
        self.assertEqual(movie.year, 2012)
        self.assertEqual(movie.fee,5.0)
        self.assertEqual(movie.movie_status,'Available')
    
    def test_str(self):
        movie = Movie("Hansel and Gretel",2012)
        self.assertEqual(movie.__str__(),"Hansel and Gretel")

    def test_eq(self):
        movie = Movie("Hansel and Gretel",2012)
        movie2 = Movie("Pitch Perfect",2012,)
        movie3 = Movie("Hansel and Gretel",2012)
        self.assertEqual(movie.__eq__(movie2), False)
        self.assertEqual(movie.__eq__(movie3), True)

class TestCustomer(unittest.TestCase):
    def test_init(self):
        customer= Customer("John Doe", "Lincoln")
        self.assertEqual(customer.name,'John Doe')
        self.assertEqual(customer.city,'Lincoln')
        self.assertEqual(customer.payment, 0.0)
        self.assertEqual(customer.cMovie,[])

    def test_customerMovie(self):
        customer = Customer("John Doe", "Lincoln")
        self.assertEqual(customer.customerMovie(), None)



controller = VideoController()
controller.addcustomer ("John Doe", "Lincoln", 0.00)
controller.addmovie ("Pitch Perfect", 2012, "Available") 
controller.find_customer ("John Doe")
controller.find_movie  ("Pitch Perfect")
controller.rental_movie ("Pitch Perfect", "John Doe")
controller.return_movie ("Pitch Perfect")
controller.displayCustomer ("John Doe")
controller.displayMovie ("Pitch Perfect")
controller.trackpayment  ("John Doe")

if __name__ == '__main__':
    unittest.main()