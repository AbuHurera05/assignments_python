import requests

# GET Request Practice
# names = ['Ali','Hamza','Sara','Ahmad']

# for name in names:
#    response = requests.get(f"https://api.agify.io?name={name}")
#    if response.status_code == 200:
#       data = response.json()
#       print(f"Age for name {name}: {data["age"]}")
#    else:
#       print("Faild request due to error")