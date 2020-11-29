import mysql.connector
import socket
import hashlib
import bcrypt
import time
from pyisemail import is_email
import re

def sql_error():
    while True:
#  starting server and declaering port 5000 as connections for signup server
        host = ""
        port = 5000
        server_socket = socket.socket()  # get instance
        # The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen at once, set to 1 to stop overloading connection due to poor wifi and waiting for multiproceesing and threading to be added(todo)
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
            # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        data = "Error"
        conn.send(data.encode())
        conn.close()  # close the connection
# checks if sql is connectable 
try:
    db = mysql.connector.connect(
    host="54.36.106.157",
    user="mrooodpd_ben",
    passwd="Kaloo2015",
    database="mrooodpd_users"
    )
    cursor = db.cursor()        
    cursor.execute("SELECT VERSION()")
    results = cursor.fetchone()
    # Check if anything at all is returned
    if results:
        print(True)
    else:
        print(False)              
except mysql.connector.Error:
    print("ERROR IN CONNECTION")
    sql_error()
#  main server loop and checks if email is real and submits to database else returns a message to the clients side
def server_program():
    while True:
        server_program.userinfo=[]
        # get the hostname
        host = ""
        port = 5000  # initiate port no above 1024
        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        i=0
        while i<=3:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                    break
            username = data
            if i >=1:
                server_program.userinfo.append(username)
            if i <=2:
                data = "s"
                conn.send(data.encode())
            i=i+1
        email = server_program.userinfo[0]
        if(re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None):
            mydb = mysql.connector.connect(
                host="54.36.106.157",
                user="mrooodpd_ben",
                passwd="Kaloo2015",
                database="mrooodpd_users"
            )

            mycursor = mydb.cursor()

            email=server_program.userinfo[0]
            password=server_program.userinfo[1]
            Username=server_program.userinfo[2]

            mycursor = mydb.cursor()
            sql = "SELECT Username FROM Users WHERE Username = %s"
            adr = (Username,)
            mycursor.execute(sql, adr)
            UserRet = mycursor.fetchall()
            print(Username)
            check= "[('"
            check = check + Username
            check = check + "',)]"
            check=str(check)
            print(check)
            print(UserRet)
            if not not UserRet:
                data="User exist"
                conn.send(data.encode())
                print("User exist")
                print(UserRet)
                conn.close()
                break
            else:
                print("done")
            
            password = bytes(password, encoding= 'utf-8')
            email = bytes(email, encoding= 'utf-8')

            start = time.time()
            salt = b"$2b$16$in1GeZyEw5nudl/YzZYmLO"
            password = bcrypt.hashpw(password, salt)
            email= bcrypt.hashpw(email, salt)
            end = time.time()
            print("time:", end - start)
            print("salt:", salt.decode('utf-8'))
            print("hash: ")
            sql = "INSERT INTO Users (Username, Email, Password) VALUES (%s, %s, %s)"
            val = (Username, email, password)
            mycursor.execute(sql, val)
            
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            del server_program.userinfo[:]
            print("Closed")
            data = "Close"
            conn.send(data.encode())
        else:
            data = "email incorrect"
            conn.send(data.encode())
            print("email incorrect")

while True:
    server_program()





if __name__ == '__main__':
    server_program()
