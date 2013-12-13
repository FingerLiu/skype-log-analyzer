#-*- coding :UTF-8-*-
import jieba
from apptypes import skypeid_skypename_dic,id_nicknames_dic ,skypename_skypeid_dic
#import predictionio
#client = predictionio.#client(appkey="KaJwG2eUkmt4iTjiAHcw56hPQyW8FbeWKD5YfQAK7OldYSuvv2Sk0Wqxqa7XPkTz")
print 'Creating users...\n'
cnt=0
for user_id in skypeid_skypename_dic:
	#clien.create_user(user_id)
	cnt=cnt+1
	print 'user '+str(user_id)+' created'
print str(cnt)+' users created.'
print 'Creating items...\n'
cnt=0
for item_id in id_nicknames_dic:
	#client.create_item(item_id, ('guys',))
	cnt=cnt+1
	print 'item '+str(item_id)+' created'
print str(cnt)+' items created .'

def scanner(filename,linehandler,encoding):
	file_object=open(filename,'rU')
	try:	
		for line in file_object:
			line=line.rstrip()
			line=unicode(line,encoding)
			if line:
				linehandler(line); 
	except Exception as err:
		print(err)
	finally:
		file_object.close()

def get_skype_name(skypeline):
	if(2 < len(skypeline.split())):
		#print skypeline.split()[2].rstrip(':')
		return skypeline.split()[2].rstrip(':') 

def get_skype_id(name,skypename_skypeid_dic):
	if(skypename_skypeid_dic.has_key(name)==False):
		skypename_skypeid_dic[name]=len(skypename_skypeid_dic)+1
		skypeid_skypename_dic[len(skypeid_skypename_dic)+1]=name
		#clien.create_user(len(skypeid_skypename_dic))
		print 'user '+name+' not found during read skype log. adding with key '+str(len(skypeid_skypename_dic)+1)
	user_id=skypename_skypeid_dic[name]
	return user_id

def get_chat_info(skypeline):
#need to change the rindex method into thirdindexof
	skypeline=skypeline[skypeline.rindex(':')+1:]
	#print skypeline
	return skypeline

#considering of effectivify sub returns after the firts talked nick name found
#can not handle conditions contain more than 1 id .
def get_talked_id(skypeline,id_nicknames_dic):
	for id in id_nicknames_dic:
		for nick_name in id_nicknames_dic[id]:
			if(nick_name in skypeline):
				return id; 
	return 0

def save_pair_to_predectionio(skypeline):
	user_id=get_skype_id(get_skype_name(skypeline),skypename_skypeid_dic)
	item_id=get_talked_id(get_chat_info(skypeline),id_nicknames_dic)
	if (item_id):
		print 'user_id : '+str(user_id)
		print 'item_id : '+str(item_id)
	#client.identify(user_id)
    #client.record_action_on_item("like", item_id )

def get_talked_word(skypeline):
	word_list=jieba.cut(skypeline,cut_all=False)
	return word_list
def save_words_to_predectionio(skypeline):
	user_id=get_skype_id(get_skype_name(skypeline),skypename_skypeid_dic)
	word_list=jieba.cut(get_chat_info(skypeline),cut_all=False)
	client.identify(user_id)
	for word in word_list:
		client.record_action_on_item("like",word)
		

#def extract_key_value(src,key_checker,value_checker)
scanner("skype.log", save_pair_to_predectionio,'utf8')

#for test
for key in skypeid_skypename_dic:
	print str(key)+" : "+skypeid_skypename_dic[key]

#client.close()

