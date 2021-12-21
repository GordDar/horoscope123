from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

sign_zodiac_dict = {
    "aries": "Знак зодиака: Овен",
    "taurus": "Знак зодиака: Телец",
    "gemini": "Знак зодиака: Близнецы",
    "cancer": "Знак зодиака: Рак",
    "leo": "Знак зодиака: Лев",
    "virgo": "Знак зодиака: Дева",
    "libra": "Знак зодиака: Весы",
    "scorpio": "Знак зодиака: Скорпион",
    "sagittarius": "Знак зодиака: Стрелец",
    "capricorn": "Знак зодиака: Козерог",
    "aquarius": "Знак зодиака: Водолей",
    "pisces": "Знак зодиака: Рыбы"
}

types_dict = {
    "fire": ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}


def type(request):
    types = list(types_dict)
    # li_types_elements = ''
    # for type_numbers in types:
    #     redirect_path = reverse('types_page', args=[type_numbers])
    #     li_types_elements += f"<li><a href='{redirect_path}'>{type_numbers.title()}</a></li>"
    # response = f"""
    # <ul>
    #     {li_types_elements}
    # </ul>
    # """
    context = {
        'types':types,
    }
    return render(request, 'horoscope/types_page.html', context=context)


def types_page(request, type: str):
    # li_sign_elements = ''
    signs_for_type_list = []
    for types, signs_for_type in types_dict.items():
        if types == type:
            for keys in signs_for_type:
                signs_for_type_list.append(keys)
                # redirect_path = reverse('horoscope-name', args=[keys])
                # li_sign_elements += f"<li><a href='{redirect_path}'>{keys.title()}</a></li>"
    # response = f"""
    # <ul>
    #     {li_sign_elements}
    # </ul>
    # """
    context={
        'signs_for_type':signs_for_type_list,
        'type': type,
    }
    return render(request, 'horoscope/sign_for_types.html', context=context)


def get_info_by_day(request, month: int, day: int):
    if month > 12 or day > 31:
        return HttpResponseNotFound(f'Некорректно введена дата')
    if month == 3 and 21 <= day <= 31 or month == 4 and 1 <= day <= 20:
        sign_zodiac = 'aries'
        redirect_path = reverse('horoscope-name', args=[sign_zodiac])
        # return HttpResponseRedirect(redirect_path)
        return HttpResponse(f'Возможно вы искали знак зодиака <a href={redirect_path}>овен</a>.')
    else:
        redirect_path = reverse('start_page', args=[])
        return HttpResponse(f'К сожалению, таких данных нет, попробуйте выбрать знак зодиака из списка по <a href={redirect_path}>ссылке</a>.')


def index(request):
    zodiacs = list(sign_zodiac_dict)
    # for sign in zodiacs:
    #     redirect_path = reverse('horoscope-name', args=[sign])
    #     li_elements += f"<li> <a href='{redirect_path}'> {sign.title()} </a> </li>"
    context={
        "zodiacs":zodiacs,
    }
    return render(request, "horoscope/index.html", context=context)


def get_info_about_zodiac_sign(request, sign_zodiac: str):
    description = sign_zodiac_dict.get(sign_zodiac)
    data = {
        "description_zodiac":description,
        "sign": sign_zodiac.title(),
        "zodiacs":sign_zodiac_dict,
        "sign_name": description.split(' ')[2]
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из 4 цифр - {sign_zodiac}')


def get_info_about_zodiac_sign_by_number(request, sign_zodiac: int):
    zodiacs = list(sign_zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Вы ввели неверное число для поиска знака зодиака - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)

def get_info_by_number(request):
    return render(request, 'horoscope/info_by_number.html', {})



