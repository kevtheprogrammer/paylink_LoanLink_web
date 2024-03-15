
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import RetrieveAPIView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView


class SignInView(TokenObtainPairView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        response.data['access_token'] = access_token
        return response


class SignUpView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        return self.request.user


class UserDetailsView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class DashboardView(TemplateView):
    template_name = '_admin/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['au'] = User.objects.filter(is_active=True).count()
        context['vu'] = User.objects.filter(is_verified=True).count()
        context['users'] = User.objects.all() 
        context['await_vu'] = User.objects.all().count() - User.objects.filter(is_verified=True).count()

        return context



class UserListView(ListView):
    model = User
    template_name = '_admin/users-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['au'] = User.objects.filter(is_active=True).count()
        context['vu'] = User.objects.filter(is_verified=True).count()
        context['users'] = User.objects.all().count()
        context['await_vu'] = User.objects.all().count(
        ) - User.objects.filter(is_verified=True).count()

        return context


class UserDetailView(DetailView):
    model = User
    template_name = '_admin/user-detail.html'
    context_object_name = 'object'


def togleVerifyUser(request, pk):
    user = User.objects.get(pk=pk)
    print('user', user)
    if user.is_verified:
        user.is_verified = False
        user.save()
        return redirect(user.get_absolute_url())
    else:
        user.is_verified = True
        user.save()
        return redirect(user.get_absolute_url())
