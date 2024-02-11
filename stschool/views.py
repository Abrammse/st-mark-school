from django.contrib import messages
from django.shortcuts import render ,redirect

from django.http import JsonResponse
from django.contrib.auth import authenticate, login

from header.models import header
from الاخبار.models import الاخبار
from mark.models import mark
from foot.models import foot
from photo .models import الصورة,الصور

from الاية.models import الاية
from الخدام.models import الخدام
from الالحان.models import اللحان1
from الالحان.models import اللحان11
from الالحان.models import اللحان12
from الالحان.models import اللحان13
from الالحان.models import اللحان2
from الالحان.models import اللحان21
from الالحان.models import اللحان22
from الالحان.models import اللحان23
from الالحان.models import اللحان3
from الالحان.models import اللحان31
from الالحان.models import اللحان32
from الالحان.models import اللحان33

from الاجبية.models import الاجبية1
from الاجبية.models import الاجبية11
from الاجبية.models import الاجبية12
from الاجبية.models import الاجبية13
from الاجبية.models import الاجبية2
from الاجبية.models import الاجبية21
from الاجبية.models import الاجبية22
from الاجبية.models import الاجبية23
from الاجبية.models import الاجبية3
from الاجبية.models import الاجبية31
from الاجبية.models import الاجبية32
from الاجبية.models import الاجبية33



from القبطى.models import القبطى1
from القبطى.models import القبطى11
from القبطى.models import القبطى12
from القبطى.models import القبطى13
from القبطى.models import القبطى2
from القبطى.models import القبطى21
from القبطى.models import القبطى22
from القبطى.models import القبطى23
from القبطى.models import القبطى3
from القبطى.models import القبطى31
from القبطى.models import القبطى32
from القبطى.models import القبطى33










from الطقس.models import الطقس1
from الطقس.models import الطقس11
from الطقس.models import الطقس12
from الطقس.models import الطقس13
from الطقس.models import الطقس2
from الطقس.models import الطقس21
from الطقس.models import الطقس22
from الطقس.models import الطقس23
from الطقس.models import الطقس3
from الطقس.models import الطقس31
from الطقس.models import الطقس32
from الطقس.models import الطقس33

from app.models import Students,FormConfiguration
from result.models import Student




def index(request):
    headerData=header.objects.all()
    markdata=mark.objects.all()
    newdata=الاخبار.objects.all()
    Ayadata = الاية.objects.all()
    footdata = foot.objects.all()
    peapledata = الخدام.objects.all()
    photodata = الصور.objects.all()
    photosdata = الصورة.objects.all()






    data = {
        'headerData': headerData,
        'markdata': markdata,
        'newdata':newdata,
        'Ayadata':Ayadata,
        'footdata': footdata,
        'peapledata': peapledata,
        'photodata': photodata,
        'photosdata': photosdata,

    }
    return render(request,'home.html',data)
def Abram(request):
    headerData=header.objects.all()
    Ayadata = الاية.objects.all()
    photodata = الصور.objects.all()
    photosdata = الصورة.objects.all()


    data={
        'headerData': headerData,
        'Ayadata': Ayadata,
        'photodata': photodata,
        'photosdata': photosdata,

    }
    return render(request,'photo.html',data)

def send(request):
    if request.method == "POST":
        name = request.POST['name']
        telephone = request.POST['tel']
        photo = request.FILES['image']
        date = request.POST['date']
        gender = request.POST['gender']
        العنوان = request.POST['العنوان']
        classname = request.POST['classname']
        degrees = request.POST['degrees']

        obj = Students()
        obj.الاسم = name
        obj.tel = telephone
        obj.data = date
        obj.photo = photo
        obj.gender = gender
        obj.Аddress = العنوان
        obj.mark = classname
        obj.degree = degrees
        obj.save()

        messages.success(request, 'تم تسجيل طلبك بنجاح برجاء التوجه لمكتب المدرسة لدفع المصاريف.',)
        return redirect('newac')

    form_config = FormConfiguration.objects.first()
    context = {
        'form_config': form_config,
    }
    return render(request, 'send.html', context)
def al7an1(request):
    al7an1data = اللحان1.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an1data': al7an1data,


    }
    return render(request,'al7an1.html',data)

def al7an11(request):
    al7an11data = اللحان11.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an11data': al7an11data,


    }
    return render(request,'al7an11.html',data)

def al7an12(request):
    al7an12data = اللحان12.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an12data': al7an12data,


    }
    return render(request,'al7an12.html',data)

def al7an13(request):
    al7an13data = اللحان13.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an13data': al7an13data,


    }
    return render(request,'al7an13.html',data)

