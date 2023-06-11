from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser,MultiPartParser
from rest_framework import status


@api_view(['GET'])
def studentsInfo(request):
    users=Student.objects.all()
    # print(users)
    serializer=StudentSerializers(users,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def studentInfo(request,pk):
    student=Student.objects.get(id=pk)
    serializer=StudentSerializers(student,many=False)
    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def Addstudent(request):

    serializer = StudentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        # print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['PUT'])
def update_student(request, pk):
    try:
        obj = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = StudentSerializers(obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        # print("hi")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        obj = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)