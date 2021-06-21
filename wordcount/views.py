from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'dog':'Louis'})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['txtWC']
    #this will print to the server terminal (runserver)
    # print(fulltext)
    wordlist = fulltext.split()

    #empty dictionary
    wordCount = {}

    for word in wordlist:
        if word in wordCount:
            # incremental
            wordCount[word] += 1
        else:
            # Add
            wordCount[word] = 1

    sortedCount = sorted(wordCount.items(), key=lambda kv:kv[1], reverse=True)
    #print(sortedCount)

    sortedDict = dict(sortedCount)
    # let us create a dictionary to pass the fulltext to
    return render(request, 'wordCount.html', {'fulltext':fulltext, 'wordCount':len(wordlist), 'wordDict': sortedDict})
