from django.shortcuts import render
from .models import batch, subjects,branch
# Create your views here.
def home(request):
	batc,err,val,pointer,count,tmarks,msg='','',0,'',0,0,''
	if request.method=='POST':
		y=request.POST.get('marksform','')
		if y=='0':
			val=request.POST['year']

			years = batch.objects.filter(year=val)
			branchs = request.POST['branch']
			if (branchs == 'CE' or branchs == 'IT' or branchs == 'ME') and val=='1':
				branchs = 'Computer Engineering'
				print(branchs)
			elif (branchs=='CE' or branchs == 'IT') and val=='2':
				branchs = 'Computer Engineering'
				print(branchs)
			else:
				branchs = 'Electronics and Communication Engineering'
			branchs = branch.objects.filter(branch = branchs)
			batc = subjects.objects.filter(year = years,branch = branchs).order_by('-credit')
			val='1'
		
		else:
			markslist = request.POST.getlist('marks[]')
			credits = request.POST.getlist('credit[]')
			j=0
			for i in markslist:
				count+=int(credits[j])
				tmarks+=int(credits[j])*int(i)
				j+=1
				print(tmarks)
			pointer = tmarks/count
			print(count,pointer)
			pointer = round(pointer,2)
			if(pointer>9):
				msg = "👌"
	else:
		pass
	return render(request,'index.html',{'batch':batc,'val':val,'err':err,'pointer':pointer,'msg':msg})