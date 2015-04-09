from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from header.models import Logo, Contact, ModalContact
from services.models import Service, UServices, Cooperation
from slider.models import SlideHead, SlideList, SlideReview
from PanelTabs.models import TabItem, TabItemList
from django.core.context_processors import csrf
from django.db import connection

# Create your views here.

def home(request):
    args = {}
    args['logo'] = Logo.objects.all()
    args['contacts'] = Contact.objects.all()
    args['contacts_modal'] = ModalContact.objects.all()
    args['services'] = Service.objects.all()
    args['cooperation'] = Cooperation.objects.all()
    args['slides_head'] = SlideHead.objects.all()
    args['slides_review'] = SlideReview.objects.all()
    args['tabs'] = TabItem.objects.all()
    args['uservices'] = UServices.objects.all()

    uservices = connection.cursor()
    uservices.execute("""
        SELECT *
        FROM uservices, service
        WHERE uservices.service_id = service.id;
    """)
    args['uservices_list'] = uservices.fetchall()

    tabs = connection.cursor()
    tabs.execute("""
        SELECT *
        FROM tab_item_list, tab_item
        WHERE tab_item_list.tab_id = tab_item.id;
    """)
    args['tabs_item'] = tabs.fetchall()


    slide_list = connection.cursor()
    slide_list.execute("""
        SELECT *
        FROM slider_list, slider_head
        WHERE slider_list.slide_id = slider_head.id;
    """)
    args['all_slides_list'] = slide_list.fetchall()
    return render_to_response('index.html', args)


