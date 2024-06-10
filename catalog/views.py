from django.shortcuts import render


def home(requests):
    return render(requests, 'home.html')


def contacts(requests):
    if requests.method == 'POST':
        name = requests.POST.get('name')
        phone = requests.POST.get('phone')
        message = requests.POST.get('message')
        print(f'{name}: {phone}\n {message}')

    return render(requests, 'contacts.html')
