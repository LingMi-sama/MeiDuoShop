from apps.admins.views import users, specs, statistical
from rest_framework_jwt.views import obtain_jwt_token
from django.urls import path
from apps.admins.views import images  # 导入图片包
from apps.admins.views import spus
from apps.admins.views import options
from apps.admins.views import channels

urlpatterns = [

    # 登录
    path('admins/authorizations', obtain_jwt_token),
    # 总人数
    path('admins/statistical/total_count', statistical.UserCountAPIView.as_view()),
    # 日增
    path('admins/statistical/day_increment', statistical.UserDayAddCountAPIView.as_view()),
    # 日活　admins/statistical/day_active/
    path('admins/statistical/day_active', statistical.UserDayActiveCountAPIView.as_view()),
    # 日下单　/admins/statistical/day_orders/
    path('admins/statistical/day_orders', statistical.UserDayOrderCountAPIVIew.as_view()),
    # 月活跃　admins/statistical/month_increment/
    path('admins/statistical/month_increment', statistical.UserMonthActiveCountAPIView.as_view()),
    # 　分类商品日访问量/admins/statistical/goods_day_views/
    path('admins/statistical/goods_day_views', statistical.GoodDayVisetCountView.as_view()),

    # 查询用户总数 ，添加用户操作
    path('admins/users', users.UserListAPIView.as_view()),
    # 查询获取规格表列表数据、保存规格表数据表数据
    path('admins/goods/specs', specs.SpecsView.as_view({'get': 'list', 'post': 'create'})),
    # 获取规格所关联的SPU信息
    path('admins/goods/simple', specs.SpecsView.as_view({'get': 'simple'})),
    # 获取单个规格信息，删除，修改
    path('admins/goods/specs/<pk>', specs.SpecsView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    # 图片CRUD
    path('admins/skus/images', images.ImagesView.as_view({'get': 'list', 'post': 'create'})),
    path('admins/skus/simple', images.SkuListAPIView.as_view()),
    # spu菜单获取
    path('admins/goods', spus.SPUView.as_view({"get": "list", 'post': 'create'})),
    #   修改SpU表数据、删除spu表数据
    path('admins/goods/<int:pk>', spus.SPUView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('admins/goods/brands/simple', spus.SPUBrandView.as_view()),
    path('admins/goods/channel/categories', spus.ChannelCategorysView.as_view()),
    path('admins/goods/channel/categories/<int:pk>', spus.ChannelCategorysView.as_view()),
    # 查询获取规格选项表列表数据、保存规格表数据
    path('admins/specs/options', options.OptionViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
    # 修改规格表数据、删除SPU表数据
    path('admins/specs/options/<pk>',
         options.OptionViewSet.as_view(actions={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('admins/goods/specs/simple', options.SPUSpecListView.as_view()),
    ### 频道菜单
    path('admins/goods/channels', channels.GoodsChannelView.as_view({"get": "list", 'post': 'create'})),
    #   修改SpU表数据、删除spu表数据
    path('admins/goods/channels/<int:pk>',
         channels.GoodsChannelView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('admins/goods/categories', channels.GoodsCategoryView.as_view()),
    # path('admins/goods/channel_types', channels.GoodsChannelGroupView.as_view()),
]

