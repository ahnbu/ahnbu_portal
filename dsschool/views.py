from ahnbu_portal import settings

from django.shortcuts import render
from django.utils import timezone
# from .forms import PostForm

from .models import Price
from .forms import PostForm
from django.shortcuts import render, redirect, reverse

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import datetime, date


def index(request):
    if request.method == "POST":
        df = dsschool()
        message = df_sql(df)
        prices_list = Price.objects.all()  # .order_by('-update_date')
        sendmessage('01033487728', '성공적으로 작동합니다.')
        return render(request, 'dsschool/index.html', {'prices_list': prices_list, 'message': message})
#        return redirect('index')
        # "Save" 버튼을 누른 후에 결과 페이지.
        # index는 메인 페이지로 이동. new_lotto는 입력 페이지로 이동
        # reverse는 결과만 보여줌
    else:
        # 템플릿 파일 경로 지정, 데이터 전달
        prices_list = Price.objects.all()  # .order_by('-update_date')
        # , 'discount': discount})
        return render(request, 'dsschool/index.html', {'prices_list': prices_list})


def df_sql(df):
    import sqlite3
    con = sqlite3.connect("./db.sqlite3")
    # ../db.sqlite3이라고 하니까 계속 업데이트 안되었음 ㅠㅠ 점 하나 빼야 됨
    result = ""
    if Price.objects.all().count() == 0:  # 기존에 없으면, 바로 추가
        # 아래 dsschool_price에서 dsschool 부분에 앱 이름이 들어가야 함
        df.to_sql('dsschool_price', con, if_exists='append', index=False)
        # result = {'message': "오늘은 이미 업데이트되었습니다."}
        sendmessage('01033487728', '성공적으로 작동합니다.')
        result = ""
    else:  # 기존에 있으면, 오늘 꺼가 있으면 업데이트 안함
        price_date = Price.objects.first().update_date
        if price_date.date() < datetime.today().date():
            df.to_sql('dsschool_price', con, if_exists='append', index=False)
            sendmessage('01033487728', '성공적으로 작동합니다.')
            result = ""
        else:
            sendmessage('01033487728', '성공적으로 작동합니다.')
            result = "오늘은 이미 업데이트되었습니다."
    return result


def dsschool():
    marketing = requests.get(
        "https://dsschool.co.kr/marketing/suggestions").text
    data_analytics = requests.get("https://dsschool.co.kr/suggestions").text

    soup_mkt = BeautifulSoup(marketing, 'html.parser')
    soup_data = BeautifulSoup(data_analytics, 'html.parser')

    # 리스트 만들기
    name = []
    summary = []
    price = []
    discount = []
    discount_price = []
    category = []
    link = []
    update_date = []

    for i in range(2):
        name.append(soup_mkt.select('h3.course-name')[i].text)
        summary.append(soup_mkt.select('h3.course-summary')[i].text)
        price_origin = soup_mkt.select('h3.course-price')[i*2].text[0:-2]
        price_origin = price_origin.replace(',', '')
        price_origin = int(price_origin)
        price.append(price_origin)
        discount_origin = soup_mkt.find_all(
            'a', {"class": "btn-course btn-purchase"})[i].text[0:2]
        discount_origin = int(discount_origin)
        discount.append(discount_origin)
        discount_price.append(int(price_origin*(100-discount_origin)/1000000))
        category.append("마케팅")
        link.append("https://dsschool.co.kr/marketing/suggestions")
        update_date.append(timezone.localtime())

    # 리스트 만들기
    # price 문자열 내 ','제거, 정수화한 후 만원 단위로 변경
    price = list(map(int, price))
    price = np.array(price)
    b = [10000]*2
    b = np.array(b)
    price = price/b
    price = list(map(int, price))

    for i in range(6):
        name.append(soup_data.select('h3.course-name')[i].text)
        summary.append(soup_data.select('h3.course-summary')[i].text)
        price_origin = soup_data.select('h3.course-price')[i].text[0:-2]
        price_origin = price_origin.replace(',', '')
        price_origin = int(price_origin)
        price.append(price_origin)
        discount_origin = soup_data.find_all(
            'a', {"class": "btn-course btn-purchase"})[i].text[0:2]
        discount_origin = int(discount_origin)
        discount.append(discount_origin)
        discount_price.append(int(price_origin*(100-discount_origin)/100))
        category.append("데이터분석")
        link.append("https://dsschool.co.kr/suggestions")
        update_date.append(timezone.localtime())

    # 정수로 변환
    price = list(map(int, price))
    discount = list(map(int, discount))

    all_list = (category, name, price, discount,
                discount_price, summary, link, update_date)
    col_names = ["category", "name", "price", "discount",
                 "discount_price", "summary", "link", "update_date"]

    from .mytool import list_to_table
    df = list_to_table(all_list, col_names)

    return df


