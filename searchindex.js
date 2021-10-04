Search.setIndex({docnames:["api/minos","api/minos.api_gateway","api/minos.api_gateway.discovery","api/minos.api_gateway.discovery.cli","api/minos.api_gateway.discovery.database","api/minos.api_gateway.discovery.database.client","api/minos.api_gateway.discovery.domain","api/minos.api_gateway.discovery.domain.endpoint","api/minos.api_gateway.discovery.domain.exceptions","api/minos.api_gateway.discovery.domain.microservice","api/minos.api_gateway.discovery.exceptions","api/minos.api_gateway.discovery.health_status","api/minos.api_gateway.discovery.health_status.checkers","api/minos.api_gateway.discovery.health_status.services","api/minos.api_gateway.discovery.launchers","api/minos.api_gateway.discovery.service","api/minos.api_gateway.discovery.views","api/minos.api_gateway.discovery.views.endpoint","api/minos.api_gateway.discovery.views.microservice","api/minos.api_gateway.discovery.views.router","authors","history","index","readme","runthetests","usage"],envversion:{"sphinx.domains.c":2,"sphinx.domains.changeset":1,"sphinx.domains.citation":1,"sphinx.domains.cpp":4,"sphinx.domains.index":1,"sphinx.domains.javascript":2,"sphinx.domains.math":2,"sphinx.domains.python":3,"sphinx.domains.rst":2,"sphinx.domains.std":2,"sphinx.ext.viewcode":1,sphinx:56},filenames:["api/minos.rst","api/minos.api_gateway.rst","api/minos.api_gateway.discovery.rst","api/minos.api_gateway.discovery.cli.rst","api/minos.api_gateway.discovery.database.rst","api/minos.api_gateway.discovery.database.client.rst","api/minos.api_gateway.discovery.domain.rst","api/minos.api_gateway.discovery.domain.endpoint.rst","api/minos.api_gateway.discovery.domain.exceptions.rst","api/minos.api_gateway.discovery.domain.microservice.rst","api/minos.api_gateway.discovery.exceptions.rst","api/minos.api_gateway.discovery.health_status.rst","api/minos.api_gateway.discovery.health_status.checkers.rst","api/minos.api_gateway.discovery.health_status.services.rst","api/minos.api_gateway.discovery.launchers.rst","api/minos.api_gateway.discovery.service.rst","api/minos.api_gateway.discovery.views.rst","api/minos.api_gateway.discovery.views.endpoint.rst","api/minos.api_gateway.discovery.views.microservice.rst","api/minos.api_gateway.discovery.views.router.rst","authors.rst","history.rst","index.rst","readme.rst","runthetests.rst","usage.rst"],objects:{"minos.api_gateway":{discovery:[2,0,0,"-"]},"minos.api_gateway.discovery":{cli:[3,0,0,"-"],database:[4,0,0,"-"],domain:[6,0,0,"-"],exceptions:[10,0,0,"-"],health_status:[11,0,0,"-"],launchers:[14,0,0,"-"],service:[15,0,0,"-"],views:[16,0,0,"-"]},"minos.api_gateway.discovery.cli":{main:[3,1,1,""],start:[3,1,1,""],status:[3,1,1,""],stop:[3,1,1,""]},"minos.api_gateway.discovery.database":{client:[5,0,0,"-"]},"minos.api_gateway.discovery.database.client":{MinosRedisClient:[5,2,1,""]},"minos.api_gateway.discovery.database.client.MinosRedisClient":{__init__:[5,3,1,""],address:[5,4,1,""],delete_data:[5,3,1,""],flush_db:[5,3,1,""],get_data:[5,3,1,""],get_redis_connection:[5,3,1,""],password:[5,4,1,""],ping:[5,3,1,""],port:[5,4,1,""],redis:[5,4,1,""],set_data:[5,3,1,""],update_data:[5,3,1,""]},"minos.api_gateway.discovery.domain":{endpoint:[7,0,0,"-"],exceptions:[8,0,0,"-"],microservice:[9,0,0,"-"]},"minos.api_gateway.discovery.domain.endpoint":{ConcreteEndpoint:[7,2,1,""],Endpoint:[7,2,1,""],GenericEndpoint:[7,2,1,""],PathPart:[7,2,1,""]},"minos.api_gateway.discovery.domain.endpoint.ConcreteEndpoint":{__init__:[7,3,1,""],path_as_str:[7,5,1,""]},"minos.api_gateway.discovery.domain.endpoint.Endpoint":{__init__:[7,3,1,""],path_as_str:[7,5,1,""]},"minos.api_gateway.discovery.domain.endpoint.GenericEndpoint":{__init__:[7,3,1,""],load_by_key:[7,3,1,""],matches:[7,3,1,""],path_as_str:[7,5,1,""]},"minos.api_gateway.discovery.domain.endpoint.PathPart":{__init__:[7,3,1,""]},"minos.api_gateway.discovery.domain.exceptions":{CannotInstantiateException:[8,6,1,""]},"minos.api_gateway.discovery.domain.exceptions.CannotInstantiateException":{__init__:[8,3,1,""],args:[8,4,1,""],with_traceback:[8,3,1,""]},"minos.api_gateway.discovery.domain.microservice":{Microservice:[9,2,1,""]},"minos.api_gateway.discovery.domain.microservice.Microservice":{"delete":[9,3,1,""],__init__:[9,3,1,""],find_by_endpoint:[9,3,1,""],load:[9,3,1,""],load_by_endpoint:[9,3,1,""],save:[9,3,1,""],to_json:[9,3,1,""]},"minos.api_gateway.discovery.exceptions":{NotFoundException:[10,6,1,""]},"minos.api_gateway.discovery.exceptions.NotFoundException":{__init__:[10,3,1,""],args:[10,4,1,""],with_traceback:[10,3,1,""]},"minos.api_gateway.discovery.health_status":{checkers:[12,0,0,"-"],services:[13,0,0,"-"]},"minos.api_gateway.discovery.health_status.checkers":{HealthStatusChecker:[12,2,1,""]},"minos.api_gateway.discovery.health_status.checkers.HealthStatusChecker":{__init__:[12,3,1,""],check:[12,3,1,""]},"minos.api_gateway.discovery.health_status.services":{HealthStatusCheckerService:[13,2,1,""]},"minos.api_gateway.discovery.health_status.services.HealthStatusCheckerService":{__init__:[13,3,1,""],callback:[13,3,1,""],context:[13,5,1,""],delay:[13,4,1,""],interval:[13,4,1,""],set_loop:[13,3,1,""],start:[13,3,1,""],start_event:[13,5,1,""],stop:[13,3,1,""]},"minos.api_gateway.discovery.launchers":{EntrypointLauncher:[14,2,1,""]},"minos.api_gateway.discovery.launchers.EntrypointLauncher":{__init__:[14,3,1,""],entrypoint:[14,4,1,""],graceful_shutdown:[14,3,1,""],launch:[14,3,1,""],loop:[14,4,1,""]},"minos.api_gateway.discovery.service":{DiscoveryService:[15,2,1,""]},"minos.api_gateway.discovery.service.DiscoveryService":{__init__:[15,3,1,""],context:[15,5,1,""],create_application:[15,3,1,""],create_site:[15,3,1,""],set_loop:[15,3,1,""],start:[15,3,1,""],start_event:[15,5,1,""],stop:[15,3,1,""]},"minos.api_gateway.discovery.views":{endpoint:[17,0,0,"-"],microservice:[18,0,0,"-"],router:[19,0,0,"-"]},"minos.api_gateway.discovery.views.endpoint":{EndpointView:[17,2,1,""]},"minos.api_gateway.discovery.views.endpoint.EndpointView":{__init__:[17,3,1,""],get:[17,3,1,""],request:[17,5,1,""]},"minos.api_gateway.discovery.views.microservice":{MicroserviceView:[18,2,1,""]},"minos.api_gateway.discovery.views.microservice.MicroserviceView":{"delete":[18,3,1,""],__init__:[18,3,1,""],get_body:[18,3,1,""],post:[18,3,1,""],request:[18,5,1,""]}},objnames:{"0":["py","module","Python module"],"1":["py","function","Python function"],"2":["py","class","Python class"],"3":["py","method","Python method"],"4":["py","attribute","Python attribute"],"5":["py","property","Python property"],"6":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:function","2":"py:class","3":"py:method","4":"py:attribute","5":"py:property","6":"py:exception"},terms:{"0":[13,22],"04":22,"05":22,"06":22,"07":22,"08":22,"1":22,"10":22,"14":22,"19":22,"2":22,"2021":22,"21":22,"27":22,"3":22,"4":22,"5":[15,22],"byte":[7,9],"class":[5,7,8,9,12,13,14,15,17,18],"default":23,"float":13,"function":3,"import":25,"new":[7,14,23],"return":[5,7,8,9,10,12,13,14,15,17,18],"true":9,A:[5,7,9],If:23,In:[23,24],No:23,The:[5,9,23],To:25,__init__:[5,7,8,9,10,12,13,14,15,17,18],__main__:21,__traceback__:[8,10],abl:23,abstracteventloop:14,accord:5,ad:21,add:21,address:[5,9,15],aiohttp:[15,17,18],aiohttpservic:15,aiomisc:[13,15],all:23,alreadi:12,alt:23,an:[9,10,14],andrea:20,ani:23,anyth:[9,12,13,14],api:[5,23],applic:15,appropri:23,ar:23,architectur:23,arg:[8,10],argumentinfo:3,async:[5,9,12,13,15,17,18],asynchron:23,asyncio:[13,15],attribut:5,audreyr:23,auto:21,avail:23,bar:5,base:[5,7,8,9,10,12,13,14,15,17,18],been:10,befor:23,being:23,bool:7,branch:23,bt:9,bug:[21,23],build:7,call:13,callback:13,can:23,cannot:8,cannotinstantiateexcept:8,cart:5,categoris:23,cd:[23,24],chang:23,check:[12,21,23],checker:[2,11],clariteia:[20,23],classmethod:[7,9],cli:[1,2,21],client:[2,4,9],code:21,codifi:7,com:[20,23],commit:23,common:25,compos:[23,24],con:23,concret:9,concrete_endpoint:[7,9],concreteendpoint:[7,9],config:[5,12,13,15],configur:5,conn_valu:5,connect:[5,21],consid:23,context:[13,15],contributor:22,cookiecutt:23,core:23,cqr:23,creat:14,create_appl:15,create_sit:15,creation:23,credit:22,custom:5,d:[23,24],data:5,databas:[1,2,9],datasourc:10,db_client:9,delai:13,delet:[9,18,21],delete_data:5,depend:[23,24],develop:22,directori:[23,24],discover:21,discoveri:[1,22],discoveryperiodichealthcheck:13,discoveryservic:[15,21],docker:[23,24],doe:[9,12,13,14],domain:[1,2,5],driven:23,each:5,easili:23,endpoint:[2,6,9,16,21],endpoint_kei:[7,9],endpointview:17,engin:[23,24],entri:21,entrypoint:14,entrypointlaunch:14,environ:5,err:[13,14],event:[13,15,23],exampl:5,except:[1,2,6,15],execut:14,featur:23,feedback:23,fenchak:20,file:23,file_path:3,fill:23,find:[9,23],find_by_endpoint:9,fix:21,flush_db:5,follow:23,foo:5,forev:14,fork:23,forward:23,found:[10,21,23],framework:23,from:[7,9,23],fulfil:23,garcia:20,gener:7,genericendpoint:7,get:[3,5,17],get_bodi:18,get_data:5,get_redis_connect:5,git:23,github:23,grace:21,graceful_shutdown:14,graceful_stop_timeout:15,gracefulli:14,guid:23,guidelin:23,ha:10,happen:23,have:[23,24],health:[12,21],health_statu:[1,2],healthstatuscheck:12,healthstatuscheckerservic:13,help:23,histori:22,http:23,imag:23,improv:21,index:22,initi:5,instal:[23,24],instanc:[9,14,17,18],instanti:8,instruct:23,integr:21,interfac:21,intern:[13,21,23],interv:13,introduct:22,io:23,ip:5,its:23,itself:5,json:5,keep:14,kei:[5,7,9],known:12,kwarg:[8,10,13],label:23,launch:14,launcher:[1,2],lead:22,leverag:23,librari:[23,24],load:9,load_by_endpoint:9,load_by_kei:7,local:23,lock:[13,15],logic:13,look:23,lookup:5,loop:[13,14,15],made:5,main:3,make:[23,24],manag:23,match:[7,9],matter:23,messag:23,method:[9,12,13,14],microservic:[2,5,6,12,16,21,23,25],microservice_kei:9,microservice_nam:9,microserviceview:18,mino:[21,23,25],minos_microservice_common:25,minosapirout:5,minosrediscli:5,model:3,modif:23,modul:[1,2,4,6,11,16,22],move:[23,24],mucci:20,must:9,name:[5,7,9],namespac:22,none:[9,12,13,14,15,17,18],noreturn:14,notfoundexcept:10,now:23,object:[3,5,7,9,10,12,14],obtain:5,offici:23,open:23,option:15,order:[5,23,24],ordersminosapirout:5,packag:[1,23],page:22,paramet:[7,9,15],pass:5,password:5,path:7,path_as_str:7,pathpart:7,perform:5,period:[13,21],periodicservic:13,ping:5,pleas:[23,24],poetri:23,point:21,port:[5,9,15],post:18,prado:20,pre:23,previou:23,project:[23,25],properti:[7,13,15,17,18],push:23,py:21,python:23,rais:10,reactiv:23,redi:[5,21],redis_cli:9,redis_host:5,redis_password:5,redis_port:5,refactor:21,refer:23,regard:23,relat:[21,23],report:23,request:[17,18],respons:[5,21],rest:21,router:[2,5,16],run:[14,22],s:[3,21,23],save:9,search:22,section:23,self:[8,10],sergio:20,servic:[1,2,3,11,14,21,23,24],set:[8,10],set_data:5,set_loop:[13,15],shutdown:14,so:23,socksit:15,sourc:[3,5,7,8,9,10,12,13,14,15,17,18,23],specif:5,specifi:5,start:[3,13,15],start_ev:[13,15],statu:[3,5,9,12,21],step:23,stop:[3,13,15,21],store:[5,9],str:[5,7],string:5,structur:21,submodul:1,subscript:21,support:21,sure:[23,24],target:23,tb:[8,10],templat:23,test:22,thi:[5,9,12,13,14,23],timeout:21,to_json:9,type:[5,7,9,12,13,14,15,17,18],typer:3,typic:5,under:23,unsubscript:21,up:24,updat:[5,21],update_data:5,us:[5,23,25],usag:[5,22],valu:5,variabl:5,verb:7,via:5,view:[1,2],vladyslav:20,wa:23,wait:23,we:23,web_app:15,web_runn:15,web_urldispatch:[17,18],well:23,when:10,whether:23,which:[5,23],with_traceback:[8,10],you:[23,24],your:23,yourself:23},titles:["minos namespace","minos.api_gateway namespace","minos.api_gateway.discovery package","minos.api_gateway.discovery.cli module","minos.api_gateway.discovery.database package","minos.api_gateway.discovery.database.client module","minos.api_gateway.discovery.domain package","minos.api_gateway.discovery.domain.endpoint module","minos.api_gateway.discovery.domain.exceptions module","minos.api_gateway.discovery.domain.microservice module","minos.api_gateway.discovery.exceptions module","minos.api_gateway.discovery.health_status package","minos.api_gateway.discovery.health_status.checkers module","minos.api_gateway.discovery.health_status.services module","minos.api_gateway.discovery.launchers module","minos.api_gateway.discovery.service module","minos.api_gateway.discovery.views package","minos.api_gateway.discovery.views.endpoint module","minos.api_gateway.discovery.views.microservice module","minos.api_gateway.discovery.views.router module","Credits","History","Welcome to Minos Microservice Common\u2019s documentation!","Introduction","Run the tests","Usage"],titleterms:{"0":21,"04":21,"05":21,"06":21,"07":21,"08":21,"1":21,"10":21,"14":21,"19":21,"2":21,"2021":21,"21":21,"27":21,"3":21,"4":21,"5":21,an:23,api_gatewai:[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],checker:12,cli:3,client:5,common:22,contribut:23,contributor:20,creat:23,credit:[20,23],databas:[4,5],develop:[20,23],discoveri:[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23],document:[22,23],domain:[6,7,8,9],endpoint:[7,17],environ:23,except:[8,10],health_statu:[11,12,13],histori:21,how:23,indic:22,introduct:23,issu:23,launcher:14,lead:20,microservic:[9,18,22],mino:[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22],modul:[3,5,7,8,9,10,12,13,14,15,17,18,19],namespac:[0,1],packag:[2,4,6,11,16],pull:23,request:23,router:19,run:[23,24],s:22,servic:[13,15],set:23,submit:23,submodul:[2,4,6,11,16],subpackag:[1,2],tabl:22,test:[23,24],up:23,usag:25,view:[16,17,18,19],welcom:22}})