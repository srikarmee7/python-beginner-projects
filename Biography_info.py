#create a fucntion
def bioGrap():
    #create a input variable to ask for the minimal details about them
    name = input("Enter your Name: ")
    dob = input("Enter your Date of birth: ")
    Address = input("Enter your address")
    movie = input("What is your favorite movie: ")
    #print the whole variable using concatenation of strings
    print("Name : " + name + "\nDate of birth : " + str(dob) + "\nAddress : " + Address + "\nfavorite : " + movie)

bioGrap()
