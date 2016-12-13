from django.shortcuts import render



def index(request):
    return render(request, 'polls/index.html')	
def black(request):
    return render(request, 'polls/black.html')
def english(request):
    return render(request, 'polls/english.html')
def englishbl(request):
    return render(request, 'polls/russian.html')
def name(request):
	try:
		ex = request.GET["A"]
	except:
		ex=""
	return render(request,'polls/name.html',{'ex':ex}) 
def namebl(request):
	try:
		ex=request.GET["A"]
	except:
		ex=""
	return render(request, 'polls/namebl.html', {'ex':ex})