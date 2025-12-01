# Python Time API

This project is a simple FastAPI application that provides an API endpoint to retrieve the local time.

## Project Structure

```
python-time-api
├── src
│   ├── main.py          # Entry point of the application
│   ├── routes
│   │   └── time.py      # API endpoint for retrieving local time
│   └── utils
│       └── helpers.py   # Utility functions for time formatting
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .gitignore            # Files to ignore in Git
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-time-api
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the API

To run the FastAPI application, execute the following command:

```
uvicorn src.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoint

- **GET /time**: Returns the current local time in a specified format.

## License

This project is licensed under the MIT License.