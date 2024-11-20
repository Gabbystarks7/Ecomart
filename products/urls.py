from ecomart.urls import path
from . import views

# Note the following:
# /products  ==> path('', ...)
# /products/new  ==> path('new', ...)
# /products/trending/Ghana  ==> path('trending/Ghana', ...)

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]