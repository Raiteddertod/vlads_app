
























from django.shortcuts import render
from django.http import JsonResponse
import gemini_api  # Импорт официальной библиотеки Gemini API

# Вставьте ваш API-ключ
api_key = 'AIzaSyDqyj5wC_na5ERaE-hy_7CLbF6SuKjS8Q4'

def query(request):
    if request.method == 'GET':
        query = request.GET.get('query')

        if not query:
            return JsonResponse({'error': 'Требуется запрос'}, status=400)

        try:
            # Инициализация клиента Gemini API
            client = gemini_api.Client(api_key)

            # Выполнение запроса
            response = client.generate(
                model='gemini-1.5-flash-latest',
                content=[{'text': query}]
            )

            return JsonResponse(response)
        except gemini_api.exceptions.ApiException as e:
            print(f'Ошибка: {e}')
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Недопустимый метод запроса'}, status=400)
