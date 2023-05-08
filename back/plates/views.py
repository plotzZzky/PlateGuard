from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from .models import Plate, ListPlates
from .serializer import serialize_plate
from .validate import validate_plate


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show_all_plates(request):
    post_name = request.user.profile.office.name
    query = ListPlates.objects.get(name=post_name)  # type:ignore
    data = [serialize_plate(item) for item in query.plate_set.all()]
    return JsonResponse({"plates": data}, safe=False)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def create_plate(request):
    try:
        post_name = request.user.profile.office.name
        post = ListPlates.objects.get(name=post_name)  # type:ignore
        number = request.POST['number'].upper()
        city = request.POST['city'].title()
        manufac = request.POST['manufac'].capitalize()
        model = request.POST['model'].capitalize()
        color = request.POST['color'].capitalize()
        year = request.POST['year']
        qru = request.POST['qru'].capitalize()
        if validate_plate(number, year, city, manufac, model, color):
            plate = Plate(
                post_name=post,
                number=number,
                city=city,
                manufacturer=manufac,
                model=model,
                color=color,
                year=year,
                qru=qru
            )
            plate.save()
            return HttpResponse('Placa criada', status=200)
        return HttpResponse('Formulario invalido', status=400)
    except KeyError:
        return HttpResponse('Formulario incompleto', status=400)


@api_view(['POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def edit_plate(request, plate_id):
    try:
        number = request.POST['number'].upper()
        city = request.POST['city'].title()
        manufac = request.POST['manufac'].capitalize()
        model = request.POST['model'].capitalize()
        color = request.POST['color'].capitalize()
        year = request.POST['year'].capitalize()
        qru = request.POST['qru'].capitalize()
        if validate_plate(number, year, city, manufac, model, color):
            query = Plate.objects.get(pk=plate_id)  # type:ignore
            query.number = number
            query.city = city
            query.manufacturer = manufac
            query.model = model
            query.color = color
            query.year = year
            query.qru = qru
            query.save()
            return HttpResponse('Placa criada', status=200)
        return HttpResponse("Formulario incorreto", status=300)
    except KeyError:
        return HttpResponse("Informções incompletas", status=400)
    except Plate.DoesNotExist:  # type:ignore
        return HttpResponse("Placa não encontrada", status=400)


@api_view(['DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_plate(request, plate_id):
    try:
        plate = Plate.objects.get(pk=plate_id)  # type:ignore
        plate.delete()
        return HttpResponse('Placa deletada', status=200)
    except Plate.DoesNotExist:  # type:ignore
        return HttpResponse('Placa não encontrada', status=400)
