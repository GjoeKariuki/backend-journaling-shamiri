from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from django.contrib.auth import authenticate, update_session_auth_hash
from users.serializers import RegisteringUserSerializer, LoginUserSerializer, GetUserSerializer, ChangePasswordSerializer
from users.models import CustomUser
from users.filters import MyUserFilter
# Create your views here.


class Registration(generics.GenericAPIView):
    serializer_class = RegisteringUserSerializer

    def post(self,request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user_data = {"email":email, "password":password}

        serializer = self.get_serializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.save()
      
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class Login(generics.GenericAPIView):
    serializer_class = LoginUserSerializer
    permission_classes = (permissions.AllowAny,)
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response ({
            "user": GetUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })



@api_view(['GET','POST'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_list(request):
    """ POST to create a new user
        GET to list all users
    """
    if request.method == 'GET':
        queryset = CustomUser.objects.all()
        filtered_queryset = MyUserFilter(request.GET,queryset=queryset).qs
        serializer = GetUserSerializer(filtered_queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = RegisteringUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer = GetUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    """ 
    GET individual user record
    PUT to update
    DELETE individual records
    """
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GetUserSerializer(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GetUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@authentication_classes([BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({"message":"Password changed successfully"}, status=status.HTTP_200_OK)
            return Response({"error":"Incorrect 'old_password'"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


