
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
    print("List of Books in order of least withdrawals to most withdrawals")

    for i in range(0,len(book_titles)):
        print("%r) %s "%((i+1),book_titles[i]))



    #Output: Books that have never been withdrawn
    for element in withdrawed:
        if element in no_withdrawal:
            no_withdrawal.remove(element)

    if len(no_withdrawal) == 0:
        print("\nAll the books have been withdrawn at least once")
    else:
        print("\nBooks that have never been withdrawn :")
        n = len(no_withdrawal)
        for i in range(0,n):
            print(book_titles[i])

    
if __name__ == "__main__":
    book_weed()   





