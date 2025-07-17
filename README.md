# Fibonacci FastAPI Service

A FastAPI web service that provides REST endpoints for calculating Fibonacci numbers.

## Features

- **GET /fibonacci/{n}** - Returns the nth Fibonacci number
- **GET /fibonacci/{n}/sequence** - Returns the nth Fibonacci number plus the complete sequence
- **GET /health** - Health check endpoint
- Input validation and error handling
- Automatic API documentation
- Efficient iterative algorithm

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jngy36/fibonacci_fastapi.git
cd fibonacci_fastapi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
python main.py
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive documentation at `http://localhost:8000/docs`

## Example Requests

```bash
# Get the 10th Fibonacci number
curl http://localhost:8000/fibonacci/10

# Get the sequence up to the 10th number
curl http://localhost:8000/fibonacci/10/sequence

# Health check
curl http://localhost:8000/health
```

## API Endpoints

### GET /fibonacci/{n}
Returns the nth Fibonacci number.

**Parameters:**
- `n` (int): The position in the Fibonacci sequence (0-1000)

**Response:**
```json
{
  "n": 10,
  "result": 55,
  "sequence": null
}
```

### GET /fibonacci/{n}/sequence
Returns the nth Fibonacci number along with the complete sequence.

**Parameters:**
- `n` (int): The position in the Fibonacci sequence (0-100)

**Response:**
```json
{
  "n": 10,
  "result": 55,
  "sequence": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
}
```

### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy"
}
```

## Error Handling

The API includes proper error handling for:
- Negative input values
- Values that are too large (to prevent excessive computation)
- Invalid input types

## License

MIT License
