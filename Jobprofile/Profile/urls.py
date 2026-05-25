# from django.urls import path
# from .views import (
#     SignupAPIView,
#     SigninAPIView,
#     ForgotPasswordAPIView,
#     JobListAPIView,
#     JobSeekerProfileView,
#     EducationCreateView,
#     ExperienceCreateView,
#     SkillCreateView,SendMessageView,ChatHistoryView
# )

# urlpatterns = [
#     # Auth
#     path('signup/', SignupAPIView.as_view()),
#     path('signin/', SigninAPIView.as_view()),
#     path('forgot-password/', ForgotPasswordAPIView.as_view()),

#     # Jobs
#     path('joblist/', JobListAPIView.as_view()),

#     # Jobseeker profile
#     path("jobseeker/profile/", JobSeekerProfileView.as_view()),
#     path("jobseeker/education/", EducationCreateView.as_view()),
#     path("jobseeker/experience/", ExperienceCreateView.as_view()),
#     path("jobseeker/skill/", SkillCreateView.as_view()),

# #   ------------------------messenger------------------
#     path("send-message/", SendMessageView.as_view()),
#     path("chat/<int:user_id>/", ChatHistoryView.as_view()),

# ]


from django.urls import path
from .views import (
    SignupAPIView,
    SigninAPIView,
    ForgotPasswordAPIView,
    JobListAPIView,
    JobSeekerProfileView,
    EducationCreateView,
    ExperienceCreateView,
    SkillCreateView,
    SendMessageView,
    ChatHistoryView,
    LogoutView,InboxView,EmployerDashboardView,

    ChatBotAPIView,

    SearchTripView, SeatAvailabilityView, BookSeatView
)

urlpatterns = [
    # Auth
    path('signup/', SignupAPIView.as_view()),
    path('signin/',SigninAPIView.as_view()),
    path('forgot-password/', ForgotPasswordAPIView.as_view()),

    # Jobs
    path('joblist/', JobListAPIView.as_view()),

    # Jobseeker profile
    path("jobseeker/profile/", JobSeekerProfileView.as_view()),
    path("jobseeker/education/", EducationCreateView.as_view()),
    path("jobseeker/experience/", ExperienceCreateView.as_view()),
    path("jobseeker/skill/", SkillCreateView.as_view()),

    # Messenger
    path("send-message/", SendMessageView.as_view()),
    path("chat/<int:user_id>/", ChatHistoryView.as_view()),

    path("logout/", LogoutView.as_view(), name="logout"),
    path("inbox/", InboxView.as_view()),
    # ---------------------------------------------------------
    path("employer/dashboard/", EmployerDashboardView.as_view()),   
# -----------Gen AI-----------------------------------
    path('chat/', ChatBotAPIView.as_view()),
    


#   ----------------------bus booking--------------------------------
    path('search-trip/', SearchTripView.as_view()),
    path('available-seats/<int:trip_id>/', SeatAvailabilityView.as_view()),
    path('book-seat/', BookSeatView.as_view()),

]


