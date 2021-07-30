#Reuben Ortiz 2411091
#pseudocode.
#write a program that uses a while loop
#prompt user to enter a positive INT
 #num = int(input)
  #assign the iniput as num
#while loop should contiune to run unless user wishes to exit with ENTER or 0
    #while != and >0 or != 0 will be used
     #avoid endless loop
#assign a varr even = 0 use the even boolean to find the even number
    #add the user input to the even varr
    #else do the oppsite for your odd numbers
 
  
#once user finishes have the program total all the inputs
 
  

#display what the user will be doing
def main():
    total = 0
    even = 0
    odd = 0
    num = 1
    print("Enter a Positive number. Press ENTER or 0 to exit the program")
    print("at the end of the program i'll total your input.")

    
    
    
    #While loop user should be able to use 'enter' or 0 to exit
    while num != '' and int(num) > 0:
        
        #user inputs number as a string will convert it to a INT later
        num = input('Enter your number here travler ')

        
        #this should allow 'enter' or 0. will see here shortly
        if num != '' and int(num) > 0:
            #convert the string to a INT.
            num =int(num)

            #a loop inside a loop. its like the movie inception
            if num % 2 == 0:
                even = even + num #short hand? even += num
            else:
                odd = odd + num
        

        #Above is if the number has no remainder it's a even. then all the
         #even numbers are added toget, else statment is just the oppsite
        

        #displaying the total
    print(f'Your total odd', odd ,'your total even', even)
main()
#end code

#fingers crossed...



