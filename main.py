from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Fibonacci Calculator API", version="1.0.0")

class FibonacciResponse(BaseModel):
    n: int
    result: int
    sequence: Optional[list] = None

def calculate_fibonacci(n: int, return_sequence: bool = False):
    """Calculate the nth Fibonacci number and optionally return the sequence"""
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n == 0:
        return 0, [0] if return_sequence else None
    elif n == 1:
        return 1, [0, 1] if return_sequence else None
    
    # Calculate Fibonacci iteratively for efficiency
    a, b = 0, 1
    sequence = [0, 1] if return_sequence else None
    
    for i in range(2, n + 1):
        a, b = b, a + b
        if return_sequence:
            sequence.append(b)
    
    return b, sequence

@app.get("/")
async def root():
    return {"message": "Fibonacci Calculator API", "endpoints": ["/fibonacci/{n}", "/fibonacci/{n}/sequence"]}

@app.get("/fibonacci/{n}", response_model=FibonacciResponse)
async def get_fibonacci(n: int):
    """Get the nth Fibonacci number"""
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    
    if n > 1000:  # Prevent very large computations
        raise HTTPException(status_code=400, detail="n must be <= 1000")
    
    try:
        result, _ = calculate_fibonacci(n)
        return FibonacciResponse(n=n, result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/fibonacci/{n}/sequence", response_model=FibonacciResponse)
async def get_fibonacci_sequence(n: int):
    """Get the nth Fibonacci number along with the complete sequence"""
    if n < 0:
        raise HTTPException(status_code=400, detail="n must be non-negative")
    
    if n > 100:  # Smaller limit for sequence to avoid large responses
        raise HTTPException(status_code=400, detail="n must be <= 100 for sequence endpoint")
    
    try:
        result, sequence = calculate_fibonacci(n, return_sequence=True)
        return FibonacciResponse(n=n, result=result, sequence=sequence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
