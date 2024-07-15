from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

# Вставьте ваш API-ключ
api_key = ' AIzaSyDqyj5wC_na5ERaE-hy_7CLbF6SuKjS8Q4'


@csrf_exempt
def query(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query')

            if not query:
                return JsonResponse({'error': 'Query is required'}, status=400)

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
            print(f'Error: {e}')
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


from django.shortcuts import render

# Create your views here.
