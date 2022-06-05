from django.shortcuts import render

from django.http import HttpResponse


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


def searching_foods(request):
    if request.method == 'POST':
        context = {
            'test1': request.POST['color'],
            'test2': request.POST['protein'],
            'test3': request.POST['country'],
        }
        return render(request, 'food/main.html', context=context)


def food_detail(request):
    pass
