import psycopg2

def dbconnect(dbName,dbUser,dbPass, dbPort = 5432,dbHost = 'localhost'):
    #create connection
    return psycopg2.connect(database = dbName , user = dbUser, host = dbHost, password = dbPass, port = dbPort)

