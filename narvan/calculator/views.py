from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def fib(number):
    if number < 2:
        return number
    return fib(number - 2) + fib(number - 1)


def fibonacci(request, number):
    # return render(request, 'base.html')
    if request.method == 'GET':
        if number >= 0:
            response = {f'fibonacci( {number} )': fib(number-1)}
        else:
            response = {'error': 'number must be positive'}
    return JsonResponse(response)


def fac(number):
    fac_sum = 1
    for i in range(1, number+1):
        fac_sum *= i
    return fac_sum


def factorial(request, number):
    if request.method == 'GET':
        if number >= 0:
            response = {f'factorial( {number} )': fac(number)}
        else:
            response = {'error': 'number must be positive'}
    return JsonResponse(response)
