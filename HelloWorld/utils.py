import base64
import requests
from urllib import parse
import json
import time


TOKEN = ""
TOKEN_EXPIRE = 0
URL = "http://192.168.1.106"
# BASE_URL = 'http://8.136.106.193:8080/'
BASE_URL = URL + ':8080'

AWB_ID_MAP = {
  '160-90001413': '41092587-c3bb-4b94-8d86-1e8c16e61d23',
  '160-90001416': '16d22d95-8c45-475a-aedd-45009ffd1fbb',
  '160-90001419': '1e2c07e6-94a8-452c-aa6f-afd73e2b54bf',
  '160-90001422': 'b04cc4a3-9111-4583-b3c7-9492b02f6bda',
  '160-90001425': '602675d5-10f7-43d0-b490-1e102adf9657',
  '160-90001428': '36294f42-8b05-42f8-8c58-5860ca7836fe',
  '160-90001431': '1de34004-0cdc-4733-885a-a6726de4153e',
  '160-90001434': '4a7d585f-ecd5-4b36-a506-a9a8812882ea'
}

PRODUCT_EXPIRE_DATE_MAP = {
  'dfd3f904-fd4c-4120-8775-b110032419a8': '20250316',
  '4d8893ac-9919-474a-9bad-f04a195adaa8': '20230810',
  '68ae5378-a153-431e-995b-3c1b8b35ca8a': '20240111',
  '5844181f-e932-4133-a250-a849771ade6a': '20250923'
}

PIECE_DETAIL_MAP = {
  '103cf0fb-868e-41d0-96ce-d601b10de136': {
    'grossWeight': 25,
    'volumetricWeight': 20
  },
  'd67da3bf-d718-4306-b5f1-e1f11a77a4cb': {
    'grossWeight': 16,
    'volumetricWeight': 20
  },
  '745fdfc8-d8b5-42c1-802d-b28fb9aff8d6': {
    'grossWeight': 35,
    'volumetricWeight': 33
  },
  '83ed91ee-2b6d-40eb-80c2-4824007965e1': {
    'grossWeight': 30,
    'volumetricWeight': 60
  },
  'a4e2b28f-e47d-45b9-85c5-90605e3e3107': {
    'grossWeight': 24,
    'volumetricWeight': 34
  },
  'aa8d9022-e962-4ca0-b948-861cde36caa6': {
    'grossWeight': 34,
    'volumetricWeight': 22
  },
  '5ce75683-415a-4177-bc18-bd358a56b124': {
    'grossWeight': 25,
    'volumetricWeight': 34
  },
  '1ed09d5e-aece-457f-ab4c-6ac5abc95c2d': {
    'grossWeight': 32,
    'volumetricWeight': 20
  },
  'd6393bee-38e0-4c42-923e-a5cb0eaa1d2f': {
    'grossWeight': 78,
    'volumetricWeight': 88
  },
  '559bdc8e-c635-4391-b7f3-8f5bfa0e183b': {
    'grossWeight': 32,
    'volumetricWeight': 33
  },
  '98ed5abf-6317-43b9-adce-4e69734584f1': {
    'grossWeight': 31,
    'volumetricWeight': 56
  },
  'c841a3af-74b6-4c20-a733-bcd7970d872d': {
    'grossWeight': 56,
    'volumetricWeight': 34
  },
  '7d13e2ab-7489-43cd-bf7f-af6f8b94d8fe': {
    'grossWeight': 45,
    'volumetricWeight': 44
  },
  '51c37027-e11c-4777-8ba7-bd6fc3e33102': {
    'grossWeight': 34,
    'volumetricWeight': 33
  },
  '776b8599-530e-4b3b-a2e9-b12bbc246a75': {
    'grossWeight': 89,
    'volumetricWeight': 77
  },
  'a4e59468-2b17-4fcc-93f6-e3518cb0597f': {
    'grossWeight': 66,
    'volumetricWeight': 76
  },
  'fc26f406-eb4b-430f-8210-8cb73ad2c31e': {
    'grossWeight': 34,
    'volumetricWeight': 33
  },
  'c746fbeb-9598-442a-907d-9dbc9f6c4dce': {
    'grossWeight': 56,
    'volumetricWeight': 55
  },
  '6d1a971d-a243-44de-a9e3-e1009d925288': {
    'grossWeight': 23,
    'volumetricWeight': 32
  },
  '2d788ea9-6d4e-44c4-87b8-98539f9f9b92': {
    'grossWeight': 22,
    'volumetricWeight': 20
  },
}

