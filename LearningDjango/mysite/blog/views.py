
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from .forms import EmailPostForm, CommentForm
from .models import Post



# django的分页类

def post_list(request):
	object_list = Post.objects.filter(status="published") #获取已经发表的文章
	paginator = Paginator(object_list,1)  #获取分页的对象
	page = request.GET.get('page')     #从http请求中获取用户请求的当前页
	 
	try:
		current_page = paginator.page(page)  #根据页码号获取第几页的数据
		posts = current_page.object_list
	except PageNotAnInteger:			#异常处理，如果用户传递的page值不是整数，则把第一页的值返回给他		
		current_page = paginator.page(1)
		posts = current_page.object_list   #把当前页传给posts
	except EmptyPage:						#如果用户传递的 page 值是一个空值，
		current_page = paginator.page(paginator.num_pages)    #返回最后一页
		posts = current_page.object_list

	return render(request,'blog/post/list.html',{"posts":posts,"page":current_page})

# def post_detail(requst,post_id):
# 	post = get_object_or_404(Post,id = post_id)
# 	return render(requst,'blog/post/detail.html',{"post":post,"post_id":post_id})


# 优化URL

def post_detail(request, year, month, day, post):    #以前的参数是`post_id`，这里修改为现状
    #post = get_object_or_404(Post, id=post_id)      #原来是通过`id`从数据库中读取相应的文章，现在不用这种方式，把这句话注释或者删除，改为用下面的方式。
    post = get_object_or_404(Post, slug=post, status="published", published__year=year, published__month=month, published__day=day)
    comments = post.comments.filter(active=True)

    if request.method =='GET':
    	comment_form = CommentForm()

    if request.method == 'POST':
    	comment_form = CommentForm(data=request.POST)     #根据 POST 过来的数据构建一个表单
    	if comment_form.is_valid():     #数据验证合法（form.is_valid）
    		new_comment = comment_form.save(commit=False)
    		new_comment.post = post
    		new_comment.save()

    return render(request, 'blog/post/detail.html', {"post":post,"comments":comments,"comment_form":comment_form,})    #因为没有`post_id`，所以也不向模板传那个值了。

#分享文章 ,,邮件

def post_share(request,post_id):
	post = get_object_or_404(Post,id=post_id,status="published")
	sent = False

	if request.method == "GET":
		form = EmailPostForm()

	if request.method == "POST":
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			post_url = request.build_absolute_uri(post.get_absolute_url())
			subject = "{0} ({1}) 推荐你阅读 '{2}'".format(cd['name'],cd['email'],post.title)
			message = "文章 '{0}' 网址 {1}\n\n{2} 的评论: {3}".format(post.title,post_url,cd['name'],cd['comments'])
			send_mail(subject,message,"515017605@qq.com",[cd['to']])
			sent = True 

	return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent},)