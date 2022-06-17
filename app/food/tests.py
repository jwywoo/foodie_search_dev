from django.test import TestCase

from .models import Food
from .views import calculating, searching_foods

# Test Food Views
class TestViews(TestCase):
    
    # Setup database
    def setUp(self):
        Food.objects.create(english_name='Rice', original_name='Rice', country='JP')
        Food.objects.create(english_name='Ramen', original_name='Ramen', country='JP', color='YL', taste="SL", protein='PR', type='BD', carbohydrate='ND',)

    #######################################################
    # ~~~~~~~~~~~~~~ TESTS FOR CALCULATING ~~~~~~~~~~~~~~ #
    #######################################################

    def test_calculatingFull(self):

        # Mock input
        feature_selected = {}
        feature_selected['country'] = 'JP'
        feature_selected['taste'] = 'SL'
        feature_selected['color'] = 'YL'
        feature_selected['protein'] = 'PR'
        feature_selected['type_food'] = 'BD'
        feature_selected['carbohydrate'] = 'ND'

        # Should find Ramen
        result = calculating(selected_features=feature_selected, foods=Food.objects.all())
        self.assertEqual(result[0].original_name, 'Ramen')

    def test_calculatingEmpty(self):

        # Mock input empty
        feature_selected = {}
        feature_selected['country'] = 'UD'

        # Should return 0 
        result = calculating(selected_features=feature_selected, foods=Food.objects.all())
        self.assertEqual(result, 0)

    #######################################################
    # ~~~~~~~~~~~~ TESTS FOR SEARCHING_FOODS ~~~~~~~~~~~~ #
    #######################################################

    def test_searching_foods_goodInput(self):
        
        # Mock input for Ramen
        data = {
            'country': 'JP',
            'color': 'YL',
            'taste': 'SL',
            'protein': 'PR',
            'type': 'UD',
            'carbohydrate': 'UD'
        }
        response = self.client.post('/food/search/', data=data)

        # Check if site exists and contains Ramen as output
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ramen")

    def test_searching_foods_noInput(self):

        # Mock input for NOTHING
        data = {
            'country': 'UD',
            'color': 'UD',
            'taste': 'UD',
            'protein': 'UD',
            'type': 'UD',
            'carbohydrate': 'UD'
        }
        response = self.client.post('/food/search/', data=data)

        # Check if site exists and contains error code
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You need to choose at least one feature")

    def test_searching_foods_perfectInput(self):
        
        # Mock input for Rice
        data = {
            'country': 'JP',
            'color': 'UD',
            'taste': 'UD',
            'protein': 'UD',
            'type': 'UD',
            'carbohydrate': 'UD'
        }
        response = self.client.post('/food/search/', data=data)

        # Check if site exists and contains Rice as output
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Rice")

    # Test searching_foods with good input
    def test_searching_foods_weirdCase(self):
        
        # Mock input for Ramen
        data = {
            'country': 'UD',
            'color': 'RD',
            'taste': 'SW',
            'protein': 'BF',
            'type': 'BD',
            'carbohydrate': 'ND'
        }
        response = self.client.post('/food/search/', data=data)

        # Check if site exists and contains Ramen as output
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ramen")

    ######################################################
    # ~~~~~~~~~~~~~ TESTS FOR RANDOM STUFF ~~~~~~~~~~~~~ #
    ######################################################

    # Test main
    def test_main(self):

        response = self.client.post('/food/')

        # Check if site exists and is the main
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Foodie Search")   
