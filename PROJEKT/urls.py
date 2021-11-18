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
            {'urlkod': 'kis', 'nev': 'Kis órarendek'},
        ]})),

    path('orarend/<str:meret>/', lambda x,meret: render(x, "linkek.html", {'linkek': [
            {'urlkod': 'tanar', 'nev': 'Tanárok órarendjei'},
            {'urlkod': 'terem', 'nev': 'Termek órarendjei'},
            {'urlkod': 'diak' , 'nev': 'Osztályok órarendjei'},
        ]})),

    path('orarend/nagy/terem/', lambda request: render(request, "nagy.html", orarend_kontextus('nagy_teor.html','css/nagy_teor.css', termek=sorted(Terem.objects.all(), key=lambda x:x.sorszam)))),
    path('orarend/nagy/tanar/', lambda request: render(request, "nagy.html", orarend_kontextus('nagy_tor.html','css/nagy_tor.css', tanarok=sorted(Tanar.objects.all(), key=lambda x:x.sorszam)))),
    path('orarend/nagy/diak/', lambda request: render(request, "nagy.html", orarend_kontextus('nagy_dor.html','css/nagy_dor.css', osztalyok=sorted(Osztaly.objects.all(), key=lambda x:x.sorszam)))),
    path('orarend/kis/tanar/', lambda request: render(request, "linkek.html", {'linkek': list(map(lambda tanar: {'urlkod':tanar.urlkod, 'nev':tanar.kreta}, Tanar.objects.all()))})),
    path('orarend/kis/tanar/<str:tanar_urlkod>/', lambda request, tanar_urlkod: render(request, "kis.html", orarend_kontextus('kis_tor.html', 'css/kis_tor.css', a_tanar=list(filter(lambda tanar: tanar.urlkod == tanar_urlkod , Tanar.objects.all()))[0]))),
    path('orarend/kis/terem/', lambda request: render(request, "linkek.html", {'linkek': list(map(lambda terem: {'urlkod':terem.urlkod, 'nev':terem.kreta}, Terem.objects.all()))})),
    path('orarend/kis/terem/<str:terem_urlkod>/', lambda request, terem_urlkod: render(request, "kis.html", orarend_kontextus('kis_teor.html', 'css/kis_teor.css', a_terem=list(filter(lambda tanar: tanar.urlkod == terem_urlkod , Terem.objects.all()))[0]))),
]

"""
path('api/get/variable/', api_get_var),
path('api/get/model-object/all/', api_get_all),
path('api/get/model-object/this/<str:pk>/', api_get_one),
path('api/post/create/', api_create),
path('api/post/update/<str:pk>/', api_update),
path('api/delete/<str:pk>/', api_delete),
"""
