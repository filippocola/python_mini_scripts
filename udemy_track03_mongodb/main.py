import pymongo
from pymongo import MongoClient

if __name__ == "__main__":
    # eseguo la connessione 
    conn = MongoClient("mongodb://admin:secret@localhost:27017")
    db = conn["mongodb"]
    print(conn.server_info())
    conn.start_session()

    # creo un database (con questa sintassi se esiste si connette altrimenti lo crea)
    #  db = conn.testdb

    # accedo alla collection 
    persone_collection = db.persone
    db.create_collection("persone")
    print(f"creato una collection: {db.list_collections().to_list()}")
    print(f"lista di db {conn.list_databases().to_list()}")
    # Creo una serie di indici 
    # persone_collection.create_index("nome", session=conn)
    # persone_collection.create_index([("cognome", pymongo.ASCENDING)])
    # persone_collection.create_index([("computer", pymongo.ASCENDING)])
    
    # creo il primo documento 
    # p1 = {"nome": "Mario", "cognome": "Rossi", "età": 30, "computer": ["asus", "apple"]}
    # p2 = {"nome": "Luigi", "cognome": "Verdi", "età": 45, "computer": ["asus"]}

    # inserisco il documento 
    # persone_collection.insert_one(p1)
    # persone_collection.insert_one(p2)




