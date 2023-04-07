from django.urls import path
from . import views

app_name = "gameapp"

urlpatterns = [
    # Profile View
    path('', views.profile, name ='profile'),

    # Leaderboard View
    path('leaderboards', views.leaderboards, name='leaderboards'),

    # Maps View
    path('maps', views.maps, name = 'maps'),

    # # Activities View
    # path('activities', views.createActivitiesView, name = 'activities'),

    # Categories
    path('categories', views.categoriesActivitesView, name='categories'),

    # Activities detail view
    path('activities/<int:pk>', views.ActivitiesDetailView.as_view(), name='activitiesDetails'),
    
    # Add time modal
    # path('addTime', views.addTime, name='add_time'),
    path('addTime', views.AddLineItem.as_view(), name='add_time'),

    # Tips View
    path('tips', views.tipsIndex, name = 'tips'),

    path('recordPoints', views.RecordPoints.as_view(), name='record_points'),

    path('setDurationField', views.SetDurationField.as_view(), name='setDurationField')

    # path('add/<int:id>', views.add_line_item_view, name='add_line_item'),

    # path('cart', views.ShowCartView.as_view(), name='show_cart'),
]


