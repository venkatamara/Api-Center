from django.urls import path

from userauth.token_controller import SignUp, Signin, UserInfo, UserCreation, UserDetails, UserPicture

urlpatterns = [

    path('signup', SignUp.as_view()),
    path('signin', Signin.as_view()),
    path('user', UserInfo.as_view()),
    path('create/<int:id>', UserCreation.as_view()),
    path('info/<int:id>', UserDetails.as_view()),
    path('picture/<int:id>', UserPicture.as_view())

]