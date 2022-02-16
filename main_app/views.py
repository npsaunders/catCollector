from pyexpat import model
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cat, Toy
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request,'cats/index.html', { 'cats': cats})

# update this view function
def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'cats/detail.html', {
    # include the cat and feeding_form in the context
    'cat': cat, 'feeding_form': feeding_form
  })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.cat_id = cat_id
        new_feeding.save()
    return redirect('detail', cat_id=cat_id)

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    # success_url = '/cats/' 

class CatUpdate(UpdateView):
    model = Cat
    fields = ('breed', 'description', 'age')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats/'

class ToyCreate(CreateView):
    model = Toy
    fields = ('name', 'color')

class ToyUpdate(UpdateView):
    model = Toy
    fields = ('name', 'color')

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'