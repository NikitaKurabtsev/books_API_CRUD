from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Books API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/register', include('registration.urls')),
    path('api/v1/swagger/', schema_view),
]
