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

def get_device_list(domain, token):
  api_path = '/dna/intent/api/v1/network-device'
  payload = None
  header = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json',
    'Accept': 'application/json' 
  }

  response = requests.get(f'{domain}{api_path}', headers=header, data=payload, verify=False)

  if response.status_code == 200:
    return(response.json()['response'])
  else: 
    return(print('Unable to get device list, error code:', response.status_code))

def get_device_info(device):
  for i in range(0, len(device)):
    print('Device', i, '\nName:', device[i]['hostname'], '\nID:', device[i]['id'], '\nIP:', device[i]['managementIpAddress'])
  return()

if __name__ == "__main__":
  domain = 'https://sandboxdnac2.cisco.com'

  token = get_api_token(domain)
  print('DNA Center API Login Token', token)

  device = get_device_list(domain, token)
  print('Device list: \n', json.dumps(device, indent=4))
  get_device_info(device)
