from resume.models import Cert, Skill, Exp, Edu
from django import template
register = template.Library()

'''
get a list of sections -| maybe done hard coded
render sections        -|
    get a list of categories in section
    render categories
        get a list of descriptions/items
        render items
'''

@register.inclusion_tag('resume/skill-list.html')
def get_cat_list(category):
    skills = Skill.objects.all()

    cat_row_query = skills.filter(category=category)
  
    return {'cat_row_list': cat_row_query,
            'category':cat_row_query[0].category}

'''
@register.inclusion_tag('resume/exp-list.html')
def get_exp_list(section):
    exp = Exp.objects.all()

    exp_tag_query = exp.filter(category=section)
    
    return {'exp_tag_list': exp_tag_query,
            'category':cat_tag_query[0].category}
            '''