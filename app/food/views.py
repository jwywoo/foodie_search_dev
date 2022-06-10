from django.shortcuts import render

from django.http import HttpResponse
from .models import Food


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


# numerator
def calculating(selected_features, foods):
    result_list = []
    numerator = 0
    for feature in selected_features.keys():
        if selected_features[feature] is not 'UD':
            numerator += 1
    temp = 0
    result = None
    for food in foods:
        denominator = 0
        # country
        if selected_features['country'] == food.country:
            denominator += 1
        # color
        if selected_features['color'] == food.color:
            denominator += 1
        # taste
        if selected_features['taste'] == food.taste:
            denominator += 1
        # protein
        if selected_features['protein'] == food.protein:
            denominator += 1
        # type
        if selected_features['type_food'] == food.type:
            denominator += 1
        # carbohydrate
        if selected_features['carbohydrate'] == food.carbohydrate:
            denominator += 1
        print(food.original_name)
        possibility = denominator/numerator
        if 0.4 <= possibility:
            result_list.append(food)
    return result_list


# Available Options
# taste
# country
# color
# protein
# type
# carbohydrate
def searching_foods(request):
    if request.method == 'POST':
        # a list of selected features to calculate
        feature_selected = {}
        country = request.POST['country']
        feature_selected['country'] = country
        taste = request.POST['taste']
        feature_selected['taste'] = taste
        color = request.POST['color']
        feature_selected['color'] = color
        protein = request.POST['protein']
        feature_selected['protein'] = protein
        type_food = request.POST['type']
        feature_selected['type_food'] = type_food
        carbohydrate = request.POST['carbohydrate']
        feature_selected['carbohydrate'] = carbohydrate

        selected = Food.objects.filter(country=country,
                                       taste=taste,
                                       color=color,
                                       protein=protein,
                                       type=type_food,
                                       carbohydrate=carbohydrate)
        if not selected:
            calculating(selected_features=feature_selected, food=Food.objects.all())
            context = {
                'text': "Wait for the results"
            }
            return render(request, 'food/main.html', context=context)
        else:
            return render(request, 'food/main.html', selected)


def food_detail(request):
    pass
