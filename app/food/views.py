from django.shortcuts import render

from django.http import HttpResponse


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


def searching_foods(request, user_input):
    pass


def food_detail(request):
    pass
