import tkinter as tk
from tkinter import Frame, ttk
from tkinter.messagebox import showinfo
from tkinter.constants import END, LEFT, TOP
from videorentalshop import VideoController

company = VideoController()
shop = tk.Tk()
shop.title("Lincoln Video Rental Shop")
shop.geometry("500x700")

cName = ["Jaime Rogers","John Doe", "Angela Peters",
"Richard Reed", "Mark Lee","Stephen Freeman"]
cCity = ["Christchurch","Lincoln","Christchurch","Christchurch","Lincoln"]

movies = ["Hansel and Gretel", "Pitch Perfect", 
"The Shawshank Redemption", "The Godfather", 
"Pulp Fiction","The Dark Knight", 
"Forrest Gump", "The Avengers"]
mYear = ["2012","2012","1994","1972","1994","2008","1994","2012"]

# add customer and movie to videocontroller's list
for acustomer in cName:
    for city in cCity:
        company.addcustomer(acustomer,city)
for amovie in movies:
    for year in mYear:
        company.addmovie(amovie,year)

# require to select customer name and movie name to rent
def button_rent():
    # selected customer 
    selCustomerIndex = cList.curselection()
    selectedCustomer = cList.get(selCustomerIndex)
    # selected movie
    selMovieIndex = mList.curselection()
    selectedMovie = mList.get(selMovieIndex)
    # if movie has been rented, return false
    if company.rental_movie(str(selectedMovie),str(selectedCustomer)) == False:
        showinfo(title="Error", message="Movie has been rented!")
    else:
        # show customer name and rented movie
        showinfo(title="Success", message= selectedCustomer + " Rents: " + selectedMovie )


# only require to select the movie name to return 
def button_return():
    # selected movie
    selMovieIndex = mList.curselection()
    selectedMovie = mList.get(selMovieIndex)
    if company.return_movie(str(selectedMovie)) == False:
        showinfo(title="Error", message="Error"  )
    else:
        # show movie name is returned
        showinfo(title="Success", message= selectedMovie + " is Returned!")


# display customer's detail
def customer_detail():
    selCustomerIndex = cList.curselection()
    selectedCustomer = cList.get(selCustomerIndex)
    customer = company.find_customer(selectedCustomer)
    rentedMovieList = customer.cMovie
    balance = customer.balance
    city = customer.city
    # if no rented movie, return Rented Movie is None
    if rentedMovieList == []:
        msg = "--------------------------\n" + str(customer.name) + "\nCity:" + str(city) + "\nBalance:" + str(balance) + "\nRented Movie: None \n"
        cDText.insert(tk.END, msg)
    else:
        msg = "--------------------------\n" + str(customer.name) + "\nCity:" + str(city) + "\nBalance:" + str(balance) + "\nRented Movie:"  + "\n" 
        cDText.insert(tk.END, msg)
        # print rented movie list
        for rentedMovie in rentedMovieList:
            print(rentedMovie)
            cDText.insert(tk.END,rentedMovie)
            cDText.insert(tk.END,"\n")

# display movie's detail
def movie_detail():
    selMovieIndex = mList.curselection()
    selectedMovie = mList.get(selMovieIndex)
    movie = company.find_movie(selectedMovie)
    status = movie.movie_status
    fee = movie.fee
    year = movie.year
    msg = "--------------------------\n" + str(movie.Movie) + "\nYear:" + str(year) + "\nStatus:" + str(status) + "\nFee:" + str(fee) + "\n"
    mDText.insert(tk.END, msg)

form = tk.Frame(relief=tk.FLAT,border=3)
form.pack(side=TOP)

# all the customer and all the video display list
form1 = tk.Frame(master=form,relief=tk.FLAT,border=3)
form1.pack(side=LEFT)

form2 = tk.Frame(master = form,relief=tk.FLAT,border=3)
form2.pack(side=LEFT)

lblCustomer = ttk.Label(master=form1, text="Customer")
lblCustomer.pack(ipadx=5, ipady=5, side=TOP)

# customer list
cList = tk.Listbox(master=form1, exportselection=0, selectmode=tk.BROWSE)
cList.pack(ipadx=5, ipady=5,padx=10)
for acustomer in cName:
    cList.insert(tk.END,acustomer)

lblMovie = ttk.Label(master=form2, text="Movie")
lblMovie.pack(ipadx=5, ipady=5, side=TOP)

# movie list
mList = tk.Listbox(master=form2,width=25, exportselection=0, selectmode=tk.BROWSE)
mList.pack(ipadx=5, ipady=5,padx=10)
for amovie in movies:
    mList.insert(tk.END,amovie)

# button Frame
form3 = tk.Frame(relief=tk.FLAT,border=3)
form3.pack(padx=5, pady=5)

btnRent = ttk.Button(master=form3, text="Rent", command=button_rent)
btnRent.pack(ipadx=10,padx=10, side=LEFT)

btnReturn = ttk.Button(master=form3, text="Return", command=button_return)
btnReturn.pack(ipadx=10,padx=10, side=LEFT)

# customer detail frame display
form4 = tk.Frame(relief=tk.FLAT,border=3)
form4.pack(padx=20)

btncDetail = ttk.Button(master= form4, text="Customer Detail", command=customer_detail)
btncDetail.pack(ipadx=20, ipady=5, side=LEFT)

cDText = tk.Text(master= form4, height=20, width=30)
cDText.pack(padx=10, pady=5, side=LEFT)

# movie detail frame display
form5 = tk.Frame(relief=tk.FLAT,border=3)
form5.pack(padx=20)

btnmDetail = ttk.Button(master=form5, text="Movie Detail", command=movie_detail)
btnmDetail.pack(ipadx=28, ipady=5,side=LEFT)

mDText = tk.Text(master=form5, height=8, width=30)
mDText.pack(padx=10, pady=5, side=LEFT)

shop.mainloop()