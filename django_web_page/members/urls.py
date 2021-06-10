from django.urls import path
from .views import UserRegisterView,UserEditProfileView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/', UserEditProfileView.as_view(), name = 'edit_user'),
    # path('<int:pk>/Profile', ShowProfile.as_view(), name ="profilePage" )
]
