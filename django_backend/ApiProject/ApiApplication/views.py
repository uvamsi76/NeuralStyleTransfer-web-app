from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .serializers import ImageSerializer
from django.core.files.base import ContentFile
from django.http import HttpResponse
from PIL import Image
import io

class ImageProcessView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']

            # Open the image using PIL
            pil_image = Image.open(image)

            # Perform your image processing here
            processed_image = pil_image.convert("L")  # Example: Convert to grayscale

            # Save processed image to a bytes buffer
            buffer = io.BytesIO()
            processed_image.save(buffer, format='JPEG')
            buffer.seek(0)

            # Create a Django file-like object
            file = ContentFile(buffer.read(), name='processed_image.jpg')

            return HttpResponse(buffer, content_type='image/jpeg')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
