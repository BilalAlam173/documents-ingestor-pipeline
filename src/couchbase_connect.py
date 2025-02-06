from dotenv import load_dotenv
import os
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

# Load environment variables from .env file
load_dotenv()

COUCHBASE_USERNAME = os.getenv("COUCHBASE_USERNAME")
COUCHBASE_PASSWORD = os.getenv("COUCHBASE_PASSWORD")
COUCHBASE_HOST = os.getenv("COUCHBASE_HOST")
print("COUCHBASE_USERNAME:", COUCHBASE_USERNAME)
print("COUCHBASE_PASSWORD:", COUCHBASE_PASSWORD)

# auth = PasswordAuthenticator(COUCHBASE_USERNAME, COUCHBASE_PASSWORD)
# cluster = Cluster(COUCHBASE_HOST, ClusterOptions(auth))
# bucket = cluster.bucket("cs-hackathon")
# collection = bucket.default_collection()
