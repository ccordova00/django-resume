from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchVector, \
SearchQuery, SearchRank, TrigramSimilarity
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from taggit.models import Tag

from .forms import EmailPostForm, CommentForm, SearchForm
from .models import Post, Comment

'''
def contact(request):
    """
    A view for a contact form. Originally for the blog but
    could be repourposed to use for the whole site.
    """
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            send_mail(
                cleaned_data['subject'],
                cleaned_data['message'],
                cleaned_data['email'], #from email.
                             ['eruditus.d@gmail.com'], #to email
            )
            return HttpResponseRedirect('blog/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':'I love your site!'}
        )
    return render(request,
                  'contact_form.html',
                  {'form': form,
                   'blog_active': True})
'''
def post_search(request):
    form = SearchForm() #initialize variables
    query = None
    results = []
    similar_results = []

    if 'query' in request.GET:   #test to see if there's anything other than None in requst.GET['query']
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query'] #clean the query
            search_vector = SearchVector('title',
                                         'body')
            search_query = SearchQuery(query)
            # exact matches
            results = Post.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector,
                                search_query)
                ).filter(search=search_query).order_by('-rank')

    return render(request, #return results
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})   

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
def post_list(request, tag_slug=None):
    '''
    default view that lists blog posts
    '''
#    context = {} #initialize context
#    context['blog_active'] = True #for navigation
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag]) 
    
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginatr.page(paginator.num_pages)

    context = {'page': page, #finalize context before render
                   'posts': posts,
                   'tag': tag,}

    return render(request,
                  'blog/post/list.html',
                  context)
                   #'blog_active':True})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    # list of active comments
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet.
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                                    .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                                      .order_by('-same_tags','-publish')[:4]
    return render(request,
                  'blog/post/detail.html',
                  {'post':post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form,
                   'similar_posts': similar_posts,
                   'blog_active': True
                  })

def post_share(request, post_id):
    #retrieve  post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        #form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'\
.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:  {}'\
.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject,
                      message,
                      'meta.low.key@gmail.com', #from email
                      [cd['to']]) #to email
            sent = True

    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
