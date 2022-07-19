import django_filters
from .models import Bill


class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Bill
        fields = {
            "client_name": ["icontains"],
            "client_org": ["icontains"],
        }