def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            df = dsschool()
            df_sql(df)
            return redirect('index')
            # "Save" 버튼을 누른 후에 결과 페이지.
            # index는 메인 페이지로 이동. new_lotto는 입력 페이지로 이동
            # reverse는 결과만 보여줌
    else:
        form = PostForm()
        # forms.py의 PostForm 클래스의 인스턴스
        prices_list = Price.objects.all()  # .order_by('-update_date')
        return render(request, 'dsschool/form.html', {'prices_list': prices_list})

        # 템플릿 파일 경로 지정, 데이터 전달


# 문자 메시지 전송

def unique_id():
    return str(uuid.uuid1().hex)


def get_iso_datetime():
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    return datetime.datetime.now().replace(tzinfo=datetime.timezone(offset=utc_offset)).isoformat()


def get_signature(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.sha256).hexdigest()


def get_headers(apiKey, apiSecret):
    date = get_iso_datetime()
    salt = unique_id()
    data = date + salt
    return {'Authorization': 'HMAC-SHA256 ApiKey=' + apiKey + ', Date=' + date + ', salt=' + salt + ', signature=' +
                             get_signature(apiSecret, data)}


def sendmessage(to, text):
    import requests
    import configparser
    # import auth
    import json
    import time
    import datetime
    import uuid
    import hmac
    import hashlib

    config = configparser.ConfigParser()
    config.read('static/sms/config.ini')
    # config.read('/static/sms/config.ini') 못찾음
#    config.read('../static/sms/config.ini') 파일 못찾음

    # f = open('static/sms/config.ini', 'r')
    # lines = f.readlines()
    # print(lines) ==> 읽힘

    apiKey = config['AUTH']['ApiKey']
    apiSecret = config['AUTH']['ApiSecret']

    if __name__ == '__main__':
        data = {
            'message': {
                'to': to,
                'from': '01033487728',
                'text': text,
            }
        }
        res = requests.post(config['SERVER']['URI']+'send',
                            headers=get_headers(apiKey, apiSecret), json=data)
        print(json.loads(res.text))


'''
def index2(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos': lottos})

def modify(request, memokey): #memokey 변수를 url에서 가져온다
    if request.method == "POST":
        #수정 저장
        memo = Memos.objects.get(pk = memokey)
        form = PostForm(request.POST, instance=memo) # 새로 입력된 인스턴스 데이터를 form 인스턴스에 새로 담는다.
        if form.is_valid():
             form.save() # 변경한 form을 저장한다 (수정, 업데이트)
             return redirect('index')
    else:
        #수정 입력
        memo = Memos.objects.get(pk = memokey) # 특정 데이터를 인스턴스에 담는다.
        form = PostForm(instance = memo) # 기존에 존재하는 데이터를 가져온다. (수정화면에 내용 포함)
        return render(request, 'memo_app/modify.html', {'memo' : memo, 'form' : form})

def delete(request, memokey):
    memo = Memos.objects.get(pk = memokey)
    memo.delete()
    return redirect('index')

'''
