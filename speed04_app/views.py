from django.shortcuts import render

# Create your views here.
def speed04_function(request):
	context = {
	    "articles": [
	       {
	        "title": "title 1",
	        "author": "Manal",
           },

           {
             "title": "title 2",
             "author": "Mona",
           },
        ],   
	}
	return render(request, 'home_page.html', context)