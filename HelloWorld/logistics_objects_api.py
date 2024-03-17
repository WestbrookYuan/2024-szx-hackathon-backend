from django.http import HttpResponse
from . import utils
import json
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'./AITest'))
import BailianTest

GET = 'GET'
POST = 'POST'
DEL = "DELETE"
PATHC = 'PATCH'
PUT = 'PUT'

baseUrl = utils.getBaseUrl()



def sort(request):
  print("\n\n--------------------------")
  if request.method == POST:
    body = json.loads(request.body)
    # print(body)
    bailian = BailianTest.CompletionTest()
    resStr = bailian.test_third_model_completions(json.dumps(body))
    if resStr:
      resStr = resStr.split('```json', 1)[1]
      resStr = resStr.split('```', 1)[0]
    print("\n>>> resStr:\n", resStr)
    orders = json.loads(resStr)
    res = []
    for order in orders:
      for i in body:
        if i["pieceId"] in order.keys():
          r = i.copy()
          r["reason"] = order[i['pieceId']]
          res.append(r)
  return HttpResponse(json.dumps(res), content_type="application/json")
  

def getByAwbNumList(request):
  print("\n\n-----------------------------------")
  if request.method == POST:
    # print("\n>>> ", request.body)
    awbs = json.loads(request.body)
    res = []
    for awb in awbs:
      res += getBySingleAwbNum(awb)
    # res.reverse()
    return HttpResponse(json.dumps(res), content_type="application/json")


def getByAwbNum(request, awbNum):
  print("\n\n-----------------------------------")
  if request.method == GET:
    res = getBySingleAwbNum(awbNum)
    return HttpResponse(json.dumps(res), content_type="application/json")

def getBySingleAwbNum(awbNum):
  
  res = []
  itemObj = {}

  headers = utils.getTokenHeader()
  baseUrl = utils.getBaseUrl() + '/logistics-objects/'
  
  # awb:
  awbId = utils.getIdByMawb(awbNum)
  if not awbId:
    return HttpResponse(json.dumps(None), content_type="application/json")
  itemObj['awbId'] = awbId
  itemObj['awbNum'] = awbNum

  if awbId:
    print("\n>>> awbObj:")
    awbObj = utils.reqs(GET, baseUrl + awbId, None, headers)
    # print(awbObj)

    # price:
    totalGrossWeight = 0

    priceData = utils.getPriceByWaybill(awbId)
    if priceData:
      priceStr = getPriceByBookingId(priceData['bookingId'])
      print("\n>>> priceStr:", priceStr)
      price = int(priceStr)
      itemObj["cost"] = int(price * priceData['factor'])
      itemObj["price"] = price
    
    # pieces and handlingInstructions:
    pieces = getPiecesByAwbObj(awbObj)
    if pieces:
      for piece in pieces:
        print("\n>>> piece:", piece)
        if "@id" in piece:
          obj = itemObj.copy()
          pieceId = utils.getRealId(piece["@id"])
          print("\n>>> pieceId:", pieceId)
          obj['pieceId'] = pieceId
          pieceDetail = utils.getDetailByPiece(pieceId)
          print("\n>>> pieceDetail:", pieceDetail)
          if pieceDetail:
            obj['grossWeight'] = pieceDetail['grossWeight']
            # obj['volumetricWeight'] = pieceDetail['volumetricWeight']
            totalGrossWeight += int(pieceDetail['grossWeight'])
            
          if 'goodsDescription' in piece:
            obj['goodsDescription'] = piece['goodsDescription']
          if 'handlingInstructions' in piece:
            obj['handlingInstructions'] = piece['handlingInstructions']

          # product:
          products = []
          if utils.checkList('containedItems', piece):
            for itemId in piece['containedItems']:
              prodObj = {}
              itemId = utils.getRealId(itemId)
              print("\n>>> itemId:", itemId)
              productItem = utils.reqs(GET, baseUrl + itemId, None, headers)
              print("\n>>> productItem:\t", productItem)
              if '@type' in productItem and productItem['@type'][1] == 'Product':
                if 'description' in productItem:
                  prodObj['description'] = productItem['description']

                products.append(prodObj)  
          obj["products"] = products
        res.append(obj)

      if 'cost' in itemObj and 'price' in itemObj:
        unitProfit = (itemObj['price'] - itemObj['cost']) / totalGrossWeight
        unitProfit = int(unitProfit)
        for i in res:
          i['unitProfit'] = unitProfit
          
  return res


