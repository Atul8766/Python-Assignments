import psycopg2
from psycopg2 import sql
import os
from prettytable import from_db_cursor
os.system("clear")
print("                ######################  Welcome To Digital Phone Book   ##########################")
print("\n1.Login")
print("\n2.Registration")
print("\n------------------------------------")
print("\nPress 1 For Login")
print("Press 2 For Registration")
check = int(input("\n\nEnter Your Choice : "))
cur = None
conn = None
def prompt_username(con):
    cur = con.cursor()
    while True:
        os.system("clear")
        print("                         ---------------------------------- Welcome To Registration  ----------------------------------")
        username = input("\n\nEnter User Name : ")
        cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_roles WHERE rolname = %s", [username])
        n, = cur.fetchone()
        if n == 0:
            return username
        print("033[1;31;20m User already exists.")

if check==1:
        os.system("clear")
        print("                         ---------------------------------- Welcome To Login ----------------------------------")
        username1 = str(input("\n\nEnter Your Username : "))
        pwd1 = str(input("\nEnter Your Password : ")) 
try:
            conn = psycopg2.connect(
            host = 'localhost',
            dbname = username1,
            user = username1,
            password = pwd1,
            port = 5432)
            cur = conn.cursor()
            print("\n\n\033[1;32;15m[User",username1,"logged in]")
            time = cur.execute('SELECT TIMEOFDAY()')
            time = cur.fetchone()
            print(time)
            print('-------------------------------------------')
            print("What do you want to do?")
            print("[view -a] to view all saved contacts")
            print("[view]    to view a specific contact")
            print("[add]     to add a new contact")
            print("[del]     to delete a contact")
            print("[update]  to update an existing contact")
            print("[exit]    to exit the program")
            create_script = '''Create table if not exists contact_phone_book(
                                ContactId int primary key,
                                FirstName text,
                                LastName text,
                                Email text,
                                PhoneNumber numeric)
            '''

            cur.execute(create_script)
            
            take = str.lower(input("\n\nEnter Your input : "))
            if take == 'view -a':
                os.system("clear")
                print("                         ---------------------------------- Contact List ----------------------------------\n\n")
                cur.execute('SELECT * FROM contact_phone_book')
                x = from_db_cursor(cur)
                print(x)
                print("\n\n\n")
            if take == 'view':
                name = str(input("\n\nEnter contact first name : "))
                search_script = "SELECT * FROM contact_phone_book where firstname=%s"
                print("\n")
                
                search_record = (name,)
                cur.execute(search_script,search_record)
                for record in cur.fetchall():
                    print("\n\033[1;32;15m[Found Succesfully]\n")
                    print(record)
                    break
                else:
                    print("\033[1;31;20m Not Found")
            if take == 'add':
                os.system("clear")
                print("                         ---------------------------------- Add Contact ----------------------------------\n\n")
                cid = int(input("\nEnter ContactId : "))
                firstname = str(input("\nEnter FirstName : "))
                Lastname = str(input("\nEnter LastName : "))
                email = str(input("\nEnter Email : "))
                Phn = int(input("\nEnter PhoneNumber : "))
                insert_script='insert into contact_phone_book (ContactId,FirstName,LastName,Email,PhoneNumber) Values(%s,%s,%s,%s,%s)'
                insert_values=[(cid,firstname,Lastname,email,Phn)]
                print("\n\n\033[1;32;15m[Contact Added Succesfully]")
                print("\n\n\n")
                for record in insert_values:
                    cur.execute(insert_script,record) 
            if take == 'del':
                name = str(input("Enter First Name : "))
                delete_script = 'Delete from contact_phone_book where firstname = %s'
                delete_record = (name,)
                cur.execute(delete_script,delete_record)
                print("\n\n\033[1;31;20m[Contact Deleted Succesfully]\n\n\n")
            if take== 'update':
                firstname1 = str(input("Enter FirstName of that contact which you want to update : "))
                cid = int(input("\nEnter ContactId : "))
                firstname = str(input("\nEnter FirstName : "))
                Lastname = str(input("\nEnter LastName : "))
                email = str(input("\nEnter Email : "))
                Phn = int(input("\nEnter PhoneNumber : "))
                upadate_script = 'Update contact_phone_book set contactid=%s,firstname=%s,lastname=%s,email=%s,phonenumber=%s where firstname=%s'
                update_record = (cid,firstname,Lastname,email,Phn,firstname1)
                cur.execute(upadate_script,update_record)
                print("\033[4;37;15m[Contact Updated Succesfully]")
            if take=='exit':
                print("\nThanks For Using Our Application\n")
                exit(0)
            conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close
    if conn is not None:
        conn.close()

if check==2:
    try:
        conn = psycopg2.connect(
        host = 'localhost',
        dbname = 'postgres',
        user = 'postgres',
        password = 'root',
        port = 5432)

        username = prompt_username(conn)
        password = input(f"\nEnter Password for {username} : ")
        query = sql.SQL("CREATE ROLE {0} LOGIN PASSWORD {1}").format(
                    sql.Identifier(username),
                    sql.Literal(password),
                )
        cur = conn.cursor()
        cur.execute(query.as_string(conn))
        cur.execute("COMMIT")
        query = sql.SQL("CREATE DATABASE {0} WITH OWNER {0} ENCODING='UTF8' LC_COLLATE='en_IN' LC_CTYPE='en_IN'").format(
            sql.Identifier(username)
        )
        cur.execute(query.as_string(conn))
        print("\n\n\033[1;32;15m[Account Created Succesfully Go To Login Page]\n\n")
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
                cur.close()
        if conn is not None:
            conn.close()
