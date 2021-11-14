


def book_search():
    
    

    #Asking for Book title and Finding it in database
    books = []
    book_list=list(range(1,18))
    book=input("Book Title : ")
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
        except ValueError:
            print("No such book exists")
    else:
        print("No such book exists")
    

    #Printing book info from database            
    for element in books:
        element=element.split(",")
        for info in element:
            print(info)


if __name__ == "__main__":
    book_search()   






