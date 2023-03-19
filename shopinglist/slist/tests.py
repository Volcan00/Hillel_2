from django.test import TestCase
from application.models import UserList, ShoppingList
from django.contrib.auth.models import User
import uuid
from django.test import Client

class UserListTestCase(TestCase):
    def setUp(self):
        self.user1_email = "test_user1@example.com"
        self.user2_email = "test_user2@example.com"
        self.user1_username = "test_user1"
        self.user2_username = "test_user2"
        user1 = User.objects.create_user(self.user1_username, self.user1_email, 'password')
        user1.save()

        user2 = User.objects.create_user(self.user2_username, self.user2_email, 'pass')
        user2.save()

        shopuser1_list = UserList(user_id = user1.id, list_id = uuid.uuid4())
        shopuser1_list.save()

        shopuser2_list = UserList(user_id = user2.id, list_id = uuid.uuid4())
        shopuser2_list.save()

        self.user1_id = user1.id
        self.user2_id = user2.id


        def test_user_list(self):
            c = Client()
            c.login(username = self.user1_name, password = "password")
            responce = c.post("/user/invite", {"email" : self.user2_email})
            responce.status_code
            self.assertEqual(responce.status_code, 200)
            shopuser1_list = UserList.objects.filter(user_id = self.user1_id).first()
            shopuser2_list = UserList.objects.filter(user_id = self.user2_id).first()
            self.assertEqual(shopuser2_list, shopuser1_list)

        def test_user_not_exist(self):
            c = Client()
            c.login(username = self.user1_name, password = "password")
            responce = c.post('/user/invite', "email" : "user3@example.com")
            self.assertEqual(responce.status_code, 404)

class UserRegister(TestCase):
    def createuser(self):
        c = Client()
        responce = c.post('/user/register', {'username' : 'test_user3', 'email' : 'user3@example.com', 'password': 'password'})
        self.assertEqual(responce.status_code, 302)
        user3 = User.objects.filter(username = 'test_user3').first()
        self.assertIsNotNone(user3)
        userlist3 = UserList.objects.filter(user_id = user3.id).first()
        self.assertIsNotNone(userlist3)

        responce = c.post('/user/register', {'username' : 'test_user4', 'email' : 'user4@example.com', 'password': 'password'})
        self.assertEqual(responce.status_code, 302)
        user4 = User.objects.filter(username = 'test_user3').first()
        self.assertIsNotNone(user4)
        userlist4 = UserList.objects.filter(user_id = user4.id).first()
        self.assertIsNotNone(userlist4)

        self.assertNotEqual(userlist3.list_id, userlist4.list_id)

class test_buy_item(TestCase):
    fixtures = ["buy_item_fixture.json"]
    def test_buy_item(self):
        shopinglist = ShoppingList.objects.filter(list_id = '').all()
        self.assertEqual(len(shopinglist), 1)
        list_pk = shopinglist[0].pk
        c = Client()
        c.login(username = "User2", password = "1111")
        responce = c.post('/shoppinglist/1/buy', {'item_id' : 1})

        shopinglist2 = ShoppingList.objects.filter(list_id = '').all()
        self.assertEqual(len(shopinglist), 1)
        self.assertEqual(shopinglist2[0].status, 'bought')


