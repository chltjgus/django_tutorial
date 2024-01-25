# Create your views here.
import requests
from django.shortcuts import render
from .models import JejuValuePlace

from django.conf import settings

DATA_API_KEY = settings.DATA_API_KEY


# Create your views here.


def call_api_jeju(request):
    # 쿼리 파라미터 방식
    page_no = int(request.GET.get("pageNo", 1))

    # api 요청
    url_base = f"http://apis.data.go.kr/6510000/goodPriceStoreService/getGoodPirceStoreList?ServiceKey={DATA_API_KEY}"

    if page_no > 1:
        url_base += f"&pageNo={page_no}"

    res_data = requests.get(url_base)

    # 안티패턴
    if not res_data.status_code == 200 or page_no < 1:
        return render(request, "error_500.html")

    api_data = res_data.json()

    total_page = api_data['response']['body']['totalCount']
    page_no = api_data['response']['body']['pageNo']
    items = api_data['response']['body']['items']['item']
    print(total_page, page_no)
    end_page_number = (total_page // 10) + 1

    data = {
        "total_page": total_page,
        "page_no": page_no,
        "items": items,
        "end_page_number": end_page_number,
    }
    for v in items:
        save_jeju_value_place_data(v)

    return render(request, "api_list.html", {"data": data})


def save_jeju_value_place_data(val: dict):
    if not JejuValuePlace.objects.filter(bsshNm=val.get('bsshNm')).exists():
        JejuValuePlace.objects.create(
            emdNM=val.get('emdNm', None),
            bsshNm=val.get('bsshNm', None),
            indutyNm=val.get('indutyNm', None),
            rnAdres=val.get('rnAdres', None),
            bsshTelno=val.get('bsshTelno', None),
            prdlstCn=val.get('prdlstCn', None),
            etcCn=val.get('etcCn', None),
            regDt=val.get('regDt', None),
            laCrdnt=val.get('laCrdnt', None),
            loCrdnt=val.get('loCrdnt', None),
            dataCd=val.get('dataCd', None),
            slctnYr=val.get('slctnYr', None),
            slctnMm=val.get('slctnMm', None),
        )