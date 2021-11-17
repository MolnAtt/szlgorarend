from django.contrib import admin
from django.urls import path, include
from APP.views import *
# , api_get_var, api_get_all, api_get_one, api_create, api_update, api_delete

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('admin/', admin.site.urls),
    # path('', index),
    path('orarend/', lambda x: render(x, "linkek.html", {'linkek': [
            {'urlkod': 'nagy', 'nev':'Nagy órarendek'},
            {'urlkod': 'csoportos', 'nev': 'Csoportosított órarendek'},
            {'urlkod': 'szeletelt', 'nev': 'Szeletelt órarendek'},
        ]})),

    path('orarend/<str:meret>/', lambda x,meret: render(x, "linkek.html", {'linkek': [
            {'urlkod': 'tanar', 'nev': 'Tanárok órarendjei'},
            {'urlkod': 'terem', 'nev': 'Termek órarendjei'},
            {'urlkod': 'diak' , 'nev': 'Osztályok órarendjei'},
        ]})),

    path('orarend/nagy/terem/', nagy_teor),

]

"""
path('api/get/variable/', api_get_var),
path('api/get/model-object/all/', api_get_all),
path('api/get/model-object/this/<str:pk>/', api_get_one),
path('api/post/create/', api_create),
path('api/post/update/<str:pk>/', api_update),
path('api/delete/<str:pk>/', api_delete),
"""
