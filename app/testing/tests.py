from django.test import TestCase
from food.models import *
from user.models import *
from relation.models import *

class TestSystem(TestCase):

    # Setup database
    def setUp(self):
        Food.objects.create(english_name='Rice', original_name='Rice', country='JP')
        Food.objects.create(english_name='Ramen', original_name='Ramen', country='JP', color='YL', taste='SL', protein='PR', type='BD', carbohydrate='ND')
        Food.objects.create(english_name='Spicy Ramen', original_name='Spicy Ramen', country='JP', color='RD', taste='SL', protein='PR', type='BD', carbohydrate='ND')

    def test_systemTest(self):
        
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

        # Check user is logged in
        response = self.client.post('/user/login/', data={'username':'paul','password':'password'})
        self.assertIn('_auth_user_id', self.client.session)

        # Search for Rice
        data = {
            'country': 'JP',
            'color': 'UD',
            'taste': 'UD',
            'protein': 'UD',
            'type': 'UD',
            'carbohydrate': 'ND'
        }
        response = self.client.post('/food/search/', data=data)

        # Check if site exists and contains Rice as output
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rice")

        # add Rice as favorite food
        response = self.client.post('/relation/add/1/')

        # check if Rice is indeed in userlikes 
        food = Food.objects.get(pk=1)
        response = self.client.get('/relation/userlikes/')
        self.assertEquals(response.context['liked_foods'][0], food)

        # Remove Rice from userlikes
        response = self.client.post('/relation/remove/1/')
        response = self.client.get('/relation/userlikes/')

        # Nothing should be in userlikes anymore
        self.assertEquals(len(response.context['liked_foods']), 0)

        # Logout and check we are logged out
        response = self.client.get('/user/logout/')
        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, 'Logout')
        self.assertContains(response, 'Signup')
