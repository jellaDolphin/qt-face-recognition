# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from restapi.api import Histogram


class GenerateHistogramView(APIView):

    def post(self, request, histogram_type):
        # get the image location
        image_location = request.data.get('image_url')

        # use opencv to create a histogram and return results
        histogram = Histogram(image_location, histogram_type=histogram_type)
        data = histogram.generate()
        return Response(data)

    def get(self, request, histogram_type):
        return Response({'foo': 'bar'})
