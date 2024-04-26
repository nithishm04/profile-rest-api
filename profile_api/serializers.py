from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kargs ={
          'password' :{
              'write only': True,
              'style':{'input_type': 'paasword'}
          }
        }

    def create(self, validated_data):

        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):

        if 'password in validated_data':
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
