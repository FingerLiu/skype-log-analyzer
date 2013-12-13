#-*-encoding:UTF-8-*-
import jieba
import sky_extracter_UTF8  
def create_dic():
	in_file=open("skype.log",'rU')
	out_file=open("skypedic.txt",'a')
	try:	
		for line in file_in:
			line=line.rstrip()
			line=unicode(line,'utf8')
			if line:
				save_words_to_dic(line,out_file); 
	except Exception as err:
		print(err)
	finally:
		in_file.close()
		out_file.close()
	#用结巴分词
	#将分出的词加入程序专用字典
	#去重
def save_words_to_dic(line,out_file):
	chart_info=skype_extracter_UTF8.get_chart_info(line)
	words=jieba.cut(chart_info,cut_all=False)
	for word in words:
		if dic_filter(word):
			#输出到字典
			out_file.write(word + '\n')
def dic_filter(word):
	return True;