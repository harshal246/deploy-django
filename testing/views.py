from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

import json

@api_view(["GET"])
def testing(request):
    print(json.loads(request.body.decode("utf-8")))
    return Response({"done":True})

