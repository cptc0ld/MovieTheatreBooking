from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    path('api/', include('customer.api.urls')),
    path('', include('shows.api.urls'))
]
