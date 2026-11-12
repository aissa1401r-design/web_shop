import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print(f"URL: '{url}'")
print(f"KEY: '{key}'")
print(f"URL length: {len(url) if url else 0}")
print(f"KEY length: {len(key) if key else 0}")