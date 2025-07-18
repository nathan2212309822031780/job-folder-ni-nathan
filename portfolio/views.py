from django.views.generic import DetailView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Portfolio

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/detail.html'
    context_object_name = 'portfolio'

    def get_object(self):
        return Portfolio.objects.get(user__username=self.kwargs['username'])

class PortfolioDeleteView(DeleteView):
    model = User
    template_name = 'portfolio/confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return User.objects.get(username=self.kwargs['username'])
