from django.shortcuts import render

from django.http import HttpResponse


# showing the main page
def main(request):
    return render(request, 'food/main.html', {})


def searching_foods(request):
    print(request.POST['test_input'])
    if request.method == 'POST':
        print(request.POST['test_input'])
        context = {
            'test': request.POST['test_input']
        }
        return render(request, 'food/main.html', context=context)


def food_detail(request):
    pass
