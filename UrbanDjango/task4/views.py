from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'fourth_task/shop_gp.html')


def buy_helm(request):
    title = 'Купить шлем'
    text = 'Выберите шлем'
    buy1 = 'Scorpion Exo EXO-R1 EVO CARBON AIR SOLID'
    buy2 = 'LS2 FF901 ADVANT X SOLID'
    buy3 = 'Icon Airflite Rubatone'
    context = {'helmets': ['Scorpion Exo EXO-R1 EVO CARBON AIR SOLID',
                           'LS2 FF901 ADVANT X SOLID', 'Icon Airflite Rubatone']}

    return render(request, 'fourth_task/helmets.html', context)


def basket(request):
    return render(request, 'fourth_task/basket.html')