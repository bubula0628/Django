from django.shortcuts import render
from django.views.decorators import csrf
import mysql.connector


# 接收POST请求数据
def search_post(request):
	conn = mysql.connector.connect(user='root', password='123456', database='hotel_grades', use_unicode=True)
	cursor = conn.cursor()
	ctx ={}
	if request.POST:
		res=request.POST['q']
		sql="SELECT * FROM grades WHERE hotel=%s"
		cursor.execute(sql,(res,))
		results = cursor.fetchall()
		results=results[0]
		grade=results[0]
		data=results[1]
		image=results[2]
		ctx['rlt1'] = "酒店名："+str(grade)
		ctx['rlt2']="分數："+str(data)+"......"
		ctx['rlt3']=str(image)
		cursor.close()
	return render(request, "index.html", ctx)





"""
def search_post(request):
	ctx ={}
	if request.POST:
		res=request.POST['q']
		ctx['rlt1'] = str(res)
		ctx['rlt2']="评论："+"......"
	return render(request, "index.html", ctx)
"""