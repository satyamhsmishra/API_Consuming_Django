from django.shortcuts import render
import requests
from .serializers import StudentSerializer


'''generator'''
def save_by_generator(insert_data):
    for obj in insert_data:
        yield obj


def save_data(request):
    if request.method=='GET':
        try:
            r=requests.get('Your_API_Url')   # getting the data from another application
            json=r.json()
            for obj in save_by_generator(json):
                serializer=StudentSerializer(data=obj)
                if serializer.is_valid():
                    print(serializer)
                    serializer.save()
        except Exception as e:
            print(e)
    else:
        pass

    return render(request,'home.html',{})