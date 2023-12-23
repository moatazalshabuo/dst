from django.db import models

# Create your models here.

class Courses(models.Model):
    title = models.CharField("اسم الكورس",max_length=50)
    time_start = models.TimeField('موعد بداية المحاضرة')
    time_end = models.TimeField('موعد نهاية المحاضرة')
    hours = models.IntegerField("عدد ساعات")
    cotch = models.CharField('اسم المدرب',max_length=50)
    place_descripe = models.TextField('وصف الموقع')
    place_link = models.CharField('الموقع على الخريطة',max_length=150)
    descripe_course = models.TextField('تفاصيل الكورس')
    image = models.ImageField('الصورة', upload_to='upload/%d/')
    status = models.BooleanField("الحالة",default=True,null=True,blank=True)
    
class Clients(models.Model):
    name = models.CharField("الاسم الرباعي", max_length=150)
    phone_number = models.CharField('رقم الهاتف', max_length=50)
    notes = models.TextField("ملاحظات",blank=True,null=True)
    course = models.ForeignKey(Courses, related_name='coures', on_delete=models.CASCADE)