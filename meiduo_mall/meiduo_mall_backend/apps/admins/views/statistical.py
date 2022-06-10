from datetime import date, timedelta

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.goods.models import GoodsVisitCount
from apps.admins.myserializers.statistical import GoodsVisitSerializer
from apps.users.models import User


# 总用户量
class UserCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        count = User.objects.all().count()
        today = date.today()
        return Response(
            {
                "count": count,
                "date": today,
            }
        )


# 日增人数
class UserDayAddCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        count = User.objects.filter(date_joined__gte=today).count()

        return Response({
            "count": count,
            "data": today,
        })


# 　日活跃
class UserDayActiveCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, requeset):
        today = date.today()
        count = User.objects.filter(last_login__gte=today).count()

        return Response({
            "count": count,
            "date": today,
        })


# /admins/statistical/day_orders/
class UserDayOrderCountAPIVIew(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = date.today()
        count = User.objects.filter(orderinfo__create_time__gte=today).count()
        return Response({
            "count": count,
            "date": today,
        })


# 月活跃人数
class UserMonthActiveCountAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mounth_start_today = date.today() - timedelta(60)

        data = []
        for i in range(30):
            start_time = mounth_start_today + timedelta(i)
            end_time = mounth_start_today + timedelta(i + 1)

            count = User.objects.filter(date_joined__gte=start_time, date_joined__lte=end_time).count()
            data.append({
                "count": count,
                "date": start_time,
            })
        return Response(data)


# 日分类商品访问量 /admins/statistical/goods_day_views/
class GoodDayVisetCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, requeset):
        today = date.today()
        goods = GoodsVisitCount.objects.filter(date__gte=today)
        # goods = GoodsVisitCount.objects.all()
        data = GoodsVisitSerializer(goods, many=True)

        return Response(data.data)
