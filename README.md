# MediQuick Pharmacy 💊

A modern, lightweight Python web service for pharmacy inventory management, medicine search, and order processing.

---

## 🚀 Features

- **Inventory Catalog**: Browse and query available medicines, dosages, and stock levels.
- **Order Management**: Place orders with real-time stock validation and price calculations.
- **RESTful Endpoints**: Clean JSON APIs structured with Flask Blueprints.
- **Testing Ready**: Built-in `pytest` configuration and test fixtures via `conftest.py`.

---

## 📁 Project Structure

```text
mediquick-pharmacy/
├── app.py              # Application entrypoint & Flask app factory
├── routes/
│   └── __init__.py     # API Blueprint & route handlers (medicines, orders)
├── conftest.py         # Pytest fixtures and test configuration
├── requirements.txt    # Project dependencies
├── .gitignore          # Python gitignore
└── README.md           # Documentation
```

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SaoodQazi/mediquick-pharmacy.git
cd mediquick-pharmacy
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The service will be available at `http://localhost:5000`.

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Service status and endpoint index |
| `GET` | `/health` | Health check endpoint |
| `GET` | `/api/medicines` | Get list of all medicines |
| `GET` | `/api/medicines/<id>` | Get details of a medicine by ID |
| `POST` | `/api/orders` | Place a medicine order |

---

## 📄 License

This repository is publicly available under the MIT License.