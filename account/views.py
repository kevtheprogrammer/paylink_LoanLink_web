from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import ClientRegistrationSerializer, AgentRegistrationSerializer
from .serializers import UserLoginSerializer, ClientListSerializer, Userserializer
from .models import User
from account.models import ClientProfile
from rest_framework import viewsets


class ClientRegistrationView(CreateAPIView):

    serializer_class = ClientRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'Client registered  successfully',
            }
        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)



class AgentRegistrationView(CreateAPIView):

      serializer_class = AgentRegistrationSerializer
      permission_classes = (AllowAny,)

      def post(self, request):
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'Doctor registered  successfully',
                }
            status_code = status.HTTP_200_OK
            return Response(response, status=status_code)


class UserLoginView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response = {
                'success' : 'True',
                'status code' : status.HTTP_200_OK,
                'message': 'User logged in  successfully',
                'token' : serializer.data['token'],
                }
            status_code = status.HTTP_200_OK

            return Response(response, status=status_code)


class ClientListViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = ClientProfile.objects.filter(is_client=True)
        serializer_class = ClientListSerializer
        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)

class UserListViewset(viewsets.ViewSet):
     def list(self, request):
          queryset = User.objects.filter(is_client=True)
          serializer_class = Userserializer
          serializer = serializer_class(many=True)
          return Response(serializer.data)
