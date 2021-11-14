import tkinter as tk



def book_search():
    #Checking Book Title
    book = e.get()
    print(book)
    books = []
    book_list=list(range(1,18))
    if book[0:4]=="Book":
        try:
            x = False    
            for i in book_list:
                if i == int(book[4:]):
                    x = True
                    break
                else:
                    x = False
            if x == True:
                line_number = 0
                with open("database.txt","r") as database:
                    for line in database:
                        line_number += 1
                        if book+"," in line:
                            books.append(line)
            else:
                print("No such book exists")
                output.insert(tk.END,"No such book exists")
                
        except ValueError:
            print("No such book exists")
            output.insert(tk.END,"No such book exists")    
    else:
        print("No such book exists")
        output.insert(tk.END,"No such book exists")

    #Printing book info from database            
    for element in books:
        element=element.split(",")
        for info in element:
            print(info)
            output.insert(tk.END,info)
        output.insert(tk.END,"\n")    

def book_checkout():

    from datetime import date 
    
    #Checking member ID
    while True:
        
        try:
            m = e1.get()
            if len(list(str(m))) == 4:
                if int(m)<=9999 and int(m)>0:
                    break
                else:
                    msg = "That is not a valid Member-ID"
                    print(msg)
                    output.insert(tk.END,msg)
                    break
            else:
                msg = "That is not a valid Member-ID"
                print(msg)
                output.insert(tk.END,msg)
                break
        except ValueError:
            msg = "That is not a valid Member-ID"
            print(msg)
            output.insert(tk.END,msg)
            break
    
    #Checking Book ID and changing 0 to Member-ID in database
    try:
        if len(list(str(m))) == 4: #This 'if' makes sure Member ID was entered
            b = e3.get()
            if 0<int(b)<=20:
                database = open("database.txt", "r")
                data = database.readlines()
                lines = list(data)
                line = lines[int(b)]
                database.close()
                if line[-2]==str(0) and line[-3]=="," :
                    print("Book Withdrawn")
                    output.insert(tk.END,"Book Withdrawn")
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
                        logfile.write("%r,"%int(b)+str(date)+"\n")
                else:
                    msg = "Book not available for withdrawal"
                    print(msg)
                    output.insert(tk.END,msg)
            else:
                print("Not Valid Book ID")
                output.insert(tk.END,"Not Valid Book ID")
        else:
            print("")
    except ValueError:
        print("Please type a number")
        output.insert(tk.END,"Please type a number")
         

def book_return():

    from datetime import date
    # Checks in database if book is in library
    try:
        b = e4.get()
        if 0<int(b)<=20:
            database = open("database.txt", "r")
            data = database.readlines()
            lines = list(data)
            line = lines[int(b)]
            database.close()
            if line[-2]==str(0) and line[-3]=="," :
                msg = "This Book is already in library"
                print(msg)
                output.insert(tk.END,msg)
               
            else:
                #ID is changed to 0 in database
                msg = "Book is now available for withdrawal"
                print(msg)
                output.insert(tk.END,msg)
                newline = line[:-5]+str(0)
                database = open("database.txt","r")
                data = database.read()
                data = data.replace(line, newline+"\n")
                database.close()
                database = open("database.txt","w")
                database.write(data)
                database.close()
                
        else:
            print("Not Valid Book ID")
            output.insert(tk.END,"Not Valid Book ID")
    except ValueError:
        print("Please type a number")
        output.insert(tk.END,"Please type a number")

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

