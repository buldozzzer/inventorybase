import uuid

from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.files.storage import default_storage

from . import recognizer


class RecognizerView(APIView):
    def get(self, _):
        return Response({
            'check': True
        }, status=200)

    def post(self, request):
        payload = request.data
        filename = "{}.png".format(str(uuid.uuid4()))
        with default_storage.open(filename, 'wb+') as destination:
            for chunk in payload['file'].chunks():
                destination.write(chunk)
        print(settings.MEDIA_ROOT + filename)
        result = recognizer.recognizer('media/' + filename)
        return Response({
            'extracting_data': result
        }, status=201)
