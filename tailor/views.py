from django.shortcuts import render, redirect
from .models import Male, Female, Catalog, Receipt, Blog, Comment
from django.contrib import messages
from .forms import MaleForm, FemaleForm, CommentForm

# Create your views here.
# MALE VIEW ----------------------------------------------------------------------------------------------------------------
def MaleView (request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_phone_number = request.POST.get('client_phone_number')
        client_email = request.POST.get('client_email')
        head = request.POST.get('head')
        neck = request.POST.get('neck')
        shoulder_length = request.POST.get('shoulder_length')
        chest = request.POST.get('chest')
        back = request.POST.get('back')
        arm_length_short = request.POST.get('arm_length_short')
        arm_length_long = request.POST.get('arm_length_long')
        biceps = request.POST.get('biceps')
        belly = request.POST.get('belly')
        wrist = request.POST.get('wrist')
        top_length = request.POST.get('top_length')
        trouser_length = request.POST.get('trouser_length')
        waist = request.POST.get('waist')
        laps = request.POST.get('laps')
        calf = request.POST.get('calf')
        ankle = request.POST.get('ankle')
        note = request.POST.get('note')

        malenote = Male.objects.create(client_name=client_name, client_address=client_address, client_phone_number=client_phone_number, client_email=client_email, head=head, neck=neck, shoulder_length=shoulder_length, chest=chest, back=back, arm_length_short=arm_length_short, arm_length_long=arm_length_long, biceps=biceps, belly=belly, wrist=wrist, top_length=top_length, trouser_length=trouser_length, waist=waist, laps=laps, calf=calf, ankle=ankle, note=note)

        if malenote.is_valid():
            malenote.save()
            messages.success(request, 'Clients Measurements has been saved successfully')
            return redirect('/')
        
    else: 

        return render(request, 'tailor/index.html')
    

def MaleViewTest(request):
    if request.method == 'POST':
        form = MaleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaleForm()
    context = {'form': form}
    return render(request, 'tailor/test.html', context)

# FEMALE VIEW --------------------------------------------------------------------------------------------------
def FemaleView(request):
    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_phone_number = request.POST.get('client_phone_number')
        client_email = request.POST.get('client_email')
        bust = request.POST.get('head')
        waist = request.POST.get('neck')
        hips = request.POST.get('shoulder_length')
        bust_apex = request.POST.get('chest')
        shoulder = request.POST.get('back')
        neck_to_waist = request.POST.get('arm_length_short')
        arm_length_long = request.POST.get('arm_length_long')
        arm_length_short = request.POST.get('biceps')
        belly = request.POST.get('belly')
        wrist = request.POST.get('wrist')
        note = request.POST.get('note')

        femalenote = Female.objects.create(client_name=client_name, client_address=client_address, client_phone_number=client_phone_number, client_email=client_email, bust=bust, waist=waist, hips=hips, bust_apex=bust_apex, shoulder=shoulder, neck_to_waist=neck_to_waist, arm_length_long=arm_length_long, arm_length_short=arm_length_short, belly=belly, wrist=wrist, note=note)

        if femalenote.is_valid():
            femalenote.save()
            messages.success(request, 'Clients Measurements has been saved successfully')
            return redirect('/')
        
    else: 

        return render(request, 'tailor/index.html')
    
def FemaleViewTest(request):
    if request.method == 'POST':
        form = FemaleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FemaleForm()
    context = {'form': form}
    return render(request, 'tailor/test.html', context)
    
# CATALOG VIEW --------------------------------------------------------------------------------------------

def CatalogView(request):
    catalog = Catalog.objects.all()
    
    return render(request, 'tailor/catalog.html', {"catalog": catalog})


def CatalogSingleView (request, post_id):

    single_product = Catalog.objects.get(id=post_id)
    context={
            'single_product' : single_product
        }

    return render(request,'tailor/catalog_single.html', context)

# RECEIPT VIEW -----------------------------------------------------------------------------------------

def ReceiptView(request):
    receipt = Receipt.objects.all()
    
    return render(request, 'tailor/receipt.html', {"receipt": receipt})

def ReceiptSingleView (request, post_id):

    single_receipt = Receipt.objects.get(id=post_id)
    context={
            'single_receipt' : single_receipt
        }

    return render(request,'tailor/receipt_single.html', context)


# BLOG VIEW --------------------------------------------------------------------------------------------

def BlogSingleView (request, post_id):

    single_blog= Blog.objects.get(id=post_id)
    context={
            'single_blog' : single_blog
        }

    return render(request,'tailor/blog_single.html', context)


def BlogView(request):
    blog = Blog.objects.all().order_by('date_posted')[5:]
    comment = Comment.objects.all()
    context = { "blog": blog, 'comment': comment }
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        
        comment_blog = Comment.objects.create(name=name, email=email, comment=comment)

        
        comment_blog.save()
        messages.success(request, 'Your comment has been sent successfully.')
        return redirect('commentpage')
        
    else: 

        return render(request, 'tailor/blog.html', context)
    

def CommentViewTest(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        form.save()
        messages.success(request, 'Your comment has been sent successfully.')
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'tailor/test.html', context)




