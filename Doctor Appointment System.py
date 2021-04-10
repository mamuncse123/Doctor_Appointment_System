import mysql.connector
global active_mail
global active_username
global log_in
def database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#"
    )
    database="no"
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for i in mycursor:
        if i[0]=="doctors_appointments":
            database="yes"
            break
        else:
            pass
    if database == "no":
        create_database()
    else:
        pass
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE doctors_appointments")
def table(t_n):
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="mysql123#",
            database="doctors_appointments",
        )
    table="no"
    check_table=t_n
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        if i[0] == check_table:
            table = "yes"
            break
        else:
            pass
    if table == "no":
        create_table(check_table)
def create_table(table):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    if table =="medical_college":
        mycursor.execute("CREATE TABLE medical_college (name varchar(150) NOT NULL,acronym varChar(10),location varchar(150),website varchar(150),PRIMARY KEY (acronym))")
    elif table=="admin":
        mycursor.execute(
            "CREATE TABLE admin (name varchar(150) NOT NULL,username varChar(30),mail varChar(100) NOT NULL,password varchar(100) NOT NULL,seq_key varchar(100)  NOT NULL ,status varChar(10), role varChar(10),PRIMARY KEY(mail))")
    elif table=="patients":
        mycursor.execute(
            "CREATE TABLE patients (name varchar(150) NOT NULL,username varChar(40) NOT NULL,age int NOT NULL, mobile varChar(30),address varChar(200),blood_group varChar(10),mail varChar(100) NOT NULL,password varchar(100),seq_key varchar(100) NOT NULL,PRIMARY KEY(mail))")
    elif table=="messages":
        mycursor.execute(
            "CREATE TABLE messages (name varchar(150) NOT NULL,mail varChar(100) NOT NULL,comment varchar(255) NOT NULL) ")
    elif table=="doctors":
        mycursor.execute(
            "CREATE TABLE doctors (name varchar(150) NOT NULL,username varChar(20) NOT NULL,address varChar(200), mobile varChar(30),mail varChar(100) NOT NULL,qualifications varChar(200),fee varChar(10),password varchar(100) NOT NULL,seq_key varchar(100) NOT NULL,status varChar(10),PRIMARY KEY(mail))")
    elif table == "appointments":
        mycursor.execute(
            "CREATE TABLE appointments (doctor_username varChar(20) NOT NULL,patient_username varChar(20) NOT NULL)")
    elif table == "our_mission":
        mycursor.execute(
            "CREATE TABLE our_mission (mission varChar(255))")
    elif table == "team":
        mycursor.execute(
            "CREATE TABLE team (name varChar(150) NOT NULL,mobile varChar(30),mail varChar(100))")
    elif table == "cell":
        mycursor.execute(
            "CREATE TABLE cell (mobile varChar(30))")
