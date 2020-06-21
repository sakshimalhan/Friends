from django.shortcuts import render,redirect
from social import models
from django.db.models import Q
from django.views import View
from social  import forms
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
class wall(LoginRequiredMixin,ListView):
    
    context_object_name='posts'
    template_name='social/wall.html'
    login_url='auth/login'
    def get_queryset(self):
        friendid=[friend.person2.id for friend in models.frnds.objects.filter(person1=self.request.user)]
        friendid= friendid + [friend.person1.id for friend in models.frnds.objects.filter(person2=self.request.user)]
        return models.Post.objects.filter(user__in=friendid).order_by('-created_at')
        
class Home(LoginRequiredMixin,ListView):
    context_object_name='posts'
    template_name='social/home.html'
    login_url='auth/login'
    def get_queryset(self):
        return models.Post.objects.filter(user=self.request.user)
    def get_context_data(self,*args,**kwargs):
        data=super().get_context_data(*args,**kwargs)
        data['post_form']=forms.PostForm
        return data
class post(View):
    def post(self,request):
        form=forms.PostForm(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.user=request.user
            newpost.save()
            return redirect('/home')

class PostLike(View):
    model=models.Post
    def post(self,request,pk):
        newpost=self.model.objects.get(pk=pk)
        print(1)
        models.Like.objects.create(post=newpost,user=request.user)
        return HttpResponse(code=204)

class myfriends(ListView):
    context_object_name='friends'
    template_name='social/myfriends.html'
    
    def get_queryset(self):
        friendid=[friend.person2.id for friend in models.frnds.objects.filter(person1=self.request.user)]
        friendid= friendid + [friend.person1.id for friend in models.frnds.objects.filter(person2=self.request.user)]
        return User.objects.filter(id__in=friendid)
