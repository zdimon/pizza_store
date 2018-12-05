class Shop(object):
    name = 'My Pizza shop!'


def shop_processor(request):
 shop = Shop()           
 return {'shop': shop}