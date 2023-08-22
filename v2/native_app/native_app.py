import sys
import json

message = json.loads(sys.stdin.read())
response = {"response": "Hello from native application!"}
sys.stdout.write(json.dumps(response))
sys.stdout.flush()
