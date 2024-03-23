from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status   


@api_view(['GET', 'POST'])
def user_api_view(request):

    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":

        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors)
    
@api_view(["GET", "PUT", "DELETE"])
def user_detail_view(request, pk=None):
    user = User.objects.filter(id=pk).first()

    if user:
        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == "PUT":
            user_serializer = UserSerializer(user, data=request.data )
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == "DELETE":
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({"Message":"Exitosamente eliminado!!"}, status=status.HTTP_204_NO_CONTENT)

    else:
        return Response({"message": "El usuario de esta consulta no existe"}, status=status.HTTP_400_BAD_REQUEST)