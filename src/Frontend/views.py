from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect, reverse
from django.core import serializers
from django.http import HttpResponse

from Frontend.models import Message

# Create your views here.

class Main(View):
    template = 'main.html'

    def get(self, request):
        return render(request, self.template)

    # @csrf_exempt
    def post(self, request):
        msg1 = Message(name = "You", text = request.POST['message'])
        msg1.save()
        msg2 = Message(name = "Bot", text = "This bot cannot speak yet.")
        msg2.save()
        return redirect(reverse('main'))

class About(View):
    template = 'about.html'

    def get(self, request):
        return render(request, self.template)

class Delete(View):
    template = 'delete.html'

    def get(self, request):
        Message.objects.all().delete()
        return render(request, self.template)

class Messages(View):
    def get(self, request):
        all_message = Message.objects.all()
        all_message_list = serializers.serialize('json', all_message)
        return HttpResponse(all_message_list, content_type="text/json-comment-filtered")  