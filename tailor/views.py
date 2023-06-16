from django.shortcuts import render, redirect
from .models import Male, Female
from django.contrib import messages
from .forms import MeasurementForm

# Create your views here.
def Malenote (request):
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

        return render(request, 'measurement/index.html')
    

def Tailornote2(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MeasurementForm()
    context = {'form': form}
    return render(request, 'measurement/test.html', context)


def Femalenote(request):
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

        return render(request, 'measurement/index.html')