from django.urls import path,include
# from auth.views import MyObtainTokenPairView, RegisterView
# from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]