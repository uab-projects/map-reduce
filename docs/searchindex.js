Search.setIndex({envversion:50,filenames:["index","mapreduce","mapreduce.cli","mapreduce.cli.controller","mapreduce.cli.controller.main","mapreduce.cli.controller.text_counter","mapreduce.core","mapreduce.core.listener","mapreduce.core.log","mapreduce.core.pool","mapreduce.core.splitter","mapreduce.core.trigger","mapreduce.test","modules"],objects:{"":{mapreduce:[1,0,0,"-"]},"mapreduce.cli":{controller:[3,0,0,"-"]},"mapreduce.cli.controller":{main:[4,0,0,"-"],text_counter:[5,0,0,"-"]},"mapreduce.cli.controller.main":{constants:[4,0,0,"-"],controller:[4,0,0,"-"],parser:[4,0,0,"-"]},"mapreduce.cli.controller.main.constants":{LOG_DEFAULT:[4,1,1,""]},"mapreduce.cli.controller.main.controller":{controller:[4,2,1,""]},"mapreduce.cli.controller.main.parser":{create_parser:[4,2,1,""],create_parser_options:[4,2,1,""],evalTF:[4,2,1,""]},"mapreduce.cli.controller.text_counter":{constant:[5,0,0,"-"],controller:[5,0,0,"-"],create_full_parser:[5,2,1,""],parser:[5,0,0,"-"],validator:[5,0,0,"-"]},"mapreduce.cli.controller.text_counter.constant":{READ_SIZE_DEFAULT:[5,1,1,""],READ_SIZE_MIN:[5,1,1,""],REDUCE_SIZE_DEFAULT:[5,1,1,""],REDUCE_SIZE_MIN:[5,1,1,""],SPLIT_SIZE_DEFAULT:[5,1,1,""],SPLIT_SIZE_MIN:[5,1,1,""]},"mapreduce.cli.controller.text_counter.controller":{controller:[5,2,1,""],show_result:[5,2,1,""]},"mapreduce.cli.controller.text_counter.parser":{create_full_parser:[5,2,1,""],create_parser:[5,2,1,""],create_parser_options:[5,2,1,""]},"mapreduce.cli.controller.text_counter.validator":{integer_greater_than_1:[5,2,1,""],positive_integer:[5,2,1,""],positive_integer_or_zero:[5,2,1,""]},"mapreduce.core":{listener:[7,0,0,"-"],log:[8,0,0,"-"],pool:[9,0,0,"-"],splitter:[10,0,0,"-"],trigger:[11,0,0,"-"]},"mapreduce.core.listener":{async_task:[7,0,0,"-"],done:[7,0,0,"-"]},"mapreduce.core.listener.async_task":{AsyncTask:[7,3,1,""]},"mapreduce.core.listener.done":{DoneListener:[7,3,1,""]},"mapreduce.core.log":{CONFIG_FILE:[8,1,1,""],init:[8,2,1,""]},"mapreduce.core.pool":{basic:[9,0,0,"-"],map:[9,0,0,"-"],reduce:[9,0,0,"-"]},"mapreduce.core.pool.basic":{BasicPool:[9,3,1,""],LOGGER:[9,1,1,""]},"mapreduce.core.pool.basic.BasicPool":{add:[9,4,1,""],close:[9,4,1,""],completed:[9,5,1,""],failed:[9,5,1,""],join:[9,4,1,""],scheduled:[9,5,1,""],succeeded:[9,5,1,""],task:[9,5,1,""]},"mapreduce.core.pool.map":{LOGGER:[9,1,1,""],MapPool:[9,3,1,""]},"mapreduce.core.pool.reduce":{DEFAULT_MIN_GROUP_SIZE:[9,1,1,""],LOGGER:[9,1,1,""],RedPool:[9,3,1,""]},"mapreduce.core.pool.reduce.RedPool":{add:[9,4,1,""],group_size:[9,5,1,""],on_done:[9,5,1,""]},"mapreduce.core.splitter":{"abstract":[10,0,0,"-"],LetterFileSplitter:[10,3,1,""],WordFileSplitter:[10,3,1,""],file:[10,0,0,"-"],letterfile:[10,0,0,"-"],wordfile:[10,0,0,"-"]},"mapreduce.core.splitter.abstract":{AbstractSplitter:[10,3,1,""],SPLIT_SIZE_DEFAULT:[10,1,1,""]},"mapreduce.core.splitter.abstract.AbstractSplitter":{pool:[10,5,1,""],read:[10,4,1,""],split_size:[10,5,1,""]},"mapreduce.core.splitter.file":{DEFAULT_ENCODING:[10,1,1,""],DEFAULT_READ_SIZE:[10,1,1,""],FileSplitter:[10,3,1,""]},"mapreduce.core.splitter.file.FileSplitter":{read:[10,4,1,""],read_size:[10,5,1,""]},"mapreduce.core.splitter.letterfile":{LetterFileSplitter:[10,3,1,""]},"mapreduce.core.splitter.wordfile":{WordFileSplitter:[10,3,1,""]},"mapreduce.core.trigger":{close:[11,0,0,"-"]},"mapreduce.core.trigger.close":{CloseTrigger:[11,3,1,""]},"mapreduce.core.trigger.close.CloseTrigger":{close:[11,4,1,""],closed:[11,5,1,""]},"mapreduce.test":{map:[12,0,0,"-"],reduce:[12,0,0,"-"]},"mapreduce.test.map":{LOGGER:[12,1,1,""],simple_test:[12,2,1,""]},"mapreduce.test.reduce":{LOGGER:[12,1,1,""],join_dicts:[12,2,1,""],simple_test:[12,2,1,""]},mapreduce:{__main__:[1,0,0,"-"],cli:[2,0,0,"-"],core:[6,0,0,"-"],test:[12,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","data","Python data"],"2":["py","function","Python function"],"3":["py","class","Python class"],"4":["py","method","Python method"],"5":["py","attribute","Python attribute"]},objtypes:{"0":"py:module","1":"py:data","2":"py:function","3":"py:class","4":"py:method","5":"py:attribute"},terms:{"abstract":[1,6,9],"boolean":11,"case":[4,7,10],"class":[7,9,10,11],"default":[4,5,8,10,11],"final":9,"function":[7,9,12],"import":9,"int":[5,9,10],"new":9,"return":[4,5,9,10,11,12],"true":[4,11],"while":10,__main__:0,_close:11,_fail:9,_filenam:10,_group_siz:9,_nextstep:9,_on_don:9,_pool:[9,10],_read_siz:10,_readi:9,_schedul:9,_split_siz:10,_succeed:9,_task:9,_user_on_don:9,abl:[4,7,9,10,11],abstractpool:10,abstractsplitt:10,accept:[9,11],accord:7,add:[4,5,9],after:11,again:9,algorithm:1,all:[7,9,12],allow:[7,8,9,11],along:10,alreadi:9,also:11,alter:11,alwai:11,amount:5,ani:4,appli:[1,9],applic:12,appropi:7,arg:[4,5,9,12],argpars:4,argument:[4,5,9],argumentpars:[4,5],arriv:9,assertexcept:10,async_task:[1,6],asynchron:7,asynctask:[7,9],attribut:[9,10,11],autom:9,base:[7,9,10,11],basic:[1,6],basicpool:9,been:[5,7,9,11],befor:9,behaviour:[7,11],big:9,bool:[4,5,11],buffer:[9,10],call:[7,9],callback:7,can:[4,5,7,9,11],charact:[5,10],check:[5,9,10],choos:[1,5],cli:1,close:[1,6,9],closetrigg:[9,11],come:[9,11],complet:[7,9],compon:12,concret:[10,11],conf:8,config:8,config_file:8,configur:8,constant:[1,2,3],contain:[4,5,10,11],content:0,continu:7,control:[1,2],converg:12,convert:[4,5],core:1,count:5,counter:5,cpu:9,creat:[4,5,9,10],create_full_pars:5,create_pars:[4,5],create_parser_opt:[4,5],custom:9,data:[9,10,11],deal:10,default_encoding:10,default_min_group_size:9,default_read_size:10,defin:[3,4,5,7,9,10,11],depend:7,desir:5,determin:4,develop:7,dict:[5,12],dictionari:[5,12],disk:10,don:7,done:[1,6],donelisten:[7,9,10],dynam:[9,11],each:10,easi:9,either:7,element:9,enabl:8,encod:10,end:7,enough:[9,10],entri:[1,9],environ:7,equal:12,error:[4,7],evaltf:4,event:[7,9,11],eventual:9,everi:10,except:5,exception:4,exchang:9,execut:[3,5,7,9,11],exist:10,extern:[7,9,11],fail:9,fals:[4,5],feedback:9,file:[1,5,6,8],filenam:[5,10],filenotfounderror:10,filesplitt:10,fill:[4,5],finish:[7,9],first:10,found:10,from:[5,9,10,11],full:5,further:9,gener:[9,10],given:[3,4,5],goe:10,greater:5,group:9,group_siz:9,guid:5,had:7,handl:[3,7,9,10,11],have:[7,9],help:[9,12],here:[7,10,11],ignor:9,implement:[7,9,10],impli:9,includ:9,incom:[9,11],independ:4,index:0,inherit:7,init:8,initial:8,inmedi:9,input:[1,9],integ:5,integer_greater_than_1:5,interfac:[4,5,7,10],item:[5,9,12],job:7,join:[9,12],join_dict:12,just:[5,9,10],kei:12,kind:9,know:[7,9,11],kwarg:9,last:5,less:5,letter:[4,5,10],letterfil:[1,6],letterfilesplitt:10,level:4,librari:[4,9,11],like:10,line:10,list:9,listen:[1,6],littl:12,log:[1,4,6],log_default:4,logger:[8,9,12],lowercas:4,main:[1,2,3],make:9,manual:[9,11],mappool:9,mapreduc:0,mean:[4,7,9,11],merg:12,method:[9,11],minimum:[5,9,10],model:[7,9],modifi:7,modul:0,more:[9,10,11],most:[9,10],much:9,multiprocess:[9,11],must:7,name:11,need:[7,9],next:[9,10],nextstep:9,no_out:5,none:[5,10],noth:10,notifi:7,number:[5,9,10],object:[7,9,10,11,12],obviou:9,offici:5,on_don:9,onc:[3,9],once:9,onli:9,open:10,oper:[9,12],option:5,orient:9,other:9,otherwis:4,output:1,packag:0,page:0,paradigm:[3,4,9,10],parallel:9,parser:[1,2,3],pass:9,pend:7,perform:[3,4,7,9,10,12],piec:[9,10],point:1,pool:[1,6],posit:5,positive_integ:5,positive_integer_or_zero:5,prepar:9,present:9,prevent:9,print:5,problem:10,process:[7,9,11],program:10,proper:9,properti:9,provid:7,python:[4,8,9],rais:[4,5,10],read:[5,10],read_siz:10,read_size_default:5,read_size_min:5,reader:10,readi:[7,9],real:9,receiv:[9,11,12],redpool:9,reduce_size_default:5,reduce_size_min:5,requir:[4,5],result:[5,9],run:[7,9],same:12,save:10,schedul:[7,9],script:12,search:0,see:[4,10],select:5,self:9,send:[9,10],sent:[9,10],seri:11,set:[4,9,11],show:[5,7],show_result:5,simple_test:12,size:[5,9,10],softwar:[1,3,5,10],sourc:[4,5,7,8,9,10,11,12],specifi:[5,10,11],split:[5,10],split_siz:10,split_size_default:[5,10],split_size_min:5,splitter:[1,6],stage:9,start:[7,9],statu:11,step:[9,10],stop:9,stope:9,store:9,str:[4,5,8,10],string:[4,5],structur:10,subject:5,submodul:0,subpackag:0,succeed:9,succesfulli:7,successfulli:9,sum:[9,12],system:8,take:[9,10],task:[3,4,5,7,9],teacher:5,tell:[9,11],test:1,text:[5,10],text_count:[1,2,3],than:5,thei:[9,10],them:[7,9,10],therefor:[7,9],thi:[5,7,9,10,11],those:9,thread:9,through:9,time:10,togeth:9,too:9,total:9,transfer:9,trigger:[1,6,7,9],until:[9,10],uppercas:4,utf:10,valid:[1,2,3],valu:[4,12],valueerror:5,wai:[7,9],wait:9,want:11,were:7,what:[7,9],when:[5,7,9,10,11],where:[7,10],who:7,whole:10,without:7,word:[5,10],wordfil:[1,6],wordfilesplitt:10,work:9,workflow:[5,9],would:7,you:11},titles:["Welcome to Map Reduce&#8217;s documentation!","mapreduce package","mapreduce.cli package","mapreduce.cli.controller package","mapreduce.cli.controller.main package","mapreduce.cli.controller.text_counter package","mapreduce.core package","mapreduce.core.listener package","mapreduce.core.log package","mapreduce.core.pool package","mapreduce.core.splitter package","mapreduce.core.trigger package","mapreduce.test package","mapreduce"],titleterms:{"abstract":10,__main__:1,async_task:7,basic:9,cli:[2,3,4,5],close:11,constant:[4,5],content:[1,2,3,4,5,6,7,8,9,10,11,12],control:[3,4,5],core:[6,7,8,9,10,11],document:0,done:7,file:10,indice:0,letterfil:10,listen:7,log:8,main:4,map:[0,9,12],mapreduc:[1,2,3,4,5,6,7,8,9,10,11,12,13],modul:[1,2,3,4,5,6,7,8,9,10,11,12],packag:[1,2,3,4,5,6,7,8,9,10,11,12],parser:[4,5],pool:9,reduc:[0,9,12],splitter:10,submodul:[1,4,5,7,9,10,11,12],subpackag:[1,2,3,6],tabl:0,test:12,text_count:5,trigger:11,valid:5,welcom:0,wordfil:10}})