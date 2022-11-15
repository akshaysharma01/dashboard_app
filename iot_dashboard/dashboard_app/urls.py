from django.urls import path
from .views import home,about,signin,logout,signup

urlpatterns = [
    # path('signup/', RegisterAPI.as_view(), name="signup-url"),
    # path('device/',devices,name='devices-url'),
    # path('details/',device_details,name='details-url'),
    path('signup/',signup,name='signup-url'),
	path('about/',about,name='about-url'),
    path('home/',home,name='home-url'),
    path('', signin, name="signin-url"),
] 