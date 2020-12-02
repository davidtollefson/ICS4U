from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Student
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method =='POST':
        newStudent = StudentSerializer(data=request.data)
        if newStudent.is_valid():
            newStudent.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(newStudent.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def students_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)
    

    elif request.method == 'PUT':
        updatedStudent = StudentSerializer(student, data=request.data, context={'request': request})
        if updatedStudent.is_valid():
            updatedStudent.save()
            return Response(status=status.HTTP_200_OK)
        
        return Response(updatedStudent.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()

        return Response(status=status.HTTP_200_OK)