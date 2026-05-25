from rest_framework import serializers
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate
from .models import Joblist

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

    
    def validate_password(self, value):
        if not re.search(r'[A-Z]', value):
            raise serializers.ValidationError(
                "Password must contain at least one capital letter."
            )

        if not re.search(r'[0-9]', value):
            raise serializers.ValidationError(
                "Password must contain at least one number."
            )

        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password'],
        )
        return user



class SigninSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate(self,data):
        user=authenticate(username=data.get('username'),password=data.get('password'))
       
        if not user:
             raise serializers.ValidationError(" invalid username or password")

        data['user'] = user
        return data


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    new_password = serializers.CharField(write_only=True)





class JobSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Joblist
        fields = [ 'title','company_name','location','experience','skills','salary','description', 
                  'posted_on'
                 ]

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience can't be negative")
        return value

   
   
   
   
   
   
   
   
   
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['skills'] = instance.skills.split(',')
    #     return data














# from rest_framework import serializers
# from django.contrib.auth.models import User

# class SignupSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email','first_name','last_name' ,'password']

#     def create(self, validated_data):
#         user = User.objects.create_user(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             password=validated_data['password'],

#         )
#         return user


# -=============================================================================================

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    JJobSeekerProfile,
    JobSeekerEducation,
    JobSeekerExperience,
    JobSeekerSkill
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class JobSeekerEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerEducation
        fields = "__all__"


class JobSeekerExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerExperience
        fields = "__all__"


class JobSeekerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobSeekerSkill
        fields = "__all__"


class JobSeekerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    educations = JobSeekerEducationSerializer(many=True, read_only=True)
    experiences = JobSeekerExperienceSerializer(many=True, read_only=True)
    skills = JobSeekerSkillSerializer(many=True, read_only=True)

    class Meta:
        model = JJobSeekerProfile
        fields = "__all__"
# =====================messenger===================================================

        
from rest_framework import serializers
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source="sender.username", read_only=True)
    receiver_username = serializers.CharField(source="receiver.username", read_only=True)

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["sender"]



# ============================================================================

from rest_framework import serializers
from .models import Job, Application

class JJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class ApplicationSerializer(serializers.ModelSerializer):
    applicant_name = serializers.CharField(source="applicant.username")

    class Meta:
        model = Application
        fields = ["id", "applicant", "applicant_name", "status"]
# --------------gen AI-------------------------
from rest_framework import serializers

class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()

# ---------just gothrough bus booking s/m------------------

from rest_framework import serializers
from .models import Route, Bus, Seat, Trip, Booking


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"
        read_only_fields = ['user']   # ✅ FIX

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"