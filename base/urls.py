from django.urls import path
from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate, DeleteView, CustomLoginView, RegisterPage, ProductReorder
from django.contrib.auth.views import LogoutView

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ProductList.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('product-create/', ProductCreate.as_view(), name='product-create'),
    path('product-update/<int:pk>/', ProductUpdate.as_view(), name='product-update'),
    path('product-delete/<int:pk>/', DeleteView.as_view(), name='product-delete'),
    path('product-reorder/', ProductReorder.as_view(), name='product-reorder'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="base/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="base/password_reset_sent.html"), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="base/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="base/password_reset_complete.html"), name = 'password_reset_complete'),
]
