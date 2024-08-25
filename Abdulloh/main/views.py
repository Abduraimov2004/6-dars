from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def set_cookie(request):
    if request.method == 'POST':
        cookie_name = request.POST.get('cookie_name')
        cookie_value = request.POST.get('cookie_value')
        response = render(request, 'message.html', {
            'message': 'Cookie muvaffaqiyatli o‘rnatildi!',
            'success': True,
            'cookie_name': cookie_name,
            'cookie_value': cookie_value
        })
        response.set_cookie(cookie_name, cookie_value)
        return response
    return redirect('index')


def get_cookie(request):
    cookie_name = request.GET.get('cookie_name')
    if cookie_name:
        cookie_value = request.COOKIES.get(cookie_name, 'Cookie mavjud emas')
        return render(request, 'message.html', {
            'message': 'Cookie topildi!' if cookie_value != 'Cookie mavjud emas' else 'Cookie topilmadi!',
            'success': cookie_value != 'Cookie mavjud emas',
            'cookie_name': cookie_name,
            'cookie_value': cookie_value
        })
    return redirect('index')


def update_cookie(request):
    if request.method == 'POST':
        cookie_name = request.POST.get('cookie_name')
        new_value = request.POST.get('cookie_value_update')
        if request.COOKIES.get(cookie_name):
            response = render(request, 'message.html', {
                'message': 'Cookie muvaffaqiyatli yangilandi!',
                'success': True,
                'cookie_name': cookie_name,
                'cookie_value': new_value
            })
            response.set_cookie(cookie_name, new_value)
        else:
            response = render(request, 'message.html', {
                'message': 'Cookie mavjud emas, avval uni qo‘shing.',
                'success': False
            })
        return response
    return redirect('index')


def delete_cookie(request):
    cookie_name = request.GET.get('cookie_name')
    if cookie_name in request.COOKIES:
        response = render(request, 'message.html', {
            'message': 'Cookie muvaffaqiyatli o‘chirildi!',
            'success': True,
            'cookie_name': cookie_name
        })
        response.delete_cookie(cookie_name)
    else:
        response = render(request, 'message.html', {
            'message': 'Cookie topilmadi, o‘chirilishi mumkin emas.',
            'success': False,
            'cookie_name': cookie_name
        })
    return response


def set_session(request):
    if request.method == 'POST':
        session_name = request.POST.get('session_name')
        session_value = request.POST.get('session_value')
        request.session[session_name] = session_value
        return render(request, 'message.html', {
            'message': 'Session muvaffaqiyatli o‘rnatildi!',
            'success': True,
            'session_name': session_name,
            'session_value': session_value
        })
    return redirect('index')


def get_session(request):
    session_name = request.GET.get('session_name')
    if session_name:
        session_value = request.session.get(session_name, 'Session mavjud emas')
        return render(request, 'message.html', {
            'message': 'Session topildi!' if session_value != 'Session mavjud emas' else 'Session topilmadi!',
            'success': session_value != 'Session mavjud emas',
            'session_name': session_name,
            'session_value': session_value
        })
    return redirect('index')


def update_session(request):
    if request.method == 'POST':
        session_name = request.POST.get('session_name')
        new_value = request.POST.get('session_value_update')
        if request.session.get(session_name):
            request.session[session_name] = new_value
            return render(request, 'message.html', {
                'message': 'Session muvaffaqiyatli yangilandi!',
                'success': True,
                'session_name': session_name,
                'session_value': new_value
            })
        else:
            return render(request, 'message.html', {
                'message': 'Session mavjud emas, avval uni qo‘shing.',
                'success': False
            })
    return redirect('index')


def delete_session(request):
    session_name = request.GET.get('session_name')
    if session_name in request.session:
        del request.session[session_name]
        return render(request, 'message.html', {
            'message': 'Session muvaffaqiyatli o‘chirildi!',
            'success': True,
            'session_name': session_name
        })
    else:
        return render(request, 'message.html', {
            'message': 'Session mavjud emas, o‘chirilishi mumkin emas.',
            'success': False,
            'session_name': session_name
        })
