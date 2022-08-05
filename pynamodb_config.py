import os

region = os.getenv("DYNAMODB_REGION", None)
if not region:
    host = os.getenv("DYNAMODB_HOST", "http://localhost:8000")
