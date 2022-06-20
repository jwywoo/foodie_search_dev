from multiprocessing.connection import Client
from django.test import TestCase
from food.models import *
from .models import User
from .views import *

class TestViews(TestCase):

    # Setup database
    def setUp(self):
        Food.objects.create(english_name='Rice', original_name='Rice', country='JP')
        Food.objects.create(english_name='Ramen', original_name='Ramen', country='JP', color='YL', taste='SL', protein='PR', type='BD', carbohydrate='ND')
        Food.objects.create(english_name='Spicy Ramen', original_name='Spicy Ramen', country='JP', color='RD', taste='SL', protein='PR', type='BD', carbohydrate='ND')

    #####################################################
    #~~~~~~~~~~~~~ TESTS FOR USER_SIGNUP ~~~~~~~~~~~~~~ #
    #####################################################

    def test_user_signup_GetRequest(self):

        response = self.client.get('/user/signUp/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, "Signup Here!")


    def test_user_signup_Valid(self):

        # Mock input for signup
        data = {
            'username': 'paul',
            'email' : 'paulabijaber@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post('/user/signUp/', data=data)

        # Check if site exists and Databse contains my info
        self.assertEquals(response.status_code, 200)
        self.assertEquals(User.objects.get(pk=1).username, 'paul')
        

    def test_user_signup_NotValid(self):

        # Mock input for signup
        data = {
            'username': 'paul',
            'email' : 'paulabijaber@gmail.com',
            'password': 'password',
            'password2': 'passwdwasdord'
        }
        response = self.client.post('/user/signUp/', data=data)

        # Check if site exists and signup failed so database doesnt contain anything
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(User.objects.all()), 0)

    #####################################################
    #~~~~~~~~~~~~~ TESTS FOR USER_LOGOUT ~~~~~~~~~~~~~~ #
    #####################################################

    def test_user_logout(self):

        User.objects.create_user(username='paul', email='paulabijaber@gmail.com', password='password')

        data = {
            'username': 'paul',
            'password': 'password'
        }

        c = Client
        response = c.get('/user/login/', data=data)
        response = c.get('/user/logout/')
        
        self.assertEquals(response.status_code, 302)