def getPriceByBookingId(awbId):
  headers = utils.getTokenHeader()
  baseUrl = utils.getBaseUrl() + '/logistics-objects/'

  # booking:
  bookingObj = utils.reqs(GET, baseUrl + awbId, None, headers)
  if 'BookingRequest' in bookingObj and '@id' in bookingObj['BookingRequest']:
    bookingRequestId = utils.getRealId(bookingObj['BookingRequest']['@id'])
    bookingReqObj = utils.reqs(GET, baseUrl + bookingRequestId, None, headers)
    print("\n>>> bookingReqObj:", bookingReqObj)
    if 'BookingOption' in bookingReqObj and '@id' in bookingReqObj['BookingOption']:
      bookingOptId = utils.getRealId(bookingReqObj['BookingOption']['@id'])
      bookingOptObj = utils.reqs(GET, baseUrl + bookingOptId, None, headers)
      print('\n>>> bookingOptObj:', bookingOptObj)
      if 'Price' in bookingOptObj and '@id' in bookingOptObj['Price']:
        priceId = utils.getRealId(bookingOptObj['Price']['@id'])
        priceObj = utils.reqs(GET, baseUrl + priceId, None, headers)
        print("\n>>> price: ", priceObj)
        if '@graph' in priceObj:
          for graph in priceObj['@graph']:
            if 'numericalValue' in graph and '@value' in graph['numericalValue']:
              return graph['numericalValue']['@value']






def getPiecesByAwbObj(awbObj):
  headers = utils.getTokenHeader()
  baseUrl = utils.getBaseUrl() + '/logistics-objects/'

  # shipment:
  if 'shipment' in awbObj:
    shipmentIdObj = awbObj["shipment"]
    if '@id' in shipmentIdObj:
      shipId = utils.getRealId(shipmentIdObj['@id'])
      print("\n>>> shipObj:")
      shipObj = utils.reqs(GET, baseUrl + shipId, None, headers)
      print(shipObj)
      goodsDescription = ''
      if 'goodsDescription' in shipObj:
        goodsDescription = shipObj['goodsDescription']
      print('\n>>> goodsDescription:', goodsDescription)
      # pieces:
      if 'pieces' in shipObj:
        pieceIdObjs = shipObj['pieces']
        if isinstance(shipObj['pieces'], dict):
          pieceIdObjs = [shipObj['pieces']]
        res = []
        for pieceIdObj in pieceIdObjs:
          if '@id' in pieceIdObj:
            pieceId = utils.getRealId(pieceIdObj['@id'])
            print("\n>>> pieceObj")
            pieceObj = utils.reqs(GET, baseUrl + pieceId, None, headers)
            print(pieceObj)
            if '@graph' in pieceObj:
              piece = None
              handlingInstructions = []
              for graph in pieceObj['@graph']:
                if '@type' in graph and graph['@type'][1] == 'Piece':
                  graph["goodsDescription"] = goodsDescription
                  piece = graph
                if '@type' in graph and graph['@type'] == 'HandlingInstructions':
                  handlingInstructions.append(graph['serviceTypeCode'])
              piece['handlingInstructions'] = handlingInstructions
              res.append(piece)
        return res



