from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from myapp.camera import VideoCamera
import json

vid_cam = VideoCamera()
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

        yield((b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'))
        

def get_result(request):
    js_data = None
    while True:
        predicted_dict = vid_cam.get_result()
        js_data = json.dumps(predicted_dict)
        return JsonResponse({'js_data':js_data})

def video_feed(request):
    return (StreamingHttpResponse(gen(vid_cam),content_type='multipart/x-mixed-replace; boundary=frame'))