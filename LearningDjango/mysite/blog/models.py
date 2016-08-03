#coding:utf-8

from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

class Post(models.Model):
	STATUS_CHOICE =(('draft','Draft'),('published',"Published"),)


	title =models.CharField(max_length=250)   
	#文章标题，CharField 表示对应数据库中表的列是用来存字符串的,

	slug = models.SlugField(max_length=250,unique_for_date="published") 
	

	author = models.ForeignKey(User,related_name="blog_posts")

	body = models.TextField()
	#文章正文，TextField 用来存储大文本字符

	published = models.DateTimeField(default=timezone.now)

	created = models.DateTimeField(auto_now_add=True)
	#文章创建时间，DateTimeField用于存储时间，设定auto_now_add参数为真，则在文章被创建时会自动添加创建时间
	
	updated = models.DateTimeField(auto_now=True)
	#文章最后一次编辑时间，auto_now=True表示每次修改文章时自动添加修改的时间

	status = models.CharField(max_length=10,choices=STATUS_CHOICE, default='draft')
	#TATUS_CHOICES，field 的 choices 参数需要的值，choices选项会使该field在被渲染成form时被
	#渲染为一个select组件，这里我定义了两个状态，一个是Draft（草稿），一个是Published（已发布），
	#select组件会有两个选项：Draft 和 Published。但是存储在数据库中的值分别是'd'和'p'，这就是 choices的作用。


	class Meta:     
		ordering = ('-published',) 
		#Meta 包含一系列选项，这里的 ordering 表示排序，- 号表示逆序

	def __str__ (self):   #主要用于交互解释器显示表示该类的字符串
		return self.title

#优化URL

	def get_absolute_url(self):
		return reverse('blog:post_detail', args=[self.published.year, self.published.strftime('%m'), self.published.strftime('%d'), self.slug])

#添加评论

class Comment(models.Model):
	post = models.ForeignKey(Post,related_name='comments')
	name = models.CharField('评论者的名字',max_length=80)
	body = models.TextField('评论内容')
	created = models.DateTimeField('评论发表时间',auto_now_add=True)
	updated = models.DateTimeField('更新发表时间'，auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return "Comment by {0} on {1}".format(self.name,self.post)

