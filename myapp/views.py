from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import staff,time
from django.shortcuts import get_object_or_404
def mainpage(request):
    time_list=time.objects.all()
    staff_list=staff.objects.all()

    #顯示班表
    time_week1=time.objects.filter(week='Mon.').order_by('time')
    time_week2=time.objects.filter(week='Tue.').order_by('time')
    time_week3=time.objects.filter(week='Wed.').order_by('time')
    time_week4=time.objects.filter(week='Thu.').order_by('time')
    time_week5=time.objects.filter(week='Fri.').order_by('time')
    time_week6=time.objects.filter(week='Sat.').order_by('time')
    time_week7=time.objects.filter(week='Sun.').order_by('time')

    #先弄成集合，再丟到網頁
    context={'time_week1':time_week1,'time_week2':time_week2,'time_week3':time_week3,'time_week4':time_week4,'time_week5':time_week5,'time_week6':time_week6,'time_week7':time_week7}
    

    return render(request, "mainpage.html",context)

        
def insert(request):
    time_list=time.objects.all()
    staff_list=staff.objects.all()

    times = None
    week = None
    stid = None

    if request.method=='POST':
        match request.POST.get('time'):
            case '1':
                times='8:10-9:00'
            case '2':
                times='9:10-10:00'
            case '3':
                times='10:20-11:10'
            case '4':
                times='11:20-12:10'
            case '5':
                times='12:20-13:10'
            case '6':
                times='13:20-14:10'
            case '7':
                times='14:20-15:10'
            case '8':
                times='15:30-16:20'
            case '9':
                times='16:30-17:20'
            

        match request.POST.get('week'):
            case 'Mon.':
                week='Monday'
            case 'Tue.':
                week='Tuesday'
            case 'Wed.':
                week='Wednesday'
            case 'Thu.':
                week='Thursday'
            case 'Fri.':
                week='Friday'
            case 'Sat.':
                week='Saturday'
            case 'Sun.':
                week='Sunday'

    #確認員工存不存在
        for getstaff in staff_list:
            a=str(getstaff.cId)
            if a == request.POST.get('id'):#撞到改1,getstaff(int),POST(str)
                stid=request.POST.get('id')


        #確認有沒有被拿走
        for gettime in time_list:
            if gettime.time == request.POST.get('time') and gettime.week == request.POST.get('week'):#都撞到改1
                times='1'
                week='1'

        

        #create
        if not(stid == None):
            if not(times == '1' and week == '1'):
                    savetime=time()
                    savetime.stId=staff.objects.get(cId=request.POST.get('id'))
                    savetime.week=request.POST.get('week')
                    savetime.time=request.POST.get('time')
                    savetime.save()
                    return render(request, "insertpage.html",locals())
            else:
                messages.error(request,'already be selected!')
                return render(request, "insertpage.html",locals())
        else:
            messages.error(request,'wrong id!')
            return render(request, "insertpage.html",locals())
    else:                
        return render(request, "insertpage.html",locals())
        
def search(request):   

    staff_list=staff.objects.all()
    stid = None
    #確認員工存不存在
    if request.method=='POST':  
        for getstaff in staff_list:
            a=str(getstaff.cId)
            if a == request.POST.get('id'):#撞到改1,getstaff(int),POST(str)
                stid=request.POST.get('id')
        if not(stid == None):
            time_week1=time.objects.filter(stId=request.POST.get('id'),week='Mon.').order_by('time')
            time_week2=time.objects.filter(stId=request.POST.get('id'),week='Tue.').order_by('time')
            time_week3=time.objects.filter(stId=request.POST.get('id'),week='Wed.').order_by('time')
            time_week4=time.objects.filter(stId=request.POST.get('id'),week='Thu.').order_by('time')
            time_week5=time.objects.filter(stId=request.POST.get('id'),week='Fri.').order_by('time')
            time_week6=time.objects.filter(stId=request.POST.get('id'),week='Sat.').order_by('time')
            time_week7=time.objects.filter(stId=request.POST.get('id'),week='Sun.').order_by('time')
            context={'time_week1':time_week1,'time_week2':time_week2,'time_week3':time_week3,'time_week4':time_week4,'time_week5':time_week5,'time_week6':time_week6,'time_week7':time_week7}
            return render(request, "searchpage.html",context)
        else:
            messages.error(request,'wrong id!')
            return render(request, "searchpage.html",locals())
    else:
        return render(request, "searchpage.html",locals())
def edit(request,pk):
    edt=time.objects.get(id=pk)
    time_list=time.objects.all()
    times = None
    week = None
    if request.method == "POST":
        match request.POST.get('time'):
            case '1':
                times='8:10-9:00'
            case '2':
                times='9:10-10:00'
            case '3':
                times='10:20-11:10'
            case '4':
                times='11:20-12:10'
            case '5':
                times='12:20-13:10'
            case '6':
                times='13:20-14:10'
            case '7':
                times='14:20-15:10'
            case '8':
                times='15:30-16:20'
            case '9':
                times='16:30-17:20'
            

        match request.POST.get('week'):
            case 'Mon.':
                week='Monday'
            case 'Tue.':
                week='Tuesday'
            case 'Wed.':
                week='Wednesday'
            case 'Thu.':
                week='Thursday'
            case 'Fri.':
                week='Friday'
            case 'Sat.':
                week='Saturday'
            case 'Sun.':
                week='Sunday'
        #確認有沒有被拿走
        for gettime in time_list:
            if gettime.time == request.POST.get('time') and gettime.week == request.POST.get('week'):#都撞到改1
                times='1'
                week='1'
        if not(times == '1' and week == '1'):
            edt.week=request.POST.get('week')
            edt.time=request.POST.get('time')
            edt.save()
            return redirect('/search')
        else:
            messages.error(request,'already be selected!')
            return render(request, "editpage.html",context)
    context={'edit':edt}
    return render(request, "editpage.html",context)

def delete(request,pk):   
    dele=time.objects.get(id=pk)

    if request.method == "POST":
        dele.delete()
        return redirect('/search')
    context={'del':dele}
    return render(request, "deletepage.html",context)