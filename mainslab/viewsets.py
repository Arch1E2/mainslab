from argparse import Action
from .serializers import BillSerializer
from .models import Bill
from .filters import BillFilter
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
import openpyxl
import datetime


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BillFilter

    #create from xlsx file
    @action(detail=False, methods=['POST'])
    def xlsx_parse(self, request, *args, **kwargs):
        files = request.FILES['files']
        wb = openpyxl.load_workbook(files)
        sheet = wb.active
        rows = sheet.rows
        for row in rows:
            if row[0].value == 'client_name':
                pass
            else:
                row_data = {
                    'client_name': row[0].value,
                    'client_org': row[1].value,
                    'number': row[2].value,
                    'date': row[4].value.strftime('%Y-%m-%d'),
                    'sum': row[3].value,
                    'service': row[5].value,
                }
                serializer = BillSerializer(data=row_data)
                if serializer.is_valid():
                    print("valid")
                    serializer.save()
                else:
                    print(row_data)
                    print(serializer.errors)

        return Response("200")
