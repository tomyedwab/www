import json
import os
import sys

from atproto import Client, models
from dotenv import load_dotenv

load_dotenv()

c = Client()
c.login(os.getenv("BLUESKY_LOGIN"), os.getenv("BLUESKY_PASSWORD"))
print("Logged into BlueSky")

with open(sys.argv[1]) as f:
    contents = json.load(f)

if contents["$type"] == "site.standard.publication":
    r = models.SiteStandardPublication.Record.model_validate(contents)
elif contents["$type"] == "site.standard.document":
    r = models.SiteStandardDocument.Record.model_validate(contents)
else:
    raise Exception("unknown type: " + contents["$type"])
print(f"Record parsed: {r}")


with open("cids.json") as f:
    cids = json.load(f)
print("Loaded CIDs")

record = c.com.atproto.repo.create_record(
    models.ComAtprotoRepoCreateRecord.Data(
        repo=c.me.did,
        collection=contents["$type"],
        record=r,
    )
)
print(f"Uploaded record: {record}")

cids[sys.argv[1]] = {
    "cid": record.cid,
    "uri": record.uri,
}
with open("cids.json", "w") as f:
    json.dump(cids, f, indent=2)
