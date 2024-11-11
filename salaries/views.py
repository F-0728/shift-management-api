from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Salary
from .serializers import SalarySerializer

class SalaryViewSet(viewsets.ModelViewSet):

    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    @action(detail=False, methods=['get'])
    def get_by_company(self, request):
        if 'company_id' in request.query_params:
            company_id = request.query_params.get('company_id')
        else:
            company_id = None
        if company_id:
            salaries = self.get_queryset().filter(company_id=company_id)
        serializer = SalarySerializer(salaries, many=True)
        return Response(serializer.data)
