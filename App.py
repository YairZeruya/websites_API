from flask import Flask, jsonify,request
from flasgger import Swagger
from website_data import websites
import sqlite3

app = Flask(__name__)
swagger = Swagger(app)

def add_website(country, website_category, website_url):
    connection = get_db_connection()
    connection.execute('INSERT INTO websites (country, website_category, website_url) VALUES (?, ?, ?)', (country,website_category, website_url))
    connection.commit()
    connection.close()

def get_all_websites():
    connection = get_db_connection()
    websites = connection.execute('SELECT * FROM websites').fetchall()
    connection.close()
    return websites

def get_websites_by_country(country):
    connection = get_db_connection()
    websites = connection.execute('SELECT * FROM websites WHERE country = ?', (country,)).fetchall()
    connection.close()
    return websites

def get_db_connection():
    connection = sqlite3.connect('websites.db')
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = get_db_connection()
    connection.execute('''CREATE TABLE IF NOT EXISTS websites(
                       country TEXT NOT NULL,
                       website_category TEXT NOT NULL,
                       website_url TEXT NOT NULL)''')
    connection.commit()
    connection.close()

@app.route('/<country>', methods=["GET"])
def get_websites(country):
    """
    Endpoint to get websites for a specific country.
    ---
    parameters:
      - name: country
        in: path
        type: string
        required: true
        description: The name of the country.
    responses:
      200:
        description: A JSON object containing websites for the specified country.
      404:
        description: country Not Found
    """
    websites_json = []
    # Fetch all websites for the specified country
    websites = get_websites_by_country(country)
    websites_json = {country: {website['website_category']: website['website_url'] for website in websites}}
    return jsonify(websites_json)

@app.route('/add', methods=["POST"])
def add_website_to_db():
    """
    Endpoint to add a website to the database.
    ---
    parameters:
      - name: country
        in: query
        type: string
        required: true
        description: The name of the country.
      - name: website_category
        in: query
        type: string
        required: true
        description: The category of the website.
      - name: website_url
        in: query
        type: string
        required: true
        description: The URL of the website.
    responses:
      200:
        description: Website added successfully.
    """
    country = request.args.get('country')
    website_category = request.args.get('website_category')
    website_url = request.args.get('website_url')
    add_website(country, website_category, website_url)
    return "Website added successfully."

if __name__ == '__main__':
    create_table()
    if not get_all_websites():
      for country in websites:
          for website_category, website_url in websites[country].items():
              add_website(country, website_category, website_url)
    # Fetch all websites from the database
    all_websites = get_all_websites()
    # Print the content of each row
    for row in all_websites:
        print(row['country'], row['website_category'], row['website_url'])
    app.run(debug= True, port= 8088)
