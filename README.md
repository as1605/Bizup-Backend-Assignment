## Task
```
Make a python based REST API to extract important colors from an image.
Input will be a logo image, output will be 2 color values - a) color of the image border, b) primary logo color


The api specification should be as the following 
Get request to your_api_endpoint with image src url as a attribute
For e.g. 

http://your_api_endpoint.com?src=https://storage.googleapis.com/bizupimg/profile_photo/goodwell_logo.png

should return json 

{
'logo_border': '#ECECEC',
'dominant_color': '#0A67BB'
}


Run your api on these 4 samples and present the output colors in a file named 'test_outputs.md' in your repo.

https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg
https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png
https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg
https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png

Note: Aim of the assignment is to evaluate SDE related skills(logic, modularity, readability), so please use your best judgement in case of confusion over a specific terminology. 
```
## Installation
* ```git clone https://github.com/as1605/Bizup-Backend-Assignment.git && cd backend```
* [python](https://www.python.org/downloads/)
* [virtual environment](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)
```python3 -m venv env```
* dependencies
```python3 -m pip install -r requirements.txt```
* run ```python3 manage.py runserver```
* from browser or otherwise, make GET request in format ```http://localhost:8000/?src=https://storage.googleapis.com/bizupimg/profile_photo/goodwell_logo.png```
## Outputs
![Example](https://storage.googleapis.com/bizupimg/profile_photo/goodwell_logo.png)

`{"logo_border": "#095796", "dominant_color": "#5899CE"}`

![Sample1](https://storage.googleapis.com/bizupimg/profile_photo/WhatsApp%20Image%202020-08-23%20at%203.11.46%20PM%20-%20Himanshu%20Kohli.jpeg) 

`{"logo_border": "#5E980E", "dominant_color": "#EEEEEE"}`

![Sample2](https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png) 

`{"logo_border": "#000000", "dominant_color": "#000000"}`

![Sample3](https://storage.googleapis.com/bizupimg/profile_photo/bhawya_logo.jpeg) 

`{"logo_border": "#8F0A1E", "dominant_color": "#BF9962"}`

![Sample4](https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png) 

`{"logo_border": "#000010", "dominant_color": "#3B3967"}`
