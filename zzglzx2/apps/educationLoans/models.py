# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField

class EducationLoans(models.Model):
	title=UEditorField(u'题目	',height=50,width=500,blank=False,toolbars='mini')
	Content=UEditorField(u'内容	',height=1000,width=400,default='test',imagePath="uploadimg/",imageManagerPath="imglib",toolbars='large',options={"elementPathEnabled":True},filePath='upload',blank=True)
	upTime=models.DateTimeField(auto_now_add=True)
	c=(('zzgl','资助管理'),('qgzx','勤工助学'),('zxdk','助学贷款'),('ylbx','医疗保险'),('bcdc','补偿贷偿'),('other','其他'))
	category=models.CharField(max_length=20,choices=c,default='zzgl')
	visted=models.IntegerField(default=1,editable=False)
	photo=models.ImageField(null=True,blank=True,upload_to='upload')
	attachment=models.FileField(null=True,blank=True,upload_to='upload')
	
	def __unicode__(self):
		return ("%s--- %s"%(self.title,self.upTime))

	class Meta:
		verbose_name=u'助学贷款'