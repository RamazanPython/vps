from django_filters import rest_framework as filters

from vps.models import Vps


class VpsFilter(filters.FilterSet):

    class Meta:
        model = Vps
        fields = (
            "status",
            "ram",
            "hdd",
            "cpu"
        )

