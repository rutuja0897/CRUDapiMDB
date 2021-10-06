from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from tutorials.models import User
from tutorials.serializers import UserSerializer

# Create your views here.

@csrf_exempt
def UserApi(request,id=0):
    if request.metho=='GET':
        users=User.objects.all()
        user_serializer=UserSerializer(users,many=True)
        return JsonResponse(user_serializer.data,safe=False)

    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)


    elif request.metho=='PUT':
        user_data=JSONParser().parse(request)
        user=User.objects.get(UserId=user_data['UserId'])
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update successfully",safe=False)
        return JsonResponse("Failed to update")

    elif request.method=="DELETE":
        user=User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)

