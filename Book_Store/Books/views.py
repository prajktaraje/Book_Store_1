from django.shortcuts import render
from .forms import Add_Book_Informations
from .models import Book
# Create your views here.
def home(request):
    semp=Book.objects.all()
    context={'semp': semp}
    return render(request, 'Book_Store/showinfo.html',context)


def Add_Book_Information(request):
    if request.method=='POST' :     
        fm=Add_Book_Informations(request.POST )
        if fm.is_valid():
            Book_Author=fm.cleaned_data['Author']
            Book_Title=fm.cleaned_data['Title']
            reg=Book(Author=Book_Author,Title=Book_Title)
            reg.save()
            fm=Add_Book_Informations()  

    if request.method=='GET':
        fm=Add_Book_Informations() 

    return render(request,'Book_Store/add_and_show.html',{'form':fm})    