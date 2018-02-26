from django.views.generic import TemplateView
from django.db import connection
from pprint import pprint
import json

from pir.models import PirPage

class ReportView(TemplateView):

    template_name = 'report/home.html'

    def get(self, request, *args, **kwargs):
        
        all_entries = PirPage.objects.all()

        # cursor = connection.cursor()
        # cursor.execute("SELECT `section`, `sector`, `market`, `body` FROM `pir_pirpage` ")
        # _result = cursor.fetchall()

        # context = {
        #     'all_entries': json.dumps(_result, indent=4),
        # }
        # return self.render_to_response(context)

        
        # all_entries = PirPage.objects.raw("SELECT * FROM `pir_pirpage`")
        # for x in all_entries:
        #   x.bodyobj = json.loads(x.body)

        context = {
            'all_entries': all_entries,
        }
        return self.render_to_response(context)