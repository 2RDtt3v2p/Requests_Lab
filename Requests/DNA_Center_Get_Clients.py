import requests
import json
import sys

def get_api_token(domain):
  username = 'devnetuser'
  password = 'Cisco123!'
  api_path = '/dna/system/api/v1/auth/token'

  response = requests.post(f'{domain}{api_path}', auth=(username, password), verify=False)

  if response.status_code == 200:
    return(response.json()['Token'])
  else:
    return(print('Unable to get token, error code:', response.status_code))

if __name__ == "__main__":
  domain = 'https://sandboxdnac2.cisco.com'
  token = get_api_token(domain)
  print('DNA Center API Login Token', token)
