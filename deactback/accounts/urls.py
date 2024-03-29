from django.urls import path
from .views import CreateUserView

app_name = "accounts"

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name="signup")
]
