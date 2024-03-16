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

  #STEPS THROUGH THE LIST BASED ON NUMBER OF ITMES IN THE LIST
  #for i in device:
  #FOR EACH DEVICE IN THE LIST PRINTS THE ID AND MGMT IP
  #  print('Device ID:', device['id'], 'Device IP:', device['managementIpAddress']) 
  return()

def add_device(domain, token):
  api_path = '/dna/intent/api/v1/network-device'
  device = {
  'ipAddress': ['192.0.2.1'],
  'snmpVersion': 'v2',
  'snmpROCommunity': 'readonly',
  'snmpRWCommunity': 'readwrite',
  'snmpRetry': '1',
  'snmpTimeout': '60',
  'cliTransport': 'ssh',
  'userName': 'devuser1',
  'password': 'secret123!',
  'enablePassword': 'secret456!',
  }

  headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }

  response = requests.post(f'{domain}{api_path}', headers=headers, json=device, verify=False)
  print(response)

  return()

if __name__ == "__main__":
  domain = 'https://sandboxdnac2.cisco.com'

  token = get_api_token(domain)
  print('DNA Center API Login Token', token)

 # device = get_device_list(domain, token)
 # print('Device list: \n', json.dumps(device, indent=2))
 # get_device_info(device)

  add_device(domain, token)