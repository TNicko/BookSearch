from datetime import date



def book_checkout():

    #Asking for Member-ID
    while True:
        try:
            m=int(input("Member-ID : "))
            if len(list(str(m))) == 4:
                if m<=9999 and m>0:
                    break
                else:
                    print("That is not a valid Member-ID")
            else:
                print("That is not a valid Member-ID")

        except ValueError:
            print("That is not a valid Member-ID")
        
    
    #Asking for Book ID and changing 0 to Member-ID in database
    try:
        b=int(input("Book ID : "))
        if 0<b<=20:
            database = open("database.txt", "r")
            data = database.readlines()
            lines = list(data)
            line = lines[b]
            database.close()
            if line[-2]==str(0) and line[-3]=="," :
                print("Book Withdrawn")
                newline = line[:-2] + str(m)
                database = open("database.txt", "r")
                data = database.read()
                data = data.replace(line, newline+"\n")
                database.close()
                database = open("database.txt", "w")
                database.write(data)
                database.close()
                #Adding withdrawn book to logfile
                date = date.today()
                with open("logfile.txt","a") as logfile:
                    logfile.write("%r,"%b+str(date)+"\n")
            else:
                print("Book not available for withdrawal")
                
        else:
            print("Not Valid Book ID")
        
    except ValueError:
        print("Please type a number")
        

    
    
if __name__ == "__main__":
    book_checkout()




    
        


    



        



        
        





    
        
