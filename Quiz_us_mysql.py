from flask import jsonify, request
import flask
import mysql.connector
import json
import MySQLdb


app = flask.Flask(__name__)
app.config['DEBUG']= True


def hello():
    try:
        # Connect to the database
        connection = mysql.connector.connect(host='localhost',
                                             database='healapp',
                                             user='root',
                                             password='monikaheal1')
        query = "SELECT * FROM quiz_us"

        with connection.cursor(mysql.connector.cursors.DictCursor) as cursor:
            cursor.execute(query)
            data = cursor.fetchall()

        return json.dumps(data, indent=4)

    # Close the cursor and the connection
    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

            print("MySQL connection is closed")

@app.route('/hi')
def hiw():
    return jsonify(hello())



if __name__ == "__main__":
    app.run()
