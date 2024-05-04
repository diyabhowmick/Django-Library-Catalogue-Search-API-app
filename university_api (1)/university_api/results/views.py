# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import BookSerializer
# class StudentMarks(APIView):
#     def get(self, request, reg_no, date_of_birth):
#         try:
#             student = Student.objects.get(reg_no=reg_no, dob=date_of_birth)
#             serializer = StudentSerializer(student)
#             return Response(serializer.data)
#         except Student.DoesNotExist:
#             return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookDetails(APIView):
    def get(self, request, title):
        try:
            book = Book.objects.get(title=title)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
