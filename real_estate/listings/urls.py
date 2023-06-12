from django.conf import settings
from listings import views
from django.urls import path

from django.conf.urls.static import static

urlpatterns = [
  path('all_listings', views.list_all_items, name='all_listings'),  # route to all listings/items
  path('single_listing/<pk>', views.single_listing, name='single_listing'),
  path('insert_listing', views.listing_form, name='insert_listing'),

  path('single_listing/update_listing/<pk>', views.listing_update, name='update_listing'),

  path('single_listing/delete_listing/<pk>', views.listing_delete, name='update_listing'),

  path('', views.list_all_items, name='')

  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)