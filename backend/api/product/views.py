from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from api.models import Product
from .serializers import ProductSerializer

class ProductView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the Product items for given requested user
        '''
        Products = Product.objects.filter(user = request.user.id)
        serializer = ProductSerializer(Products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Product with given Product data
        '''
        data = {
            'name': request.data.get('name'),
            'doc_type': request.data.get('doc_type'),
            'doc_id1': request.data.get('doc_id1'),
            'doc_id2': request.data.get('doc_id2'),
            'extern_code': request.data.get('extern_code'),
            'since': request.data.get('since'),
            'user': request.user.id,
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
