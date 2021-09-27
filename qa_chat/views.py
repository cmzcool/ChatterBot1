from django.shortcuts import render
from django.views import View
from .chatbot_logic import talk
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
from django.http import HttpResponse
@method_decorator(csrf_exempt, name='dispatch')
class QuestionView(View):
    def post(self, request, *args, **kwargs):
        response = talk(request.POST['question'])

        return HttpResponse(response, 200)