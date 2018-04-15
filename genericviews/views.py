from django.shortcuts import render

# Create your views here.
from django.views import generic

from genericviews.forms import ProductForm
from genericviews.models import Product


# normal view to handle the entry of the product and store it on the database
def makeentry(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            rollNo = request.POST.get('rollNo', '')
            mobile = request.POST.get('mobile', '')
            complaintType = request.POST.get('complaintType', '')
            hostelNo = request.POST.get('hostelNo', '')
            wing = request.POST.get('wing', '')
            roomNo = request.POST.get('roomNo','')
            complaintTitle = request.POST.get('complaintTitle', '')
            complaintDesc = request.POST.get('complaintDesc', '')

        product = Product(name=name, rollNo=rollNo, mobile=mobile, complaintType=complaintType, hostelNo=hostelNo, wing=wing, roomNo=roomNo, complaintTitle=complaintTitle, complaintDesc=complaintDesc)

        product.save()

        return render(request, 'genericviews/finalmessage.html', {'message': 'Thanks'})
    else:
        form = ProductForm()
        return render(request, 'genericviews/makeentry.html', {'form': form})


# generic view to fetch the data then show in a list
class IndexView(generic.ListView):
    # a name to refer to the object_list(to be used in the index.html)
    context_object_name = 'product_list'
    template_name = 'genericviews/index.html'

    def get_queryset(self):
        return Product.objects.all()


# generic view to show the details of a particular object
class DetailsView(generic.DetailView):
    model = Product
    template_name = 'genericviews/detail.html'

