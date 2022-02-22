# Pseudo code

from matplotlib.style import library
from typing import List, Tuple, Dict
from collections import namedtuple
import math
import itertools


#order to register the library


#step 1: function that gets input 
# create classes for books, lib, sign up and scanning
# defininig function
# for book class, we need id and score
# for lib we need, id, no of books, list of books, signup duration, scan per day, list of books scanned, total possible score, affordable days
# for sign up we need order of library, picking first library for signup,
# scanning we need books scanned already

#
# function to calculate the score
# number of affordable days for each library = total days - (duration of signup + (total books / books per day)) #attribute of library class
# best library is the one with less affordable days then most scores\


# duration of signup and scores involved
# we will have a list of libraries added, so we can always check the next library if it has the same books, if yes we skip to the next one or maybe skip the books

# we cannot add the same book on the same day
# sorry my network went off

# |   |   | 3,2| 4,1 | 0|   |   |
# |   |   |    |5    | 2| 3 |   |

# after sorting by SCOREs


# Input function
def read_file(filename):
    with open(filename) as f:
        lines = [list(map(int, i.rstrip().split())) for i in f.readlines()]
        #B: number of books
        #L: number of libraries
        #D: number of days

        B, L, D = lines.pop(0)
        bscores = lines.pop(0)
        line = lines

        
        
        return B, L, D, bscores, line

       
#output function
class Books(dict): #toyyib
    def __init__(self, ids, score):
        self.ids = ids
        self.score = score

        
        
class Libraries(dict): #doyin and toyyib
#for lib we need, id, no of books, list of books, signup duration, scan per day, list of books scanned, total possible score, affordable days
    def __init__(self,id,spd, signup_dur, book_list, bscores):
        self.spd = spd
        self.id = id
        self.signup_dur = signup_dur
        self.book_list = book_list
        self.bscores = bscores
        #self.books = {book_list[i]: bscores[i] for i in range[len(book_list))}
        self.books = [Books(i, bscores[i]) for i in range(len(book_list))]

    def affordable_days(self, total_days):
        self.affordable_day = total_days - (self.signup_dur + math.ceil(len(self.books) / self.spd))
        return self.affordable_day
        
    def scan_next(self, books_scanned):
        possibleBooks = [x for x in self.books if x not in books_scanned]
        if len(possibleBooks) > 0:
            return max(possibleBooks, key=lambda x: x.score)
        else:
            return False

    def total_possible_score(self):
        score = 0
        for book in self.book_list:
            score += self.bscores[book]
        return score
    
    def scannable_books(self, daysLeft):
        possibleScan = self.spd*daysLeft
        if possibleScan > len(self.books):
            return len(self.books)
        return possibleScan
    


class SignUp(): # Dapo and Dunsin
    def __init__(self, libraries: List[Libraries]):
        self.libraries = libraries # = # sorted list, sorted by scores and days of signup
        
    def getNextLibrary(self, total_days: int):
        """
            to help select the next best library

        """
        # to use the duration and total days
        # calculate the days left
        # calculate highest scores
        # check highest number of uncommon

        # libr = {'0': [33, 6, 3], "1" : [43,7,2]}

        self.libraries.sort(key = lambda x: (x.affordable_days(total_days), x.total_possible_score()))
        return (self.libraries)[0]                                                    
        

    def updateLibraries(self, currentLibrary : Libraries, totalDays: int):
        """
            removes the signed up library
            
        """
        self.libraries.remove(currentLibrary)
        #self.libraries = list(set(self.libraries)-set([x for x in self.libraries if x.signup_dur >= totalDays]))
        unregisteredLibraries = [x for x in self.libraries if x.signup_dur >= totalDays]
        self.libraries = list(itertools.filterfalse(lambda x: x in unregisteredLibraries, self.libraries ))
        
class Scan: 
    def __init__(self):
        pass


def write_solution(file_name, output):
    l = len(output)
    with open("solution_" + file_name, "w") as f:
        f.write(l)
        for i in range(output):
            #f.write(output[i].id, len(selectedBooks))
            # 
            pass
    pass


def main():
    
    file_name = 'Book_scanning_2020/data/a_example.txt'
    B, L, D, bscores, line = read_file(file_name)
    
    lob: List[Books] = [Books(i, bscores[i]) for i in range(B)]   
    
    lol: List[Libraries] = [Libraries(id = i/2,spd = line[i][2] , signup_dur = line[i][1] , book_list = line[i+1] , bscores = bscores) for i in range(0, len(line), 2) ] #list of libraries

    unregisteredLibraries: SignUp = SignUp(lol)
    output: List[Libraries] = []
    scannedBooks = []

    while D > 0 and len(unregisteredLibraries.libraries) > 0:
        selectedLibrary: Libraries = unregisteredLibraries.getNextLibrary(D)
        D = D - selectedLibrary.signup_dur
        unregisteredLibraries.updateLibraries(selectedLibrary, D)

        booksForLibrary = []
        for i in range(selectedLibrary.scannable_books(D)):
            selectedBook = selectedLibrary.scan_next(scannedBooks)
            if selectedBook == False:
                continue
            scannedBooks.append(selectedBook)
            booksForLibrary.append(selectedBook)
        
        selectedLibrary.books = booksForLibrary
        output.append(selectedLibrary)
    
    print(output)


    #write_solution(file_name, output) #write solution


if __name__ == "__main__":
    main()