from django.core.files.storage import Storage
from django.conf import settings


class FastDFSStorage(Storage):
    """自定义文件存储类"""
    """自定义文件存储系统，修改存储的方案"""

    def __init__(self, fdfs_base_url=None):
        """
        构造方法，可以不带参数，也可以携带参数
        :param base_url: Storage的IP
        """
        self.fdfs_base_url = fdfs_base_url or settings.FDFS_BASE_URL

    def _open(self, name, mode='rb'):
        """
        用于打开文件
        :param name: 要打开的文件名
        :param mode: 打开文件模式
        """
        pass

    def _save(self, name, content):
        """
        文件上传时会调用此方法
        :param name: 要上传的文件名
        :param content: 要上传的文件对象
        :return: file_id
        """
        pass

    def url(self, name):
        """
        当使用image字段.url属性时就会来调用此方法获取到要访问的图片绝对路径
        :param name: file_id
        :return: http://192.168.103.210:8888 + file_id
        """
        return self.fdfs_base_url + name