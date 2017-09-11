from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from extra.serializers import WorksheetsSerializer
from test_task_app.models import Claims, WorkSheets
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.authentication import BasicAuthentication
from test_task_app.views import CsrfExemptSessionAuthentication


class SendClaim(APIView):
    """
    Send claim. After sending claim.status changes to SENT.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self, pk):
        try:
            return Claims.objects.get(id=pk)
        except Claims.DoesNotExist:
            raise Http404

    @csrf_exempt
    def post(self, request, pk):
        if not request.user.has_perm('test_task_app.send_claims'):
            return HttpResponse(status=403)

        claim = self.get_object(pk)
        claim.update(**{'status': 'SENT', "sent_date": timezone.now()})
        return HttpResponse(status=200)


class WorksheetsList(APIView):
    """
    Retrieve and create worksheet instances.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @csrf_exempt
    def get(self, request):
        if not request.user.has_perm('test_task_app.view_worksheets'):
            return HttpResponse(status=403)

        worksheets = WorkSheets.objects.all()
        serializer = WorksheetsSerializer(worksheets, many=True)

        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        if not request.user.has_perm('test_task_app.add_worksheets'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = WorksheetsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class WorksheetsDetail(APIView):
    """
    Retrieve, update and delete worksheet instance by id.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self, pk):
        try:
            return WorkSheets.objects.get(id=pk)
        except WorkSheets.DoesNotExist:
            raise Http404

    @csrf_exempt
    def get(self, request, pk):
        if not request.user.has_perm('test_task_app.view_worksheets'):
            return HttpResponse(status=403)

        worksheet = self.get_object(pk)
        serializer = WorksheetsSerializer(worksheet)

        return JsonResponse(serializer.data)

    @csrf_exempt
    def put(self, request, pk):
        if not request.user.has_perm('test_task_app.change_worksheets'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        worksheet = self.get_object(pk)
        serializer = WorksheetsSerializer(worksheet, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    @csrf_exempt
    def delete(self, request, pk):
        if not request.user.has_perm('test_task_app.delete_worksheets'):
            return HttpResponse(status=403)

        worksheet = self.get_object(pk)
        worksheet.delete()
        return HttpResponse(status=200)