def al7an2(request):
    al7an2data = اللحان2.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'al7an2data': al7an2data,

    }
    return render(request, 'al7an2.html', data)

def al7an21(request):
    al7an21data = اللحان21.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an21data': al7an21data,


    }
    return render(request,'al7an21.html',data)

def al7an22(request):
    al7an22data = اللحان22.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an22data': al7an22data,


    }
    return render(request,'al7an22.html',data)

def al7an23(request):
    al7an23data = اللحان23.objects.all()
    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,
        'al7an23data': al7an23data,


    }
    return render(request,'al7an23.html',data)

def al7an3(request):
    al7an3data = اللحان3.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'al7an3data': al7an3data,

    }
    return render(request, 'al7an3.html', data)

def al7an31(request):
    al7an31data = اللحان31.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'al7an31data': al7an31data,

    }
    return render(request, 'al7an31.html', data)

def al7an32(request):
    al7an32data = اللحان32.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'al7an32data': al7an32data,

    }
    return render(request, 'al7an32.html', data)

def al7an33(request):
    al7an33data = اللحان33.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'al7an33data': al7an33data,

    }
    return render(request, 'al7an33.html', data)





def kpaty1(request):
    kpaty1data = القبطى1.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty1data': kpaty1data,

    }
    return render(request, 'kpaty1.html', data)

def kpaty11(request):
    kpaty11data = القبطى11.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty11data': kpaty11data,

    }
    return render(request, 'kpaty11.html', data)

def kpaty12(request):
    kpaty12data = القبطى12.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty12data': kpaty12data,

    }
    return render(request, 'kpaty12.html', data)


def kpaty13(request):
    kpaty13data = القبطى13.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty13data': kpaty13data,

    }
    return render(request, 'kpaty1.html', data)

def kpaty2(request):
    kpaty2data = القبطى2.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty2data': kpaty2data,

    }
    return render(request, 'kpaty2.html', data)
def kpaty21(request):
    kpaty21data = القبطى21.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty21data': kpaty21data,

    }
    return render(request, 'kpaty21.html', data)
def kpaty22(request):
    kpaty22data = القبطى22.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty22data': kpaty22data,

    }
    return render(request, 'kpaty23.html', data)
def kpaty23(request):
    kpaty23data = القبطى23.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty23data': kpaty23data,

    }
    return render(request, 'kpaty23.html', data)


def kpaty3(request):
    kpaty3data = القبطى3.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty3data': kpaty3data,

    }
    return render(request, 'kpaty3.html', data)
def kpaty31(request):
    kpaty31data = القبطى31.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty31data': kpaty31data,

    }
    return render(request, 'kpaty31.html', data)
def kpaty32(request):
    kpaty32data = القبطى32.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty32data': kpaty32data,

    }
    return render(request, 'kpaty32.html', data)
def kpaty33(request):
    kpaty33data = القبطى33.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'kpaty33data': kpaty33data,

    }
    return render(request, 'kpaty33.html', data)


def taks1(request):
    taks1data = الطقس1.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks1data': taks1data,

    }
    return render(request, 'taks1.html', data)
def taks11(request):
    taks11data = الطقس11.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks11data': taks11data,

    }
    return render(request, 'taks11.html', data)
def taks12(request):
    taks12data = الطقس12.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks12data': taks12data,

    }
    return render(request, 'taks12.html', data)
def taks13(request):
    taks13data = الطقس13.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks13data': taks13data,

    }
    return render(request, 'taks13.html', data)


def taks2(request):
    taks2data = الطقس2.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks2data': taks2data,

    }
    return render(request, 'taks2.html', data)
def taks21(request):
    taks21data = الطقس21.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks21data': taks21data,

    }
    return render(request, 'taks21.html', data)
def taks22(request):
    taks22data = الطقس22.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks22data': taks22data,

    }
    return render(request, 'taks22.html', data)
def taks23(request):
    taks23data = الطقس23.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks23data': taks23data,

    }
    return render(request, 'taks23.html', data)


def taks3(request):
    taks3data = الطقس3.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks3data': taks3data,

    }
    return render(request, 'taks3.html', data)

def taks31(request):
    taks31data = الطقس31.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks31data': taks31data,

    }
    return render(request, 'taks31.html', data)
def taks32(request):
    taks32data = الطقس32.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks32data': taks32data,

    }
    return render(request, 'taks32.html', data)
def taks33(request):
    taks33data = الطقس33.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'taks33data': taks33data,

    }
    return render(request, 'taks33.html', data)



