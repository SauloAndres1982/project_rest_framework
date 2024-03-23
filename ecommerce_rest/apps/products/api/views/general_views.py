from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import *

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class =MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)

class CategoryProductListAPIView(GeneralListApiView):
    serializer_class =CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state=True)

class IndicatorListAPIView(GeneralListApiView):
    serializer_class =IndicatorSerializer

    def get_queryset(self):
        return Indicator.objects.filter(state=True)
