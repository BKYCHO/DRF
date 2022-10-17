from msilib.schema import ReserveCost
from rest_framework.response import Response
from .serialaziers import WomenSerialaizer
from .models import Women
from rest_framework.views import APIView 



# class WomenModel():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts':WomenSerialaizer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerialaizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'posts': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': "Method PUT not allowed"})

        try:
            instanse = Women.objects.get(pk=pk)
        except:
            return Response({'error': "Object does not exists"})

        serializer = WomenSerialaizer(data=request.data, instance=instanse)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'posts': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({'error': "Method Delete not allowed"})

        try:
            instanse = Women.objects.get(pk=pk)
            instanse.delete()
        except:
            return Response({'error': "Object does not exists"})
 
        # serializer = WomenSerialaizer(data=request.data)
        # serializer.is_valid(raise_exception=True)

        # serializer.save()       

        return Response({'posts': "delete post:" + str(pk)})











