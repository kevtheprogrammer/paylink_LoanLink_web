# serializers.py

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(required=False, allow_null=True)
    nrc_front = serializers.ImageField(required=False, allow_null=True)
    nrc_back = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = ('first_name', 'avatar',  'email', 'nrc_front', 'nrc_back', 'last_name', 'dob',
                  'nrc',   'phone', 'location')

    def update(self, instance, validated_data):
        # Update the user instance with the validated data
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.nrc = validated_data.get('nrc', instance.nrc)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.location = validated_data.get('location', instance.location)

        # Update the avatar field only if it's provided
        avatar = validated_data.get('avatar', None)
        nrc_back = validated_data.get('nrc_back', None)
        nrc_front = validated_data.get('nrc_front', None)

        if avatar:
            instance.avatar = avatar

        if nrc_front:
            instance.nrc_front = nrc_front

        if nrc_back:
            instance.nrc_back = nrc_back

        # Save the changes to the user instance
        instance.save()

        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'avatar', 'avatar',  'email', 'nrc_front', 'nrc_back', 'first_name', 'last_name', 'dob', 'nrc',
                  'phone', 'location', 'date_joined', 'is_active', 'is_verified')
