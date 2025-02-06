import os
from dotenv import load_dotenv
load_dotenv()
print("COUCHBASE_USERNAME:", os.getenv("COUCHBASE_USERNAME"))
print("COUCHBASE_PASSWORD:", os.getenv("COUCHBASE_PASSWORD"))