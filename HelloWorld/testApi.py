from django.http import HttpResponse
from . import utils

def hello(request):
  res = "Hi~"
  return HttpResponse(res)

def generateToken(request):
  if request.method == 'POST':
    token = utils.generateToken()
    return HttpResponse(token)
