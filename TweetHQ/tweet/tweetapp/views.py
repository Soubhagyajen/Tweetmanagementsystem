from django.shortcuts import render
from .models import Tweet,Like
from .forms import tweetForm,UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
# def demo(request):
#     return render(request,'index.html')
def home(request):
    print("Home view is called")
    tweets = Tweet.objects.all()
    # print(f"Tweets: {tweets}")
    return render(request,'tweet_list.html',{'tweets':tweets})

@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = tweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
       form = tweetForm()
    return render(request,'tweet_form.html',{'form':form})

@login_required
def edit_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id,user = request.user)
    if request.method == 'POST':
        form = tweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet = form.save(commit = False)
            tweet.user = request.user
            tweet.save()
            return redirect('home')
    else:
        form = tweetForm(instance = tweet)

    return render(request,'tweet_form.html',{'form':form})

@login_required
def delete_tweet(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id , user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('home')
    return render(request,'delete_tweet.html',{'tweet':tweet})


def Register(request):
    if request.method == 'POST':
      form = UserRegistrationForm(request.POST)
      if form.is_valid():
          user = form.save(commit=False)
          user.set_password(form.cleaned_data['password1'])
          user.save()
          login(request,user)
          return redirect('home')
          
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def Like_tweets(request,tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id , user = request.user)
    Like.objects.get_or_create(user = request.user,tweet=tweet)
    return render(request,'tweet_list.html',{'tweet':tweet})


@login_required
def unlike_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet,pk = tweet_id , user = request.user)
    Like.objects.filter(user=request.user, tweet=tweet).delete()
    return render(request,'tweet_list.html',{'tweet':tweet})