from rest_framework import viewsets, mixins

from .serializers import PersionInfoSerializer
from .models import PersionInfo
from rest_framework.response import Response


class PersionInfoViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    返回用于展示的联系方式
    """
    serializer_class = PersionInfoSerializer
    queryset = PersionInfo.objects.all()