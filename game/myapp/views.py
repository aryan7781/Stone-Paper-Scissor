from django.shortcuts import render
from django.http import StreamingHttpResponse
from myapp.camera import VideoCamera
# Create your views here.
def index(request):
    return render(request,'index.html')

def rules(request):
    return render(request,'rules.html')

def play(request):
    return render(request,'play_board.html')

def profile(request):
    return render(request,'profile.html')

def singleplayer(request):
    return render(request, 'single_player.html')

def multiplayer(request):
    return render(request, 'multi_player.html')

def gen(camera):
    while True:
        frame=camera.get_frame()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),content_type='multipart/x-mixed-replace; boundary=frame')