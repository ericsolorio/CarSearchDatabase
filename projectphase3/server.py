from flask import Flask, render_template, request, url_for, redirect
import json
import sqlite3
from sqlite3 import Error
from flask import jsonify

app = Flask(__name__)

database = r"database.sqlite"

with app.app_context():

    @app.route("/")
    def start():
        return render_template("login.html")

    @app.route("/print")
    def tempprint():
        return render_template("print.html")

    @app.route("/normalaccount")
    def norm():
        return render_template("normacct.html")

    @app.route("/availability")
    def avai():
        return render_template("availability.html")

    @app.route("/acctinfo")
    def tempinfo():
        return render_template("info.html")

    @app.route("/business")
    def tempbus():
        return render_template("businessacct.html")
    
    @app.route("/newManufacturers")
    def tempmanu():
        return render_template("manufacturers.html")

    @app.route("/newDealerships")
    def tempdealer():
        return render_template("dealerships.html")
    
    #########creds################
    @app.route('/', methods=['POST'])
    def cred():
        content = request.get_json()
        print(content)

        username = content['username']
        password = content['password']
        print(username)
        print(password)

        conn = sqlite3.connect(database)
        cur = conn.cursor()

        cur.execute(f"""
        SELECT u_type 
        FROM user
        WHERE u_username = ?
        AND u_password = ?""", (username, password)
        )

        results = cur.fetchall()

        if(results != []):

            cur.execute(f"""
            SELECT u_fullname 
            FROM user
            WHERE u_username = ?
            AND u_password = ?""", (username, password)
            )

            fullname = cur.fetchall()
            print(fullname[0][0])

            with open("temp.json", "w") as json_file:
                json.dump(fullname[0][0],json_file)

            if(results[0][0] == 'NORMAL'):
                return 'NORMAL'
            elif(results[0][0] == 'BUSINESS'):
                return 'BUSINESS'
        
        
        else:
            return 'nah'


    @app.route('/dealerCreation', methods=['POST'])
    def dealerfunc():
        content = request.get_json()

        conn = sqlite3.connect(database)
        cur = conn.cursor()

        manager = content['manager']
        email = content['email']
        address = content['address']
        phonenumber = content['phonenumber']
        nationName = content['nation']

        print(manager)
        print(email)
        print(address)
        print(phonenumber)
        print(nationName)

        cur.execute(f"""
            SELECT n_nationkey
            FROM nation
            WHERE n_name = ?
        """,(nationName,))

        resultsnation = cur.fetchall()
        print(resultsnation)
        nationnum = resultsnation[0][0]

        cur.execute(f"""
            SELECT COUNT(*)
            FROM dealership
        """)

        resultsrow = cur.fetchall()

        nextRow = resultsrow[0][0] + 1

        print(nextRow)

        cur.execute(f"""
            INSERT INTO dealership (d_dealerid, d_manager, d_email, d_address, d_phonenumber, d_nationkey)
            VALUES(?, ?, ?, ?, ?, ?)
        """,(nextRow, manager, email, address, phonenumber, nationnum))
        conn.commit()

        return 'yup'




    @app.route('/manuCreation', methods=['POST'])
    def manufunc():
        content = request.get_json()

        conn = sqlite3.connect(database)
        cur = conn.cursor()

        address = content['address']
        phonenumber = content['phonenumber']
        email = content['email']
        nationName = content['nation']

        print(address)
        print(phonenumber)
        print(email)
        print(nationName)

        cur.execute(f"""
            SELECT n_nationkey
            FROM nation
            WHERE n_name = ?
        """,(nationName,))

        resultsnation = cur.fetchall()
        print(resultsnation)
        nationnum = resultsnation[0][0]

        cur.execute(f"""
            SELECT COUNT(*)
            FROM manufacturer
        """)

        resultsrow = cur.fetchall()

        nextRow = resultsrow[0][0] + 1

        print(nextRow)

        cur.execute(f"""
            INSERT INTO manufacturer (m_id, m_address, m_phonenumber, m_email, m_nationkey)
            VALUES(?, ?, ?, ?, ?)
        """,(nextRow,address,phonenumber,email,nationnum))
        conn.commit()

        return 'yup'




    @app.route('/search', methods=['POST'])
    def addname():
        content = request.get_json()
        
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        make = content['make']
        if(make == ''):
            make = '%'
        model = content['model']
        if(model == ''):
            model = '%'
        year = content['year']
        if(year == ''):
            year = '%'
        color = content['color']
        if(color == ''):
            color = '%'
        engine = content['engine']
        if(engine == ''):
            engine = '%'
        transmission = content['transmission']
        if(transmission == ''):
            transmission = '%'
        classtype = content['classtype']
        if(classtype == ''):
            classtype = '%'

        print(make)
        print(model)
        print(year)
        print(color)
        print(engine)
        print(transmission)
        print(classtype)

        cur.execute(f"""
        SELECT d_address
        FROM orders, cars, availability, dealership
        WHERE c_carid = o_carid
        AND d_dealerid = o_dealerid
        AND a_orderid = o_orderid
        AND c_make LIKE ?
        AND c_model LIKE ?
        AND c_year LIKE ?
        AND c_color LIKE ?
        AND c_engine LIKE ?
        AND c_transmission LIKE ?
        AND c_class LIKE ?

        """,(make, model, year, color, engine, transmission, classtype))

        results = cur.fetchall()
        print(results)
        

        return jsonify(results)
    

    @app.route('/services', methods=['GET'])
    def servicefunc():
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        with open('temp.json', "r") as json_file:
            name = json.load(json_file)
        print(name)

        fullname = str(name)
        print(fullname)

        cur.execute(f"""
        SELECT c_make, c_model, d_address, s_type
        FROM user, cars, services, dealership
        WHERE u_userid = s_userid
        AND c_carid = s_carid
        AND d_dealerid = s_dealerid
        AND u_fullname = ?

        """,([fullname]))
        
        results = cur.fetchall()
        print(results)

        return results


    @app.route('/purchases', methods=['GET'])
    def purfunc():
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        with open('temp.json', "r") as json_file:
            name = json.load(json_file)
        print(name)

        fullname = str(name)
        print(fullname)

        cur.execute(f"""
        SELECT c_model, c_make
        FROM user, cars, purchases
        WHERE u_userid = p_userid
        AND c_carid = p_carid
        AND u_fullname = ?

        """,([fullname]))
        
        results = cur.fetchall()
        print(results)

        return results


    @app.route('/avab/<string:carid>', methods=['GET'])
    def avabfunc(carid):
        print(carid)
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        print(carid)
        #print(fullname)

        cur.execute(f"""
        SELECT d_address
        FROM availability, orders, dealership, cars
        WHERE a_orderid = o_orderid
        AND o_dealerid = d_dealerid
        AND c_carid = ?
        """,(carid,))
        results = cur.fetchall()
        
        return results


    @app.route('/printdb', methods=['GET'])
    def printdbfunc():
        conn = sqlite3.connect(database)
        cur = conn.cursor()

        cur.execute(f"""
        SELECT * FROM availability
        """)
        results1 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM cars
        """)
        results2 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM dealership
        """)
        results3 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM hq
        """)
        results4 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM manufacturer
        """)
        results5 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM nation
        """)
        results6 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM orders
        """)
        results7 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM purchases
        """)
        results8 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM region
        """)
        results9 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM services
        """)
        results10 = cur.fetchall()

        cur.execute(f"""
        SELECT * FROM user
        """)
        results11 = cur.fetchall()

        combine = results1+results2+results3+results4+results5+results6+results7+results8+results9+results10+results10+results11
        
        return combine

    

    # ######GETS ALL GRADES###########
    # @app.route('/grades', methods=['GET'])
    # def get_grades():
    #     result = Student.query.all()
    #     grades = {}
    #     for r in result:
    #         grades[r.name] = r.grade
    #     return grades

    # ########GET SPECIFIC GRADE#############
    # @app.route('/grades/<string:name>', methods=['GET'])
    # def get_specificgrade(name):
    #     result = Student.query.all()
    #     grades = {}
    #     for r in result:
    #         grades[r.name] = r.grade
    #     return {name: grades[name]}

    # #########ADD USER################
    # @app.route('/grades', methods=['POST'])
    # def addname():
    #     content = request.get_json()
        
    #     db.session.add(Student(name=content['name'], grade = content['grade']))
    #     db.session.commit()

    #     result = Student.query.all()
    #     grades = {}
    #     for r in result:
    #         grades[r.name] = r.grade
    #     return grades

    # #############EDIT##################
    # @app.route('/grades/<string:name>', methods=['PUT'])
    # def editname(name):
    #     content = request.get_json()
        
    #     student = Student.query.filter_by(name=name).first()
    #     student.grade = content['grade']
    #     db.session.commit()

    #     result = Student.query.all()
    #     grades = {}
    #     for r in result:
    #         grades[r.name] = r.grade
    #     return grades

    # ##########DELETE USER###############
    # @app.route('/grades/<string:name>', methods=['DELETE'])
    # def deleteuser(name):
    #     student = Student.query.filter_by(name=name).first()
    #     db.session.delete(student)
    #     db.session.commit()

    #     result = Student.query.all()
    #     grades = {}
    #     for r in result:
    #         grades[r.name] = r.grade
    #     return grades 





    if __name__ == "__main__":
        app.run(debug=True)