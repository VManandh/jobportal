from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer,SigninSerializer,ForgotPasswordSerializer,JobSerializer
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .models import Joblist
from rest_framework.permissions import AllowAny


# from rest_framework.permissions import IsAuthenticated

class SignupAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully",
                 "data":serializer.data
                },
                status=status.HTTP_201_CREATED
            )
              
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













# class SigninAPIView(APIView):

#     def post(self, request):
#         serializer = SigninSerializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.validated_data['user']

#             return Response(
#                 {
#                     "message": "Login successful",
#                     "user_id": user.id,
#                     "username": user.username,
#                     "email": user.email
#                 },
#                 status=status.HTTP_200_OK
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        email = serializer.validated_data['email']
        new_password = serializer.validated_data['new_password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        user.set_password(new_password)
        user.save()

        return Response(
            {"message": "Password reset successful"},
            status=status.HTTP_200_OK
        )




class JobListAPIView(APIView):
    def get(self, request):
        jobs = Joblist.objects.all().order_by('-posted_on')
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Job created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class SigninAPIView(APIView):

#     def post(self, request):
#         serializer = SigninSerializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#             login(request, user)   # session-based login

#             return Response(
#                 {"message": "Login successful",
#                  "user":user.username},
#                 status=status.HTTP_200_OK
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class SignoutAPIView(APIView):
#     # permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response(
#             {"message": "Logout successful"},
#             status=status.HTTP_200_OK
#         )








# from rest_framework.generics import CreateAPIView
# from django.contrib.auth.models import User
# from .serializers import SignupSerializer

# class SignupAPIView(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = SignupSerializer




# -===========================================================
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import (
    JJobSeekerProfile,
    JobSeekerEducation,
    JobSeekerExperience,
    JobSeekerSkill
)
from .serializers import (
    JobSeekerProfileSerializer,
    JobSeekerEducationSerializer,
    JobSeekerExperienceSerializer,
    JobSeekerSkillSerializer
)


class JobSeekerProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        profile = request.user.jobseeker_profile
        serializer = JobSeekerProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = request.user.jobseeker_profile
        serializer = JobSeekerProfileSerializer(
            profile, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class EducationCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        data["profile"] = request.user.jobseeker_profile.id
        serializer = JobSeekerEducationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ExperienceCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        data["profile"] = request.user.jobseeker_profile.id
        serializer = JobSeekerExperienceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SkillCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        data["profile"] = request.user.jobseeker_profile.id
        serializer = JobSeekerSkillSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# ====================================================
# ---------------------------------messenger---------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


class SendMessageView(APIView):
    # permission_classes = [AllowAny]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    
    permission_classes = [IsAuthenticated]




    # def post(self, request):

    #   sender = request.user
    #   print("SENDER:", sender)
    #   print("IS EMPLOYER:", hasattr(sender, "employer_profile"))
    #   print("IS JOBSEEKER:", hasattr(sender, "jobseeker_profile"))
    #   return Response({"debug": "working"})

    def post(self, request):
        receiver_id = request.data.get("receiver")
        content = request.data.get("content")

        if not receiver_id or not content:
            return Response(
                {"error": "receiver and content required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            receiver = User.objects.get(id=receiver_id)
        except User.DoesNotExist:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        sender = request.user

        sender_is_js = hasattr(sender, "jobseeker_profile")
        sender_is_emp = hasattr(sender, "employer_profile")

        receiver_is_js = hasattr(receiver, "jobseeker_profile")
        receiver_is_emp = hasattr(receiver, "employer_profile")

        # ✅ Employer → Job Seeker (Always Allowed)
        if sender_is_emp and receiver_is_js:
            Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content
            )
            return Response({"success": "Message sent by employer"})

        # ✅ Job Seeker → Employer (Allowed only if employer sent first)
        if sender_is_js and receiver_is_emp:

            employer_started_chat = Message.objects.filter(
                sender=receiver,   # employer
                receiver=sender    # job seeker
            ).exists()

            if not employer_started_chat:
                return Response(
                    {"error": "You cannot start conversation. Employer must message first."},
                    status=status.HTTP_403_FORBIDDEN
                )

            Message.objects.create(
                sender=sender,
                receiver=receiver,
                content=content
            )

            return Response({"success": "Reply sent to employer"})

        return Response(
            {"error": "Invalid messaging roles"},
            status=status.HTTP_400_BAD_REQUEST
        )

# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import SessionAuthentication, TokenAuthentication
# from rest_framework import status
# from django.contrib.auth.models import User
# from .models import Message
# from .serializers import MessageSerializer


# class SendMessageView(GenericAPIView):

#     serializer_class = MessageSerializer
#     authentication_classes = [SessionAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         receiver_id = request.data.get("receiver")
#         content = request.data.get("content")

#         if not receiver_id or not content:
#             return Response(
#                 {"error": "receiver and content required"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

#         try:
#             receiver = User.objects.get(id=receiver_id)
#         except User.DoesNotExist:
#             return Response(
#                 {"error": "User not found"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         sender = request.user

#         sender_is_js = hasattr(sender, "jobseeker_profile")
#         sender_is_emp = hasattr(sender, "employer_profile")

#         receiver_is_js = hasattr(receiver, "jobseeker_profile")
#         receiver_is_emp = hasattr(receiver, "employer_profile")

#         # ✅ Employer → Job Seeker
#         if sender_is_emp and receiver_is_js:
#             Message.objects.create(
#                 sender=sender,
#                 receiver=receiver,
#                 content=content
#             )
#             return Response({"success": "Message sent by employer"})

#         # ✅ Job Seeker → Employer (Reply Only)
#         if sender_is_js and receiver_is_emp:

#             employer_started_chat = Message.objects.filter(
#                 sender=receiver,
#                 receiver=sender
#             ).exists()

#             if not employer_started_chat:
#                 return Response(
#                     {"error": "You cannot start conversation. Employer must message first."},
#                     status=status.HTTP_403_FORBIDDEN
#                 )

#             Message.objects.create(
#                 sender=sender,
#                 receiver=receiver,
#                 content=content
#             )

#             return Response({"success": "Reply sent to employer"})

#         return Response(
#             {"error": "Invalid messaging roles"},
#             status=status.HTTP_400_BAD_REQUEST
#         )


class ChatHistoryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        messages = Message.objects.filter(
            Q(sender=request.user, receiver_id=user_id) |
            Q(sender_id=user_id, receiver=request.user)
        ).order_by("timestamp")

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)




# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token

# user = User.objects.get(username="tcs_hr")  
# token, created = Token.objects.get_or_create(user=user)

# print(token.key)




from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class SigninAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SigninSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']

            token, created = Token.objects.get_or_create(user=user)

            return Response(
                {
                    "message": "Login successful",
                    "token": token.key,          # 🔥 CRITICAL
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email,

                    # Optional but VERY useful
                    "is_employer": hasattr(user, "employer_profile"),
                    "is_jobseeker": hasattr(user, "jobseeker_profile"),
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# =======================================
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    print("--",permission_classes)

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"})
# =========================================


# {
#    "receiver": 12,
#    "content": "We shortlisted your profile"
# }



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.db.models import Q, Max
from django.contrib.auth.models import User
from .models import Message


class InboxView(APIView):

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        # Get users this person has chatted with
        chat_users = Message.objects.filter(
            Q(sender=user) | Q(receiver=user)
        ).values_list("sender", "receiver")

        participants = set()

        for sender_id, receiver_id in chat_users:
            if sender_id != user.id:
                participants.add(sender_id)
            if receiver_id != user.id:
                participants.add(receiver_id)

        inbox = []

        for participant_id in participants:

            last_msg = Message.objects.filter(
                Q(sender=user, receiver_id=participant_id) |
                Q(sender_id=participant_id, receiver=user)
            ).order_by("-timestamp").first()

            other_user = User.objects.get(id=participant_id)

            inbox.append({
                "user_id": other_user.id,
                "username": other_user.username,
                "last_message": last_msg.content,
                "timestamp": last_msg.timestamp
            })

        # Sort by latest message
        inbox.sort(key=lambda x: x["timestamp"], reverse=True)

        return Response(inbox)


# ==========================================================================================================
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from .models import Job, Application

class EmployerDashboardView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        employer = request.user

        jobs = Job.objects.filter(employer=employer)
        total_jobs = jobs.count()

        applications = Application.objects.filter(job__employer=employer)
        total_applications = applications.count()

        shortlisted = applications.filter(status="shortlisted").count()

        job_data = []

        for job in jobs:
            applicant_count = Application.objects.filter(job=job).count()

            job_data.append({
                "job_id": job.id,
                "title": job.title,
                "applicants": applicant_count
            })

        return Response({
            "employer": employer.username,
            "total_jobs": total_jobs,
            "total_applications": total_applications,
            "shortlisted_candidates": shortlisted,
            "jobs": job_data
        })
# --------------------------------Gen AI--------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
from .serializers import ChatSerializer

client = OpenAI(api_key="")


class ChatBotAPIView(APIView):

    def post(self, request):

        serializer = ChatSerializer(data=request.data)

        if serializer.is_valid():
            user_message = serializer.validated_data['message']

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": user_message}
                ]
            )

            reply = response.choices[0].message.content

            return Response({
                "user_message": user_message,
                "ai_reply": reply
            })

        return Response(serializer.errors)
# -----------------# ---------just gothrough bus booking s/m------------------
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Trip, Seat, Booking
from .serializers import TripSerializer, SeatSerializer, BookingSerializer
from rest_framework import serializers


# Search bus
class SearchTripView(ListAPIView):
    serializer_class = TripSerializer

    def get_queryset(self):
        source = self.request.query_params.get("source")
        destination = self.request.query_params.get("destination")
        date = self.request.query_params.get("date")

        return Trip.objects.filter(
            route__source=source,
            route__destination=destination,
            journey_date=date
        )
 # Get seat availability 
class SeatAvailabilityView(ListAPIView):
    serializer_class = SeatSerializer

    def get_queryset(self):
        trip_id = self.kwargs['trip_id']
        trip = Trip.objects.get(id=trip_id)

        booked_seats = Booking.objects.filter(trip=trip).values_list('seat_id', flat=True)

        return Seat.objects.filter(bus=trip.bus).exclude(id__in=booked_seats)
    
# Book seat Api 
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import Booking
from .serializers import BookingSerializer

class BookSeatView(CreateAPIView):
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        trip = serializer.validated_data['trip']
        seat = serializer.validated_data['seat']

        if Booking.objects.filter(trip=trip, seat=seat).exists():
            raise ValidationError("Seat already booked")

        user = User.objects.first()   # ✅ FIX
        serializer.save(user=user)