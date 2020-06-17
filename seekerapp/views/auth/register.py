import json 
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from django.views.decorators.csrf import csrf_exempt
from seekerapp.models import Seeker

# Csrf_exempt is an access token
@csrf_exempt
def register_user(request): 
    req_body = json.loads(request.body.decode())
    # Information that will be taken from the AuthUser 
    new_user = User.objects.create_user(
        username=req_body['username'], 
        password=req_body['password'], 
        first_name=req_body['firstName'], 
        last_name=req_body['lastName'], 
    )
    # Seeker is equal to user that comes from Django as well as city & state
    seeker = Seeker.objects.create(
        city=req_body['city'], 
        state=req_body['state'],
        user=new_user
    )

    seeker.save()
    # Creates association with token and user
    token = Token.objects.create(user=new_user)
    # Django way of converting to JSON
    data = json.dumps({"valid": True, "token": token.key, "seeker_id": new_user.seeker.id})

    return HttpResponse(data, content_type='application/json')