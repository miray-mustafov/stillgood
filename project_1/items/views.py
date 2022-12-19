from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from project_1.items.models import ItemImage, Item

from project_1.items.forms import ItemDetailsForm, ItemAddForm, ItemEditForm, ItemDeleteForm
from django.core.paginator import Paginator, EmptyPage

UserModel = get_user_model()


def item_add_view(request):
    user = UserModel.objects.get(pk=request.user.pk, username=request.user.username)
    if request.method == "POST":
        form = ItemAddForm(request.POST, request.FILES)
        images = request.FILES.getlist('images')

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            for image in images:
                ItemImage.objects.create(image=image, item=item)

            return redirect('item details', pk=item.pk)

    form = ItemAddForm(instance=user, )
    context = {'form': form}
    return render(request, template_name='items/item-add.html', context=context)


class ItemDetails(DetailView):
    context_object_name = 'current_item'
    template_name = 'items/item-details.html'
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object.user  # !
        images = ItemImage.objects.filter(item=self.object)
        context['images'] = images

        indicators = [i for i in range(1, len(images) + 1)]  # taking [1: len+1] indxs for the indicator buttons
        context['indicators'] = indicators
        return context


#
class ItemEditView(UpdateView):
    context_object_name = 'current_item'
    template_name = 'items/item-edit.html'
    form_class = ItemEditForm
    model = Item

    def get_success_url(self):
        return reverse_lazy('item details', kwargs={'pk': self.object.pk})


class ItemDelete(DeleteView):
    template_name = 'items/item-delete.html'
    model = Item
    success_url = reverse_lazy('home page')


# class ItemAddView(CreateView):
#     context_object_name = 'item'
#     template_name = 'items/item-add.html'
#     # success_url = 'items/item-details.html'
#     success_url = 'common/home-page.html'
#     form_class = ItemAddForm
#     model = Item
#
#     # override
#     def form_valid(self, form):
#         """If the form is valid, save the associated model."""
#         self.object = form.save()
#         return super().form_valid(form)

def image_carousel(request):
    return render(request, template_name='image-carousel.html')

#
# def upload(request):
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             ItemImage.objects.create(images=image)
#
#     images = ItemImage.objects.all()  # for edit later in item
#     return render(request, 'multiple-image-demo.html', {'images': images})
