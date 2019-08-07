#!/usr/bin/python3
from MergeData.MergeData import MergeClass

if __name__ == '__main__':
    filePaths = []
    newFile = ""
    
    print("Inserire il path dei file da unire, per terminare inserimento digitare stop")
    while not newFile=="stop":
        newFile = input("Inserire nuovo path o 'stop':")
        if newFile!="stop":
            filePaths.append(newFile)
        else:
            destination = input("Inserire path dal file da creare:")
    sep = input("Qual è il separatore di colonne? Per default inserire [n]:")
    intervall = input("Inserire intervallo corretto tra i dati, per default inserire [n]:")
    print("Inserimento terminato.\nInizio operazioni...")
    
    if sep != 'n' and intervall != 'n':
        my_mc = MergeClass(filePaths, destination, sep = sep, intervall = int(intervall))
    elif sep == 'n' and intervall != 'n':
        my_mc = MergeClass(filePaths, destination, intervall = int(intervall))
    elif sep != 'n' and intervall == 'n':
        my_mc = MergeClass(filePaths, destination, sep = sep)
    else:
        my_mc = MergeClass(filePaths, destination)
    my_mc.main()
