from django.urls import path

from hanbat.chat.views.views import StaffView, DomitoryView, StudentView

urlpatterns = [
    path('staff', StaffView.as_view()),
    path('domitory', DomitoryView.as_view()),
    path('student', StudentView.as_view())
]