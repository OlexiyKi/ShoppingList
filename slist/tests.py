from django.test import TestCase
from .models import UserList, ShoppingList, Item
from django.contrib.auth.models import User
import uuid
from django.test import Client
import datetime

# Create your tests here.
class UserListTestCase(TestCase):
    def setUp(self):
        self.user_name1 = 'test_user_1'
        self.user_email1 = 'user_1@gmail.com'
        self.user_password1 = 'passuser1'
        self.user_name2 = 'test_user_2'
        self.user_email2 = 'user_2@gmail.com'
        self.user_password2 = 'passuser2'

        user_1 = User.objects.create_user(username=self.user_name1, email=self.user_email1, password=self.user_password1)
        user_1.save()
        shoppinglist_user1 = UserList(user_id=user_1.id, list_id=uuid.uuid4())

        shoppinglist_user1.save()

        user_2 = User.objects.create_user(username=self.user_name2, email=self.user_email2, password=self.user_password2)
        user_2.save()
        shoppinglist_user2 = UserList(user_id=user_2.id, list_id=uuid.uuid4())
        shoppinglist_user2.save()

        self.user1_id = user_1.id
        self.user2_id = user_2.id



    def test_user_list_id_mapping(self):
        user = Client()
        user.login(username=self.user_name1, password=self.user_password1)
        response = user.post('/user/invite', {'email': self.user_email2})
        self.assertEqual(response.status_code, 200)

        user_list1 = UserList.objects.filter(id=self.user1_id).first()

        user_list2 = UserList.objects.filter(id=self.user2_id).first()

        self.assertEqual(user_list2.list_id, user_list1.list_id)

    def test_user_not_exsist(self):
        user = Client()
        user.login(username=self.user_name2, password=self.user_password2)
        response = user.post('/user/invite', {'email': 'user3@exe.com'})
        self.assertEqual(response.status_code, 404)




class UserRegister(TestCase):
    def createuser(self):
        user = Client()
        response = user.post('/user/register', {'username': 'user_3', 'email': 'user3@gmail.com', 'password': 'passuser3'})
        user3 = User.objects.filter(username='user_3').first()
        self.assertIsNotNone(user3)
        user3_list = UserList.objects.filter(id=user3.id).first()
        self.assertIsNotNone(user3_list)

        response = user.post('/user/register', {'username': 'user_4', 'email': 'user4@gmail.com', 'password': 'passuser4'})
        user4 = User.objects.filter(username='user_4').first()
        self.assertIsNotNone(user4)
        user4_list = UserList.objects.filter(id=user4.id).first()
        self.assertIsNotNone(user4_list)

        self.assertNotEqual(user3_list.list_id, user4_list.list_id)



class BuyItem(TestCase):
    fixtures = ['buy_item_fixture.json']
    def test_buy_item(self):
        user = Client()
        user.login(username='user1', password='1111')

        response = user.post('/shoppinglist/1/buy', {'item': 1})   #ємулируем нажатие на кнопку Купить в указанном єндпоинте

        shoppinglist_user = ShoppingList.objects.filter(list_id='fe462e19-dc73-4433-906b-fe62f6405919').first()
        self.assertEqual('done', shoppinglist_user.status)


    # def test_add_itam(self):
    #     user = Client()
    #     user.login(username='user1', password='1111')
    #
    #     response = user.post("/shopping_list", {'item_name': 'pepper', 'amount': '1', 'shop_id': '1'})
    #
    #     added_item = Item.objects.filter(name='pepper').first()
    #
    #     self.assertEqual(added_item.name, 'pepper')










