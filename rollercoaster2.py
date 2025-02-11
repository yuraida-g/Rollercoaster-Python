print("Welcome to the RollerCoaster Ride !!!!!!!")

height= float(input("Enter your height:"))
age = int(input("Enter age: "))
bill = 0

if height >= 120 :
   print("welcome")
   
   if age < 10 :
      bill = 6
      print("Pay $6")
      
   elif age <= 18:
      bill = 9
      print("Pay $9")

   elif age >= 45 and age  <= 55:
      print("Free")
      
   else :
      bill = 15
      print("Pay $15")
      
   wantsPhoto = input("Do you wish for a picture enter Y or N: ")
   if wantsPhoto == "Y" :
      bill += 3
      print("You bill is: " , bill)
      
else:
     print("Sorry , You cannot ride")