def Agpia1(request):
    Agpia1data = الاجبية1.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia1data': Agpia1data,

    }
    return render(request, 'Agpia1.html', data)

def Agpia11(request):
    Agpia11data = الاجبية11.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia11data': Agpia11data,

    }
    return render(request, 'Agpia11.html', data)

def Agpia12(request):
    Agpia12data = الاجبية12.objects.all()
    Ayadata = الاية.objects.all()


    data = {

        'Ayadata': Ayadata,
        'Agpia12data': Agpia12data,

    }
    return render(request, 'Agpia12.html', data)

def Agpia13(request):
    Agpia13data = الاجبية13.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia13data': Agpia13data,

    }
    return render(request, 'Agpia13.html', data)



def Agpia2(request):
    Agpia2data = الاجبية2.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia2data': Agpia2data,

    }
    return render(request, 'Agpia2.html', data)

def Agpia21(request):
    Agpia21data = الاجبية21.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia21data': Agpia21data,

    }
    return render(request, 'Agpia21.html', data)

def Agpia22(request):
    Agpia22data = الاجبية22.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia22data': Agpia22data,

    }
    return render(request, 'Agpia22.html', data)

def Agpia23(request):
    Agpia23data = الاجبية23.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia23data': Agpia23data,

    }
    return render(request, 'Agpia23.html', data)


def Agpia3(request):
    Agpia3data = الاجبية3.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia3data': Agpia3data,

    }
    return render(request, 'Agpia3.html', data)

def Agpia31(request):
    Agpia31data = الاجبية31.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia31data': Agpia31data,

    }
    return render(request, 'Agpia31.html', data)

def Agpia32(request):
    Agpia32data = الاجبية32.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia32data': Agpia32data,

    }
    return render(request, 'Agpia32.html', data)

def Agpia33(request):
    Agpia33data = الاجبية33.objects.all()
    Ayadata = الاية.objects.all()

    data = {

        'Ayadata': Ayadata,
        'Agpia33data': Agpia33data,

    }
    return render(request, 'Agpia33.html', data)



def meka3(request):

    Ayadata = الاية.objects.all()



    data={

        'Ayadata': Ayadata,



    }
    return render(request,'al7an2.html',data)


def meka4(request):

    Ayadata = الاية.objects.all()


    data = {

        'Ayadata': Ayadata,


    }
    return render(request, 'al7an3.html', data)
def meka2(request):

    Ayadata = الاية.objects.all()

    data={

        'Ayadata': Ayadata,


    }
    return render(request,'al7an1-1.html',data)


def system(request):



 return render(request,'index.html')
def search_school(request):
    if request.method == 'GET':
        school_id = request.GET.get('school-search')
        students = Student.objects.filter(idschool=school_id)

        selected_student = None
        subjects = []
        total_grades = []
        success_message = request.GET.get('success_message')

        if students:
            selected_student = students[0]
            subjects = selected_student.subjects.all()
            for subject in subjects:
                grade = subject.grade
                if grade.isdigit():
                    try:
                        total_grades.append(int(grade))
                    except ValueError:
                        pass
        else:
            success_message = "لا توجد بيانات صحيح"

        if 'pdf' in request.GET:
            # Generate PDF or perform any other action if needed
            pass

        # Check if results should be open or closed
        results_open = True  # Set to True by default
        if 'close_results' in request.GET:
            results_open = False


        context = {
            'students': students,
            'selected_student': selected_student,
            'subjects': subjects,
            'total_grades': sum(total_grades),
            'success_message': success_message,
            'student': selected_student,  # Add this line to pass the selected student to the template
            'results_open': results_open,
        }

        return render(request, 'search.html', context)

    return render(request, 'search.html')
def new(request):
    Ayadata = الاية.objects.all()
    newdata=الاخبار.objects.all()
    data={

        'newdata': newdata,
        'Ayadata': Ayadata,


    }

    return render(request,'NewNews.html',data)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('pass')

        try:
            student = Student.objects.get(username=username, password=password)
            # Login successful, perform necessary actions
            # ...

            if 'login_success' not in request.session:
                messages.success(request, 'تم تسجيل الدخول بنجاح.')
                request.session['login_success'] = True

            return redirect('search')

        except Student.DoesNotExist:
            # Login failed, handle error
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة.')

    # Get messages from the session
    stored_messages = messages.get_messages(request)
    for message in stored_messages:
        pass  # Iterate over messages to process them, but without displaying them

    return render(request, 'login.html')