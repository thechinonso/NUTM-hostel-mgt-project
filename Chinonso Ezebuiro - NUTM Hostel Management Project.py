# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:27:55 2021

@author: user
"""

#Chinonso Ezebuiro

#NUTM Hostel Management Software


import random
import datetime

name = []
phno = []
add = []         #Addresses of students
checkin = []     #Students check-in dates 
checkout = []    #Students check-out dates
roomno = []      #Students room numbers
studentId = []   #Students IDs
day = []         #The Days of the week that the students checked in




#Function to checkout a student from the hostel

def checkoutt(): 
    checker = int(input ("Enter student id: "))
    if checker in studentId:
        checkout[studentId.index(checker)] = datetime.datetime.today().strftime('%Y-%m-%d')
        print (" \nYou have successfully checked out\n-----------------------"
                "--------------------------")
    else:
        print("details not found, It seems you were never checked in :-)"
              "\n-------------------------------------------------")



#Function to allocate rooms and student ID

def Allocation():   
        name_in = input ("Enter your name: ")
        phn_in = input ("Enter your phone number: ")
        add_in = input ("Enter your address: ")
        date_in = input ("Enter date(YYYY-MM-DD): ")
        date_in = Date(date_in)
        day_in = dayfind(date_in)
        name.append(name_in), phno.append(phn_in),add.append(add_in),
        checkin.append(date_in), day.append(day_in), checkout.append(Date("2020-09-30"))
        croom = ['1A','1B','2A','2B','3A','3B','4A','4B','5A','5B',
                  '6A','6B','7A','7B','8A','8B','9A','9B','10A','10B',
                  '11A','11B','12A','12B','13A','13B','14A','14B','15A','15B',
                  '16A','16B','17A','17B','18A','18B','19A','19B','20A','20B']
        room_in = random.choice(croom)
        while room_in in roomno:
            room_in = random.choice(croom)
        roomno.append(room_in)
        
        id_in = random.randint(50001,54534)
        while id_in in studentId:
            id_in = random.randint(50001,54534)
        studentId.append(id_in)
        
        
        print ("\n-------------------------------------------------\n"
                "Room allocated,your details are:\n\nID: "+str(studentId[-1])+
                "\nRoom: "+ str(roomno[-1])+"\n\nThank you\n------------------"
                "-------------------------------")
       
        
        
#Function to set checkout date to records
           
def check_checkout(x): 
    if checkout[x]==Date("2020-09-30"):
        return "N/A"
    return checkout[x]

  
    
#Function to validate date format

def Date(x): 
    try:
        datetime.datetime.strptime(x,'%Y-%m-%d')
        return x
    except ValueError:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        x = input("Enter correct date format: ")
        return Date(x)  
  


#Function to print room information    

def Room_Information():
    print ("\n-------------------------------------------------")
    print ('Hello, Here are the amenities present in the rooms:'
            '\n\nSingle bed\nMattress\nPillows\nWorkstation\nDesk chair'
            '\nFunctional door\nIn-shower rack\nAccess control card'
            '\n-------------------------------------------------')



#Function to display food menu (Breakfast, Lunch, and Dinner)

def Student_lounge():
    Breakfast_menu = ["Chicken pie and fruit juice", "Chicken and Chips", 
                      "Sandwich and juice",]
    Lunch_menu = ["Jollof rice, salad and chicken", "White rice and stew", 
                  "Spaghetti and beef" ]
    Dinner_menu = ["Boiled Plantain and eggs", "Pounded yam and efo riro", 
                    "Beans pudding/moi-moi"]
    
    print("\nEnter meal of the day:\n1.Breakfast\n2.Lunch\n3.Dinner")
    choicest  = int(input("\nEnter option: "))
    print ("\n-------------------------------------------------")
    if choicest ==1:
        print("Breakfast menu:\n")
        for i in Breakfast_menu:
            print (i)
    elif choicest==2:
        print("Lunch menu:\n")
        for i in Lunch_menu:
            print (i)
    elif choicest==3:
        print("Dinner menu:\n")
        for i in Dinner_menu:
            print (i)
    print ("\n-------------------------------------------------")
          


            
#Function to display records of an individual student or all students

def Record(): 
    rec  = int(input("Check records of:\n\n1.A scholar\n2.All scholars\n\nEnter option: "))
    print ("\n-------------------------------------------------")
    if rec==1:
        checker = int(input("Enter student id: "))
        if checker in studentId:
            i = studentId.index(checker)
            print ("\nNAME: "+str(name[i])+"\nPHONE: "+str(phno[i])+"\nADDRESS: " 
                    +str(add[i])+"\nCHECKED-IN: "+str(checkin[i])+" ("+ day[i]+")"
                    "\nCHECKED-OUT: "+str(check_checkout(i))+"\nROOM NUM: " 
                        +str(roomno[i])+"\nID: "+str(studentId[i]))
            print ("\n-------------------------------------------------")      
    elif rec ==2:
        for i in range(0,(len(name))):
            print ("\nNAME:"+str(name[i])+" | PHONE:"+str(phno[i])+" | ADDRESS:"
                    +str(add[i])+" | CHECKED-IN:"+str(checkin[i])+" ("+ day[i]+")"
                    " | CHECKED-OUT:"+str(check_checkout(i))+
                    " | ROOM NUM:"+str(roomno[i])+ " | ID:"+str(studentId[i]))
        print ("\n-------------------------------------------------")
    else:
        print("Enter valid input")
        print ("-------------------------------------------------")
        Record()
        




#To determine the day of the week the student checked in

def dayfind(y): 
    x = datetime.datetime.strptime(y,'%Y-%m-%d').weekday()
    if x == 0:
        return"Monday"
    if x== 1:
        return "Tuesday"
    if x == 2:
        return"Wednesday"
    if x== 3:
        return "Thursday"
    if x == 4:
        return"Friday"
    if x== 5:
        return "Saturday"
    if x == 6:
        return"Sunday"
    



# Home Page

def Home(): 
    print("\n-------------------------------------------------\nWelcome to  the NUTM Hostel Management portal\n"
          "-------------------------------------------------")
    check = True
    while (check):
        print ("\nPlease select option \n\n1.Allocate hostel and Student ID\n2.Room information\n3.Room service\n4.Records\n5.Student checkout\n6.Quit")
        
        select = int(input("\nEnter option: "))   
        if (select==1):
            Allocation()
        elif (select == 2):
            Room_Information()
        elif (select == 3):
            Student_lounge()
        elif (select == 4):
            Record()
        elif (select == 5):
            checkoutt()
        elif (select == 6):
            print("Goodbye")
            check = False
        else:
            print("Wrong input value, Enter valid input")
                
        
        
# Initiating the program by calling the home function
Home() 
            
            