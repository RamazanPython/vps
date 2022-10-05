from rest_framework import serializers

from vps.models import Vps


class VpsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vps
        fields = (
            'uid',
            'cpu',
            'ram',
            'hdd',
            'status',
        )


class VpsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vps
        fields = (
            'uid',
            'cpu',
            'ram',
            'hdd',
            'status',
        )


class VpsChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vps
        fields = (
            'status',
        )
