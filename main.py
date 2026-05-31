import requests

message = "VS Code debugging is working"
version = requests.__version__

print(message)
print("Requests version:", version)