from django.shortcuts import render, get_object_or_404 , redirect
from .models import Event, Eventparticipant
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist


def event_list(requset):
    event_list  = Event.objects.order_by('date').filter(status='Published')
    # for event in w
    paginator = Paginator(event_list, 2) # 3 posts in each page        
    page = requset.GET.get('page')
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    context = {'events':events, 'page':page}
    return render(requset, 'event_site/event/list.html',context)

def event_detail(request, year, month, day, title):
    event  = get_object_or_404(Event, slug=title, status='Published', date__year=year, date__month=month, date__day=day)
    try :
        user_participted_in_this_event = Eventparticipant.objects.get(user_id=request.user.id, event_id=event.id)
        message = "you already participated in this event"
        print(user_participted_in_this_event)
    except ObjectDoesNotExist:
        message = "not participted before"
        user_participted_in_this_event = False
    try:
        
        num_of_users_paricipted_in_this_event = len(Eventparticipant.objects.filter(event_id=event.id))
    except ObjectDoesNotExist:
        # no users in this event
        num_of_users_paricipted_in_this_event = False
    context  = {'event': event, 'user_participted_in_this_event':user_participted_in_this_event, 'message':message , 'num_of_users_paricipted_in_this_event':num_of_users_paricipted_in_this_event}
    return render(request, 'event_site/event/detail.html', context)

@login_required
def participate(request, event_id):
    event  = get_object_or_404(Event, id=event_id)
    user_id = request.user.id
    event_id = event.id
    Eventparticipant.objects.create(user_id=user_id, event_id=event_id)
    return redirect(event)
#participate