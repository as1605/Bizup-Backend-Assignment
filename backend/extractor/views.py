from django.http import JsonResponse
import requests as web_requests
import io
from PIL import Image
import numpy as np
import cv2 as cv

# Create your views here.
def index(request):
    src = request.GET.get('src')
    if src is None:
        return JsonResponse({"Error" : "Please specify image src"})
    img_response = web_requests.get(src)
    if img_response.status_code >=400 :
        return JsonResponse({"Host Error" : str(img_response.status_code)})
    
    #Reads image
    image_bytes = io.BytesIO(img_response.content)
    img = Image.open(image_bytes).convert("RGB")
    img = np.array(img)
    #Finds threshold value for segmentation
    thresh = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    ret, thresh = cv.threshold(thresh, 0, 255, cv.THRESH_BINARY+cv.THRESH_TRIANGLE)
    
    #sorts according to threshold result
    border = []
    primary = []
    for col in img:
        for c in col:
            if int(c[0])+int(c[1])+int(c[2]) > 3*int(ret):
                primary.append(c)
            else:
                border.append(c)

    #takes average of that segment
    primary_r, primary_b, primary_g = 0, 0, 0
    for c in primary:
        primary_r += int(c[0])
        primary_g += int(c[1])
        primary_b += int(c[2])
    primary_r /= len(primary)+1
    primary_g /= len(primary)+1
    primary_b /= len(primary)+1
    border_r, border_b, border_g = 0, 0, 0
    for c in border:
        border_r += int(c[0])
        border_g += int(c[1])
        border_b += int(c[2])
    border_r /= len(border)+1
    border_g /= len(border)+1
    border_b /= len(border)+1

    #converts to rgb hex
    primary_rgb = "#%0.2X%0.2X%0.2X" % (int(primary_r), int(primary_g), int(primary_b))
    border_rgb  = "#%0.2X%0.2X%0.2X" % (int(border_r), int(border_g), int(border_b))

    output = {
        'logo_border' : border_rgb,
        'dominant_color' : primary_rgb,
    }
    return JsonResponse(output)