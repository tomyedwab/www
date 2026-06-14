import os
import sys

from dotenv import load_dotenv

from atproto import Client

load_dotenv()

c = Client()
c.login(os.getenv("BLUESKY_LOGIN"), os.getenv("BLUESKY_PASSWORD"))
print("Logged into BlueSky")

with open(sys.argv[1], "rb") as f:
    contents = f.read()
print(f"Read {len(contents)} bytes.")

upload = c.upload_blob(contents)
print(f"Uploaded blob: {upload.blob}")
