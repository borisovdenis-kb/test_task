from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
from test_task_app.models import Claims, Offers
from extra.serializers import ClaimsSerializer, OffersSerializer


def claims_detail(request, pk):
    """        
    get:
    This endpoint to read one claim instance. Available for superuser and creditorgs.
    When creditorg call this endpoint claim.status
    """
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


def offers_detail(request, pk):
    """        
    get:
    This endpoint to read one offer instance. Available for superuser and creditorgs.
    """
    if not request.user.is_authenticated():
        return HttpResponse(status=401)

    try:
        offer = Offers.objects.get(id=pk)
    except Claims.DoesNotExist:
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
