from django.shortcuts import render;

def wishes(request):
	return render(request,'FirstApp/wishes.html')

def hello(request):
	return render(request,'FirstApp/hello.html')


# {{templ-tag-vars}}
import datetime;
import time;
def datetimefunction(request):
	date1 = datetime.datetime.now();
	print(date1)
	date2 = time.ctime();
	dict1 = {"server_datetime": date1, "server_datetime2": date2}
	return render(request, 'FirstApp/datetime.html', context=dict1)

#student-data & date-time using {{templ-tags}}
import datetime
import time
def student_datetime(request):
	date1=datetime.datetime.now();
	date2=time.ctime();
	rollno = 1001;
	sname='sai';
	marks=95;
	dict1 = {'server_datetime':date1,'server_datetime2':date2,'rollno':rollno,'sname':sname,'marks':marks};
	return render(request,'FirstApp/studentdatetime.html',dict1);

#server date&time with dynamic-wishes
import datetime
def wishes2(request):
    date1=datetime.datetime.now()
    msg1='Hello User/Client...GOOD';
    hr=int(date1.strftime('%H'));
    if hr<12:
        msg1+=' Morning!!'
    elif hr<16:
        msg1+=' Afternoon!!'
    elif hr<20:
        msg1+=' Evening!!'
    else:
        msg1='Hello User/Client...Very Good Night!!'
    dict1={'date1':date1,'msg1':msg1}
    return render(request,'FirstApp/wishes2.html',context=dict1);

