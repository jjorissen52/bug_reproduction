from django.conf.urls import url, include
from django.contrib import admin
from two_factor.urls import urlpatterns as tf_urls
from two_factor.gateways.twilio.urls import urlpatterns as tf_twilio_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include(tf_urls)),
    url(r'', include(tf_twilio_urls)),
]