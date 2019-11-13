from rest_framework import viewsets

from home.models import Questions
from .serializers import QuestionSerializer


from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .utils import render_to_pdf
from django.template.loader import get_template

import requests as r

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()


def GeneratePDF(request, question_id):
    #API CALL
    url = 'https://financialmodelingprep.com/api/v3/company/profile/QQQ'
    portfolio_beta = r.get(url).json()['profile']['beta']

    morningstar_url = 'https://api.morningstar.com/v2/service/mf/FundShareClassBasicInfo/ticker/QQQ?accesscode=mcbwsojhhr693v3dxeinpcx0gytxm16u&format=JSON'
    prospectus_objective = r.get(morningstar_url).json()['data'][1]['api']['ProspectusObjective']
    question = get_object_or_404(Questions, pk=question_id) 
    beta = question.beta 
    risk_measurment = ""
    if abs(float(beta) - float(portfolio_beta)) < .25:
        risk_measurment = "Appears Normal"
    elif abs(float(beta) - float(portfolio_beta)) < .4:
        risk_measurment = "Suspicious Behavior"
    else:
        risk_measurment = "ALERT! REVIEW IMMEDIATELY"
    results = []
    if beta < .9:
        results = ['Convertible Bond','Corporate Bond-General','Corporate Bond-High Quality','Corporate Bond-High Yield','Government Bond-Adjustable-Rate Mortgage','Government Bond-General','Government Bond-Mortgage','Government Bond-Treasury','Income','Municipal-Bond California','Municipal Bond-National','Municipal Bond-New York','Municipal Bond-Single State']
    elif beta < 1.05:
        results =  ['Asset Allocation','Balanced','Equity-Income','Growth-and-Income','Multi Sector Bond','Short Term World Income']
    else:
        results = ['Aggressive Growth','Diversified Emerging-Markets Stock','Europe Stock','Foreign Stock','Growth','Multi Asset Global','Pacific Stock','Small Company','Specialty-Communications','Specialty-Financial','Specialty-Health','Specialty-Natural Resources','Specialty-Precious Metals','Specialty-Real Estate','Specialty-Technology','Specialty-Unaligned','Specialty Utilities','World Bond','World Stock']
    template = get_template('results.html')
    context = {
        "beta": question.beta,
        "name": question.name,
        "results": results,
        "portfolio_beta": portfolio_beta,
        'prospectus_objective': prospectus_objective,
        "risk_measurement": risk_measurment,
        "notes": question.reviewed_notes
    }
    html = template.render(context)
    pdf = render_to_pdf('results.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Client_%s.pdf" %("12343")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse(pdf, content_type='application/pdf')

# class BetListView(ListAPIView):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer

# class BetDetailView(RetrieveAPIView):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer

# class BetCreateView(CreateAPIView):
#     queryset = Bet.objects.all()
#     serializer_class = BetSerializer
