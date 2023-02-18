from django.shortcuts import render
from django.http import HttpResponse
from slist.models import ShoppingList, UserList, Item

# Create your views here.  #обработчики єндпоинтов
def index(request):
    user_list = UserList.objects.filter(user_id=1).first()
    result = ShoppingList.objects.filter(list_id=user_list[0].list_id)

    return HttpResponse("Hello, it's shopping list")


def add_item(request):
    return HttpResponse('add item')


def buy_item(request, item_id):
    return HttpResponse('buy item')


def remove_item(request, item_id):
    return HttpResponse('remove item')