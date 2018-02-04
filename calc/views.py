from django.shortcuts import render
from .models import batch, subjects,branch
# Create your views here.
def home(request):
	batc,err,val,pointer,count,tmarks,msg='','',0,'',0,0,''
	if request.method=='POST':
		y=request.POST.get('marksform','')
		if y=='0':
			val=request.POST['year']
			branchs = request.POST['branch']
			if (((branchs == 'CE' or branchs == 'IT' or branchs == 'ME') and val=='1') or ((branchs=='ECE' or branchs=='EIC' or branchs=='EE') and val=='2')):
				branchs = 'Computer Engineering'
				val='1'
			elif (((branchs == 'CE' or branchs == 'IT' or branchs == 'ME') and val=='2') or ((branchs=='ECE' or branchs=='EIC' or branchs=='EE') and val=='1')):
				branchs = 'Electronics and Communication Engineering'
				val='1'
			elif (branchs=='CE' or branchs == 'IT') and val=='3':
				branchs = 'Computer Engineering'
			years = batch.objects.filter(semester=val)
			branchs = branch.objects.filter(branch = branchs)
			batc = subjects.objects.filter(semester = years,branch = branchs).order_by('-credit')
			print(batc)
			val='1'
		
		else:
			markslist = request.POST.getlist('marks[]')
			credits = request.POST.getlist('credit[]')
			j=0
			for i in markslist:
				count+=int(credits[j])
				tmarks+=int(credits[j])*int(i)
				j+=1
			pointer = tmarks/count
			pointer = round(pointer,2)
			if(pointer>=9):
				msg = "WEll Done. Keep it up.👌"
			elif pointer>=8:
				msg = "Thodi or mehnat kro. 😌"
			elif pointer>=7:
				msg = "Padhai pr dhayan do. 😤"
			elif pointer>=6:
				msg="Tera kuch nhi ho skta. 😅"
			elif pointer>=4:
				msg="Tumse na ho payega. 😉"
	else:
		pass
	return render(request,'index.html',{'batch':batc,'val':val,'err':err,'pointer':pointer,'msg':msg})