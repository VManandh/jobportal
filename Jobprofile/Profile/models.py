from django.db import models
class Joblist(models.Model):
    title=models.CharField(max_length=20,blank=True, null=True)
    company_name=models.CharField(max_length=30)
    skills=models.CharField(max_length=100)
    experience=models.PositiveBigIntegerField()
    location=models.CharField(max_length=30)
    salary=models.IntegerField()
    description=models.TextField()
    posted_on=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    marital_status = models.CharField(max_length=20)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    
#  ------------------=================-----------------=====================--------------------------------------------------
from django.db import models
from django.contrib.auth.models import User


class JJobSeekerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="jobseeker_profile"
    )

    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class JobSeekerEducation(models.Model):
    profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name="educations"
    )

    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    passing_year = models.CharField(max_length=10)
    percentage = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
class JobSeekerExperience(models.Model):
    profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name="experiences"
    )

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    currently_working = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"

class JobSeekerSkill(models.Model):
    profile = models.ForeignKey(
        JobSeekerProfile,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
# ==============messenger part=====================

# from django.db import models
# from django.contrib.auth.models import User

# class JobSeekerProfile_Msgner(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         related_name="jobseeker_profile"
#     )
#     full_name = models.CharField(max_length=200)


class EmployerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="employer_profile"
    )
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class Message(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="received_messages"
    )

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"
# -============================================================================================



from django.db import models
from django.contrib.auth.models import User

class EEmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.company_name


class Job(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default="applied")  
    # applied / shortlisted / rejected

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"


# from django.contrib.auth.models import User
# from Your_app_name.models import EmployerProfile, Job, Application

# employer = User.objects.create_user(username="employer1", password="1234")

# EmployerProfile.objects.create(
#     user=employer,
#     company_name="Infosys",
#     location="Bangalore"
# )

# Job.objects.create(
#     employer=employer,
#     title="Backend Developer",
#     description="Need DRF Developer"
# )

# applicant = User.objects.create_user(username="STR", password="1234")

# job = Job.objects.first()

# Application.objects.create(
#     job=job,
#     applicant=applicant,
#     status="applied"
# )








# from django.contrib.auth.models import User
# from Profile(your_app_name).models import EEmployerProfile

# employer = User.objects.create_user(username="employer1", password="1234")

# EEmployerProfile.objects.create(
#     user=employer,
#     company_name="Infosys",
#     location="Bangalore"
# )

# from django.contrib.auth.models import User
# from Profile.models import Job
# employer = User.objects.get(username="employer1")
# Job.objects.create(
#     employer=employer
#     title="Backend Developer",
#     description="Need DRF Developer"
# )
  

# #step1 from django.contrib.auth.models import User
# #step2 from Profile.models import  Application
# If you know job id:
# s3 job = Job.objects.get(id=1) or job = Job.objects.get(title="Backend Developer")


# (or)
# If unsure, list jobs:
# Job.objects.all() but dont use this because job is a foreign key you can select only one job at a time

# If user exists:
# s4 applicant = User.objects.get(username="STR")

# (or )
# If not created yet:
# # applicant = User.objects.create_user(username="STR", password="1234")

# s5 Application.objects.create(
#     job=job,
#     applicant=applicant,
#     status="applied"
# )


# ---------just gothrough bus booking s/m------------------
from django.db import models
from django.contrib.auth.models import User


class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    distance = models.IntegerField()

    def __str__(self):
        return f"{self.source} to {self.destination}"


class Bus(models.Model):
    bus_name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=20)
    total_seats = models.IntegerField()

    def __str__(self):
        return self.bus_name


class Seat(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"{self.bus.bus_name} Seat {self.seat_number}"


class Trip(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    journey_date = models.DateField()
    departure_time = models.TimeField()

    def __str__(self):
        return f"{self.bus.bus_name} - {self.journey_date}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} booked {self.seat}" 