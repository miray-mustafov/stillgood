from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from project_1.common.models import Favourite
from project_1.items.models import ItemImage, Item

from project_1.items.forms import ItemAddForm, ItemEditForm

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

        context['is_favoured'] = \
            Favourite.objects.filter(user=self.request.user, item=self.object).first()
        return context


#
class ItemEditView(UpdateView):
    context_object_name = 'current_item'
    template_name = 'items/item-edit.html'
    form_class = ItemEditForm
    model = Item

    def get_success_url(self):
        return reverse_lazy('item details', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        images = request.FILES.getlist('images')
        ItemImage.objects.filter(item=self.object).delete()
        for image in images:
            ItemImage.objects.create(image=image, item=self.object)

        return super().post(request, *args, **kwargs)


class ItemDelete(DeleteView):
    context_object_name = 'current_item'
    template_name = 'items/item-delete.html'
    model = Item
    success_url = reverse_lazy('home page')


def image_carousel(request):
    return render(request, template_name='image-carousel.html')
