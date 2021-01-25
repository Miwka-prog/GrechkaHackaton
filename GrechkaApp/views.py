from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from . import parser
# Create your views here.


def get_array(is_increase=True):

    # name, price, url_img, url
    array = parser.get_groats(3)
    for i in array:
        print(i['price'])

    is_swap = True
    while is_swap:
        is_swap = False
        for i in range(len(array) - 1):
            if float(array[i]['price']) > float(array[i + 1]['price']):
                array[i], array[i + 1] = array[i + 1], array[i]
                is_swap = True

    if not is_increase:
        array.reverse()

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
    return array_name, array_price, array_url_img, array_url


def get_settings(request):
    # if this is a POST request we need to process the form data
    error_message = "123"
    if request.method == 'POST':
        print(request)
        print('Post запрос')
        print(request.POST)
        post_dict = request.POST.dict()
        print(post_dict)
        if post_dict['list'] == '1':
            array_name, array_price, array_url_img, array_url = get_array(True)
        else:
            array_name, array_price, array_url_img, array_url = get_array(False)
    # if a GET (or any other method) we'll create a blank form
    else:
        array_name, array_price, array_url_img, array_url = get_array(True)
    return render(request, 'GrechkaApp/index.html', {
       'array': zip(array_name, array_price, array_url_img, array_url)
     })
