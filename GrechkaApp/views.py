from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from . import parser
# Create your views here.


def get_settings(request):
    # if this is a POST request we need to process the form data
    error_message = "123"
    if request.method == 'POST':
        print(request)
        print('Post запрос')
    # if a GET (or any other method) we'll create a blank form
    else:
        # Get
        print(request)
        array1 = parser.get_groats_rozetka(parser.URL_ROZETKA, 3)
        array2 = parser.get_groats_epicentr(parser.URL_EPICENTR, 3)
        array3 = parser.get_groats_bigl(parser.URL_BIGL, 3)
        # name, price, url_img, url

        array = list()
        for i in [array1, array2, array3]:
            for j in i:
                array.append(j)

        for i in array:
            print(i['price'])

        is_swap = True
        while is_swap:
            is_swap = False
            for i in range(len(array) - 1):
                if float(array[i]['price']) > float(array[i+1]['price']):
                    array[i], array[i+1] = array[i+1], array[i]
                    is_swap = True
            print(is_swap)

        for i in array:
            print(i['price'])

        array_name = list()
        array_price = list()
        array_url_img = list()
        array_url = list()
        for i in range(len(array)):
            array_name.append(array[i]['title'])
            array_price.append(array[i]['price'])
            array_url_img.append(array[i]['link_img'])
            array_url.append(array[i]['link_item'])
        print(array_name)
        print(array_price)
        print(array_url_img)
        print(array_url)

        return render(request, 'GrechkaApp/index.html', {
        'message': 'Hello',
        'array': zip(array_name, array_price, array_url_img, array_url)
        })
