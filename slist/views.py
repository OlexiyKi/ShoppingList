from django.shortcuts import render, redirect
from django.http import HttpResponse
from slist.models import ShoppingList, UserList, Item, MallList
import datetime


# Create your views here.  #обработчики єндпоинтов
def index(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_list = UserList.objects.filter(user_id=user_id).first()
        if request.method == "POST":
            if request.POST.get('Add'):                         #кнопка возвращает в POST значение с параметра name="Add"
                item_name = request.POST.get('item')
                amount = request.POST.get('amount')
                shop_id = request.POST.get('shop')
                shop_objct = MallList.objects.filter(pk=int(shop_id)).first()    #нужно призаписи нового товара передать в shop_id объект класса, но не id как число

                item_objct = Item(name=item_name, shop_id=shop_objct)
                item_objct.save()

                new_item = ShoppingList(list_id=user_list.list_id, item_id=item_objct, quantity=amount)
                new_item.save()

        result = list(ShoppingList.objects.filter(list_id=user_list.list_id).all())     #возвращает квери-сет объект поэтому нужно или в список или дикт обернуть, чтоб рендерить
    else:
        return redirect('/user/login')

    return render(request, 'item_form.html', {'shopping_list_data': result,
                                              'shops': MallList.objects.all().filter(list_id=user_list.list_id)})  #ключи (н-р) 'shopping_list_data' -- єто название {переменной} в темплейте



def buy_item(request, item_id):
    """add other endpoint from same html form: <button type="submit" formaction="/updateAddress" formmethod="POST" name="remove">remove</button>"""
    if request.user.is_authenticated:
        if request.POST.get('done'):
            item_objct = Item.objects.filter(pk=int(item_id)).first()
            bought_item = ShoppingList.objects.filter(item_id=item_objct).first()
            bought_item.status = 'done'
            bought_item.buy_day = datetime.datetime.now()
            bought_item.price = request.POST.get('price')
            bought_item.save()
        if request.POST.get('remove'):
            item_objct = Item.objects.filter(pk=int(item_id)).first()
            bought_item = ShoppingList.objects.filter(item_id=item_objct).first()
            bought_item.delete()
    else:
        return redirect('/user/login')

    return redirect('/shopping_list/')


def remove_item(request, item_id):
    if request.user.is_authenticated:
        if request.POST.get('Remove'):
            item_objct = Item.objects.filter(pk=int(item_id)).first()
            bought_item = ShoppingList.objects.filter(item_id=item_objct).first()
            bought_item.delete()
    else:
        return redirect('/user/login')

    return redirect('/shopping_list/')