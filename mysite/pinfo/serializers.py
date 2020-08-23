from .models import PersionInfo
from rest_framework import serializers

class PersionInfoSerializer(serializers.ModelSerializer):
    """
    主页上轮播的广告图
    """
    class Meta:
        model = PersionInfo
        fields = ("name", "phone", "profession", "school", "principal")