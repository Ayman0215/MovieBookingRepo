
#3

# - First find what movie they are watching, how may people are watching that movie, and if they are a member or not.
# - Then apply the discounts.
# - Make an equation for any situation at hand.

import sys
import random

case1 = "Jurassic Park"
case2 = "F1"
case3 = "Superman"
case4 = "Fantastic Four"

volumeDiscountPct = 0.1   # - Use it in volumeDiscountPct
memberDiscountPct = 0.15   # - memberDiscountPct
salesTaxPct = 0.09 # - salesTaxPct

movies = [f"{case1}", f"{case2}", f"{case3}", f"{case4}"]  # - ...

def findMoviePriceByMovieName(movie):
    if movie not in movies: # - ...
        movie = str(input(f"Sorry, try again. Please let me know what movie you are watching? The options are {movies}: "))
    elif movie in movies:
        moviePrice = random.randint(10,20)  
    return moviePrice

def calculateInitialBill(moviePrice, numOfPeople):
    # TODO: Can we avoid the extra variable initialBillAmount?    
    bill = numOfPeople * moviePrice
    return bill

def applyVolumeDiscount(bill, numberOfPeople):
    # TODO: Can we avoid the extra variable appliedVolumeDiscount?
    if numberOfPeople >= 6 :
        bill = bill * (1 - volumeDiscountPct)
    return bill

def applyMemberDiscount(bill, isAMember):
    # TODO: Can we avoid the extra variable appliedVolumeDiscount?
    if isAMember == "Y" or "y" :
        bill = bill * (1 - memberDiscountPct)
    return bill

def applySalesTax(bill):
    # TODO: Can we avoid the extra variable subtotal?
    subtotal = bill * (1 + salesTaxPct)
    return subtotal

#Adds a movie of the users choice.
def addMovie():
    addedMovie = input("Would you like to add a movie? Y or N: ")
    if addedMovie == "Y" or "y":
        addedMovie = input("What is the name of your movie in mind? ")
        movies.append(addedMovie)
    elif addedMovie == "N" or "n" :
        print("Ok")
    else:
        print("I will take that as a [NO].")
    return movies

#Removes a movie of the users choice.
def removeMovie():
    removedMovie = input("Would you like to remove a movie? Y or N: ")
    if removedMovie == "Y" or "y":
        removedMovie = input("What is the name of your movie in mind? ")
        if removedMovie not in movies:
            removedMovie = input("Sorry, that is not an option, please try again: ")
            if removedMovie == None or [] or removedMovie not in movies:
                sys.exit("No funny business in the theaters")
            else:
                print("I will take that as a [NO].")
        elif removedMovie in movies:
            movies.remove(removedMovie) #Review Check
    elif removedMovie == "N" or "n":
        print("Ok")
    else:
        print("I will take that as a [NO].")
    return movies

def booking():
    booking = input("Would you like to book a movie? Y or N: ")
    if booking == "Y" or "y":
        ...
    else:
        ...
    #addMovie()
    #removeMovie()

def toExit():
    exiting = input("Would you like to leave the theater? Y or N: ")
    if exiting == "Y" or "y":
        sys.exit
    print("Ok, lets continue.")
#-------------------------------------------------------------------------------------------------------------#        

def MovieReciept():

    #Take necessary inputs
    movie = str(input(f"Hello! Welcome back to Python Theaters! What is the movie you are watching today? The options are {movies}: "))  # - ...
    numberOfPeople = int(input("And how many people are going to that movie? "))    # - ...
    isMember = str(input("Is any one in your party a member of Python Theaters? Please say Y or N: "))   # - ...

    # Validate Inputs & return if they are bad
    while numberOfPeople <= 0:
        numberOfPeople = input("Please try again, how many people are going to that movie?")    

    # Find Movie price by movie name
    # inputs: movie name
    # outputs: movie price
    moviePrice = findMoviePriceByMovieName(movie)

    # Calculate initial bill amount
    # inputs: movePrice , numberOfPeople 
    # outputs: bill amount
    bill = calculateInitialBill(moviePrice, numberOfPeople)

    # Apply volume discount
    # inputs: bill amount, numberOfPeople
    # outputs: discountedBillAMount
    bill = applyVolumeDiscount(bill, numberOfPeople)

    # Apply member discount
    # inputs: member discount percentage, initial bill amount or bill amount with volume discount 
    # outputs: bill amount with member discount or bill amount with both
    bill = applyMemberDiscount(bill, isMember)

    # Add Sales tax
    # inputs: sales tax percentage, initial bill amount / bill amount with volume discount / bill amount with member discount / bill amount with both
    # outputs: bill amount with sales tax
    subtotal = applySalesTax(bill)
    
    subtotal = round(float(subtotal), 2)

    print(f"Here is your recipet: Your subtotal is ${subtotal}, by going to the {movie} movie, which is ${moviePrice} per person, by going with {numberOfPeople} people.")
    print("We hope to see you come back soon")

#-------------------------------------------------------------------------------------------------------------#

while True:
    MovieReciept()
    #addMovie()
    #removeMovie()
    toExit()
    booking()
#-------------------------------------------------------------------------------------------------------------#

# - Case #1: Number of People is less than 6.

# - Input: F1, 1, No
# - Ouput: $11.12


# - Case #2: Number of People is greater than 6.

# - Input: Superman, 8, Yes
# - Ouput:$97.84

# - Case #3: The group has a member.

# - Input: Jurassic Park, 3, Yes
# - Ouput:$33.35

# - Case #4: The group doesn't have a member.

# - Input: Fantastic Four, 2, No
# - Ouput: $22.24

# - Case #5: >6, No Member.
# - Input: Fantastic Four, 8 , No
# - Ouput: $117.72

# - Case #5: <=0
# - Input: 0
# - Ouput: Please try again

# - Case #5: other than in member input
# - Input: NOO
# - Ouput: "I will take that as a [NO].


# TODO:
# Less than 6, no member -- objective didn't reflect, but this was covered.
# Greater than 6, no member -- Not covered </
# Less than 6, member -- objective didn't reflect, but this was covered.
# greater than 6, member -- objective didn't reflect, but this was covered.
# Error cases:
# less thna 0 as people input -- Not covered
# Y/N - other than in member input -- Not covered
# 