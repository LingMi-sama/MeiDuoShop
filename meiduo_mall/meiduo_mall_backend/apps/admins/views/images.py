from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.goods.models import SKUImage, SKU
from apps.admins.myserializers.images import ImagesSerializer
from apps.admins.myserializers.skus import SKUSerializer
from apps.admins.utils import PageNum
from rest_framework.permissions import IsAdminUser
from fdfs_client.client import Fdfs_client


class ImagesView(ModelViewSet):
    queryset = SKUImage.objects.all()
    serializer_class = ImagesSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    # 保存的位置

    def create(self, request, *args, **kwargs):
        image = request.FILES.get('image')
        sku = request.data.get('sku')

        client = Fdfs_client('utils/fastdfs/client.conf')
        res = client.upload_by_buffer(image.read())
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        image_url = res['Remote file_id']
        image = SKUImage.objects.create(sku_id=sku, image=image_url)

        data = {
            'id': image.id,
            'sku': image.sku_id,
            'image': image.image.url
        }
        return Response(data, status=201)

    def update(self, request, *args, **kwargs):
        image = request.FILES.get('image')
        sku_id = kwargs.get('pk')

        client = Fdfs_client('utils/fastdfs/client.conf')
        res = client.upload_by_buffer(image.read())
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        image_url = res['Remote file_id']
        image = SKUImage.objects.filter(id=sku_id).update(image=image_url)

        if image:
            image_object = SKUImage.objects.get(id=sku_id)
            data = {
                'id': image_object.id,
                'sku': image_object.sku_id,
                'image': image_object.image.url
            }
            return Response(data, status=201)
        return Response(status=403)

    def simple(self, request):
        skus = SKU.objects.all()
        ser = SKUSerializer(skus, many=True)
        return Response(ser.data)


# 　新增图片　选择商品
class SkuListAPIView(ListAPIView):
    queryset = SKU.objects.all()
    serializer_class = SKUSerializer
