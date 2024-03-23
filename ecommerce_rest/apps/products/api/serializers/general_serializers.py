from apps.products.models import CategoryProduct, MeasureUnit, Indicator

from rest_framework import serializers

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CategoryProduct
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MeasureUnit
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

class IndicatorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Indicator
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
