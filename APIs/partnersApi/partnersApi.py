from django.utils import timezone
from rest_framework.parsers import JSONParser
from extra.serializers import WorksheetsSerializer
from django.http import HttpResponse, JsonResponse
from test_task_app.models import Claims, WorkSheets


def send_claim(request, pk):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    try:
        claim = Claims.objects.get(id=pk)
    except Claims.DoesNotExist:
        return HttpResponse(status=404)

    user = request.user

    if request.method == 'POST':
        if not user.has_perm('test_task_app.send_claims'):
            return HttpResponse(status=403)

        claim.update(**{'status': 'SENT', "sent_date": timezone.now()})
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)


def worksheets_list(request):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    user = request.user

    if request.method == 'GET':
        if not user.has_perm('test_task_app.view_worksheets'):
            return HttpResponse(status=403)

        worksheets = WorkSheets.objects.all()
        serializer = WorksheetsSerializer(worksheets, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        if not user.has_perm('test_task_app.add_worksheets'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = WorksheetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def worksheets_detail(request, pk):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    try:
        worksheet = WorkSheets.objects.get(id=pk)
    except WorkSheets.DoesNotExist:
        return HttpResponse(status=404)

    user = request.user

    if request.method == 'GET':
        if not user.has_perm('test_task_app.view_worksheets'):
            return HttpResponse(status=403)

        serializer = WorksheetsSerializer(worksheet)

        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        if not user.has_perm('test_task_app.change_worksheets'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = WorksheetsSerializer(worksheet, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if not user.has_perm('test_task_app.delete_worksheets'):
            return HttpResponse(status=403)

        worksheet.delete()
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)
