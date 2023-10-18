from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import *

# Create your views here.
class StudentListView(generic.ListView):
        model = Student

class StudentDetailView(generic.DetailView):
        model = Student

class PortfolioListView(generic.ListView):
        model = Portfolio

class PortfolioDetailView(generic.DetailView):
        model = Portfolio

        def get_context_data(self, **kwargs):
            # Call the base implementation first to get the context
            context = super(PortfolioDetailView, self).get_context_data(**kwargs)
            # Create any data and add it to the context
            context['project_data'] = Project.objects.all()
            return context

class ProjectListView(generic.ListView):
        model = Project

class ProjectDetailView(generic.DetailView):
        model = Project

# creates a new project within an existing portfolio
def createProject(request, portfolio_id):
        form = ProjectForm()
        portfolio = Portfolio.objects.get(pk=portfolio_id)

        if request.method == "POST":
                # create dictionary with portfolio id and form data
                project_data = request.POST.copy()
                project_data['portfolio_id'] = portfolio_id

                # get the data from the form
                form = ProjectForm(project_data)

                if form.is_valid():
                      project = form.save(commit=False)
                      project.portfolio = portfolio
                      project.save()

                return redirect('portfolio-detail', portfolio_id)
                
        context = {'form': form}
        return render(request, 'portfolio_app/project_form.html', context)

# deletes an existing project
def deleteProject(request, portfolio_id, project_id):
       # get the desired project from the database
       project = Project.objects.get(pk=project_id)
       
       # if user selects the delete button, delete the project
       if request.method == "POST":
              project.delete()

              # redirect user to the main page for the current portfolio
              return redirect('portfolio-detail', portfolio_id)
       
       # add info about the project to the HTML context
       context = {'project': project}
       return render(request, 'portfolio_app/project_delete.html', context)

# update an existing project
def updateProject(request, portfolio_id, project_id):
       # get desired project from the database
       project = Project.objects.get(pk=project_id)
       # access the form for the specified project
       form = ProjectForm(instance=project)

       if request.method == "POST":
              form = ProjectForm(request.POST, instance=project)
              
              # save the valid form to the database
              if form.is_valid():
                     form.save()

              return redirect('portfolio-detail', portfolio_id)

       context = {'form': form}
       return render(request, 'portfolio_app/project_form.html', context)

# update the information for an existing portfolio
def updatePortfolio(request, student_id, portfolio_id):
       # get the portfolio for the current student
       portfolio = Portfolio.objects.get(pk=portfolio_id)
       # access the form for the specified portfolio
       form = PortfolioForm(instance=portfolio)

       if request.method == "POST":
              form = PortfolioForm(request.POST, instance=portfolio)
              
              # save the valid form to the database
              if form.is_valid():
                     form.save()

              return redirect('student-detail', student_id)
       
       context = {'form': form}
       return render(request, 'portfolio_app/portfolio_form.html', context)


def index(request):
    student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", student_active_portfolios)
    return render( request, 'portfolio_app/index.html', {'student_active_portfolios':student_active_portfolios})