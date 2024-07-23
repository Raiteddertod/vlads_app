
from django.shortcuts import render
from django.http import JsonResponse, request
import requests

# Вставьте ваш API-ключ
api_key = 'AIzaSyDqyj5wC_na5ERaE-hy_7CLbF6SuKjS8Q4'

def query(request):
    if request.method == 'GET':
        try:
            query = request.GET.get('query')

            if not query:
                return JsonResponse({'error': 'Требуется запрос'}, status=400)

            response = requests.post(
                'https://api.generativeai.googleapis.com/v1/generate',
                headers={
                    'Authorization': f'Bearer {api_key}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gemini-1.5-flash-latest',
                    'content': [{'text': query}]
                }
            )

            response.raise_for_status()
            result = response.json()

            return JsonResponse(result)
        except requests.exceptions.RequestException as e:
            print(f'Ошибка: {e}')
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Недопустимый метод запроса'}, status=400)
