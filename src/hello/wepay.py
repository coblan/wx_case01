from helpers.wechat.wepay.jsapi import JSApiWePay
from helpers.wechat.wepay.appapi import APPApiWePay

from helpers.wechat import views as we_views
from .models import WXOrder

class MyWePay(JSApiWePay):
    APPID='wx7018edf138c754f4'
    APPSECRET='468e7fc6e416c59c7927d7a467005a66'
    MACHID='1304944001'
    APISECERT='6a3fb1c0eb1611e5afb352540056e71a'
    WXOrderModel=WXOrder
    def order_create(self, wxorder):
        wxorder.body='test production'
        wxorder.total_fee=100
        wxorder.detail='this is for test'
        super(MyWePay,self).order_create(wxorder)

class MyAppWePay(APPApiWePay):
    APPID='wx7018edf138c754f4'
    APPSECRET='468e7fc6e416c59c7927d7a467005a66'
    MACHID='1304944001'
    APISECERT='6a3fb1c0eb1611e5afb352540056e71a'
    WXOrderModel=WXOrder
    def order_create(self, wxorder):
        wxorder.body='test production'
        wxorder.total_fee=100
        wxorder.detail='this is for test'
        super(MyAppWePay,self).order_create(wxorder)    

def monkey_patch():
    we_views.JSApiWePay=MyWePay
    we_views.APPApiWePay=MyAppWePay

monkey_patch()