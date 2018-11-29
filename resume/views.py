from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from django.forms import Form

from collections import defaultdict

from resume.models import Cert, Skill, Exp, Edu

import weasyprint 

def front_page(request):
    if request.method == "POST":
        skills = Skill.objects.all()
        certs = Cert.objects.all()
        exp = Exp.objects.all()
        edu = Edu.objects.all()

        #getting QuerySet of distinct skill categories,
        #and by running off "skills" we avoid hitting the DB twice
        skill_cats = skills.values('category').distinct() 

        skill_cats_list = [] #a list for the categories
        
        for cat in skill_cats:  #putting the QuerySet into a list
            skill_cats_list.append(cat['category'])

        form = request.POST
        html = render_to_string('resume/resume_index3.html',
                                   {'resumeActive':True,
                                    'skills':skills,
                                    'skill_cats_list': skill_cats_list,
                                    #'skill_program' : skill_program,
                                    #'program_sec': program_sec,
                                    'certs': certs,
                                    'exp': exp,
                                    'edu': edu})
        
        #checking which sections to hide on pdf download
        css = "#intro-box {display: none;} \
        #download-pdf {display: none;} "
        #html = "<html><head></head><body>"
        for field in form:
            #html = html + "<p>" + field + " value: " + field[0] + "</p>"
            #assert False
            css = css + "#" + field +"-display" + " {display: " + ('none' if (form[field] == "False") else "") + ";}"
        
        #return HttpResponse(html)
        
        #assert False
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename=corban-cordova-awesome-resume.pdf'
        weasyprint.HTML(string=html).write_pdf(response,
            stylesheets=[weasyprint.CSS(string=css)])
        return response
        
    
    else:
        skills = Skill.objects.all()
        certs = Cert.objects.all()
        exp = Exp.objects.all()
        edu = Edu.objects.all()

        #getting QuerySet of distinct skill categories,
        #and by running off "skills" we avoid hitting the DB twice
        skill_cats = skills.values('category').distinct() 

        skill_cats_list = [] #a list for the categories
        
        for cat in skill_cats:  #putting the QuerySet into a list
            skill_cats_list.append(cat['category'])
        
        #assert False
        return render(request,
        'resume/resume_index3.html',
        {'resumeActive': True,
            'skills':skills,
            'skill_cats_list': skill_cats_list,
            #'skill_program' : skill_program,
            #'program_sec': program_sec,
            'certs': certs,
            'exp': exp,
            'edu': edu})
