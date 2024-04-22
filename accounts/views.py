 
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .forms import UploadUsersCSVForm
from django.contrib.auth import logout
from django.views.generic import CreateView
from .forms import UserCreationForm
from django.urls import reverse_lazy
import pandas as pd
from django.contrib.auth.hashers import make_password
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(email=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    user = get_object_or_404(User, email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    token = Token.objects.create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

# User views

class UserListView(ListView):
     model = User
     template_name = 'users/users.html'
     context_object_name = 'users'

     def get_context_data(self, *args, **kwargs):
          context = super().get_context_data(**kwargs)
          paginator = Paginator(self.object_list, 10)
          page_number = self.request.GET.get('page')
          page_obj = paginator.get_page(page_number)
          context['page_obj'] = page_obj

        #   user_count = User.objects.all().count()
        # #   print('user_count --->',user_count)
        #   context['user_count'] = user_count

          return context


class UserDetailView(DetailView):
     model = User
     template_name = 'users/user.html'
     context_object_name = 'user'

class UserDeleteView(DeleteView):
     model = User
     success_url = reverse_lazy('user-list')
     template_name = 'users/user.html'

def upload_users_csv(request):
    if request.method == 'POST':
        form = UploadUsersCSVForm(request.POST, request.FILES)

        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']

            try:
                # Read the CSV file using pandas
                users = pd.read_csv(csv_file, encoding='latin-1')

                # Iterate through rows and create User objects
                for index, row in users.iterrows():
                    # Convert the password field to a string
                    password_str = str(row['password'])

                    User.objects.create(
                        email=row['email'],
                        password=make_password(password_str),
                        first_name=row['first_name'],
                        last_name=row['last_name']
                    )

                return HttpResponse("Users created successfully.")
            except Exception as e:
                return HttpResponse(f"Error: {e}")
    else:
        form = UploadUsersCSVForm()

    return render(request, 'upload_csv.html', {'form': form})


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name ='registration/signup.html'


# def register(request):
#      if r
def logout_view(request):
     if request.method == 'POST':
          logout(request)
          return redirect('login')
     return render(request, 'registration/logged_out.html')
 

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')
 