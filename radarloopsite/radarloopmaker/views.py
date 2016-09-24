import os

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from radarloopmaker.models import RadarInfo
from .get_radar_images.get_radar_images import get_latest_gif

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(SCRIPT_PATH, 'static', 'radarloopmaker')

def index(request):
    template = loader.get_template('radarloopmaker/index.html')
    return HttpResponse(template.render())


def locationfromID(request, ID):
    # get all radars from DB that have same location:
    radar_RIDB = RadarInfo.objects.filter(radarID=ID)[0]
    radarsatlocation_listRIDBs = RadarInfo.objects.filter(location=radar_RIDB.location)

#    template = loader.get_template('radarloopmaker/locationfromID.html')
#    context = RequestContext(request, {
#        'radar_DB_list': radarsatlocation_listRIDBs
#        })
#    return HttpResponse(template.render(context))

    # dummy = []
    # for obj in radarsatlocation_listRIDBs:
        # dummy.append(obj.location)
    return render(request,'radarloopmaker/locationfromID.html', {'radar_DB_list': radarsatlocation_listRIDBs})

def makegiftolatest(request):
    # get data from form
    selected_radarID = str(request.POST['chosenID'])
    frame_count = int(request.POST['noofframes'])

    #make the gif
    gifname = 'radar_loop.gif'
    gifpath = os.path.join(STATIC_PATH, gifname)
    gifpath_forhtml = os.path.join('radarloopmaker', gifname)

    get_latest_gif(gifpath, selected_radarID, latest=frame_count)

    template = loader.get_template('radarloopmaker/gifdisplay.html')
    context = RequestContext(request, {
        'gifname':gifpath_forhtml
    })

    return HttpResponse(template.render(context))
