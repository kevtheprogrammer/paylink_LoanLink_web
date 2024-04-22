from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from userProfile.models import ClientProfile,AgentProfile
from user.models import User
from loan.models import Loan


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

#Client Serializers 
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'address',
                  'credit_score', 'phone','bank','bank_acc','gender')

#Agent Serializers
class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ('agent_id', 'first_name', 'last_name', 'email', 'address',
                   'phone','bank','bank_acc','gender')

#Client register serializer
class ClientRegistrationSerializer(serializers.ModelSerializer):

    profile = ClientSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        ClientProfile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            last_name=profile_data['last_name'],
            phone=profile_data['phone'],
            gender=profile_data['gender'],
            email=profile_data['email']
        )
        return user

#Agnet registration serializer
class AgentRegistrationSerializer(serializers.ModelSerializer):

        profile = AgentSerializer(required=False)

        class Meta:
            model = User
            fields = ('email', 'password', 'profile')
            extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
             profile_data = validated_data.pop('profile', None)
             user = User.objects.create_user(**validated_data)
             if profile_data:
                 AgentProfile.objects.create(
                 user=user,
                **profile_data
            )
             return user

#User login serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        # Validate email and password
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError(
                    'Incorrect email or password.'
                )
        else:
            raise serializers.ValidationError(
                'Both email and password are required.'
            )

        # Generate JWT token
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exist.'
            )

        return {
            'email': user.email,
            'token': jwt_token
        }
    
#Client list serializer
class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all__'

#Loan list serializer
class LoanListSerializer(serializers.ModelField):
    class Meta:
        model = Loan
        fields = '__all__'

#Client details serializer
class ClientDetailsSerializer(serializers.ModelSerializer):
   class Meta:
        model = ClientProfile
        fields = '__all_'


#Client update serializer
class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientProfile
        fields = '__all_'

#Agent update serializer
class AgentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = '__all_'

#Agent list serializer
class AgentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentProfile
        fields = ('agent_id', 'first_name', 'last_name', 'email', 'address',
                   'phone','bank','bank_acc','gender')
        

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = '__all__'