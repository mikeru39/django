from authapp.models import ShopUser
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory
from django.contrib.auth.decorators import user_passes_test
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления лучше сделаем неактивным
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    fields = '__all__'
    success_url = reverse_lazy('admin:categories')
    template_name = 'adminapp/category_create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Редактирование категории'
        return context


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    fields = '__all__'
    success_url = reverse_lazy('admin:categories')
    template_name = 'adminapp/category_create.html'


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name ='adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')


class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        category_pk = self.kwargs.get('category_pk')
        if category_pk:
            return qs.filter(category__pk=category_pk)
        else:
            return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        context['title'] = 'Админка. Продукты.'
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context

class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('admin:products')
    template_name = 'adminapp/product_update.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['buttom'] = 'создать'
        return context

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('admin:products')
    template_name = 'adminapp/product_update.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['buttom'] = 'сохранить'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('admin:products')