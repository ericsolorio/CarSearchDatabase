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

def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    #output all the data from user
    cur = _conn.cursor()
    cur.execute(f"""

    SELECT *
    FROM user

    """)

    results = cur.fetchall()

    with open("output/1.out", "w") as outfile:

        for row in results:
            l = '{} {} {} {}'.format(row[0], row[1], row[2], row[3])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    #find the email of robert downey
    cur = _conn.cursor()
    cur.execute(f"""

    SELECT u_email
    FROM user
    WHERE u_fullname = 'Robert Downey'
    
    """)

    results = cur.fetchall()

    with open("output/2.out", "w") as outfile:

        for row in results:
            l = '{} '.format(row[0])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")

def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    cur = _conn.cursor()

    #All the hq's in Japan
    cur.execute(f"""

    SELECT h_name
    FROM hq, nation, region
    WHERE h_nationid = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'ASIA'
    
    """)
    
    results = cur.fetchall()

    with open("output/3.out", "w") as outfile:

        for row in results:
            l = '{} '.format(row[0])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    cur = _conn.cursor()

    #All the users that have bought cars plus their emails
    # their emails in order alpabetically
    cur.execute(f"""

    SELECT u_userid, u_email
    FROM user, purchases
    WHERE u_userid = p_userid
    ORDER BY u_email
    
    """)
    
    results = cur.fetchall()

    with open("output/4.out", "w") as outfile:

        for row in results:
            l = '{:<10} {}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")


def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    cur = _conn.cursor()

    #ALL the car names of the orders with the phonenumber from hq, manu and deler
    # Each car being order aplhabetically and distincly
    cur.execute(f"""

    SELECT c_model, h_phonenumber, m_phonenumber, d_phonenumber
    FROM cars, hq, manufacturer, dealership, orders
    WHERE c_carid = o_carid
    AND h_hqid = o_hqid
    AND m_id = o_manuid
    AND d_dealerid = o_dealerid
    GROUP BY c_model
    ORDER BY c_model
    
    """)
    
    results = cur.fetchall()

    with open("output/5.out", "w") as outfile:

        for row in results:
            l = '{:<20} {:<15} {:<15} {:<15}'.format(row[0], row[1], row[2], row[3])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")

def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    cur = _conn.cursor()

    #ALL THE CARS FROM TOYOTA but only show the first 11
    cur.execute(f"""

    SELECT c_model, c_make, c_color
    FROM cars
    WHERE c_make = 'TOYOTA'
    LIMIT 11
    
    """)
    
    results = cur.fetchall()

    with open("output/6.out", "w") as outfile:

        for row in results:
            l = '{:<20} {:<15} {:<15}'.format(row[0], row[1], row[2])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")


def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    cur = _conn.cursor()

    #Who was the user/s with the most services
    #print their names and the number of services they got
    cur.execute(f"""

    SELECT u_fullname, max(sub)
    FROM
        (SELECT u_userid as subid ,count(s_serviceid) as sub
        FROM services, user
        WHERE u_userid = s_userid
        GROUP BY s_userid), user
    WHERE u_userid = subid

    """)
    
    results = cur.fetchall()

    with open("output/7.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")


## USE CASES -- searching for cars in teh website
def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")

    cur = _conn.cursor()

    #Search the cars that are available in the US
    cur.execute(f"""

    SELECT c_model, c_make
    FROM cars, availability, dealership, nation
    WHERE c_carid = a_carid
    AND d_dealerid = a_dealerid
    AND d_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'

    """)
    
    results = cur.fetchall()

    with open("output/8.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")

