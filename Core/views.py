from django.shortcuts import render
from .models import ADS, Company, Category
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def allVacancies(request):
    vacancies = ADS.objects.all()
    vacancies_json = serialize('json', vacancies)
    parsed_vacancies = json.loads(vacancies_json)

    readable_vacancies = []

    for vacancy in parsed_vacancies:
        fields = vacancy['fields']
        created_at_str = fields['created_at']
        created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        formatted_date = created_at.strftime('%d %b')
        
        
        deadline = created_at + timedelta(days=30)
        formatted_deadline = deadline.strftime('%d %b')

        company_id = fields['company_id']
        company_instance = Company.objects.get(id=company_id)
        category_ids = fields['category_id']
        
        categories = []
        for category_id in category_ids:
            category_instance = Category.objects.get(id=category_id)
            category_info = {
                'id': category_id,
                'image': str(category_instance.image),
                'name': str(category_instance.name),
                'slug': str(category_instance.slug), 
            }
            categories.append(category_info)

        readable_vacancy = {
            'id': vacancy['pk'],
            'name': fields['name'],
            'company_id': {
                'id': company_id,
                'image': str(company_instance.image),
                'name': str(company_instance.name),
                'slug':str(company_instance.slug),
                'description':str(company_instance.description),
                'phone':str(company_instance.phone),
                'website':str(company_instance.website),
                'location':str(company_instance.location),
            },
            'demands': fields['demands'],
            'responsibilities': fields['responsibilities'],
            'conditions': fields['conditions'],
            'created_at': formatted_date,
            'deadline': formatted_deadline, 
            'to_choose': fields['to_choose'],
            'views_count': fields['views_count'],
            "email": fields['email'],
            'category_id': categories,
            'slug': fields['slug'],
        }
        readable_vacancies.append(readable_vacancy)

    return JsonResponse({'vacancies': readable_vacancies}, safe=False)

@require_POST
@csrf_exempt
def update_likes(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        vacancy_slug = data.get('slug')
        to_choose = data.get('to_choose', False)


        try:
            vacancy = ADS.objects.get(slug=vacancy_slug)
            vacancy.to_choose = to_choose
            vacancy.save()
            return JsonResponse({'success': True})
        except ADS.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Vacancy not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


@require_POST
@csrf_exempt
def update_views_count(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        vacancy_slug = data.get('slug')
        views_count = data.get('views_count',0)  # Remove the trailing comma

        try:
            vacancy = ADS.objects.get(slug=vacancy_slug)
            vacancy.views_count = views_count
            vacancy.save()
            return JsonResponse({'success': True})
        except ADS.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Vacancy not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
