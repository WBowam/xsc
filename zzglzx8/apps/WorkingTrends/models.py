# -*- coding: utf-8 -*-
from django.db import models
from DjangoUeditor.models import UEditorField

class Tab(models.Model):
	publish=models.BooleanField(u'发布',default=False)
	title=models.CharField(u'题目',max_length=100,blank=False)
	content=UEditorField(u'内容	',height=1000,width=500,default='test',imagePath="uploadimg/",imageManagerPath="imglib",toolbars='biglarge1',options={"elementPathEnabled":True},filePath='upload',blank=True)
	upTime=models.DateTimeField(u'上传时间',auto_now_add=True)
	c=(('zzgl','资助管理'),('qgzx','勤工助学'),('zxdk','助学贷款'),('ylbx','医疗保险'),('bcdc','补偿贷偿'),('other','其他'))
	#c=(('xggg','相关公告'),('gzdt','工作动态'),('zzzc','资助政策'),('bszn','办事指南 '),('zpxx',' 招聘信息'),('zgzxjd','勤工助学基地'),('wdxz','文档下载'),('other','其他'))
	#c1=(('zzgl','资助管理'),('qgzx','勤工助学'),('zxdk','助学贷款'),('ylbx','医疗保险'),('bcdc','补偿贷偿'),('other','其他'))
	category=models.CharField(u'分类',max_length=20,choices=c,default='zzgl')
	visted=models.IntegerField(u'被浏览次数',default=1,editable=False)
	photo=models.ImageField(u'图片',null=True,blank=True,upload_to='upload')
	attachment=models.FileField(u'附件',null=True,blank=True,upload_to='upload')
	
	def __unicode__(self):
		return ("%s--- %s"%(self.title,self.upTime))

	class Meta:
		verbose_name_plural=u'工作动态'
		#app_label=u'助学贷款'
		ordering=['-upTime']