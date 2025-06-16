from django.shortcuts import render

def home(request):
    """Главная страница"""
    return render(request, 'home.html')

def about(request):
    """Страница 'О компании'"""
    return render(request, 'about.html')

def history(request):
    """Страница 'История'"""
    return render(request, 'history.html')

def team_page(request):
    """Страница 'Команда' (использует named URL)"""
    return render(request, 'team.html')

def services(request):
    """Страница 'Услуги' (использует named URL)"""
    return render(request, 'services.html')

def services_dev(request):
    """Страница 'Разработка'"""
    return render(request, 'services_dev.html')

def contacts(request):
    """Страница 'Контакты'"""
    return render(request, 'contacts.html')