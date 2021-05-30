from django.shortcuts import render
from django.http import JsonResponse
import requests
import io
from PIL import Image
import numpy as np

# Create your views here.
def index(request):
    src = request.GET.get('src')
    if src is None:
        return JsonResponse({"Error" : "Please specify image src"})
    response = requests.get(src)
    if response.status_code >=400 :
        return JsonResponse({"Host Error" : str(response.status_code)})
    image_bytes = io.BytesIO(response.content)
    img = np.array(Image.open(image_bytes))
    colors, count = np.unique(img.reshape(-1,img.shape[-1]), axis=0, return_counts=True)
    lb="#"
    lb+="%0.2X" % img[1][1][-3]
    lb+="%0.2X" % img[1][1][-2]
    lb+="%0.2X" % img[1][1][-1]
    dc="#"
    dc+="%0.2X" % colors[count.argmax()][-3]
    dc+="%0.2X" % colors[count.argmax()][-2]
    dc+="%0.2X" % colors[count.argmax()][-1]
    output = {
        'logo_border' : lb,
        'dominant_color' : dc,
    }
    return JsonResponse(output)