import json 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from django.views.decorators.csrf import csrf_exempt
from seekerapp.models import Seeker

@csrf_exempt
def login_user(request): 
    req_body = json.loads(request.body.decode())

    if request.method == 'POST': 
        username = req_body['username']
        password = req_body['password']
        authenticated_user = authenticate(username=username, password=password)

        if authenticated_user is not None: 
            # From the token, get the user whose information matches the authenticated user
            token = Token.objects.get(user=authenticated_user)
            # Dumps returns a string representing a json object from an object
            data = json.dumps({"valid": True, "token": token.key, "seeker_id": authenticated_user.seeker.id})
            return HttpResponse(data, content_type="application/json")
        else: 
            data = json.dumps({"valid": False})
            return HttpResponse(data, content_type="application/json")