from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
CORS(app)

@app.route('/example', methods=['GET'])
def example_route():
    # Execute a sample query
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    # Process the result or return it as JSON
    #data = [{'id': row[0], 'name': row[1]} for row in result]
    return jsonify(result)


@app.route('/register', methods=['POST'])
def new_account_register() :
    # Create a new connection and cursor
    db = mysql.connector.connect(
        host='host.docker.internal',
        port=3307,
        user='root',
        password='root',
        database='ter'
    )
    cursor = db.cursor()

    data =request.get_json()
    
    if 'username' not in data or 'password' not in data or 'email' not in data :
        return jsonify({'error':'Requête invalide'}), 400
    
    cursor.execute("SELECT * FROM users WHERE username = %s", (data['username'],))
    if cursor.fetchone() is not None:
        return jsonify({'error': 'Username already exists'}), 400
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (data['email'],))
    if cursor.fetchone() is not None:
        return jsonify({'error': 'Email already exists'}), 400
    
    # Add new user to the database
    hashed_password = generate_password_hash(data['password'])
    cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", 
                   (data['username'], hashed_password, data['email']))

    # Commit changes and close connection
    db.commit()
    cursor.close()
    db.close()

    return jsonify({'message': 'Account registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login(): 
    
    db = mysql.connector.connect(
        host='host.docker.internal',
        port=3307,
        user='root',
        password='root',
        database='ter'
    )
    
    cursor = db.cursor()

    data =request.get_json()
    data = request.get_json()

    if 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    # Find the user in the database
    cursor.execute("SELECT * FROM users WHERE email = %s", (data['email'],))
    user = cursor.fetchone()
    


    # If the user does not exist or the password does not match, return an error
    if user is None or not check_password_hash(user[2], data['password']):
        return jsonify({'error': 'Invalid username or password', "username" : user[2]}), 401

    db.commit()
    cursor.close()
    db.close()
    # If the username and password match, the login is successful
    return jsonify({'message': 'Login successful',
                    'username': user[1]}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
