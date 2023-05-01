from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def EmployeeAPIAll(request):
    if request.method=='GET':
        stu=Employee.objects.all()
        serializer=EmployeeSerializer(stu,many=True)
        return Response({'status':'sucess','Employee':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def EmployeeAPIOne(request,pk):
    if request.method=='GET':
        data=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(data,many=False)
        return Response({'status':'sucess','Employee':serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def EmployeeAPIAdd(request):
    if request.method=='POST':
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Employee Detail uploaded sucessfully','status':'sucess','Employee':serializer.data},
                            status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def  EmployeeAPIUpdate(request,pk):
    if request.method=='PUT':
        id=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(id,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Employee Data Updated Sucessfully','status':'Sucess','Employee':serializer.data},status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def EmployeeAPIDelete(request,pk):
    Employee.objects.get(id=pk).delete()
    return Response({'msg':'Employee Detail Deleted Sucessfully','status':'Sucess'},status=status.HTTP_200_OK)