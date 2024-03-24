import json
import random
import string
from typing import Callable

import httpx
from django.contrib import admin  # noqa
from django.http import HttpRequest, HttpResponse, JsonResponse  # noqa
from django.urls import path

create_random_string: Callable[[int], str] = lambda size: "".join(  # noqa
    [random.choice(string.ascii_letters) for i in range(size)]  # noqa
)  # noqa


def generate_article_idea(request: HttpRequest) -> JsonResponse:
    content = {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }
    return JsonResponse(content)


async def get_current_market_state(request: HttpRequest):
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=XSN17SDSA5RAM5W2"
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url)
    rate: str = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return JsonResponse({"rate": rate})


async def get_exchange_rate(request: HttpRequest) -> HttpResponse:
    post_data = json.loads(request.body)
    source = post_data.get("source")
    destination = post_data.get("destination")

    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={source}&to_currency={destination}&apikey=XSN17SDSA5RAM5W2"

    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get(url=url)
    rate: str = response.json()["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

    result = f"Exchange rate for {source} to {destination} is {rate}"
    return HttpResponse(result)


urlpatterns = [
    path(route="generate-article", view=generate_article_idea),
    path(route="market", view=get_current_market_state),
    path(route="exchange-rate", view=get_exchange_rate),
]
