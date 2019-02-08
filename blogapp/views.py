from django.shortcuts import render_to_response,get_object_or_404,render
from django.core.paginator import Paginator
from .models import movie,movie_type

EVERYPAGE_MOVIES_NUM = 6

# Create your views here.
def movies_list(request):
    page_num = request.GET.get('page',1)#获取url的页面需求(GET参数)
    movie_all_list = movie.objects.all()
    paginator = Paginator(movie_all_list,EVERYPAGE_MOVIES_NUM)#进行分页
    page_of_movies = paginator.get_page(page_num)#django考虑到的转换页面函数
    current_page_num = page_of_movies.number#获取当前页码
    #获取当前页码前后各两页
    pages_range = list(range(max(current_page_num-2 ,1),current_page_num)) + \
                 list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))
    #加上页码省略标记
    if pages_range[0]-1 >=2:
        pages_range.insert(0,'...')
    if paginator.num_pages - pages_range[-1]>=2:
        pages_range.append('...')
    #加上首页尾页
    if pages_range[0]!=1:
        pages_range.insert(0,1)
    if pages_range[-1] != paginator.num_pages:
        pages_range.append(paginator.num_pages)

    content = {}
    content['movies'] = page_of_movies.object_list
    content['page_of_movies'] = page_of_movies
    content['movie_types'] = movie_type.objects.all()
    content['pages_range'] = pages_range
    return render_to_response('movies_list.html',content)

def movie_detail(request,movie_pk):
    content = {}
    content['movie'] = get_object_or_404(movie,pk=movie_pk)
    return render(request,'movie_detail.html',content)

def movie_type_list(request,movie_type_pk):
    page_num = request.GET.get('page',1)#获取url的页面需求(GET参数)
    movies_type = get_object_or_404(movie_type,pk=movie_type_pk)
    movie_class_list = movie.objects.filter(type_name=movies_type)
    paginator = Paginator(movie_class_list,EVERYPAGE_MOVIES_NUM)#进行分页
    page_of_movies = paginator.get_page(page_num)#django考虑到的转换页面函数
    current_page_num = page_of_movies.number#获取当前页码
    #获取当前页码前后各两页
    pages_range = list(range(max(current_page_num-2 ,1),current_page_num)) + \
                 list(range(current_page_num,min(current_page_num+2,paginator.num_pages)+1))
    #加上页码省略标记
    if pages_range[0]-1 >=2:
        pages_range.insert(0,'...')
    if paginator.num_pages - pages_range[-1]>=2:
        pages_range.append('...')
    #加上首页尾页
    if pages_range[0]!=1:
        pages_range.insert(0,1)
    if pages_range[-1] != paginator.num_pages:
        pages_range.append(paginator.num_pages)


    content = {}
    content['page_of_movies'] = page_of_movies
    content['pages_range'] = pages_range
    content['movie_type'] = movies_type
    content['movies'] = page_of_movies.object_list
    content['movie_types'] = movie_type.objects.all()
    return render_to_response('movie_type_list.html',content)