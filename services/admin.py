from django.contrib import admin
from header.models import Logo, Contact, ModalContact
from services.models import Service, UServices, Cooperation
from slider.models import SlideHead, SlideList, SlideReview
from PanelTabs.models import TabItem, TabItemList

# Register your models here.

class SlideListInline(admin.TabularInline):
    model = SlideList
    extra = 5
    max_num = 5

class SlideHeadAdmin(admin.ModelAdmin):
    inlines = [
        SlideListInline,
    ]

class TabItemListInline(admin.TabularInline):
    model = TabItemList
    extra = 5

class TabItemAdmin(admin.ModelAdmin):
    inlines = [
        TabItemListInline,
    ]

class UServicesInline(admin.TabularInline):
    model = UServices
    extra = 10
    exclude = ('changed',)

class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        UServicesInline,
    ]


admin.site.register(SlideReview)
admin.site.register(Logo)
admin.site.register(Contact)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Cooperation)
admin.site.register(SlideHead, SlideHeadAdmin)
admin.site.register(ModalContact)
admin.site.register(TabItem, TabItemAdmin)



