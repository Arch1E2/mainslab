from wsgiref.validate import validator
from rest_framework import serializers
from .models import Bill
import datetime

# # validate integer field
# def is_int(value):
#     try:
#         return int(value)
#     except:
#         raise serializers.ValidationError('This field must be integer')

# #validate float field
# def is_float(value):
#     try:
#         return float(value)
#     except:
#         raise serializers.ValidationError('This field must be float')

# # validate date field
# def is_date(value):
#     try:
#         valid = datetime.datetime.strptime(value, '%d-%m-%y').date()
#     except:
#         valid = 0

#     if valid == 0:
#         raise serializers.ValidationError('This field must be date')
#     else:
#         return valid

# #validate not empty field
# def is_not_empty(value):
#     if value == '' and value == '-':
#         raise serializers.ValidationError('This field must be not empty')
#     else:
#         return value


class BillSerializer(serializers.ModelSerializer):

    client_name = serializers.CharField()
    client_org = serializers.CharField()
    number = serializers.IntegerField()
    date = serializers.DateField()
    sum = serializers.FloatField()
    service = serializers.CharField()

    class Meta:
        model = Bill
        fields = '__all__'

    
    def validate_client_name(self, value):
        if len(value) > 0 and value != '-':
            return value
        else:
            raise serializers.ValidationError('This field must be not empty')

    def validate_client_org(self, value):
        if len(value) > 0 and value != '-':
            return value
        else:
            raise serializers.ValidationError('This field must be not empty')

    def validate_number(self, value):
        if type(value) == int:
            return value
        else:
            try:
                return int(value)
            except:
                raise serializers.ValidationError('This field must be integer')

    def validate_date(self, value):
        if type(value) == datetime.date:
            return value
        else:
            try:
                print(value)
            except:
                raise serializers.ValidationError('This field must be date')

    def validate_sum(self, value):
        if type(value) == float:
            return value
        else:
            try:
                return float(value)
            except:
                raise serializers.ValidationError('This field must be float')


    def validate_service(self, value):
        if len(value) > 0 and value != '-':
            return value
        else:
            raise serializers.ValidationError('This field must be not empty')