from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import *

# Create your views here.
class StudentListView(generic.ListView):
        model = Student
class StudentDetailView(generic.DetailView):
        model = Student
class PortfolioListView(generic.ListView):
        model = Portfolio
class PortfolioDetailView(generic.DetailView):
        model = Portfolio
class ProjectListView(generic.ListView):
        model = Project
class ProjectDetailView(generic.DetailView):
        model = Project

def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})