import pickle

def storeData():
    # initializing data to be stored in db
    adnan = {'emp_no' : '1','emp_name' : 'adnan', 'salary' : 40000}
    umar = {'emp_no' : '2','emp_name' : 'umar', 'salary' : 40000}

    # database
    db = {}
    db['adnan'] = adnan
    db['umar'] = umar

    # Its important to use binary mode
    dbfile = open('binaryFile.bin', 'ab')
    
    # source, destination
    pickle.dump(db, dbfile)                     
    dbfile.close()

def loadData():
    query = input("Enter your query to search:")
    # for reading also binary mode is important
    dbfile = open('binaryFile.bin', 'rb')     
    db = pickle.load(dbfile)
    for keys in db:
        if query in db:
            print(keys, '=>', db[keys])
            break
    else:
        print("Sorry nothing found!")
    dbfile.close()

storeData()
loadData()