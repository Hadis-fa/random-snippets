import requests
import sys
import json


# the package that is used for API is request
if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=15&term=" + sys.argv[1]
)

# we have a library called json to format our json file in a better way
# print(json.dumps(response.json(), indent=2))
o = response.json()
for result in o["results"]:
    print(result["trackName"])

#run black "name of your python file" to organize your code
