from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import contactUsForm
from service.models import Service
from django.core.paginator import Paginator
from enquiry.models import Enquiry
from artist.models import Artist

def homePage(request):
    artist_data = Artist.objects.all()
    return render(request, 'index.html',{'artist_data': artist_data})

def aboutUs(request):
    return render(request, 'about.html')

def contactUs(request):
    try:
        if request.method=="POST":
            name = request.POST.get('full-name')
            email = request.POST['email']
            url = "/thankyou/?name={}".format(name)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request, 'contact.html')

def enquiryFormFn(request):
    if request.method =="POST":
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        des = request.POST.get('message')
        en = Enquiry(full_name=name, email=email, company=company, description=des)
        en.save()
        url = "/thankyou/?name={}".format(name)
        return HttpResponseRedirect(url)
    return render(request, 'contact.html')

def listingPage(request):
    return render(request, 'listing-page.html')

def formPage(request):
    data = {}
    fn = contactUsForm()
    data = {'form': fn}
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        output = first_name+' '+last_name
        
    return render(request, 'forms.html', {'form':fn})

def thankYouPage(request):
    if request.method=="GET":
        name= request.GET['name']
    return render(request, 'thank-you.html', {'name': name})

def servicesPage(request):
    serviceData= Service.objects.all().order_by('title')
    paginator = Paginator(serviceData, 2)
    page_number = request.GET.get('page')
    ServiceDataFinal = paginator.get_page(page_number)
    totalPages = ServiceDataFinal.paginator.num_pages
    # print("total pages",totalPages)
    # pageList=[]
    # for n in range(totalPages):
    #     pageList.append(n+1)
    if request.method == "GET":
        st = request.GET.get('service_title')
        if st != None:
            ServiceDataFinal= Service.objects.filter(title__icontains = st)
    data = {
        'serviceData': ServiceDataFinal,
        'totalPages': totalPages,
        'totalPagesList':[n+1 for n in range(totalPages)],
        'pageNo':page_number,
    }
    return render(request, 'services.html', data)
# def blogs(request):
#     return HttpResponse("This is blog page od my site")

# def blogDetail(request, courseid):
#     return HttpResponse(courseid)