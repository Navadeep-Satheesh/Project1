import os
import requests

url = 'https://api.ipify.org'
response = requests.get(url)
ip = response.text
print(ip)

# Call the function to get the IP address
