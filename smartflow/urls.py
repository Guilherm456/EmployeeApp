
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v1',
      description="API's to create and manage employees and their departments",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls', namespace='api')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
