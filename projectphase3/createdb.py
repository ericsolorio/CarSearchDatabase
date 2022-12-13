import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    cur = _conn.cursor()
    cur.execute(f"""
        
    CREATE TABLE user (
        u_userid integer(100),
        u_fullname varchar(100),
        u_email varchar(100),
        u_phonenumber integer(100),
        u_password varchar(100),
        u_type varchar(100),
        u_username varchar(100)
    )""")

    cur.execute(f"""
    CREATE TABLE purchases (
        p_id integer(100),
        p_carid integer(100),
        p_userid integer(100)
    )
    """)


    cur.execute(f"""
    CREATE TABLE services (
        s_serviceid integer(100),
        s_carid integer(100),
        s_userid integer(100),
        s_dealerid integer(100),
        s_type varchar(100)
    )
    """)


    cur.execute(f"""
    CREATE TABLE availability (
        a_avabid integer(100),
        a_orderid integer(100)
    )
    """)


    cur.execute(f"""
    CREATE TABLE cars(
        c_carid integer(100),
        c_model varchar(100),
        c_make varchar(100),
        c_year integer(100),
        c_color varchar(100),
        c_engine varchar(100),
        c_transmission varchar(100),
        c_class varchar(100),
        c_tint varchar(100),
        c_convertible varchar(100),
        c_carbon varchar(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE dealership(
        d_dealerid integer(100),
        d_manager varchar(100),
        d_email varchar(100),
        d_address varchar(100),
        d_phonenumber integer(100),
        d_nationkey integer(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE manufacturer(
        m_id integer(100),
        m_address varchar(100),
        m_phonenumber integer(100),
        m_email varchar(100),
        m_nationkey integer(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE orders(
        o_orderid integer(100),
        o_hqid integer(100),
        o_manuid integer(100),
        o_dealerid integer(100),
        o_carid integer(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE hq(
        h_hqid integer(100),
        h_name varchar(100),
        h_nationid integer(100),
        h_address varchar(100),
        h_ceo varchar(100),
        h_phonenumber integer(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE nation(
        n_nationkey integer(100),
        n_name varchar(100),
        n_regionkey integer(100)
    )
    """)

    cur.execute(f"""
    CREATE TABLE region(
        r_regionkey integer(100),
        r_name varchar(100),
        r_hemisphere varchar(100)
    )
    """)


    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    cur = _conn.cursor()

    cur.execute(f"""
    DROP TABLE user
    """)
    cur.execute(f"""
    DROP TABLE purchases
    """)
    cur.execute(f"""
    DROP TABLE services
    """)
    cur.execute(f"""
    DROP TABLE availability
    """)
    cur.execute(f"""
    DROP TABLE cars
    """)
    cur.execute(f"""
    DROP TABLE dealership
    """)
    cur.execute(f"""
    DROP TABLE manufacturer
    """)
    cur.execute(f"""
    DROP TABLE orders
    """)
    cur.execute(f"""
    DROP TABLE hq
    """)
    cur.execute(f"""
    DROP TABLE nation
    """)
    cur.execute(f"""
    DROP TABLE region
    """)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    cur = _conn.cursor()

    # cur.execute(f"""
    # sqlite3
    # .open database.sqlite
    # .mode csv
    # .separator ","
    # .import ./csvdata/Avalability.csv availability
    # """)


    #.import --skip 1 ./data/AVALIBILITY.csv availability
    #   .import --skip 1./data/CAR.csv cars
    #  .import --skip 1 ./data/DEALERSHIP.csv dealership
    # .import --skip 1 ./data/HQ.csv hq
    # .import --skip 1 ./data/Manufacturer.csv manufacturer
    # .import --skip 1 ./data/Nation.csv nation
    # .import --skip 1 ./data/ORDERS.csv orders
    #   .import --skip 1 ./data/Purchases.csv purchases
    # .import  --skip1 ./data/Region.csv region
    # .import --skip1 ./data/SERVICES.csv services
    # .import -- skip 1 ./data/User.csv user



    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        #dropTable(conn)
        #createTable(conn)
        #populateTable(conn)

        Q1(conn)

    
    closeConnection(conn, database)


if __name__ == '__main__':
    main()







######################
# results = cur.fetchall()


#     #print('\n'.join(f'{tup[0]:>10} {tup[1]} {tup[2]} {tup[3]}' for tup in results))

#     # with open("1.out", "w") as outfile:
#     #     outfile.write('       wId wName                                          wCap        sId        nId')
#     #     outfile.write('\n')
#     #     outfile.write('\n'.join((f'{tup[0]:>10} {tup[1]} {tup[2]:<20} {tup[3]:^5} {tup[4]}' for tup in results)))

#     df = pd.DataFrame.from_records(results, columns =['w_warehousekey', 'w_name', 'w_capacity', 'w_suppkey','w_nationkey'])
  
#     print(df.to_string()) 
    
#     # with open("1.out", "w") as outfile:
#     #     outfile.write('       wId wName                                          wCap        sId        nId')
#     #     outfile.write('\n')
#     #     outfile.write(str(df))
######################




######################

# df = pd.DataFrame.from_records(results, columns =['w_warehousekey', 'w_name', 'w_capacity', 'w_suppkey','w_nationkey'])
  
#     print(df.to_string())

#     left_aligned_df = df.style.set_properties(**{'text-align': 'left'})

#     with open("1.out", "w") as outfile:
#         outfile.write(df.to_string())

######################

######################
    # file = open('./csvdata/Avalability.csv')
    # contents = csv.reader(file)
    # file1 = open('./csvdata/Car.csv')
    # contents1 = csv.reader(file)
    # file2 = open('./csvdata/Dealership.csv')
    # contents2 = csv.reader(file)
    # file3 = open('./csvdata/HQ.csv')
    # contents3 = csv.reader(file)
    # file4 = open('./csvdata/Manufacturer.csv')
    # contents4 = csv.reader(file)
    # file5 = open('./csvdata/Nation.csv')
    # contents5 = csv.reader(file)
    # file6 = open('./csvdata/Orders.csv')
    # contents6 = csv.reader(file)
    # file7 = open('./csvdata/Purchases.csv')
    # contents7 = csv.reader(file)
    # file8 = open('./csvdata/Region.csv')
    # contents8 = csv.reader(file)
    # file9 = open('./csvdata/Services.csv')
    # contents9 = csv.reader(file)
    # file10 = open('./csvdata/User.csv')
    # contents10 = csv.reader(file)
######################