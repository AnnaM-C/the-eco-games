from django.urls import path
from . import views

app_name = "gameapp"

urlpatterns = [
    # Profile View
    path('', views.profile, name ='profile'), # Change to account

    # Update Location View
    path('locationupdate', views.locationUpdateView, name = 'locationUpdater'),

    # Leaderboard View
    path('leaderboards', views.leaderboards, name='leaderboards'),

    # Update Leaderboard AJAX View
    path('leaderboardUpdate', views.leaderboardUpdater, name = 'leaderboardUpdate'),

    # Maps View
    path('maps', views.maps, name = 'maps'),

    # Competitions view
    path('competitions/<int:compYear>/<int:compMonth>', views.competitions, name='competitions'),

    # Competitions (current) view
    path('competitions', views.compete, name='compete'),

    # # Activities View
    # path('activities', views.createActivitiesView, name = 'activities'),

    # Categories
    path('categories', views.categoriesActivitesView, name='categories'),

    # Activities detail view
    path('activities/<int:pk>', views.ActivitiesDetailView.as_view(), name='activitiesDetails'),
    
    # Url to send time and activity ID to server
    path('addTime', views.AddLineItem.as_view(), name='add_time'),

    # Tips View
    path('tips', views.tipsIndex, name = 'tips'),

    path('recordPoints', views.RecordPoints.as_view(), name='record_points'),

    path('emptyCart', views.emptyCart, name='emptyCart'),

    # path('setDurationField', views.SetDurationField.as_view(), name='setDurationField')

    # path('add/<int:id>', views.add_line_item_view, name='add_line_item'),

    # path('cart', views.ShowCartView.as_view(), name='show_cart'),
]