def book_weed():
    
    from collections import Counter

    #Saves logfile and database lines as a list
    logfile = open("logfile.txt","r")
    log = logfile.readlines()
    lines = list(log)
    logfile.close()
    lines.remove(lines[0])

    database = open("database.txt", "r")
    data = database.readlines()
    datalines = list(data)
    database.close()

    #Makes a list of book ID's (with repetition) that have been withdrawn
    book_id = []  
    for book in lines:
        
        if book[1]==",":
            book_id.append(int(book[0]))
        elif book[2]==",":
            book_id.append(int(book[:2]))
            

    #Changes different book ID's with same book title to same ID
    for i in range(len(book_id)):
        if book_id[i] == 6:
            book_id[i] = 7
        elif book_id[i] == 11:
            book_id[i] = 12
        elif book_id[i] == 17:
            book_id[i] = 18
        else:
            book_id[i] = book_id[i]


    #Checks for any book ID's that have never been withdrawn
    no_withdrawal=[]
    for i in range(1,21):
        if i not in book_id:
            no_withdrawal.append(i)

    no_withdrawal.remove(6)
    no_withdrawal.remove(11)
    no_withdrawal.remove(17)



    #Makes list of book ID's from least withdrawn to most withdrawn
    withdrawed = [] 
    for x in range(0,len(book_id)):
        count = Counter(book_id)
        minimum = min(count.values())
        minValue = next(i for i in reversed(book_id) if count[i] == minimum)
        withdrawed.append(minValue)
        book_id.remove(minValue)
    withdrawed = list(dict.fromkeys(withdrawed))
            
    no_withdrawal.extend(withdrawed)#adds book ID's that were never withdrawn
    least_most = no_withdrawal      



    #Changes Book ID's to their Book Titles
    book_titles = []
    for i in least_most:
        line = datalines[i]
        if i < 10:
            book_titles.append(line[16:21])
        elif i == 10:
            book_titles.append(line[17:22])
        else:
            book_titles.append(line[17:23])


    #Output: Least withdrawn books to most withdrawn books
    msg = "List of Books in order of least withdrawals to most withdrawals"     
    print(msg)
    output.insert(tk.END,msg)
    for i in range(0,len(book_titles)):
        print("%r) %s "%((i+1),book_titles[i]))
        output.insert(tk.END,"%r) %s "%((i+1),book_titles[i]))
        


    #Output: Books that have never been withdrawn
    for element in withdrawed:
        if element in no_withdrawal:
            no_withdrawal.remove(element)

    if len(no_withdrawal) == 0:
        msg = "\nAll the books have been withdrawn at least once"
        print(msg)
        output.insert(tk.END,msg)
    else:
        msg = "\nBooks that have never been withdrawn :"
        print(msg)
        output.insert(tk.END,msg)
        n = len(no_withdrawal)
        for i in range(0,n):
            print(book_titles[i])
            output.insert(tk.END,book_titles[i])
            

#---------------MAIN---------------#
root = tk.Tk()

root.title("Library Management System")
root.geometry("800x700")
root.configure(bg="#060400")

label = tk.Label(root, text = " "*100, bg="#060400")
label.grid(column = 0, row = 0)

#Book Search
eLabel = tk.Label(root, text="Search for book : ", bg="#060400")
eLabel.grid(column = 0, row = 1)
e = tk.Entry(root, width=20)
e.grid(column = 0, row = 2)
buttonSearch = tk.Button(root,text="Book\nSearch", padx=18
                         ,command=book_search, bg="#060c0c")
buttonSearch.grid(column = 0, row = 3)

#Book Checkout
e1Label = tk.Label(root, text="Member ID : ", bg="#060400")
e1Label.grid(column = 0, row = 4)
e1 = tk.Entry(root, width=20)
e1.grid(column = 0, row = 5)

e3Label = tk.Label(root, text="Book ID : ", bg="#060400")
e3Label.grid(column = 0, row = 6)
e3 = tk.Entry(root, width=20)
e3.grid(column = 0, row = 7)
buttonCheckout = tk.Button(root, text="Book\nCheckout", padx=10
                           ,command=book_checkout, bg="#060c0c")
buttonCheckout.grid(column = 0, row = 8)

#Book Return
e4Label = tk.Label(root, text="Book ID : ", bg="#060400")
e4Label.grid(column = 0, row = 9)
e4 = tk.Entry(root, width=20)
e4.grid(column = 0, row = 10)
buttonReturn = tk.Button(root,text="Book\nReturn",padx=18
                         ,command = book_return, bg="#060c0c")
buttonReturn.grid(column = 0, row = 11)


#Book Weed
buttonWeed = tk.Button(root, text="Book\nWeed", padx=21
                       ,command = book_weed, bg="#060c0c")
buttonWeed.grid(column = 0, row = 12)

#Output
output=tk.Listbox(root)
output.config(width=60,height=40)
output.grid(column = 1, row = 1, rowspan = 26)

#Exit
buttonExit = tk.Button(root, text="Exit", padx=10,
                       command= root.destroy, bg="#060c0c")
buttonExit.grid(column = 0, row = 20)


root.mainloop()