def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    cur = _conn.cursor()

    #Search the cars that are available in the US, and
    # the hq is from japan
    cur.execute(f"""

    SELECT c_model, c_make
    FROM 
    cars, availability, dealership, nation

    WHERE c_carid = a_carid
    AND d_dealerid = a_dealerid
    AND d_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    AND c_model IN 
        (SELECT c_model as aye
        FROM cars, availability, nation, hq, orders
        WHERE c_carid = a_carid
        AND a_availabilityid = o_orderid
        AND o_hqid = h_hqid
        AND h_nationid = n_nationkey
        AND n_name = 'JAPAN'
        AND a_soldtype = 'new')
    AND c_make IN 
        (SELECT c_make
        FROM cars, availability, nation, hq, orders
        WHERE c_carid = a_carid
        AND a_availabilityid = o_orderid
        AND o_hqid = h_hqid
        AND h_nationid = n_nationkey
        AND n_name = 'JAPAN'
        AND a_soldtype = 'new')
    AND a_soldtype = 'new'

    """)
    
    results = cur.fetchall()

    with open("output/9.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')

    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    cur = _conn.cursor()

    # a user just registered to the website

    cur.execute(f"""

    INSERT INTO user (u_userid, u_fullname, u_email, u_phonenumber)
    VALUES(10, 'Toph', 'toph@unclemando.com', 9048098394);

    """)

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    cur = _conn.cursor()

    # hq account wants to make new manufacturer

    cur.execute(f"""

    INSERT INTO manufacturer (m_id, m_address, m_phonenumber, m_email, m_nationkey)
    VALUES(9, 'test blvd', 4233448907, 'test@country.com', 99);

    """)

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    cur = _conn.cursor()

    # hq account wants to make new manufacturer

    cur.execute(f"""

    INSERT INTO manufacturer (m_id, m_address, m_phonenumber, m_email, m_nationkey)
    VALUES(9, 'test blvd', 4233448907, 'test@country.com', 99);

    """)

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    cur = _conn.cursor()

    # hq account wants to make new manufacturer

    cur.execute(f"""

    INSERT INTO dealership (d_dealerid, d_manager, d_email, d_address, d_phonenumber, d_nationkey)
    VALUES(16, 'test', 'test', 'test', 0000000000, 99);

    """)

    print("++++++++++++++++++++++++++++++++++")

def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    cur = _conn.cursor()

    # user wants to update his phonenumber

    cur.execute(f"""

    UPDATE user
    SET u_phonenumber = 1111111111
    WHERE u_fullname = 'Jose Munoz';

    """)

    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    cur = _conn.cursor()

    # hq account wants to delete manufacturer

    cur.execute(f"""

    DELETE FROM manufacturer
    WHERE m_id = 9;

    """)

    print("++++++++++++++++++++++++++++++++++")


def Q16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q16")

    #Show all the customers names that bought cars from the FRANCE
    # plus the car that they bought

    cur = _conn.cursor()
    cur.execute(f"""

    SELECT u_fullname, c_model, c_make
    FROM user, purchases, dealership, nation, cars
    WHERE u_userid = p_userid
    AND d_dealerid = p_dealerid
    AND d_nationkey = n_nationkey
    AND c_carid = p_carid
    AND n_name = 'FRANCE'
    GROUP BY u_fullname

    """)

    results = cur.fetchall()

    with open("output/16.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")


def Q17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q17")

    #show the users that bought cars out of the united states
    #but get car service in the united states
    cur = _conn.cursor()
    cur.execute(f"""

    SELECT u_fullname
    FROM 
        (SELECT u_fullname as u_subname
        FROM user, purchases, dealership, nation
        WHERE u_userid = p_userid
        AND d_dealerid = p_dealerid
        AND d_nationkey = n_nationkey
        AND n_name != 'UNITED STATES'
        GROUP BY u_fullname),
    user, services, dealership, nation
    WHERE u_fullname = u_subname
    AND u_userid = s_serviceid
    AND s_dealerid = d_dealerid
    AND d_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    GROUP BY u_fullname
    ORDER BY U_fullname


    """)

    results = cur.fetchall()

    with open("output/17.out", "w") as outfile:

        for row in results:
            l = '{:<20}'.format(row[0])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")


def Q18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q18")

    #count select oil change services done in the US
    cur = _conn.cursor()
    cur.execute(f"""

    SELECT count(s_serviceid)
    FROM services, dealership, nation
    WHERE s_dealerid = d_dealerid
    AND d_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    AND s_type = 'oil change'


    """)

    results = cur.fetchall()

    with open("output/18.out", "w") as outfile:

        for row in results:
            l = '{:<20}'.format(row[0])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")

def Q19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q19")

    #print the names and how many cars they bought
    cur = _conn.cursor()
    cur.execute(f"""


    SELECT u_fullname, count(p_id)
    FROM user, purchases
    WHERE p_userid = u_userid
    GROUP BY p_userid


    """)

    results = cur.fetchall()

    with open("output/19.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0], row[1])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")

def Q20(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q20")

    #print the person who bought the least cars
    cur = _conn.cursor()
    cur.execute(f"""

    SELECT min(subppl), u_fullname
    FROM(
        SELECT count(p_id) subppl, p_userid as subuser
        FROM user, purchases
        WHERE p_userid = u_userid
        GROUP BY p_userid),
        user
    WHERE subuser = u_userid

    """)

    results = cur.fetchall()

    with open("output/20.out", "w") as outfile:

        for row in results:
            l = '{:<20}{}'.format(row[0],row[1])
            outfile.write(l)
            outfile.write('\n')
            
    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"database.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        
        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)
        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        #Q10(conn)
        #Q11(conn)
        #Q12(conn)
        #Q13(conn)
        #Q14(conn)
        #Q15(conn)

        Q16(conn)
        Q17(conn)
        Q18(conn)
        Q19(conn)
        Q20(conn)

    
    closeConnection(conn, database)


if __name__ == '__main__':
    main()





# orders should just like all the cars the hq id, manu id 
# basically cars but with more detail
