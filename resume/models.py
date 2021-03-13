from datetime import datetime

from django.db import models


class Resume(models.Model):
    name=models.CharField(max_length=200,verbose_name='نام من')
    speciality=models.CharField(max_length=300,verbose_name="تخصص")
    about=models.TextField(verbose_name='درباره من')
    phone=models.CharField(max_length=100,verbose_name='موبایل')
    email=models.EmailField(verbose_name='ایمیل')
    logo=models.ImageField(upload_to='logo',verbose_name='لوگو',blank=True)
    instagram=models.CharField(max_length=300,verbose_name='اینستاگرام')
    twitter=models.CharField(max_length=300,verbose_name='توییتز')
    facebook=models.CharField(max_length=300,verbose_name='فیسبوک')


    def __str__(self):
        return self.name

class Experience(models.Model):
    when=models.DateTimeField(default=datetime.now,verbose_name='چه موقع')
    job=models.CharField(max_length=300,verbose_name='چه شغلی')
    how=models.CharField(max_length=300,verbose_name= 'کجا یا چگونه',blank=True)
    description=models.TextField(verbose_name='درباره تجربتون')


    def __str__(self):
        return self.job

class Projects(models.Model):
    name=models.CharField(max_length=200,verbose_name='نام')
    image=models.ImageField(upload_to='projects',verbose_name='عکس پروژه',blank=True)
    link=models.CharField(max_length=500,verbose_name='لینک پروژه',blank=True)
    description=models.TextField(verbose_name='توضیحات')
    forWho=models.CharField(max_length=300,verbose_name='برای چه کسی پروژه را انجام دادید',blank=True)


    def __str__(self):
        return self.name