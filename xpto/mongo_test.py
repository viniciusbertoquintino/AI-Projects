import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
try:
    print(client.server_info())  # Mostra informações do servidor
    print("MongoDB está funcionando!")
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)