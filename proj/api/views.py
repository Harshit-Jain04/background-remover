# myapi/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import ImageSerializer
from PIL import Image
import rembg
import base64
from django.http import FileResponse,HttpResponse
import tempfile
import os
import io
from datetime import datetime
from PIL import Image

class ProcessImageView(APIView):

    def post(self, request):
        if "Authorization" not in request.headers:
            return HttpResponse("Unauthorized",status =401)
        if request.headers['Authorization'] !="12345":
            return HttpResponse("Wrong token",status=400)
       
        if request.method == 'POST':
        # Check if request contains an image file
            if 'image' not in request.FILES:
                return HttpResponse('No image file provided', status=400)

            # Read the image file from the request
            image_file = request.FILES['image']
            a = rembg.remove(Image.open(image_file))
            
            im = io.BytesIO()
            a.save(im,format='png')
            return HttpResponse(im.getvalue(), content_type='image/png')
            #return Response(processed_image)
            
            

        return HttpResponse('Unsupported method', status=405)
        
def check(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Django Website</title>
    </head>
    <body>
        <h1>Welcome to My Django Website</h1>
        <p>This Website is working.</p>
    </body>
    </html>
    """
    return HttpResponse(html_content)

    
