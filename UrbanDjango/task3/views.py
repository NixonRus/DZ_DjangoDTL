from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'third_task/shop_gp.html')


def buy_helm(request):
    title = 'Купить шлем'
    text = 'Выберите шлем'
    buy1 = 'Scorpion Exo EXO-R1 EVO CARBON AIR SOLID'
    buy2 = 'LS2 FF901 ADVANT X SOLID'
    buy3 = 'Icon Airflite Rubatone'
    context = {
        'title': title,
        'text': text,
        'buy1': buy1,
        'buy2': buy2,
        'buy3': buy3,
    }
    return render(request, 'third_task/helmets.html', context)


def basket(request):
    return render(request, 'third_task/basket.html')


