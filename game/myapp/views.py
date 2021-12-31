from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def rules(request):
    return render(request,'rules.html')

def play(request):
    return render(request,'play_board.html')

def profile(request):
    return render(request,'profile.html')