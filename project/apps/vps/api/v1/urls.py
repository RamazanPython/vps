from django.urls import path

from vps.api.v1.views import VpsViewSet

urlpatterns = [
    path("", VpsViewSet.as_view({"get": "list", "post": "create"}), name="vps_list"),
    path("<uid>/", VpsViewSet.as_view({"get": "retrieve"}), name="vps_detail"),
    path("<uid>/change_status/", VpsViewSet.as_view({"put": "change_status"}), name="vps_change_status"),
]
