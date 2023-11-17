from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime 
from django.db.models import Q


class MasterRoom_API(APIView):
    def post(self,request):
        serializer=MasterRoom_Serializers_Input(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('Rooms_name')
            if not MasterRoom.objects.filter(Rooms_name=name).first():
                MasterRoom.objects.create(**serializer.validated_data).save()
                return Response({'message':f'{name} meeting room is Created Successfully'},status=status.HTTP_201_CREATED)
            return Response({'message':f'{name} meeting room is already Exists'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        queryset=MasterRoom.objects.all()
        Booking_datas=MasterRoom_Serializers(queryset,many=True)
        return Response(Booking_datas.data,status=status.HTTP_200_OK)


    

class Booking_API(APIView):
    def post(self,request):
        serializer=Booking_Serializers(data=request.data)
        if serializer.is_valid():
            room=serializer.validated_data.get('Booking_Room')
            Name=serializer.validated_data.get('Bookingname')
            start_time=serializer.validated_data.get('Starting_Time')
            end_time=serializer.validated_data.get('Ending_Time')
            data=serializer.validated_data.get('date')
         
            booking=Booking.objects.filter(Booking_Room=room,date=data,Starting_Time=start_time,Ending_Time=end_time).first() or Booking.objects.filter(Booking_Room=room,date=data,Ending_Time=start_time).first()

            
            if not booking:
                Booking.objects.create(**serializer.validated_data).save()
                return Response({'message':f'Mr/Mrs {Name} your meeting room is Booked successfully by you'},status=status.HTTP_201_CREATED)
                    
            return Response({'message':f'Mr/Mrs {Name} your meeting room is Not Available On that time in this Room after {booking.Ending_Time.strftime("%H:%M")} is available'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        queryset=Booking.objects.all()
        Booking_datas=Booking_Serializers(queryset,many=True)
        return Response(Booking_datas.data,status=status.HTTP_200_OK)
    
    def put(self,request):
        id=request.query_params.get('id')
        queryset=Booking.objects.get(id=id)
        serializer=Booking_Serializers(queryset,data=request.data) 
        if serializer.is_valid():
            room=serializer.validated_data.get('Booking_Room')
            Name=serializer.validated_data.get('Bookingname')
            start_time=serializer.validated_data.get('Starting_Time')
            end_time=serializer.validated_data.get('Ending_Time')
            
            booking=Booking.objects.filter(Booking_Room=room,Starting_Time=start_time,Ending_Time=end_time).first()
            if not booking:
                if  Booking.objects.filter(Booking_Room=room,Ending_Time=start_time).first():
                     return Response({'message':f'Mr/Mrs {Name} your meeting room is Not Available On that time in this Room'},status=status.HTTP_404_NOT_FOUND)
                serializer.save()
                return Response({'message':f'Mr/Mrs {Name} your meeting room is Booking Updated successfully by you'},status=status.HTTP_201_CREATED)
                    
            return Response({'message':f'Mr/Mrs {Name} your meeting room is Not Available On that time in this Room after {booking.Ending_Time.strftime("%H:%M")} is available'},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request):
        id=request.query_params.get('id')
        queryset=Booking.objects.get(id=id)
        queryset.delete()
        return Response({'message':f'{queryset.Bookingname } meeting room is Deleted Sucessfully'},status=status.HTTP_200_OK)

class BookingSearchAPI(APIView):
    def get(self, request):
        serializer = BookingSearchSerializer(data=request.query_params)
        if serializer.is_valid():
            room_id = serializer.validated_data.get('room_id', None)
            start_time = serializer.validated_data.get('start_time', None)
            end_time = serializer.validated_data.get('end_time', None)

            query_params = {}
            if room_id:
                query_params['Booking_Room'] = room_id
            if start_time:
                query_params['Starting_Time__gte'] = start_time
            if end_time:
                query_params['Ending_Time__lte'] = end_time

            bookings = Booking.objects.filter(**query_params)

          
            serializer = Booking_Serializers(bookings, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    