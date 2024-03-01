# Website Data API

This Flask application provides an API for managing and accessing website data categorized by country and category. It allows users to add websites to the database, retrieve websites by country, category, or both, and fetch all websites for a specific country.

## Setup

1. Install Flask and required dependencies:

```bash
pip install Flask
pip install flasgger
```

2. Run the Flask application:
```bash
python app.py
```

3. Create a SQLite database file named `websites.db` in the project directory (created automatically in the code).

The API will be available at [http://localhost:8088/apidocs](http://localhost:8088/apidocs).


# Endpoint
### 1. Get Websites by Country

#### Endpoint: `/<country>`

- **Method:** GET
- **Parameters:**
  - `country`: The name of the country.
- **Response:**
  - 200: A JSON object containing websites for the specified country.
  - 404: If the country is not found.     
- **Example:**
  ```http
  GET /israel
  ```

### 2. Get Websites by Category

#### Endpoint: `/<country>/<category>`

- **Method:** GET
- **Parameters:**
  - `country`: The name of the country.
  - `category`: The category of the website.
- **Response:**
  - 200: A JSON object containing websites for the specified country and category.
  - 404: If the country or category is not found.
- **Example:**
  ```http
  GET /usa/news
   ```

  ### 3. Add Website

#### Endpoint: `/add`

- **Method:** POST
- **Parameters:**
  - `country`: The name of the country.
  - `category`: The category of the website.
  - `url`: The URL of the website.
- **Response:**
  - 200: If the website is added successfully.
- **Example:**
  ```http
  POST /add?country=germany&category=news&url=https://www.example.com
  ```

**Swagger UI**

The API documentation is available using Swagger UI at [http://localhost:8088/apidocs](http://localhost:8088/apidocs).