def admin_create_account():
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    name = input("Enter Full Name :  ")
    while True:
        if len(name) >=2:
            break
        else:
            name = input("Enter Full Name :  ")
    username = input("Enter username (length (8-30)) : ")
    while True:
        u_n = check_username(username)
        if len(username) >= 5 and len(username) <= 40 and u_n == 0:
            break
        else:
            username = input("Enter username (length (8-30)) : ")
    mail = input("Enter Mail (Length (8-100) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il == 0:
            break
        else:
            if ma_il==1:
                print("Already have an account!")
            else:
                print("Please maintain required!")
            mail = input("Enter Mail (Length (8-100) ) : ")
    password = input("Enter Password (length (5-100)):  ")
    if len(password) >= 5 and len(password) <= 100:
        pass
    else:
        while True:
            password = input("Wrong ! Enter Password (length (5-100)):  ")
            if len(password) >=5 and len(password) <= 100:
                break
    seq_key = input("Enter Security Key :  ")
    while True:
        if len(seq_key) >= 3:
            break
        else:
            seq_key = input("Enter Security Key :  ")
    status = "pending"
    role = "parent"
    query = "SELECT * from admin"
    mycursor.execute(query)
    result = mycursor.fetchall()
    if result:
        status = "pending"
        role = "child"
    else:
        status = "approved"
        role = "parent"
    query = "INSERT INTO admin (name,username,mail,password,seq_key,status,role)VALUES(%s,%s,%s,%s,%s,%s,%s)"
    s = (name,username,mail,password,seq_key,status,role)
    mycursor.execute(query, s)
    mydb.commit()
    print("              Create Successfully !                ")
def patient_create_account():
    name = input("Enter Full Name :  ")
    while True:
        if len(name) > 3:
            break
        else:
            name = input("Enter Full Name :  ")
    patient_username = input("Enter username (length (8-30)) : ")
    while True:
        u_n = check_username(patient_username)
        if len(patient_username) >= 5 and len(patient_username) <= 40 and u_n == 0:
            break
        else:
            patient_username = input("Enter username (length (8-30)) : ")
    while True:
        try:
            age = int(input("Enter Age : "))
            break
        except:
            print("Wrong!")
    mobile = input("Enter Mobile Number : ")
    address = input("Enter Address : ")
    blood_group = input("Enter blood group : ")
    mail = input("Enter Mail (Length (8-100) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il == 0:
            break
        else:
            if ma_il == 1:
                print("Already have an account!")
            else:
                print("Please maintain required!")
            mail = input("Enter Mail (Length (8-100) ) : ")
    password = input("Enter Password (length (5-100)):  ")
    while True:
        if len(password) >= 5 and len(password) <= 100:
            break
        else:
            password = input("Wrong ! Enter Password (length (5-100)):  ")
    seq_key = input("Enter Security Key :  ")
    while True:
        if len(seq_key) >= 3:
            break
        else:
            seq_key = input("Enter Security Key :  ")

    # Insert Data
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO patients (name,username,age,mobile,address,blood_group,mail,password,seq_key )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    s = (name,patient_username,age,mobile,address,blood_group,mail,password,seq_key )
    mycursor.execute(query, s)
    mydb.commit()
    print("                  Create Successfully !                 ")
def doctor_create_account():
    name = input("Enter Full Name :  ")
    while True:
        if len(name) > 3:
            break
        else:
            name = input("Enter Full Name :  ")
    doctor_username = input("Enter username (length (8-30)) : ")
    while True:
        u_n = check_username(doctor_username)
        if len(doctor_username) >= 5 and len(doctor_username) <= 40 and u_n == 0:
            break
        else:
            doctor_username = input("Enter username (length (8-30)) : ")
    qualification=input("Enter Qualification : ")
    while True:
        if len(qualification) >= 2 and len(qualification) <= 200 :
            break
        else:
            qualification=input("Enter Qualification : ")
    mobile = input("Enter Mobile Number : ")
    address = input("Enter Address : ")
    while True:
        try:
            fee = int(input("Enter Fee : "))
            break
        except:
            print("Wrong!")
    mail = input("Enter Mail (Length (8-100) ) : ")
    while True:
        ma_il = check_mail(mail)
        if len(mail) >= 8 and len(mail) <= 100 and ma_il == 0:
            break
        else:
            if ma_il == 1:
                print("Already have an account!")
            else:
                print("Please maintain required!")
            mail = input("Enter Mail (Length (8-100) ) : ")
    password = input("Enter Password (length (5-100)):  ")
    while True:
        if len(password) >= 5 and len(password) <= 100:
            break
        else:
            password = input("Wrong ! Enter Password (length (5-100)):  ")
    seq_key = input("Enter Security Key :  ")
    while True:
        if len(seq_key) >= 3:
            break
        else:
            seq_key = input("Enter Security Key :  ")
    status = "pending"
    # Insert Data
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    query = "INSERT INTO doctors (name,username,address,mobile,mail,qualifications,fee,password,seq_key,status )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    s = (name, doctor_username,address, mobile,  mail,qualification,fee, password, seq_key,status)
    mycursor.execute(query, s)
    mydb.commit()
    print("                  Create Successfully !                 ")
def check_username(username):
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    count = 0
    edit_query = ("SELECT mail FROM admin WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == username:
            count += 1
            return count
    edit_query = ("SELECT username FROM patients WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == username:
            count += 1
            return count
    edit_query = ("SELECT username FROM doctors WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == username:
            count += 1
            return count
    return count
def check_mail(m_ail):
    global  active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    count=0
    edit_query=("SELECT mail FROM admin WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result =mycursor.fetchall()
    for db in result:
        if db[0]==m_ail:
            count+=1
            return count
    edit_query=("SELECT mail FROM patients WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0]==m_ail:
            count += 1
            return count
    edit_query = ("SELECT mail FROM doctors WHERE mail!=%s")
    edit = (active_mail,)
    mycursor.execute(edit_query, edit)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == m_ail:
            count += 1
            return count
    return count
def login(input_mail,input_pass):
    global log_in
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT mail,password,username,name FROM patients")
    for i in mycursor:
        if i[0] == input_mail :
            if i[1]==input_pass:
                active_mail = input_mail
                active_username=i[2]
                log_in = True
                print(f"Welcome Back {i[3]}!")
                patient()
            else:
                print("Wrong Password!")
                home()

        else:
            pass
    tcursor = mydb.cursor()
    tcursor.execute("SELECT mail,password,username,status,name FROM doctors")
    for i in tcursor:
        if i[0] == input_mail  :
            if i[1] == input_pass:
                if i[3]=="approved":
                    active_mail = input_mail
                    active_username = i[2]
                    log_in = True
                    print(f"Welcome Back {i[4]}!")
                    doctor()
                else:
                    print("This account haven't approved by admin.")
                    home()
            else:
                print("Wrong Password!")
                home()
        else:
            pass
    mycursor.execute("SELECT mail,password,status,name FROM admin")
    for i in mycursor:
        if i[0] == input_mail:
            if i[1] == input_pass:
                if i[2] == "approved":
                    active_mail = input_mail
                    active_username = ""
                    log_in = True
                    print(f"Welcome Back {i[3]}!")
                    admin()
                else:
                    print("This account haven't approved by admin.")
                    home()
            else:
                print("Wrong Password!")
                home()
        else:
            pass
    if log_in!=True:
        print("No account in this mail !")
def patient():
    global log_in
    global active_mail
    global active_username
    log_in=True
    e_name = ""
    e_username=""
    e_age=""
    e_mobile=""
    e_address=""
    e_blood=""
    e_mail = ""
    e_seq_key = ""
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    while True:
        ps = input("1. Profile\n2. Profile Edit\n3. View\n4. Appointment List\n5. Book Appointment\n6. Doctor Search\n7. Change Password\n8. Delete My Account\n9. Logout\n10. About Us\n11. Contact Us\n")
        if ps=='1':
            query = ("SELECT * from patients WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("Username : ", row[1])
                print("Age : ", row[2])
                print("Mobile : ",row[3])
                print("Address : ",row[4])
                print("Blood Group : ",row[5])
                print("Mail : ", row[6])
                print("Password : ", row[7])
                print("Security Key : ", row[8])
        elif ps=='2':
            query = ("SELECT * from patients WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 3:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name = row[0]
                print("Username : ", row[1])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    while True:
                        e_username = input("Enter username (length (8-30)) : ")
                        u_n = check_username(e_username)
                        if len(e_username) >= 5 and len(e_username) <= 40 and u_n == 0:
                            break
                        else:
                            e_username = input("Enter username (length (8-30)) : ")
                else:
                    e_username=row[1]
                print("Age : ", row[2])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    while True:
                        try:
                            e_age = int(input("Enter Age : "))
                            break
                        except:
                            print("Wrong!")
                else:
                    e_age=row[2]
                print("Mobile : ", row[3])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_mobile = input("Enter Mobile Number : ")
                else:
                    e_mobile=row[3]
                print("Address : ", row[4])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_address = input("Enter Address : ")
                else:
                    e_address = row[4]
                print("Blood Group : ", row[5])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_blood = input("Enter Blood Group : ")
                else:
                    e_blood = row[5]
                print("Mail : ", row[6])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il == 0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail = row[6]
                print("Security Key : ", row[8])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_seq_key = input("Enter Security Key ?")
                    if e_seq_key == "":
                        while True:
                            e_seq_key = input("Enter Security Key ?")
                            if e_seq_key == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_seq_key = row[8]
            edit_query = (
                "UPDATE patients SET name=%s ,username=%s,age=%s,mobile=%s,address=%s,blood_group=%s,mail=%s,seq_key=%s WHERE mail=%s")
            edit = (e_name, e_username,e_age,e_mobile,e_address,e_blood,e_mail, e_seq_key, active_mail,)
            mycursor.execute(edit_query, edit)
            mydb.commit()
            active_mail = e_mail
            active_username = e_username
            print("Update Complete!")
        elif ps=='3':
            view()
        elif ps=='4':
            query = ("SELECT doctor_username from appointments WHERE patient_username=%s")
            s = (active_username,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result:
                l=[]
                for username in result:
                    if username[0] not in l:
                        l.append(username[0])
                query2 = ("SELECT name,username,address,mobile,mail,qualifications from doctors")
                mycursor.execute(query2)
                result2 = mycursor.fetchall()
                count=1
                for row in result2:
                    if row[1] in l:
                        print(f"{count}. Doctor Name : ", row[0])
                        print(" Address : ", row[2])
                        print(" Mobile : ", row[3])
                        print(" Mail : ", row[4])
                        print(" Qualifications : ", row[5])
                        count+=1
        elif ps=='5':
            d_username=input("Enter doctor user name : ")
            query = ("SELECT name,username,address,mobile,mail,qualifications,fee from doctors where username=%s")
            s = (d_username,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result:
                for row in result:
                    print("Doctor Name : ", row[0])
                    print("Address : ", row[2])
                    print("Mobile : ", row[3])
                    print("Mail : ", row[4])
                    print("Qualifications : ", row[5])
                    print("Fee : ",row[6])
                book=input("Want to book ?\n1.yes\n2.no\n")
                if book=='1':
                    query = "INSERT INTO appointments ( doctor_username,patient_username )VALUES(%s,%s)"
                    s = (d_username,active_username)
                    mycursor.execute(query, s)
                    mydb.commit()
                    print("                  Appointment Successfully !                 ")
        elif ps=='6':
            option=input("1. View All \n2. Search\n")
            if option=='1':
                query = (
                    "SELECT name,username,address,mobile,mail,qualifications,fee from doctors")
                mycursor.execute(query,)
                result = mycursor.fetchall()
                if result:
                    for row in result:
                        print()
                        print("Doctor Name : ", row[0])
                        print("Address : ", row[2])
                        print("Mobile : ", row[3])
                        print("Mail : ", row[4])
                        print("Qualifications : ", row[5])
                        print("Fee : ", row[6])
            else:
                d_username = input("Enter doctor user name or name : ")
                d_name=d_username
                query = ("SELECT name,username,address,mobile,mail,qualifications,fee from doctors where username=%s or name=%s")
                s = (d_username,d_name,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    for row in result:
                        print()
                        print("Doctor Name : ", row[0])
                        print("Address : ", row[2])
                        print("Mobile : ", row[3])
                        print("Mail : ", row[4])
                        print("Qualifications : ", row[5])
                        print("Fee : ", row[6])
                else:
                    print("Not Found!")
        elif ps=='7':
            print()
            forget_password()
        elif ps=='8':
            sure=input("Delete?\n1.yes\n2.no\n")
            if sure =='1':
                edit_query = (
                    "DELETE FROM patients WHERE mail=%s")
                edit = (active_mail,)
                mycursor.execute(edit_query, edit)
                mydb.commit()
                print("Account Delete Complete!")
                active_mail = ""
                active_username = ""
                log_in = False
                home()
            else:
                patient()
        elif ps=='9':
            active_mail = ""
            active_username = ""
            log_in = False
            home()
        elif ps == '10':
            about_us()
            print()
        elif ps == '11':
            contact_us()
            print()
def doctor():
    global log_in
    global active_mail
    global active_username
    log_in = True
    e_name = ""
    e_username = ""
    e_age = ""
    e_mobile = ""
    e_address = ""
    e_blood = ""
    e_mail = ""
    e_seq_key = ""
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    while True:
        ps = input(
            "1. Profile\n2. Profile Edit\n3. View\n4. Appointment List\n5. Book Appointment\n6. Doctor Search\n7. Change Password\n8. Delete My Account\n9. Logout\n10. About us\n11. Contact us\n")
        if ps=='1':
            query = ("SELECT * from doctors WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("Username : ", row[1])
                print("Address : ", row[2])
                print("Mobile : ", row[3])
                print("Mail : ", row[4])
                print("Qualifications : ", row[5])
                print("Fee : ",row[6])
                print("Password : ", row[7])
                print("Security Key : ", row[8])
                print("Status : ",row[9])
        elif ps=='2':
            query = ("SELECT * from doctors WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 3:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name=row[0]
                print("Username : ", row[1])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    while True:
                        e_username = input("Enter username (length (8-30)) : ")
                        u_n = check_username(e_username)
                        if len(e_username) >= 5 and len(e_username) <= 40 and u_n == 0:
                            break
                        else:
                            e_username = input("Enter username (length (8-30)) : ")
                else:
                    e_username=row[1]
                print("Address : ", row[2])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_address = input("Enter Address : ")
                else:
                    e_address=row[2]
                print("Mobile : ", row[3])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_mobile=input("Enter Mobile : ")
                else:
                    e_mobile=row[3]
                print("Mail : ", row[4])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il == 0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail=row[4]
                print("Qualifications : ", row[5])
                a = input("1. Edit\n2. Skip")
                e_qualification=""
                if a == '1':
                    e_qualification = input("Enter Qualification : ")
                    while True:
                        if len(e_qualification) >= 2 and len(e_qualification) <= 200:
                            break
                        else:
                            e_qualification = input("Enter Qualification : ")
                else:
                    e_qualification=row[5]
                print("Fee : ", row[6])
                e_fee=0
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    while True:
                        try:
                            e_fee = int(input("Enter Fee : "))
                            break
                        except:
                            print("Wrong!")
                else:
                    e_fee=row[6]
                print("Security Key : ", row[8])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_seq_key = input("Enter Security Key :  ")
                    while True:
                        if len(e_seq_key) >= 3:
                            break
                        else:
                            e_seq_key = input("Enter Security Key :  ")
                else:
                    e_seq_key=row[8]
                edit_query = (
                    "UPDATE doctors SET name=%s ,username=%s,address=%s,mobile=%s,mail=%s,qualifications=%s,fee=%s,seq_key=%s WHERE mail=%s")
                edit = (e_name, e_username, e_address,  e_mobile, e_mail,e_qualification,e_fee, e_seq_key, active_mail,)
                mycursor.execute(edit_query, edit)
                mydb.commit()
                active_mail = e_mail
                active_username = e_username
                print("Update Complete!")
        elif ps=='3':
            view()
        elif ps=='4':
            Input=input("1. View Doctor\n2. View Patient")
            if Input=='1':
                query = ("SELECT doctor_username from appointments WHERE patient_username=%s")
                s = (active_username,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    l = []
                    for username in result:
                        if username[0] not in l:
                            l.append(username[0])
                    query2 = ("SELECT name,username,address,mobile,mail,qualifications from doctors")
                    mycursor.execute(query2)
                    result2 = mycursor.fetchall()
                    count = 1
                    for row in result2:
                        if row[1] in l:
                            print(f"{count}. Doctor Name : ", row[0])
                            print(" Address : ", row[2])
                            print(" Mobile : ", row[3])
                            print(" Mail : ", row[4])
                            print(" Qualifications : ", row[5])
                            count += 1
            elif Input=='2':
                query = ("SELECT patient_username from appointments WHERE doctor_username=%s")
                s = (active_username,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    l = []
                    for username in result:
                        if username[0] not in l:
                            l.append(username[0])
                    query2 = ("SELECT name,username,age,mobile,address,blood_group,mail from patients")
                    mycursor.execute(query2)
                    result2 = mycursor.fetchall()
                    count = 1
                    for row in result2:
                        if row[1] in l:
                            print(f"{count}. Patient Name : ", row[0])
                            print(" Patient Username : ",row[1])
                            print(" Patient Age : ",row[2])
                            print(" Mobile : ", row[3])
                            print(" Address : ", row[4])
                            print(" Patient Blood group : ",row[5])
                            print(" Mail : ", row[6])
                            count += 1
        elif ps=='5':
            d_username = input("Enter doctor user name : ")
            query = ("SELECT name,username,address,mobile,mail,qualifications,fee from doctors where username=%s")
            s = (d_username,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            if result:
                for row in result:
                    print("Doctor Name : ", row[0])
                    print("Address : ", row[2])
                    print("Mobile : ", row[3])
                    print("Mail : ", row[4])
                    print("Qualifications : ", row[5])
                    print("Fee : ", row[6])
                book = input("Want to book ?\n1.yes\n2.no\n")
                if book == '1':
                    query = "INSERT INTO appointments ( doctor_username,patient_username )VALUES(%s,%s)"
                    s = (d_username, active_username)
                    mycursor.execute(query, s)
                    mydb.commit()
                    print("                  Appointment Successfully !                 ")
        elif ps=='6':
            option = input("1. View All \n2. Search\n")
            if option == '1':
                query = (
                    "SELECT name,username,address,mobile,mail,qualifications,fee from doctors")
                mycursor.execute(query, )
                result = mycursor.fetchall()
                if result:
                    for row in result:
                        print()
                        print("Doctor Name : ", row[0])
                        print("Address : ", row[2])
                        print("Mobile : ", row[3])
                        print("Mail : ", row[4])
                        print("Qualifications : ", row[5])
                        print("Fee : ", row[6])
            else:
                d_username = input("Enter doctor user name or name : ")
                d_name = d_username
                query = (
                    "SELECT name,username,address,mobile,mail,qualifications,fee from doctors where username=%s or name=%s")
                s = (d_username, d_name,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    for row in result:
                        print()
                        print("Doctor Name : ", row[0])
                        print("Address : ", row[2])
                        print("Mobile : ", row[3])
                        print("Mail : ", row[4])
                        print("Qualifications : ", row[5])
                        print("Fee : ", row[6])
                else:
                    print("Not Found!")
        elif ps=='7':
            print()
            forget_password()
        elif ps=='8':
            sure = input("Delete?\n1.yes\n2.no\n")
            if sure == '1':
                edit_query = (
                    "DELETE FROM doctors WHERE mail=%s")
                edit = (active_mail,)
                mycursor.execute(edit_query, edit)
                mydb.commit()
                print("Account Delete Complete!")
                active_mail = ""
                active_username = ""
                log_in = False
                home()
            else:
                doctor()
        elif ps=='9':
            active_mail = ""
            active_username = ""
            log_in = False
            home()
        elif ps == '10':
            about_us()
            print()
        elif ps == '11':
            contact_us()
            print()
def admin():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    global active_mail
    global active_username
    global log_in
    e_name = ""
    e_mail = ""
    e_seq_key = ""
    mycursor = mydb.cursor()
    while True:
        in_put = input(
            "1. Profile\n2. Edit Profile\n3. View\n4. Approve Account\n5. Delete Account\n6. Change Password\n7. Medical College\n8. Logout\n9. About Us\n10. Messages\n11. Contact Us\n")
        if in_put == '1':
            query = ("SELECT * from admin WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                print("Mail : ", row[1])
                print("Password : ",row[2])
                print("Security Key : ", row[3])
        elif in_put == "2":
            query = ("SELECT name,mail,seq_key from admin WHERE mail=%s")
            s = (active_mail,)
            mycursor.execute(query, s)
            result = mycursor.fetchall()
            for row in result:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_name = input("Enter Full Name :  ")
                    while True:
                        if len(e_name) > 3:
                            break
                        else:
                            e_name = input("Enter Full Name :  ")
                else:
                    e_name = row[0]
                print("Mail : ", row[1])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_mail = input("Enter Mail (Length (11-10) ) : ")
                    while True:
                        ma_il = check_mail(e_mail)
                        if len(e_mail) >= 11 and len(e_mail) <= 100 and ma_il == 0:
                            break
                        else:
                            e_mail = input("Enter Mail (Length (11-100) ) : ")
                else:
                    e_mail = row[1]
                print("Security Key : ", row[2])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    e_seq_key = input("Enter Security Key ?")
                    if e_seq_key == "":
                        while True:
                            e_seq_key = input("Enter Security Key ?")
                            if e_seq_key == "":
                                continue
                            else:
                                break
                    else:
                        pass
                else:
                    e_seq_key = row[2]
            edit_query = (
                "UPDATE admin SET name=%s ,mail=%s,seq_key=%s WHERE mail=%s")
            edit = (e_name, e_mail, e_seq_key, active_mail,)
            mycursor.execute(edit_query, edit)
            mydb.commit()
            active_mail = e_mail
            active_username = ""
            print("Update Complete!")
        elif in_put=='3':
            print()
            view()
        elif in_put == '4':
            x = input("1. Admin\n2. Doctor\n")
            if x == '1':
                a = input("Enter mail or username: ")
                query = ("SELECT mail,username from admin WHERE mail=%sor username=%s")
                s = (a,a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                status = "approved"
                if result:
                    print("Account Found!")
                    edit_query = (
                        "UPDATE admin SET status=%s WHERE mail=%s or username=%s")
                    edit = (status, a,a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Approved Complete!")
                else:
                    print("No Account Found!")
            elif x == '2':
                a = input("Enter mail or username : ")
                query = ("SELECT mail,username from doctors WHERE mail=%s or username=%s")
                s = (a, a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                status = "approved"
                if result:
                    print("Account Found!")
                    edit_query = (
                        "UPDATE doctors SET status=%s WHERE mail=%s or username = %s")
                    edit = (status, a, a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Approved Complete!")
                else:
                    print("No Account Found!")
        elif in_put == '5':
            x = input("1. Admin\n2. Doctor\n3. Patient\n")
            if x == '1':
                a = input("Enter mail : ")
                query = ("SELECT mail,role from admin WHERE mail=%s")
                s = (a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    for i in result:
                        if i[1] == "parent":
                            print("You haven't permission!")
                        else:
                            edit_query = (
                                "DELETE FROM admin WHERE mail=%s")
                            edit = (a,)
                            mycursor.execute(edit_query, edit)
                            mydb.commit()
                            print("Account Delete Complete!")
                else:
                    print("No Account Found!")
            elif x == '2':
                a = input("Enter mail or username : ")
                query = ("SELECT mail from doctors WHERE mail=%s or username=%s")
                s = (a, a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    edit_query = (
                        "DELETE FROM doctors WHERE mail=%s or username=%s")
                    edit = (a, a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Delete Complete!")
                else:
                    print("No Account Found!")
            elif x == '3':
                a = input("Enter mail or username : ")
                query = ("SELECT mail from patients WHERE mail=%s or username=%s")
                s = (a, a,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    print("Account Found!")
                    # Delete student account
                    edit_query = (
                        "DELETE FROM patients WHERE mail=%s or username=%s")
                    edit = (a, a,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    # get patients username
                    edit_query = (
                        "SELECT username FROM patients WHERE mail=%s or username=%s")
                    edit = (a, a,)
                    mycursor.execute(edit_query, edit)
                    result = mycursor.fetchall()
                    del_user=""
                    for i in result:
                        del_user = i[0]
                        break
                    # Delete course
                    edit_query = (
                        "DELETE FROM appointments WHERE patient_username=%s")
                    edit = (del_user,)
                    mycursor.execute(edit_query, edit)
                    mydb.commit()
                    print("Account Delete Complete!")
                else:
                    print("No Account Found!")
        elif in_put == '6':
            forget_password()
            print()
        elif in_put=='7':
            while True:
                m_c=input("1. Add\n2. Edit\n3. Delete\n4. View\n5. Search\n")
                if m_c=='1'or m_c=='2' or m_c=='3' or m_c=='4' or m_c=='5':
                    medical_college(m_c)
                else:
                    break
        elif in_put == '8':
            active_mail = ""
            active_username = ""
            log_in = False
            home()
        elif in_put == '9':
            e_mobile=""
            about_us()
            print()
            i=input("1. Add 2. Edit\n")
            if i=='1':
                j=input("1. Team 2. Mission\n")
                if j=='1':
                    name = input("Enter Full Name :  ")
                    while True:
                        if len(name) > 3:
                            break
                        else:
                            name = input("Enter Full Name :  ")
                    mobile = input("Enter Mobile : ")
                    mail = input("Enter Mail (Length (8-100) ) : ")
                    query = "INSERT INTO team (name,mobile,mail)VALUES(%s,%s,%s)"
                    s = (name, mobile,mail,)
                    mycursor.execute(query, s)
                    mydb.commit()
                    print("              Add Successfully !                ")
                elif j=='2':
                    m = input("Enter Mission :  ")
                    while True:
                        if len(m) > 2:
                            break
                        else:
                            m = input("Enter Mission :  ")
                    query = "INSERT INTO our_mission (mission)VALUES(%s)"
                    s = (m,)
                    mycursor.execute(query, s)
                    mydb.commit()
                    print("              Add Successfully !                ")
            elif i=='2':
                n_ame=input("Enter Team Member Name : ")
                query = mycursor.execute("SELECT * FROM team WHERE name='%s'")
                s = (n_ame,)
                mycursor.execute(query, s)
                result = mycursor.fetchall()
                if result:
                    for i in result:
                        print("Name : ",i[0])
                        a = input("1. Edit\n2. Skip")
                        if a == '1':
                            e_name = input("Enter Full Name :  ")
                            while True:
                                if len(e_name) > 3:
                                    break
                                else:
                                    e_name = input("Enter Full Name :  ")
                        else:
                            e_name=i[0]
                        print("Mobile : ", i[1])
                        a = input("1. Edit\n2. Skip")
                        if a == '1':
                            e_mobile = input("Enter Mobile :  ")
                        else:
                            e_mobile=i[1]
                        print("Mail : ", i[2])
                        a = input("1. Edit\n2. Skip")
                        if a == '1':
                            e_mail = input("Enter Mail (Length (11-10) ) : ")
                            while True:

                                if len(e_mail) >= 11 and len(e_mail) <= 100 :
                                    break
                                else:
                                    e_mail = input("Enter Mail (Length (11-100) ) : ")
                        else:
                            e_mail=i[2]
                        edit_query = (
                            "UPDATE team SET name=%s ,mobile=%s,mail=%s  WHERE name=%s")
                        edit = (e_name,e_mobile, e_mail,n_ame)
                        mycursor.execute(edit_query, edit)
                        mydb.commit()
                        print("Edit Complete!")
        elif in_put=='10':
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql123#",
                database="doctors_appointments",
            )
            mycursor = mydb.cursor()
            count = 0
            edit_query = ("SELECT * FROM messages")
            mycursor.execute(edit_query)
            result = mycursor.fetchall()
            if result:
                for db in result:
                    print("Name : ",db[0])
                    print("Mail : ",db[1])
                    print("Comment : ",db[2])
                print()
            else:
                print("No Messages!\n")
        elif in_put == '11':
            mycursor.execute("SELECT * FROM cell")
            result = mycursor.fetchall()
            print("Cell : ")
            count = 1
            for row in result:
                print(f"{count}. ", row[0])
                count += 1
            print()
            i = input("1. Add 2. Edit\n")
            if i == '1':
                add_cell = input("Enter Mobile/Telephone Number ) : ")
                while True:
                    if len(add_cell)>0:
                        break
                    else:
                        add_cell = input("Enter Mobile/Telephone Number  : ")
                query = "INSERT INTO cell(mobile)VALUES(%s)"
                s = (add_cell,)
                mycursor.execute(query, s)
                mydb.commit()
                print("              Add Successfully !                ")
            elif i=='2':
                e_cell=""
                c_ell = input("Enter Cell Number : ")
                query123= ("SELECT * FROM cell WHERE mobile=%s")
                s = (c_ell,)
                mycursor.execute(query123, s)
                result = mycursor.fetchall()

                if result:
                    for i in result:
                        print("Cell Number : ", i[0])
                        a = input("1. Edit\n2. Skip")
                        if a == '1':
                            e_cell = input("Enter Cell Name :  ")
                            while True:
                                if len(e_cell) > 0:
                                    break
                                else:
                                    e_cell = input("Enter Cell Name :  ")
                        else:
                            e_cell = i[0]
                        edit_query = (
                            "UPDATE cell SET  mobile=%s  WHERE mobile=%s")
                        edit = (e_cell,c_ell)
                        mycursor.execute(edit_query, edit)
                        mydb.commit()
                        print("Edit Complete!")
def medical_acronym(ac):
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    count = 0
    edit_query = ("SELECT acronym FROM medical_college")
    mycursor.execute(edit_query)
    result = mycursor.fetchall()
    for db in result:
        if db[0] == ac:
            count += 1
            return count
    return 0
def medical_college(m_c):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    if m_c=='1':#add
        state = int(0)
        name = input("Enter Full Name :  ")
        while True:
            if len(name) >= 2:
                break
            else:
                name = input("Enter Full Name :  ")
        ac = input("Enter Acronym :  ")
        while True:
            state=medical_acronym(ac)
            if len(ac) >= 2 and state ==0:
                break
            else:
                if state !=0:
                    print("Already have!")
                ac = input("Enter Acronym :  ")
        lc = input("Enter Location :  ")
        while True:
            if len(lc) >= 2:
                break
            else:
                lc = input("Enter Location :  ")
        website = input("Enter Website :  ")
        query = "INSERT INTO medical_college (name,acronym,location,website)VALUES(%s,%s,%s,%s)"
        s = (name,ac,lc,website)
        mycursor.execute(query, s)
        mydb.commit()
        print("              Add Successfully !                ")
    elif m_c=='2':#edit
        ac=""
        name=""
        lc=""
        website=""
        ac_search = input("Enter Acronym :  ")
        query = ("SELECT * from medical_college ")
        mycursor.execute(query)
        result = mycursor.fetchall()
        for row in result:
            if row[1]==ac_search:
                print("Name : ", row[0])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    name = input("Enter Full Name :  ")
                    while True:
                        if len(name) >= 2:
                            break
                        else:
                            name = input("Enter Full Name :  ")
                else:
                    name = row[0]
                print("Acronym : ", row[1])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    ac = input("Enter Acronym :  ")
                    while True:
                        state = medical_acronym(ac)
                        if len(ac) >= 2 and (state ==0 or ac==row[1]):
                            break
                        else:
                            if state != 0:
                                print("Already have!")
                            ac = input("Enter Acronym :  ")
                else:
                    ac=row[1]
                print("Location : ", row[2])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    lc = input("Enter Location :  ")
                    while True:
                        if len(lc) >= 2:
                            break
                        else:
                            lc = input("Enter Location :  ")
                else:
                    lc=row[2]
                print("Website : ", row[3])
                a = input("1. Edit\n2. Skip")
                if a == '1':
                    website = input("Enter Location :  ")
                else:
                    website=row[3]
                edit_query = (
                    "UPDATE medical_college SET name=%s,acronym=%s,location=%s,website=%s WHERE  acronym=%s")
                edit = (name,ac,lc,website,ac_search)
                mycursor.execute(edit_query, edit)
                mydb.commit()
                print("              Edit Successfully !                ")
    elif m_c=='3':#Delete
        ac = ""
        ac = input("Enter Acronym :  ")
        query = ("SELECT acronym from medical_college")
        mycursor.execute(query)
        result = mycursor.fetchall()
        for a_c in result:
            if a_c[0] == ac:
                edit_query = (
                    "DELETE FROM medical_college WHERE  acronym=%s")
                edit = (ac,)
                mycursor.execute(edit_query, edit)
                mydb.commit()
                print("Delete! ")
                admin()
        print("Not found!")
    elif m_c=='4':#View
        query = ("SELECT * from medical_college")
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result:
            for row in result:
                print("Name : ", row[0])
                print("Acronym : ", row[1])
                print("Location : ", row[2])
                print("Website : ", row[3])
                print()
        else:
            print("No Data!")
    elif m_c=='5':#Search
        ac = ""
        ac = input("Enter Acronym :  ")
        query = ("SELECT * from medical_college")
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result:
            for row in result:
                if row[1]==ac:
                    print("Name : ", row[0])
                    print("Acronym : ", row[1])
                    print("Location : ", row[2])
                    print("Website : ", row[3])
                    print()
                    admin()
            print("Not Found!")
        else:
            print("No Data!")
def create():
    print("""
        1. Patient
        2. Doctor
        3. Admin
        4. Back
        5. Exit
        """)
    cre = input()
    if cre=='1':
        patient_create_account()
        home()
    elif cre=='2':
        doctor_create_account()
        home()
    elif cre == '3':
        admin_create_account()
        home()
    elif cre == '4':
        home()
    elif cre=='5':
        exit()
def home():
    global active_mail
    global active_username
    global log_in
    active_mail = ""
    active_username = ""
    log_in = False
    database()
    table("admin")
    table("doctors")
    table("patients")
    table("medical_college")
    table("messages")
    table("appointments")
    table("our_mission")
    table("team")
    table("cell")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT mail FROM admin")
    re_su_lt = mycursor.fetchall()
    if re_su_lt:
        print("")
    else:
        print("Create Admin Account")
        admin_create_account()
    while True:
        print(""" 
          1. LOG IN
          2. Create Account
          3. Forget Password ?
          4. About us
          5. Contact us
          6. EXIT

          Enter Your Choose : 
        """)
        choice = input()
        if choice == "1":
            login_mail = input("Enter Mail : ")
            login_passwd = input("Enter Password : ")
            login(login_mail, login_passwd)
        elif choice == "2":
            create()
        elif choice == "3":
            forget_password()
        elif choice=='4':
            about_us()
        elif choice=='5':
            contact_us()
        elif choice == "6":
            exit()
        else:
            home()
def forget_password():
    global log_in
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    f_mail=""
    if log_in == False:
        f_mail=input("Enter Mail : ")
        opinion = check_mail(f_mail)
        if opinion==0:
            home()
    p_s_q=input("1. Password \n2. Security Key : \n")
    if p_s_q=="1":
        mycursor.execute("SELECT mail,password FROM patients")
        result = mycursor.fetchall()
        for i in result:
            if i[0] == active_mail or i[0]==f_mail:
                while True:
                    statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                    if statement == '1':
                        pass_ = input("Enter previous password : ")
                        if pass_ == i[1]:
                            print("Correct !")
                            password = input("Enter Password (length (5-100)):  ")
                            while True:
                                if len(password) >= 5 and len(password) <= 100:
                                    query = ("UPDATE patients SET password=%s WHERE mail=%s OR mail=%s")
                                    s = (password,active_mail,f_mail)
                                    mycursor.execute(query, s)
                                    mydb.commit()
                                    print('password change successfully !')
                                    home()
                                else:
                                    password = input("Wrong ! Enter Password (length (5-100)):  ")
                        else:
                            print("Wrong Answer !")
                    else:
                        if login==True:
                            return
                        else:
                            home()
            mycursor.execute("SELECT mail,password FROM doctors")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_mail or i[0]==f_mail:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            pass_ = input("Enter previous password : ")
                            if pass_ == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE doctors SET password=%s WHERE mail=%s OR mail=%s")
                                        s = (password, active_mail,f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        home()

                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            if login == True:
                                return
                            else:
                                home()
            mycursor.execute("SELECT mail,password FROM admin")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_mail or i[0]==f_mail:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            pass_ = input("Enter previous password : ")
                            if pass_ == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE admin SET password=%s WHERE mail=%s OR mail=%s")
                                        s = (password, active_mail,f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        print('password change successfully !')
                                        home()

                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            if login == True:
                                return
                            else:
                                home()
    elif p_s_q=='2':
        mycursor.execute("SELECT mail,seq_key FROM patients")
        result = mycursor.fetchall()
        for i in result:
            if i[0] == active_mail or i[0]==f_mail :
                while True:
                    statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                    if statement=='1':
                        q = input("Enter Security Key : ")
                        if q == i[1]:
                            print("Correct !")
                            password = input("Enter Password (length (5-100)):  ")
                            while True:
                                if len(password) >= 5 and len(password) <= 100:
                                    query=("UPDATE patients SET password=%s WHERE mail=%s OR mail=%s")
                                    s=(password,active_mail,f_mail)
                                    mycursor.execute(query,s)
                                    mydb.commit()
                                    home()
                                else:
                                    password = input("Wrong ! Enter Password (length (5-100)):  ")
                        else:
                            print("Wrong Answer !")
                    else:
                        if login == True:
                            return
                        else:
                            home()
        mycursor.execute("SELECT mail,seq_key FROM doctors")
        result = mycursor.fetchall()
        for i in result:
            if i[0] == active_mail or i[0] == f_mail:
                while True:
                    statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                    if statement == '1':
                        q = input("Enter Security Key : ")
                        if q == i[1]:
                            print("Correct !")
                            password = input("Enter Password (length (5-100)):  ")
                            while True:
                                if len(password) >= 5 and len(password) <= 100:
                                    query = ("UPDATE doctors SET password=%s WHERE mail=%s OR mail=%s")
                                    s = (password, active_mail,f_mail)
                                    mycursor.execute(query, s)
                                    mydb.commit()
                                    home()
                                else:
                                    password = input("Wrong ! Enter Password (length (5-100)):  ")
                        else:
                            print("Wrong Answer !")
                    else:
                        if login == True:
                            return
                        else:
                            home()
            mycursor.execute("SELECT mail,seq_key FROM admin")
            result = mycursor.fetchall()
            for i in result:
                if i[0] == active_mail or i[0] == f_mail:
                    while True:
                        statement = input("Want Change Password ? press 1\nPress Any key For Back : \n")
                        if statement == '1':
                            q = input("Enter Security Key : ")
                            if q == i[1]:
                                print("Correct !")
                                password = input("Enter Password (length (5-100)):  ")
                                while True:
                                    if len(password) >= 5 and len(password) <= 100:
                                        query = ("UPDATE admin SET password=%s WHERE mail=%s OR mail=%s")
                                        s = (password, active_mail,f_mail)
                                        mycursor.execute(query, s)
                                        mydb.commit()
                                        home()
                                    else:
                                        password = input("Wrong ! Enter Password (length (5-100)):  ")
                            else:
                                print("Wrong Answer !")
                        else:
                            if login == True:
                                return
                            else:
                                home()
def about_us():
    global log_in
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM team")
    result = mycursor.fetchall()
    print("Management Team : ")
    for row in result:
        print("Name : ",row[0])
        print("Mobile : ", row[1])
        print("Mail : ", row[2])
    mycursor.execute("SELECT * FROM our_mission")
    result = mycursor.fetchall()
    for row in result:
        print("Our Mission : ",row[0])
def contact_us():
    global log_in
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM cell")
    result = mycursor.fetchall()
    print("Cell : ")
    count=1
    for row in result:
        print(f"{count}. ", row[0])
        count+=1
    opinion=input("Want to send message? 1. yes 2. no \n")
    if opinion=='1':
        name = input("Enter Full Name :  ")
        while True:
            if len(name) > 3:
                break
            else:
                name = input("Enter Full Name :  ")
        mail = input("Enter Mail (Length (8-100) ) : ")
        while True:
            if len(mail) >= 8 and len(mail) <= 100  :
                break
            else:
                print("Please maintain required!")
                mail = input("Enter Mail (Length (8-100) ) : ")
        comment =input("Enter Comment : ")
        while True:
            if len(comment) >= 1 and len(comment) <= 255 :
                break
            else:
                print("Required!")
                comment = input("Enter comment ) : ")
        query = "INSERT INTO messages (name,mail,comment)VALUES(%s,%s,%s)"
        s = (name,mail,comment)
        mycursor.execute(query, s)
        mydb.commit()
        print("              Send Successfully !                ")
    else:
        print()
def view():
    global active_mail
    global active_username
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="mysql123#",
        database="doctors_appointments",
    )
    mycursor = mydb.cursor()
    while True:
        option = input("1. Doctor \n2. Patient\n3. Medical College\n4. Back\n")
        if option == '1':
            query = (
                "SELECT name,username,address,mobile,mail,qualifications,fee from doctors")
            mycursor.execute(query, )
            result = mycursor.fetchall()
            if result:
                for row in result:
                    print()
                    print("Doctor Name : ", row[0])
                    print("Address : ", row[2])
                    print("Mobile : ", row[3])
                    print("Mail : ", row[4])
                    print("Qualifications : ", row[5])
                    print("Fee : ", row[6])
            else:
                print("No Result!")
            print()
        elif option == '2':
            query = ("SELECT * from patients ")
            mycursor.execute(query, )
            result = mycursor.fetchall()
            if result:
                for row in result:
                    print("Name : ", row[0])
                    print("Username : ", row[1])
                    print("Age : ", row[2])
                    print("Mobile : ", row[3])
                    print("Address : ", row[4])
                    print("Blood Group : ", row[5])
                    print("Mail : ", row[6])
            else:
                print("No Result!")
            print()
        elif option == '3':
            query = ("SELECT * from medical_college ")
            mycursor.execute(query, )
            result = mycursor.fetchall()
            if result:
                for row in result:
                    print("Name : ", row[0])
                    print("Acronym : ", row[1])
                    print("Location : ", row[2])
                    print("Website : ", row[3])
            else:
                print("No Result!")
            print()
        elif option=='4':
            break
home()