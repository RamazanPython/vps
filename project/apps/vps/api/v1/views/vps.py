from rest_framework.decorators import action
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema_view

from vps.api.v1.serializers import VpsChangeStatusSerializer, VpsCreateSerializer, VpsListSerializer
from vps.api.v1.filters import VpsFilter
from vps.api.v1.docs import vps_schema
from vps.models import Vps
from utils.mixins import MethodMatchingViewSetMixin


@extend_schema_view(**vps_schema)
class VpsViewSet(MethodMatchingViewSetMixin,
                 ListModelMixin,
                 RetrieveModelMixin,
                 CreateModelMixin,
                 GenericViewSet):
    queryset = Vps.objects.all()
    model = Vps
    serializer_class = VpsListSerializer
    lookup_field = 'uid'
    action_serializers = {
        'create': VpsCreateSerializer,
        'change_status': VpsChangeStatusSerializer
    }
    filterset_class = VpsFilter

    @action(
        methods=['PUT'],
        detail=True,
    )
    def change_status(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(VpsListSerializer(instance).data, status=status.HTTP_200_OK)
