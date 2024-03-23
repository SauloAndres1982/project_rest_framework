from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer

class ProductCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Producto creado correctamente"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
                
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state=True).first()
    
    def delete(self, request, pk=None):

        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({"Message":"Producto eliminado correctamente"}, status=status.HTTP_200_OKS)
        
        return Response({"Error": "No existe un producto con estos datos."}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response({"Error": "No existe un producto con estos datos."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        instance = self.get_object()
        if instance:
            product_serializer = self.serializer_class(instance, data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
        
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    