from django.shortcuts import render
from django.http import HttpResponse
from slist.models import ShoppingList, UserList, Item, MallList

# Create your views here.  #обработчики єндпоинтов
def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = ShoppingList.objects.filter(list_id=user_list.list_id)     #возвращает квери-сет объект
    new_r = [itm.__dict__ for itm in result]                            #поэтому каждый элемент этого сета делаем диктом, чтоб мочь отобразить его наполенение
    if request.method == "POST":
        pass

    return render(request, 'item_form.html', {'shopping_list_data': new_r, 'shops': MallList.objects.all().filter(list_id=user_list.list_id)})


def add_item(request):
    return HttpResponse('add item')


def buy_item(request, item_id):
    return HttpResponse('buy item')


def remove_item(request, item_id):
    return HttpResponse('remove item')