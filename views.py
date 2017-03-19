from django.shortcuts import render_to_response

def q(request):
        a=[1,2,3,4]
        b=[1,3,5,6]
        ra=range(len(a))
        c=zip(a,b)
        return render_to_response('q.html',{'a':a,'b':b,'ra':ra,'c':c})
