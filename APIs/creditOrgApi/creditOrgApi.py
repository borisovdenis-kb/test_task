from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from test_task_app.models import Claims, Offers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import BasicAuthentication
from extra.serializers import ClaimsSerializer, OffersSerializer
from test_task_app.views import CsrfExemptSessionAuthentication


class ClaimsList(APIView):
    """
    Retrieve and Create claims instances.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    @csrf_exempt
    def get(self, request):
        user = request.user
        if not user.has_perm('test_task_app.view_claims'):
            return HttpResponse(status=403)

        claims = Claims.objects.all()
        serializer = ClaimsSerializer(claims, many=True)

        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request):
        user = request.user
        if not user.has_perm('test_task_app.add_claims'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = ClaimsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class ClaimsDetail(APIView):
    """
    Retrieve, update and delete claim instance by id.
    """
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get_object(self, pk):
        try:
            return Claims.objects.get(id=pk)
        except Claims.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        if not request.user.has_perm('test_task_app.view_claims'):
            return HttpResponse(status=403)

        claim = self.get_object(pk)
        serializer = ClaimsSerializer(claim)

        if request.user.groups.get().name == 'creditorg':
            claim.update(**{'status': 'RECIEVED'})

        return JsonResponse(serializer.data)

    def put(self, request, pk):
        if not request.user.has_perm('test_task_app.change_claims'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        claim = self.get_object(pk)
        serializer = ClaimsSerializer(claim, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, pk):
        if not request.user.has_perm('test_task_app.delete_claims'):
            return HttpResponse(status=403)

        claim = self.get_object(pk)
        claim.delete()
        return HttpResponse(status=200)


# def claims_list(request):
#     if not request.user.is_authenticated():
#         return HttpResponse(status=401)
#
#     user = request.user
#
#     if request.method == 'GET':
#         if not user.has_perm('test_task_app.view_claims'):
#             return HttpResponse(status=403)
#
#         claims = Claims.objects.all()
#         serializer = ClaimsSerializer(claims, many=True)
#
#         return JsonResponse(serializer.data, safe=False)
#
#     if request.method == 'POST':
#         if not user.has_perm('test_task_app.add_claims'):
#             return HttpResponse(status=403)
#
#         data = JSONParser().parse(request)
#         serializer = ClaimsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


def claims_detail(request, pk):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    try:
        claim = Claims.objects.get(id=pk)
    except Claims.DoesNotExist:
        return HttpResponse(status=404)

    user = request.user

    if request.method == 'GET':
        if not user.has_perm('test_task_app.view_claims'):
            return HttpResponse(status=403)

        serializer = ClaimsSerializer(claim)

        if request.user.groups.get().name == 'creditorg':
            claim.update(**{'status': 'RECIEVED'})

        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        if not user.has_perm('test_task_app.change_claims'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = ClaimsSerializer(claim, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if not user.has_perm('test_task_app.delete_claims'):
            return HttpResponse(status=403)

        claim.delete()
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)


def offers_list(request):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    user = request.user

    if request.method == 'GET':
        if not user.has_perm('test_task_app.view_offers'):
            return HttpResponse(status=403)

        offers = Offers.objects.all()
        serializer = OffersSerializer(offers, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        if not user.has_perm('test_task_app.add_offers'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = OffersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    else:
        return HttpResponse(status=405)


def offers_detail(request, pk):
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    try:
        offer = Offers.objects.get(id=pk)
    except Offers.DoesNotExist:
        return HttpResponse(status=404)

    user = request.user

    if request.method == 'GET':
        if not user.has_perm('test_task_app.view_offers'):
            return HttpResponse(status=403)

        serializer = OffersSerializer(offer)

        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        if not user.has_perm('test_task_app.change_offers'):
            return HttpResponse(status=403)

        data = JSONParser().parse(request)
        serializer = OffersSerializer(offer, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        if not user.has_perm('test_task_app.delete_offers'):
            return HttpResponse(status=403)

        offer.delete()
        return HttpResponse(status=200)

    else:
        return HttpResponse(status=405)
