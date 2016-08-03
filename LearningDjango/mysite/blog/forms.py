#! /usr/bin/env python3
# coding:utf-8

from django import forms
from .models import Comment

# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False, widget=forms.Textarea)

#美化表单

class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class": "","placeholder":"please input your name"}),)
	email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"your email",}),)
	to = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"email that you sent",}),)
	comments = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
	name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"","placeholder":"please input your name"}),)
	body = forms.CharField(required=False,widget=forms.Textarea)
	
	class Meta:    """指定一些 Meta 选项以改变 form 被渲染后的样式"""
		model = Comment 
		fields = ('name','body')
