'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    print("Conn type  :", type(conn))
    print("Connection :", conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Insert records to DEPT Table
    '''
    query = ["insert into dept_322 values(10, 'ACCOUNTING', 'NEW YORK')",
             "insert into dept_322 values(20, 'RESEARCH', 'DALLAS')",
             "insert into dept_322 values(30, 'SALES', 'CHICAGO')",
             "insert into dept_322 values(40, 'OPERATIONS', 'BOSTON')"]
    for each in query:
        cursor.execute(each)
    '''
    records = [(10, 'ACCOUNTING', 'NEWYORK'),
             (20, 'RESEARCH', 'DALLAS'),
             (30, 'SALES', 'CHICAGO'),
             (40, 'OPERATIONS', 'BOSTON')]
    for record in records:
        query = "INSERT INTO DEPT_322 VALUES(%s, %s, %s)"
        cursor.execute(query, record)
    # controller - service - dao
    '''
    query = [(10, 'ACCOUNTING', 'NEWYORK'),
             (20, 'RESEARCH', 'DALLAS'),
             (30, 'SALES', 'CHICAGO'),
             (40, 'OPERATIONS', 'BOSTON')]
    for each in query:
        dept_no = each[0]
        d_name = each[1]
        location = each[2]
        val = "insert into DEPT_322 values({},{},{})".format(dept_no,d_name,location)
        print(val)
        cursor.execute("insert into DEPT_322 values({},{},{})".format(dept_no,d_name,location))
    '''
    print("----Records inserted into DEPT successfully-----")    
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()


list1 = [1, 2, 3]  # CREATE
print(list1)  # RETRIEVE
list1.append(100)  # UPDATE
del list1[3]  # DELETE


