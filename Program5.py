#Beginning of Program 5 

#Create Variables 
count = 0 #This will be used in our function 

#Create File to write to 
file = open("Prime.dat", "w") #This is the name of the file written to


#Create Function to test to see if Number entered is Prime

def getfactor(num): #constructor for function with num as argument. This will be what the user enters
    count = 0 #Create a local variable count inside the function 
    for i in range(1, num + 1): #Now create a for loop which will start at 1 and end at the number entered plus 1
        if (num % i) == 0: #This checks if the remainder of the number entered divided by the current i (iteration) is equal to 0 
            count = count + 1 #This displays the number of factors within the number entered
    if (count > 2): #There there are more than two factors for num entered then it is not prime
         print("This is not a prime Number")
    elif (count == 2): #If Prime numbers are only 1 and itself, so if count = 2 it is prime
         print(num) #Display the number entered


#The function below will retrieve the first 200 Prime Numbers

def solution(): #Function name
    iterations = 0  #Iterations shows how many prime numbers are displayed
    for n in range(2,1225): #This iterates the numbers from 2 - 1225 to check each for prime numbers
        count = 0   #This count is going to be used to show the number of factors each number has
        for i in range(1, n+1): #Prepare second for loop to check for factor
             if (n % i) == 0:   #Check to see if the modulus of each number is 0
                count = count + 1   #iterate count this area represents each of the prime numbers that would be listed for a number 
        if (count == 2): #This checks to see if the values of the prime numbers are only 1 and itself
           iterations = iterations + 1 #This will display how many prime numbers we currently have
           print("Prime Number: " + str(n) + " ||  Number of Prime Numbers:  " + str(iterations)) #Display the final message 
           file.write("Prime Number: " + str(n) + " || Total Prime Number:  " + str(iterations) + "\n") #Write the info to the file prime.dat
   

solution() #This is the call to the function

file.close() #This will close the file
