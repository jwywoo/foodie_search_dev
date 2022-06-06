from django.shortcuts import render

from django.http import HttpResponse


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


# Available Options
# taste
# country
# color
# protein
# type
# carbohydrate
def searching_foods(request):
    if request.method == 'POST':
        taste = request.POST['taste']
        country = request.POST['country']
        color = request.POST['color']
        protein = request.POST['protein']
        type_food = request.POST['type']
        carbohydrate = request.POST['carbohydrate']
        return render(request, 'food/main.html', context={})


def food_detail(request):
    pass
