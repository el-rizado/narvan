from json import JSONEncoder
from django.http import JsonResponse, HttpResponseBadRequest


def fib(number):
    if number < 2:
        return number
    return fib(number - 2) + fib(number - 1)


def fibonacci(request):
    number = int(request.GET['number'])
    if number > 0:
        response = {f'fibonacci({number})': fib(number-1)}
    else:
        response = {'error': 'number must be positive'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)
    return JsonResponse(response, encoder=JSONEncoder)


def fac(number):
    fac_sum = 1
    for i in range(1, number+1):
        fac_sum *= i
    return fac_sum


def factorial(request):
    number = int(request.GET['number'])
    if number >= 0:
        response = {f'factorial({number})': fac(number)}
    else:
        response = {'error': 'number must be equal or greater than 0'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)
    return JsonResponse(response, encoder=JSONEncoder)


def ack(number1, number2):
    if number1 == 0:
        return number2+1
    elif number1 > 0 and number2 == 0:
        return ack(number1-1, 1)
    else:
        return ack(number1-1, ack(number1, number2-1))


def ackermann(request):
    number1 = int(request.GET['number1'])
    number2 = int(request.GET['number2'])
    if number1 >= 0 and number2 >= 0:
        response = {f'ackermann({number1},{number2})': ack(number1, number2)}
    else:
        response = {'error': 'numbers must be equal or greater than 0'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)
    return JsonResponse(response, encoder=JSONEncoder)
