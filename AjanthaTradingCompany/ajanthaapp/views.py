from django.shortcuts import render , redirect
from django.views import View
from ajanthaapp.models import Product, Category , Contact
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexPageView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'ajanthaapp/index.html', {'products' : products})
    
class CreateProductView(LoginRequiredMixin , View):
    flag = False
    def get(self, request):
        all_category = Category.objects.all()
        return render(request, 'ajanthaapp/add-product.html', {'category' : all_category})
    
    def post(self, request):
        flag = False
        try :
            category_id = request.POST.get('category')
            obj = Category.objects.get(pk = category_id)

            Product.objects.create(
                name = request.POST.get('pname'),
                code = request.POST.get('pcode'),
                price = request.POST.get('pprice'),
                comment = request.POST.get('pcomment'),
                image = request.FILES.get('image'),
                category = obj
            )

            return redirect('ajantha:home')

        except Exception as e :
            flag = False
            print(f'{type(e).__name__} : {e}')
        return render(request, 'ajanthaapp/add-product.html', {'flag' : flag})


class CreateCategoryView(LoginRequiredMixin , View):
    flag = False
    def get(self, request):
        return render(request, 'ajanthaapp/add-category.html')
    
    def post(self, request):
        try :
            category_name = request.POST.get('cname')
            category = Category(name = category_name)
            category.save()
            print("Product Added Successfully")
            flag = True
            
            return redirect('ajantha:home')
    
        except Exception as e :
            flag =  False
            print(f'{type(e).__name__} : {e}')
        return render(request, 'ajanthaapp/add-category.html', {'flag' : flag})
    

class ViewProductView(View):
    def get(self, request, id):
        product = Product.objects.get(pk = id)
        return render(request, 'ajanthaapp/view-product.html', {'product' : product})
    

class EditProductView(LoginRequiredMixin , View):
    def get(self, request, id):
        product = Product.objects.get(pk = id)
        return render(request, 'ajanthaapp/edit-product.html', {'product' : product})
    
    def post(self, request, id):
        try :
            db_product = Product.objects.get(pk = id)

            db_product.name = request.POST.get('pname')
            db_product.code = request.POST.get('pcode')
            db_product.price = request.POST.get('pprice')
            db_product.comment = request.POST.get('pcomment')
            db_product.image = request.FILES.get('image')

            db_product.save()

            return redirect('ajantha:home')

        except Exception as e :
            print(f'{type(e).__name__} : {e}')
        return render(request, 'ajanthaapp/add-product.html')
    

class DeleteProductView(LoginRequiredMixin , View):
    def get(self, request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return redirect('ajantha:home')
    

class SearchProductView(View):
    def post(self, request):
        search = request.POST.get('search')
        search_list = Product.objects.filter(
                Q(name__icontains=search) | Q(category__name__icontains=search)
            )
    
        return render(request, 'ajanthaapp/searchlist.html', {'search_list': search_list})
    

class TilesView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Tiles')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/tiles.html', {'products' : products})
    
class BathFittingView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Bath Fitting')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/bath-fitting.html', {'products' : products})
    
class TilesAdhesiveView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Tiles Adhesive')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/tiles-adhesive.html', {'products' : products})

class PlumbingPipesAndFittingsView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Plumbing Pipes & Fittings')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/plumbing-and-fittings.html', {'products' : products})

class KitchenSinkView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Kitchen Sink')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/kitchen-sink.html', {'products' : products})

class BathAcessoriesView(View):
    def get(self, request):
        products = Product.objects.filter(category__name = 'Bath Acessories')
        print("Fetched Products : ", products)
        return render(request, 'ajanthaapp/bath-acessories.html', {'products' : products})
    
class AllProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'ajanthaapp/all-product.html', {'products' : products})
    

class ContactView(View):
    flag = False
    def get(self, request):
        return render(request, 'ajanthaapp/index.html')
    
    def post(self, request):
        flag = False
        try :
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            message = request.POST.get('message')

            Contact.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email,
                mobile = mobile,
                message = message
            )

            flag = True
            return redirect('ajantha:home')

        except Exception as e :
            flag = False
            print(f'{type(e).__name__} : {e}')
        return redirect('ajantha:home')


    



    
