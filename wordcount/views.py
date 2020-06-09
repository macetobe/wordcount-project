from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render (request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']
    count=fulltext.split()
    worddictionary={}
    for word in count:
        if word in worddictionary:
            #increase the number of times the word is repeated
            worddictionary[word]+=1
        else:
            #equate the word to one to show that the word was not repeated
            worddictionary[word]=1
    return render(request,'count.html',{"fulltext":fulltext,'length':len(count),"worddictionary":worddictionary.items()})

def about(request):
    return render(request,"about.html")
