from django.views.generic import View
from django.shortcuts import render
from .models import Table_1, Table_2

class HelloPageView(View):
    def get(self, request, *args, **kwargs):
        table_1_obj = Table_1.objects.get(table_1_id=1)
        context = {
            "header": table_1_obj.field_1,
            "text": table_1_obj.table_2.field_2
        }
        return render(request, 'home_page.html', context)