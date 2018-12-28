import json
import requests

def json_grabber():
  response=requests.get('https://rohitcoder.cf/extra/rakshit/api.php')
  data = json.loads(response.text)
  return data['sentence']
