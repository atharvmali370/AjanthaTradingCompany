from django.urls import path
from ajanthaapp.views import IndexPageView, CreateProductView , CreateCategoryView , ViewProductView , EditProductView , DeleteProductView , SearchProductView , TilesView , BathFittingView , TilesAdhesiveView , PlumbingPipesAndFittingsView , KitchenSinkView , BathAcessoriesView , AllProductView , ContactView

urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
    path('add-product/', CreateProductView.as_view(), name='add-product'),
    path('add-category/', CreateCategoryView.as_view(), name='add-category'),
    path('view-product/<int:id>/', ViewProductView.as_view(), name='view-product'),
    path('edit-product/<int:id>/', EditProductView.as_view(), name='edit-product'),
    path('delete-product/<int:id>/', DeleteProductView.as_view(), name='delete-product'),
    path('search-product/', SearchProductView.as_view(), name='search-product'),

    path('tiles/', TilesView.as_view(), name='tiles'),
    path('bath-fitting/', BathFittingView.as_view(), name='bath-fitting'),
    path('tiles-adhesive/', TilesAdhesiveView.as_view(), name='tiles-adhesive'),
    path('plumbing-and-fittings/', PlumbingPipesAndFittingsView.as_view(), name='plumbing-and-fittings'),
    path('kitchen-sink/', KitchenSinkView.as_view(), name='kitchen-sink'),
    path('bath-acessories/', BathAcessoriesView.as_view(), name='bath-acessories'),
    path('all-products/', AllProductView.as_view(), name='all-products'),

    path('contact/', ContactView.as_view(), name='contact'),
]
