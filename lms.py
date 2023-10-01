import json
import time
from datetime import datetime

try:
    with open('lib.json', "r") as read_it: 
        lib_data = json.load(read_it) 
except:
    lib_data = dict()
# print(lib_data)

def save_json(data,lib_json_file="lib.json"):
    with open(lib_json_file,"w") as p:
        json.dump(data,p)


class Book:
    def __init__(self,lib):
        self.lib=lib
        # self.author = auth1
    
    def displayBookData(self):
        print(f"AVAILABLE BOOKS ARE: ")
        for i in self.lib['book_details']:
            print(f"{self.lib['book_details'].index(i)+1} Title: {i['Title']}\n Author: {i['Author']} \n Quantity: {i['Quantity']}\n")
    
    def SearchingBook(self,book_name):
        self.book_name=book_name
        for i in self.lib['book_details']:
            if (i["Title"]).upper()==book_name.upper():
                print(True)
                return i['Quantity']

        print(False)
        return 0
    
    def isAvailable(self,book_name):
        self.book_name=book_name
        if self.SearchingBook(book_name)>0:
            print(f"{book_name} is available")
            return (True)
        else:
            print(f"{book_name} is not available")
            return (False)

class Student(Book):
    def __init__(self,name,address,lib):
        super().__init__(lib)
        self.name=name
        self.address=address
    
    def issueBook(self,book_name):
        self.book_name=book_name
        if super().isAvailable(book_name):
            flag=True
            for i in self.lib["book_details"]:
                if i["Title"].lower()==book_name:
                    i["Quantity"]-=1
                    break
            
            for i in self.lib["student_details"]:
                if (i['name']).lower()==(self.name).lower():
                    
                    i["total_issued_book"][book_name]=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    flag=False
                    break
            if flag:
                self.lib["student_details"].append({"name":self.name,"address": self.address,"total_issued_book": {self.book_name: datetime.now().strftime("%d/%m/%Y %H:%M:%S")}}),
            
            save_json(self.lib)
            print(("\nBook has been issued successfully").upper())
            
        pass

    def fine(self,book_name):
        self.book_name=book_name
        for i in self.lib["student_details"]:
            if (i['name']).lower()==(self.name).lower():
                assigning_date=i["total_issued_book"][self.book_name]
                returning_date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")

                dt1=assigning_date.split(" ")[0]
                dt2=returning_date.split(" ")[0]
                
                date_format = "%d/%m/%Y"
                a = time.mktime(time.strptime(dt1, date_format))
                b = time.mktime(time.strptime(dt2, date_format))
                delta = b - a
                return int(delta / 86400)
                

      
        pass
    
    def returnBook(self,book_name):
        self.book_name=book_name

        for i in self.lib["book_details"]:
                if i["Title"].lower()==book_name:
                    i["Quantity"]+=1
                    break
        

        
        for i in self.lib["student_details"]:
                if (i['name']).lower()==(self.name).lower():
                    try:
                        i["total_issued_book"].pop(self.book_name)
                        print('BOOK RETURNED SUCCESSFULLY')
                    except:
                        print("BOOK NOT IN DATABASE")
                    
                    break
        
        save_json(self.lib)
        
class Staff(Book):
    def __init__(self,book_name,lib):
        super().__init__(lib)
        self.book_name=book_name
    
    def addBook(self):
        pass

    def deleteBook(self):
        pass
        
print("Welcome to Library Management System\n")
print("WHAT IS YOU GOOD NAME, ADDRESS AND TYPE 1 IF YOU ARE A STUDENT, TYPE 2 IF YOU ARE A STAFF, TYPE 3 FOR GENRAL BOOKS INFORMATION, TYPE 4 TO EXIT")
print("(followed by spaces)\n")


while(True):
    res=input("name address and choice : ")
    try:
        name,address,choice=(res.split(" "))
    
        
        choice=int(choice)
        # print(name,choice)
        
        if choice==1:
            print("TYPE 1 TO ISSUE A BOOK, TYPE 2 TO RETURN A BOOK, TYPE 3 TO EXIT")
            choice1=int(input("Choice: "))
            b=Student(name,address,lib_data)
            bookIR=input("BOOK NAME NEED TO ISSUE/RETURN: ")
            if choice1==1:
                b.issueBook(bookIR)
                pass

            elif choice1==2:
                
                if b.fine(bookIR)>15:
                    print("HAVE TO PAY FINE FOR EXCEEDING DAYS")
                else:
                    print("NO FINE")

                b.returnBook(bookIR)
                

            elif choice1==3:
                print("THANK YOU \n")
                exit()

            else:
                print("INVALID INPUT! \n")
            
            pass
        elif choice==2:
            print("TYPE 1 TO ADD BOOK, TYPE 2 TO DELETE BOOK, TYPE 3 TO UPDATE BOOK, TYPE 4 TO EXIT")
            choice2=int(input("YOUR CHOICE: "))
            bookADU=input("BOOK NAME NEED TO ADD/ DELETE/ UPDATE: ")

            if choice2==1:
                pass
            elif choice2==2:
                pass
            elif choice3==3:
                pass
            elif choice2==4:
                print("THANK YOU \n")
                exit()

            else:
                print("INVALID CHOICE,TRY AGAIN \n")

            
            pass
        
        elif choice==3:
            print("TYPE 1 FOR BOOK DETAILS, TYPE 2 FOR SEARCHING A PARTICULAR BOOK, TYPE 3 FOR TO CHECK AVAILABILTY OF A BOOK, TYPE 4 TO EXIT")
            choice3=int(input("YOUR CHOICE: "))
            a=Book(lib_data)
            if choice3==1:
                a.displayBookData()
                pass

            elif choice3==2:
                book_name=input("Book name: ")
                a.SearchingBook(book_name)
                pass

            elif choice3==3:
                book_name=input("Book name: ")
                a.isAvailable(book_name)
                pass

            elif choice3==4:
                print("THANK YOU \n")
                exit()
            else:
                print("INVALID INPUT! \n")
                pass
        elif choice==4:
            print("THANK YOU \n")
            exit()

        else:
            print("INVALID CHOICE,TRY AGAIN \n")
            
    except Exception as e:
        print(f"{e} \n PLEASE PROVIDE 3 ARGUMENTS")

        
        


        

        
