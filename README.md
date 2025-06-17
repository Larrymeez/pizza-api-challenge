
# 🍕 Pizza API Challenge

A simple Flask REST API for managing pizzas and their restaurant offerings.

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd pizza-api-challenge
```

### 2. Create and activate a virtual environment with pipenv

```bash
pipenv shell
pipenv install flask flask_sqlalchemy flask_migrate
```

### 3. Set environment variables

For Linux/macOS:

```bash
export FLASK_APP=app
export FLASK_ENV=development
```

For Windows CMD:

```cmd
set FLASK_APP=app
set FLASK_ENV=development
```

For Windows PowerShell:

```powershell
$env:FLASK_APP = "app"
$env:FLASK_ENV = "development"
```

---

## 🛠️ Database Migration & Seeding

### 1. Initialize and apply migrations

```bash
flask db init      # only once
flask db migrate -m "Initial migration"
flask db upgrade
```

### 2. Seed the database

```bash
python seed.py
```

---

## 🔁 API Route Summary

| Method | Route                     | Description                     |
|--------|---------------------------|---------------------------------|
| GET    | `/pizzas`                 | List all available pizzas       |
| GET    | `/restaurants`            | List all restaurants            |
| GET    | `/restaurants/<id>`       | Get a restaurant with pizzas    |
| POST   | `/restaurant_pizzas`      | Add pizza to restaurant menu    |

---

## 💬 Example Requests & Responses

### GET `/pizzas`

**Request:**

```http
GET /pizzas
```

**Response:**

```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

---

### POST `/restaurant_pizzas`

**Request:**

```json
POST /restaurant_pizzas
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response:**

```json
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```

---

## ✅ Validation Rules

- `price` must be an **integer between 1 and 30** for restaurant_pizza.
- Restaurant and pizza must exist before creating a menu entry.
- Restaurant not found (GET `/restaurants/<id>`) should return 404:

  ```json
  { "error": "Restaurant not found" }
  ```

- POSTing invalid data should return 400:

  ```json
  { "errors": ["Validation errors here"] }
  ```

---

## 📬 Using Postman

1. Open Postman and import the file `challenge-1-pizzas.postman_collection.json`
2. Set the base URL to:

   ```
   http://127.0.0.1:5000
   ```

3. Try out the prebuilt requests:
   - Get pizzas
   - Get restaurants
   - Post a restaurant_pizza
   - View a single restaurant with pizzas

---

## 🧑‍💻 Author

Lawrence Miringu  
Phase 3 - Flatiron School Python Flask Challenge  
