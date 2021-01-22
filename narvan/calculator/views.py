from json import JSONEncoder
from time import time
from django.http import JsonResponse


def fib(number):
    if number < 2:
        return number
    return fib(number - 2) + fib(number - 1)


def fibonacci(request):
    try:
        number = int(request.GET['number'])
        if number > 0:
            start = time()
            result = fib(number-1)
            end = time()
            runtime = end - start
            response = {
                f'fibonacci({number})': result,
                'runtime': runtime
            }
            return JsonResponse(response, encoder=JSONEncoder)
        else:
            response = {'error': 'number must be positive'}
            return JsonResponse(response, encoder=JSONEncoder, status=400)
    except Exception:
        response = {'error': 'argument must be integer'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)


def fac(number):
    fac_sum = 1
    for i in range(1, number+1):
        fac_sum *= i
    return fac_sum


def factorial(request):
    try:
        number = int(request.GET['number'])
        if number >= 0:
            start = time()
            result = fac(number)
            end = time()
            runtime = end - start
            response = {
                f'factorial({number})': result,
                'runtime': runtime
            }
            return JsonResponse(response, encoder=JSONEncoder)
        else:
            response = {'error': 'number must be equal or greater than 0'}
            return JsonResponse(response, encoder=JSONEncoder, status=400)
    except Exception:
        response = {'error': 'argument must be integer'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)


def ack(number1, number2):
    if number1 == 0:
        return number2+1
    elif number1 > 0 and number2 == 0:
        return ack(number1-1, 1)
    else:
        return ack(number1-1, ack(number1, number2-1))


def ackermann(request):
    try:
        number1 = int(request.GET['number1'])
        number2 = int(request.GET['number2'])
        if number1 >= 0 and number2 >= 0:
            start = time()
            result = ack(number1, number2)
            end = time()
            runtime = end - start
            response = {
                f'ackermann({number1},{number2})': result,
                'runtime': runtime
            }
            return JsonResponse(response, encoder=JSONEncoder)
        else:
            response = {'error': 'numbers must be equal or greater than 0'}
            return JsonResponse(response, encoder=JSONEncoder, status=400)
    except Exception:
        response = {'error': 'arguments must be integer'}
        return JsonResponse(response, encoder=JSONEncoder, status=400)
