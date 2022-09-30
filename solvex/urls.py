"""solvex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from accounts import views as user_views
from accounts.views import logout

from django.views.generic import TemplateView
from design.views import SearchView, SearchsView


from design.views import (



#  U R L   
profile,

zeroA,

postform,

like,

likepost,

postdetail,

postlist,

comment,

commentpost,

solution,

solutionpost,

twoA,

userp,

follows,

unfollow,

prof_edit,

e_store,
self_care_products,
medical_products,
talent_products,
interior_products,
academic_products,
digital_products,
travel_products,
fashion_products,


self_care1_products,
medical1_products,
talent1_products,
interior1_products,
academic1_products,
digital1_products,
travel1_products,
fashion1_products,

usage,
terms_and_conditions,
about_us,
reportform,
landing_page,


	)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', user_views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
   
    path('logout/',logout,name='logout'),

    path('search/',SearchView.as_view(),name='search'),

    path('ok',SearchsView.as_view(),name='searchs'),

    path('unfollow/', unfollow, name='unfollow'),

    path('follows/', follows, name='follows'),

    path('userp/<str:username>/', userp, name='userp'),


    path('about_us/', about_us, name='about_us'),
    path('terms/', terms_and_conditions, name='terms_and_conditions'),
    path('usage/',usage , name='usage'),

    path('landing_page/',landing_page, name='landing_page'),

    path('profile/', profile, name='profile'),

    path('postform/', postform, name='postform'),

    path('like/<int:pk>/', likepost, name='likepost'),

    path('postlist/like/<int:pk>/', like, name='like'),

    path('comment/<int:pk>', comment, name='comment'),

    path('postlist/comment/<int:pk>/', commentpost, name='commentpost'),
 
    path('postlist/', postlist, name='postlist'),

    path('solution/<int:pk>', solutionpost, name='solutionpost'),

    path('oneA/twoA/solution/<int:pk>',solution,name='solution'),

    path('postdetail/', postdetail, name='postdetail'),

    path('zeroA/',zeroA,name='zeroA'),
    path('reportform/',reportform,name='reportform'),

    path('prof_edit/',prof_edit,name='prof_edit'),

    path('', include('design.urls')),

    path('oneA/twoA/<int:pk>/<int:user>/',twoA, name='twoA'),

    path('store/', e_store, name='e_store'),

    path('self_care/', self_care_products, name='self_care_products'),

    path('self_care/<int:pk>/', self_care_products, name='self_care_products'),

    path('medical/', medical_products, name='medical_products'),

    path('talent/', talent_products, name='talent_products'),

    path('interior/', interior_products, name='interior_products'),
    path('academic/', academic_products, name='academic_products'),
    path('digital/', digital_products, name='digital_products'),
    path('fashion/', fashion_products, name='fashion_products'),
    path('travel/', travel_products, name='travel_products'),








    path('medical1/<int:pk>/', medical1_products, name='medical1_products'),
    path('medical/medical1/<int:pk>/', medical1_products, name='medical1_products'),


    path('self_care1/<int:pk>/', self_care1_products, name='self_care1_products'),
    path('self_care/self_care1/<int:pk>/', self_care1_products, name='self_care1_products'),

    path('talent1/<int:pk>/', talent1_products, name='talent1_products'),
    path('talent/talent1/<int:pk>/', talent1_products, name='talent1_products'),

    path('interior1/<int:pk>/', interior1_products, name='interior1_products'),
    path('interior/interior1/<int:pk>/', interior1_products, name='interior1_products'),

    path('academic1/<int:pk>/', academic1_products, name='academic1_products'),
    path('academic/academic1/<int:pk>/', academic1_products, name='academic1_products'),

    path('digital1/<int:pk>/', digital1_products, name='digital1_products'),
    path('digital/digital1/<int:pk>/', digital1_products, name='digital1_products'),

    path('travel1/<int:pk>/', travel1_products, name='travel1_products'),
    path('travel/travel1/<int:pk>/', travel1_products, name='travel1_products'),

    path('fashion1/<int:pk>/', fashion1_products, name='fashion1_products'),
    path('fashion/fashion1/<int:pk>/', fashion1_products, name='fashion1_products'),




     
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)