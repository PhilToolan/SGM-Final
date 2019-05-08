from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    def get(self, request, **kwargs):
        """View function for home page of site."""

    # Render the HTML template index.html 
        return render(request, 'index.html') 

class LahinchView(TemplateView):
    def get(self, request, **kwargs):
        """View function for the Lahinch site."""
        return render(request, 'lahinch.html') 

class BallyView(TemplateView):
    def get(self, request, **kwargs):
        """View function for the Lahinch site."""
        return render(request, 'Ballybunnion.html') 

class BunView(TemplateView):
    def get(self, request, **kwargs):
        """View function for the Lahinch site."""
        return render(request, 'Bundoran.html') 

class BellView(TemplateView):
    def get(self, request, **kwargs):
        """View function for the Lahinch site."""
        return render(request, 'Bellmullet.html') 

class StrandView(TemplateView):
    def get(self, request, **kwargs):
        """View function for the Lahinch site."""
        return render(request, 'Strandhill.html') 