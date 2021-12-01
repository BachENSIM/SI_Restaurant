from django.conf.urls import url
from RestaurantApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^restaurent$', views.restaurant_api),
    url(r'^restaurent/([0-9]+)$', views.restaurant_api),

    url(r'^code_qr$', views.code_qr_api),
    url(r'^code_qr/([0-9]+)$', views.code_qr_api),

    url(r'^menu$', views.menu_api),
    url(r'^menu/([0-9]+)$', views.menu_api),

    url(r'^plat$', views.plat_api),
    url(r'^plat/([0-9]+)$', views.plat_api),

    url(r'^table$', views.table_api),
    url(r'^table/([0-9]+)$', views.table_api),

    url(r'^save_file', views.file_transfer_api)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
