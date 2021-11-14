

def book_return():

    from datetime import date
    # Checks in database if book is in library
    while True:
        try:
            b=int(input("Book ID : "))
            if 0<b<=20:
                database = open("database.txt", "r")
                data = database.readlines()
                lines = list(data)
                line = lines[b]
                database.close()
                if line[-2]==str(0) and line[-3]=="," :
                    print("This Book is already in library")
                    break
                else:
                    #ID is changed to 0 in database                                            
                    print("Book is now available for withdrawal")
                    newline = line[:-5]+str(0)
                    database = open("database.txt","r")
                    data = database.read()
                    data = data.replace(line, newline+"\n")
                    database.close()
                    database = open("database.txt","w")
                    database.write(data)
                    database.close()
                    break
            else:
                print("Not Valid Book ID")
            
        except ValueError:
            print("Please type a number")


   #Adds date of return of the book in logfile
    date=date.today()
    logfile = open("logfile.txt","r")
    log = logfile.readlines()
    lines = list(log)
    logfile.close()
    
    for book in lines:
        if len(book) < 18 and (book[0]==str(b) or book[:2]==str(b)):
            newbook=book[:-1]+","+str(date)
            logfile = open("logfile.txt","r")
            log = logfile.read()
            log = log.replace(book, newbook+"\n")
            logfile.close()
            logfile = open("logfile.txt","w")
            logfile.write(log)
            logfile.close()
            break

            
if __name__ == "__main__":
    book_return()      
             
            
        
