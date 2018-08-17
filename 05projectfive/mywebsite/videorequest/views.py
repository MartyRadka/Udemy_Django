from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm

def index(request):
    """return render with three parametres: request (cause we responding
    to a request), template (which page will be display to user),
    and context ()"""
    videos = Video.objects.order_by('-date_added')
    context = {'videos': videos}
    return render(request, 'videorequest/index.html', context)


def vrform(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)

        if form.is_valid():
            new_request = Video(videoTitle=request.POST['videoName'], videoDesc=request.POST['videoDesc'])
            new_request.save()
            return redirect('index')

    else:
        form = VideoForm()

    context = {'form': form}
    return render(request, 'videorequest/vrform.html', context)
