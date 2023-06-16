from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
import pyshorteners
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class ShortenURLView(View):
   def post(self, request):
      long_url = request.POST.get('url')
      type_tiny = pyshorteners.Shortener()
      short_url = type_tiny.tinyurl.short(long_url)
      return render(request, 'index.html', short_url)

   def get(self, request):
      return render(request, 'index.html')