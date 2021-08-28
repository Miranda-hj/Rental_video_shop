# Miranda 1141206 

class Movie:
    #constructor
    def __init__(self, movie, year):
        self.__movie = movie
        self.__mFee = 5.0
        # $5 for each movie
        self.__year = year
        # two different status: 'hold', 'owner's mobile'
        self.__status = "Hold" 

    @property
    def movie_status(self):
        return self.__status

    @movie_status.setter
    def movie_status(self,value):
        self.__status = value
    
    @property
    def fee(self):
        return self.__mFee
    
    @fee.setter
    def fee(self,value):
        self.__mFee = value

    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self,value):
        self.__year = value

    @property
    def Movie(self):
        return self.__movie

    # display movie's detail 
    def movieDetail(self):
        print(self.__movie + " " + self.__year + " " + self.__mFee + " " + self.__status)
        for movie in self.Movie:
            print(movie)

    def __str__(self):
        return self.__movie

    # def __eq__(self, other):
    #     return self.Movie == other.Movie

class Customer:
    #constructor
    def __init__(self,name,city):
        self.__cName = name
        self.__cCity = city
        self.__balance = 0.0
        self.__cMovie = []
    
    # diplay customer rental balance
    def rental_balance(self):
        return self.__balance

    # add movie to the rented list
    def add_movie(self,movie):
        self.__cMovie.append(movie)

    # remove movie to the rented list
    def remove_movie(self,movie):
        self.__cMovie.remove(movie)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        self.__balance = value
    
    @property
    def name(self):
        return self.__cName
    
    @name.setter
    def name(self,value):
        self.__cName = value
        
    @property
    def city(self):
        return self.__cCity

    @city.setter
    def city(self,value):
        self.__cCity = value
    

    @property
    def cMovie(self):
        return self.__cMovie

    # display the customer's detail
    def customerMovie(self):
        for movie in self.cMovie:
            print(movie)

    def __str__(self):
        return self.__cName + " " + self.city + " " + str(self.balance)
        
class VideoController:
    #constructor
    def __init__(self):
        self.customerlist = []
        self.movielist =[]

        #add a new customer
    def addcustomer(self,name,city):
        aCustomer=Customer(name,city)
        self.customerlist.append(aCustomer)

        #add a new movie
    def addmovie(self,movie,year):
        aMovie=Movie(movie,year)
        self.movielist.append(aMovie)
    
        # search for a customer
    def find_customer(self,name):
        for customer in self.customerlist:
            if customer.name == name:
                return customer
        return None

        # search for a movie
    def find_movie(self,movie):
        for fmovie in self.movielist:
            if fmovie.Movie == movie:
                return fmovie
        return None

        # return movie
    def return_movie(self,movie):
        fmovie = self.find_movie(movie)
        owner = fmovie.movie_status
        if owner == "Hold":
            print("DO not need to return")
            return False
        else:
            preOwner = self.find_customer(owner)
            preOwner.remove_movie(fmovie)
            fmovie.movie_status = "Hold"

        # rent movie 
    def rental_movie(self,movie,name):
        movie = self.find_movie(movie)
        customer = self.find_customer(name)
        mFee = movie.fee
        preBalance = customer.balance
        balance = preBalance - mFee
        print(balance)
        if  movie.movie_status == 'Hold':
            movie.movie_status = customer.name
            customer.add_movie(movie)
            print(movie.movie_status)
            customer.balance = balance
        else:
            print("Movie has been rented!")
            return False

        #display movie details
    def displayMovie(self,movie):
        displayMovie = self.find_movie(movie)
        status = displayMovie.movie_status
        fee = displayMovie.fee
        print("Name:", displayMovie)
        print("Status:", status)
        print("Fee:", fee)

        #display customer details
    def displayCustomer(self,name):
        displayCustomer = self.find_customer(name)
        print("Name:", displayCustomer.name)
        rentedMovieList = displayCustomer.cMovie
        print("Rented Movie:")
        for rentedMovie in rentedMovieList:
            print(rentedMovie) 
        balance = displayCustomer.balance
        print("Balance:", balance)
        
        
        # track customer's balance
    def trackBalance(self,name):
        cName = self.find_customer(name)
        balance = cName.fee
        print (cName + ':' + balance)
        
            

Hansel = Movie("Hansel and Gretel","2012")
Hansel.__status = "Jamie Rogers"
print(Hansel)
print(Hansel.fee)
print(Hansel.__status)
print(Hansel.movie_status)
C1 = Customer("Jaime Rogers","Lincoln")
print(C1)

print(C1.balance)
C1.balance = "1.0"
print(C1.balance)
