#|/usr/bin/python3
'''
Created on Aug 5, 2019

@author: Claudia Stella
@author: Carlo Cena
'''
import csv

class MergeClass(object):
    '''
    It merges csv files deleting duplicated rows.
    It accepts an array of file paths and a columns' separator
    '''

    def __init__(self, filePaths, fileDestination="merged.csv", sep = ',', intervall = 61):
        '''
        @param file_name: Path to the file
        @param fileDestination: Path to the new file
        @param sep: columns' separator, default: ','
        @param intervall: time difference between two rows, default: 61
        '''
        if not filePaths:
            print("You need to input the path to at least a csv file.")
            return 
        self.filePaths = filePaths
        if not fileDestination:
            print("Destination not provided...\nNew file created: merged.csv")
        self.fileDestination = fileDestination
        self.sep = sep
        self.intervall = intervall
        
    def main(self):
        '''
        It creates a new file merging all the inputs 
        and searches for missing data (difference between two rows greater than 60)
        '''
        my_max = 0
        previous = 0.0
        second_row = False
        missing_data = 0 #counter of missing data
        #Opening destination file as 'writecsv'
        with open(self.fileDestination, 'w') as writecsv:
            
            spamwriter = csv.writer(writecsv, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            #Iterating through all the files and coping not duplicated data in 'writecsv'
            for my_file in self.filePaths:
                
                with open(my_file) as csvfile:
                    my_reader = csv.reader(csvfile, delimiter=self.sep)
                    flag = False #flag used to avoid dealing with first row (columns title)
                    
                    for row in my_reader:
                        #If a date is greater or equal to a predecessor we have duplicated data
                        if flag and float(row[0]) > my_max:
                            
                            spamwriter.writerow(row)
                            if second_row and float(row[0]) - previous > self.intervall:
                                print("Found missing data between ",previous," and ",float(row[0]))
                                missing_data += 1
                            elif not second_row:
                                second_row = True
                            
                            previous = float(row[0])
                            my_max = float(row[0])
                            
                        elif flag and float(row[0]) <= my_max:
                            print("Duplicated data found.")
                            
                        if not flag:
                            flag = True
        print("Found ",missing_data," missing data")
                            