def getById(request, awbNum):
  print("\n\n\n\n-----------------------------------")
  if request.method == GET:
    res = []
    itemObj = {}

    headers = utils.getTokenHeader()
    baseUrl = utils.getBaseUrl() + '/logistics-objects/'

    # mawb:
    mawbId = utils.getIdByMawb(awbNum)
    itemObj['mawbId'] = mawbId
    itemObj['awbNumber'] = awbNum
    if mawbId:
      # print(">>> mawbObj:")
      mawbObj = utils.reqs(GET, baseUrl + mawbId, None, headers)
      if utils.checkList('@graph', mawbObj):
        for mawbGraph in mawbObj['@graph']:
          if utils.checkList('houseWaybills', mawbGraph):
            # print(">>> mawbGraph:", mawbGraph)
            # print(">>> houseWaybills:", mawbGraph['houseWaybills'])
            hawbIdObjList = mawbGraph['houseWaybills']
            if '@id' in mawbGraph['houseWaybills']:
              hawbIdObjList = [mawbGraph['houseWaybills']]
            for idObj in hawbIdObjList:
              # print(">>> idObj: ", idObj)
              if '@id' in idObj:
                # hawb:
                print("idObj['@id']: ", idObj['@id'])
                hawbId = utils.getRealId(idObj['@id'])
                hawbObj = utils.reqs(GET, baseUrl + hawbId, None, headers)
                print(">>> hawbObj:", hawbObj)
                
                if 'waybillNumber' in hawbObj:
                  itemObj["hawbNumber"] = hawbObj["waybillNumber"]
                  itemObj["hawbId"] = utils.getRealId(hawbObj["@id"])

                # shipment:
                if 'shipment' in hawbObj:
                  shipmentIdObj = hawbObj["shipment"]
                  products = []
                  if shipmentIdObj and '@id' in shipmentIdObj and shipmentIdObj['@id']:
                    shipmentId = utils.getRealId(shipmentIdObj['@id'])
                    itemObj["shipmentId"] = shipmentId
                    shipmentObj = utils.reqs(GET, baseUrl + shipmentId, None, headers)
                    print(">>> shipmentObj: ", shipmentObj)

                    # piece:
                    piecesIdObjList = []
                    if 'pieces' in shipmentObj:
                      piecesIdObjList = shipmentObj['pieces']
                    for piecesIdObj in piecesIdObjList:
                      print(">>> piecesIdObj: ", piecesIdObj)
                      if "@id" in piecesIdObj and piecesIdObj["@id"]:
                        pieceId = utils.getRealId(piecesIdObj["@id"])
                        pieceObj = utils.reqs(GET, baseUrl + pieceId, None, headers)
                        print(">>> pieceObj: ", pieceObj)

                        # product:
                        if '@graph' in pieceObj and len(pieceObj['@graph']) > 0:
                          for graph in pieceObj['@graph']:
                            if 'contentProducts' in graph and '@id' in graph['contentProducts']:
                              productId = utils.getRealId(graph['contentProducts']['@id'])
                              productObj = utils.reqs(GET, baseUrl + productId, None, headers)
                              print(">>> productObj:", productObj)

                              if '@graph' in productObj and len(productObj['@graph']) > 0:
                                for graph2 in productObj['@graph']:

                                  obj = itemObj.copy()

                                  if 'codeDescription' in graph2:
                                    obj['productCodeDescription'] = graph2['codeDescription']

              #                     # if '' in graph2:

                                  res.append(obj)













    return HttpResponse(json.dumps(res), content_type="application/json")


def getAwbList(request):
  if request.method == GET:
    map = utils.getAwbIdMap()
    list = []
    for i in map:
      print(i)
      list.append(i)
    return HttpResponse(json.dumps(list), content_type="application/json")


# def getById(request, id):
#   if request.method == GET:
#     print(">>> requesting: " + baseUrl + "/logistics-objects/" + id)
#     headers = utils.getTokenHeader()
#     res = requests.get(baseUrl + "/logistics-objects/" + id, headers = headers)
#     return res
    




