from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.admins.myserializers.orders import OrderSerializer
from apps.admins.utils import PageNum
from apps.orders.models import OrderInfo


class OrderView(ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    pagination_class = PageNum
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword == '':
            return OrderInfo.objects.all()
        elif keyword is None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)

    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        try:
            order = OrderInfo.objects.get(order_id=pk)
        except:
            return Response({'error': '订单编号错误'})

        status = request.data.get('status')
        if status is None:
            return Response({'error': '缺少状态值'})
        order.status = status
        order.save()
        return Response({
            'order_id': pk,
            'status': status
        })
