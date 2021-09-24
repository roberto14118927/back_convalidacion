from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.utils.decorators import method_decorator

from Control_T.serializer import Termo_Create_Serializers, Termo_Serializers , Empadre_termo_Serializers
from Control_T.models import Inventario_termo , Empadre_Termo
from Control_Em.models import Control_Empadre


#------------ VIEWS PARA EMPADRE ------------------
#TRAE TODOS LOS EMPADRES
class Empadre_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Empadre_Termo.objects.all().order_by("id")
            serializer = Empadre_termo_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response( status = status.HTTP_400_BAD_REQUEST)


#TRAE EMPADRE POR ID
class Empadre_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Empadre_Termo.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = Empadre_termo_Serializers(queryset , many=True)
                    return Response(data= serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO EMPADRE
class Empadre_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):

        id_t = request.data["id_inv_termo"] 
        id_v = request.data["id_empadre"]
        
        try:
            topic_t = Inventario_termo.objects.get(id=id_t)
            topic_v = Control_Empadre.objects.get(id=id_v)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        cow_data = request.data
        cow_data["id_inv_termo"] = topic_t
        cow_data["id_empadre"] = topic_v

        new_cow = Empadre_Termo.objects.create(
            id_empadre = cow_data["id_empadre"],
            id_inv_termo = cow_data["id_inv_termo"]
        )

        new_cow.save()
        serializer = Empadre_termo_Serializers(new_cow)

        return Response(serializer.data , status= status.HTTP_201_CREATED)



#ACTUALIZA UN EMPADRE
class Empadre_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Empadre_Termo.objects.get(id = id)
            serializer = Empadre_termo_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN EMPADRE 
class Empadre_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Empadre_Termo.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)



#----------------VIEWS PARA TERMOCRIOGENICO ----------------------
#TRAE TODOS LOS REGISTROS EN TERMO
class Termo_List(APIView):
    #permission_classes = [IsAuthenticated]
    def get (self , request ):
        try:
            queryset = Inventario_termo.objects.all().order_by("id")
            serializer = Termo_Serializers(queryset, many= True)
            return Response(data = serializer.data , status= status.HTTP_200_OK)
        except Exception as e: 
            return Response( status = status.HTTP_400_BAD_REQUEST)


#TRAE POR ID
class Termo_ListById(APIView):
    #permission_classes =[IsAuthenticated]
    def get (self , request , id=0):
        try:
            if (id > 0): 
                queryset = Inventario_termo.objects.filter(id=id)
                if len(queryset) > 0: 
                    serializer = Termo_Serializers(queryset , many=True)
                    return Response(data=serializer.data , status= status.HTTP_200_OK)
                else:
                    return Response(status = status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status = status.HTTP_404_NOT_FOUND)
                

#CREA UN NUEVO REGISTRO EN TERMO
class Termo_Create(APIView):
    @method_decorator(csrf_exempt)
    def post (self, request):
        try:
            serializer = Termo_Create_Serializers(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)
    
    

#ACTUALIZA UN REGISTRO EN TERMO
class Termo_Update(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def put (self, request , id):
        try:
            cows = Inventario_termo.objects.get(id = id)
            serializer = Termo_Serializers(cows , request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status= status.HTTP_200_OK)

        except Exception as e:
            return Response( status = status.HTTP_400_BAD_REQUEST)
    

#ELIMINA UN REGISTRO EN TERMO 
class Termo_Delete(APIView):
    #permission_classes =[IsAuthenticated]
    @method_decorator(csrf_exempt)
    def delete(self, request , id):
        try:
            user = Inventario_termo.objects.get(id =id)
            user.delete()
            return Response( status= status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_BAD_REQUEST)