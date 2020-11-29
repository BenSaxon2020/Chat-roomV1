import mysql.connector
import socket
import hashlib
import bcrypt
import time
from pyisemail import is_email
# sends error message if sql server is down
def sql_error():
    while True:
        # starting server and declaering port 1232 as connections for login server
        host = ""
        port = 1232 
        server_socket = socket.socket()  # get instance
        # The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen at once, set to 1 to stop overloading connection due to poor wifi and waiting for multiproceesing and threading to be added(todo)
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
            # receive data won't accept data packet greater than 1024 bytes
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




# main server loop and checks if login info is correct by comparing salted hashes to database else returns a message to the clients side
def server_program():
    while True:
        server_program.userinfo=[]
        # get the hostname
        host = ""
        port = 1232  # initiate port no above 1024
        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        i=0
        while i<=3:
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

        email=server_program.userinfo[0]
        Password=server_program.userinfo[1]
        Username=server_program.userinfo[2]             
        mydb = mysql.connector.connect(
        host="54.36.106.157",
        user="mrooodpd_ben",
        passwd="Kaloo2015",
        database="mrooodpd_users"
        )

        mycursor = mydb.cursor()
        sql = "SELECT Username FROM Users WHERE Username = %s"
        adr = (Username,)
        mycursor.execute(sql, adr)
        UserRet = mycursor.fetchall()
        print(Username)
        print(UserRet)
        UserRet = str(UserRet)
        UserRet_l=len(UserRet)
        UserRet_s=slice(3, UserRet_l-4, 1)
        UserRet=UserRet[UserRet_s]


        # print(UserRet)
        if Username != UserRet:
            print("fail1")
            print(Username)
            print(Password)
            print(email)
            data = "email incorrect"
            conn.send(data.encode()) 
            conn.close()
        else:
            print("sucsess")
            sql = "SELECT Email FROM Users WHERE Username = %s"
            adr = (Username,)
            mycursor.execute(sql, adr)
            EmRet = mycursor.fetchall()
            sql = "SELECT Password FROM Users WHERE Username = %s"
            adr = (Username,)
            mycursor.execute(sql, adr)
            PassRet = mycursor.fetchall()

            EmRet = str(EmRet)
            EmRet_l=len(EmRet)
            EmRet_l=EmRet_l-4
            print(EmRet_l)
            EmRet_s=slice(3, EmRet_l, 1)
            EmRet=EmRet[EmRet_s]

            PassRet = str(PassRet)
            PassRet_l=len(PassRet)
            PassRet_s=slice(3, PassRet_l-4, 1)
            PassRet=PassRet[PassRet_s]

            EmRet=EmRet.encode()
            PassRet=PassRet.encode()
            email=email.encode()
            Password=Password.encode()
            salt = b"$2b$16$in1GeZyEw5nudl/YzZYmLO"
            Password= bcrypt.hashpw(Password, salt)
            email= bcrypt.hashpw(email, salt)
            if UserRet == Username and PassRet == Password and EmRet == email:
                print(email, Password)
                data = "login"
                conn.send(data.encode()) 
                conn.close()
                print("sucsess")
            else: 
                print("fail")
                data = "email incorrect"
                conn.send(data.encode())    
                conn.close()
                print(data)
while True:
    server_program()





if __name__ == '__main__':
    server_program()