WAYBILL_PRICE_MAPING = {
  '41092587-c3bb-4b94-8d86-1e8c16e61d23': {
    'bookingId': '63f26d3d-793f-455f-bbed-70592a2b87e2',
    'factor': 0.45
  },
  '16d22d95-8c45-475a-aedd-45009ffd1fbb': {
    'bookingId': 'fdde7c15-0707-4282-801e-53d68a6b385b',
    'factor': 0.62
  },
  '1e2c07e6-94a8-452c-aa6f-afd73e2b54bf': {
    'bookingId': 'b075f329-ae9a-410b-804a-53c6c9b3ea4b',
    'factor': 0.55
  },
  'b04cc4a3-9111-4583-b3c7-9492b02f6bda': {
    'bookingId': 'e1cd059d-7bbf-4b6e-99f2-909e07320245',
    'factor': 0.77
  },
  '602675d5-10f7-43d0-b490-1e102adf9657': {
    'bookingId': '9a2c1a98-4a9d-4601-86c7-2f50ef775a87',
    'factor': 0.47
  },
  '36294f42-8b05-42f8-8c58-5860ca7836fe': {
    'bookingId': '71e9ba92-ff1f-4e70-b3ac-8e8307e501e0',
    'factor': 0.62
  },
  '1de34004-0cdc-4733-885a-a6726de4153e': {
    'bookingId': 'bd4a40e0-81c9-47b9-a601-3a76496701ed',
    'factor': 0.43
  },
  '4a7d585f-ecd5-4b36-a506-a9a8812882ea': {
    'bookingId': 'ffef3d57-1ca1-467c-b8ab-d015b3bea144',
    'factor': 0.64
  }
}


# ####################################################################################################

def getPriceByWaybill(waybillId):
  if waybillId in WAYBILL_PRICE_MAPING:
    return WAYBILL_PRICE_MAPING[waybillId]

def getDetailByPiece(pieceId):
  if pieceId in PIECE_DETAIL_MAP:
    return PIECE_DETAIL_MAP[pieceId]

def getExpireDateByProductId(productId):
  if productId in PRODUCT_EXPIRE_DATE_MAP:
    return PRODUCT_EXPIRE_DATE_MAP[productId]

def getAwbIdMap():
  return AWB_ID_MAP

def getIdByMawb(mawb):
  if mawb in AWB_ID_MAP:
    return AWB_ID_MAP[mawb]
  

def getTokenHeader():
  headers = {
    "Authorization": "Bearer " + getToken(),
    "Content-Type": "application/ld+json",
    "Accept": "application/ld+json"
  }
  return headers


def getBaseUrl():
  return BASE_URL

def setToken(token, expiresIn):
  global TOKEN
  global TOKEN_EXPIRE
  TOKEN_EXPIRE = time.time() * 1000 + expiresIn
  TOKEN = token
  # print(">>> expire in: " + str(TOKEN_EXPIRE) + ", token: " + TOKEN)
  return TOKEN

def getToken():
  t = time.time() * 1000 # 毫秒级时间戳

  TOKEN_EXPIRE
  if TOKEN_EXPIRE < t:
    return generateToken()
  return TOKEN

def generateToken():
  print("Getting token...")
  url = URL + ":8989/realms/neone/protocol/openid-connect/token"
  username = 'neone-client'
  password = 'lx7ThS5aYggdsMm42BP3wMrVqKm9WpNY'
  secret = username + ':' + password
  bs = str(base64.b64encode(secret.encode("utf-8")), 'utf-8')
  headers = {
    "Authorization": "Basic {}".format(bs),
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br"
  }

  payload = parse.urlencode({
    'grant_type': 'client_credentials',
    'client_id': 'neone-client'
  })

  jsonObj = reqs("POST", url, payload, headers)
  expiresIn = int(jsonObj['expires_in'])
  setToken(jsonObj['access_token'], expiresIn)
  return getToken()



def reqs(method, url, payload, headers):
  default_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
  }
  default_headers.update(headers)
  res = {}
  if "get" == method.lower():
    res = requests.get(url, headers = default_headers)
  if 'post' == method.lower():
    res = requests.post(url, headers = default_headers, data = payload)
  if 'delete' == method.lower():
    res = requests.delete(url, headers = default_headers)
  if 'put' == method.lower():
    res = requests.put(url, headers = default_headers, data = payload)
  if 'patch' == method.lower():
    res = requests.patch(url, headers = default_headers, data = payload)
  # print(">>> res:")
  # print("\n--- REQUESTING url: ", url)
  # print("code:", res.status_code)
  # print("text:", res.text)
  # print("-----------------------------------")
  return json.loads(res.text)


def getRealId(id):
  realId = id.split("/")[-1]
  return realId

'''
检查列表obj[key]是否存在且长度大于0
'''
def checkList(key, obj):
  return key in obj and len(obj[key]) > 0