#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Import packages
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
import time
from os import listdir
from os.path import isfile, join
import pandas as pd

# Get file names of all files in File path
mypath = 'Files' 
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Dictionary to store log data (to go into a DF)
Log_Dict = {}

#Items that need to be blacked out
exclude = [' 100246',' 100247',' 100248',' 100249',' 100250',' 100251',' 100252',' 100253',' 100254',' 100255',' 100256',' 100257',' 100258',' 100259',' 100260',' 100261',' 100262',' 100263',' 100264',' 100265',' 100266',' 100267',' 100268',' 100269',' 100270',' 100271',' 100272',' 100273',' 100274',' 100275',' 100276',' 100277',' 100278',' 100279',' 100280',' 100281',' 100282',' 100283',' 100284',' 100285',' 100286',' 100287',' 100288',' 100289',' 100290',' 100291',' 100292',' 100293',' 100294',' 100295',' 100296',' 100297',' 100298',' 100299',' 100300',' 100301',' 100302',' 100303',' 100304',' 100305',' 100306',' 100307',' 100308',' 100309',' 100310',' 100311',' 100312',' 100313',' 100314',' 100315',' 100316',' 100317',' 100318',' 100319',' 100320',' 100321',' 100322',' 100323',' 100324',' 100325',' 100326',' 100327',' 100328',' 100329',' 100330',' 100331',' 100332',' 100333',' 100334',' 100335',' 100336',' 100337',' 100338',' 100339',' 100340',' 100341',' 100342',' 100343',' 100344',' 100345',' 100346',' 100347',' 100348',' 100349',' 100350',' 100351',' 100352',' 100353',' 100354',' 100355',' 100356',' 100357',' 100358',' 100359',' 100360',' 100361',' 100362',' 100363',' 100364',' 100365',' 100366',' 100367',' 100368',' 100369',' 100370',' 100371',' 100372',' 100373',' 100374',' 100375',' 100376',' 100377',' 100378',' 100379',' 100380',' 100381',' 100382',' 100383',' 100384',' 100385',' 100386',' 100387',' 100388',' 100389',' 100390',' 100391',' 101217',' 102603',' 102604',' 102605',' 102606',' 102607',' 102608',' 102609',' 102610',' 102611',' 102612',' 102613',' 102614',' 102615',' 102616',' 102617',' 102618',' 102619',' 102620',' 102621',' 102622',' 102623',' 102625',' 103035',' 103036',' 103037',' 103038',' 103039',' 103040',' 103041',' 103042',' 103835',' 103836',' 103837',' 103838',' 103839',' 103840',' 103841',' 103842',' 103843',' 103844',' 103845',' 103846',' 103847',' 103848',' 103849',' 103850',' 103851',' 103852',' 103853',' 103854',' 103855',' 103856',' 103857',' 103858',' 103955',' 103960',' 103961',' 103966',' 103967',' 103970',' 103971',' 103973',' 103974',' 103975',' 103979',' 103980',' 103983',' 103984',' 103985',' 103986',' 103987',' 103988',' 103989',' 104562',' 104563',' 104564',' 104565',' 104566',' 104567',' 104568',' 104569',' 104570',' 104571',' 104572',' 104573',' 104574',' 104575',' 104576',' 104577',' 104578',' 104579',' 104580',' 104581',' 104582',' 104583',' 104584',' 104585',' 104586',' 104590',' 104594',' 104597',' 104601',' 104602',' 104603',' 104604',' 104605',' 105583',' 105584',' 105585',' 105586',' 105587',' 105588',' 105589',' 105590',' 105591',' 105592',' 105593',' 105594',' 105595',' 105596',' 105597',' 105598',' 105599',' 105600',' 105601',' 105602',' 105603',' 105604',' 105605',' 105606',' 105607',' 105608',' 105609',' 105610',' 105611',' 105612',' 105613',' 105623',' 105625',' 105626',' 105627',' 105628',' 105630',' 105631',' 105632',' 105633',' 105634',' 105635',' 105636',' 105637',' 105638',' 105639',' 105640',' 105641',' 105642',' 105643',' 105644',' 105645',' 105646',' 105647',' 105648',' 105650',' 105655',' 105656',' 105657',' 105658',' 105659',' 106772',' 106773',' 106777',' 106778',' 106779',' 106780',' 106781',' 106782',' 106783',' 106784',' 106785',' 106786',' 106787',' 106788',' 106789',' 106790',' 106791',' 106792',' 106793',' 106794',' 106795',' 106798',' 106799',' 106800',' 106801',' 106802',' 106803',' 106804',' 106805',' 106806',' 106807',' 106809',' 106810',' 106811',' 106812',' 106813',' 106814',' 106815',' 106816',' 106817',' 106821',' 106826',' 106827',' 106828',' 106829',' 108164',' 108165',' 108166',' 108167',' 108168',' 108169',' 108170',' 108171',' 108172',' 108173',' 108176',' 108177',' 108178',' 108179',' 108180',' 108181',' 108182',' 108183',' 108185',' 108837',' 108838',' 108839',' 108840',' 108841',' 108842',' 108843',' 108844',' 108845',' 108846',' 108847',' 110058',' 111397',' 111398',' 111399',' 111423',' 111424',' 111425',' 111426',' 111537',' 111538',' 111539',' 111540',' 111541',' 111542',' 111543',' 111544',' 111545',' 111546',' 111547',' 111548',' 111549',' 111550',' 111551',' 111552',' 111553',' 111554',' 111555',' 111556',' 111557',' 111558',' 111559',' 111560',' 111561',' 111562',' 111563',' 111564',' 111565',' 111566',' 111567',' 111568',' 111569',' 111570',' 111571',' 111572',' 111573',' 111574',' 111575',' 111576',' 111577',' 111578',' 111579',' 111580',' 111581',' 111582',' 111583',' 111584',' 111585',' 111586',' 111587',' 111588',' 111589',' 111590',' 111591',' 111592',' 111593',' 111594',' 111595',' 111596',' 111597',' 111598',' 111599',' 111600',' 111601',' 111602',' 111603',' 111604',' 111605',' 111606',' 111607',' 111608',' 111609',' 111610',' 111611',' 111612',' 111613',' 111618',' 111619',' 111620',' 111621',' 111626',' 111627',' 111633',' 111634',' 111635',' 111636',' 111637',' 111638',' 111639',' 111640',' 111641',' 111642',' 111643',' 111644',' 111645',' 111646',' 111647',' 111648',' 111649',' 111650',' 111651',' 111652',' 111653',' 111654',' 111655',' 111656',' 111657',' 111658',' 111659',' 111660',' 111661',' 111662',' 111663',' 111664',' 111665',' 111666',' 111667',' 111668',' 111669',' 111670',' 111671',' 111672',' 111673',' 111674',' 111675',' 111676',' 111677',' 111678',' 111679',' 111680',' 111681',' 111682',' 111683',' 111684',' 111685',' 111686',' 111687',' 111688',' 111689',' 111690',' 111691',' 111692',' 111693',' 111694',' 111695',' 111696',' 111697',' 111698',' 111699',' 111700',' 111701',' 111702',' 111703',' 111704',' 111705',' 111706',' 111707',' 111708',' 111709',' 111710',' 111711',' 111712',' 111713',' 111714',' 111715',' 111716',' 111717',' 111718',' 111719',' 111720',' 111721',' 111722',' 111723',' 111724',' 111725',' 111726',' 111727',' 111728',' 111729',' 111730',' 111731',' 111732',' 111733',' 111734',' 111735',' 111736',' 111737',' 111738',' 111739',' 111740',' 111741',' 111742',' 111743',' 111744',' 111745',' 111746',' 111747',' 111748',' 111749',' 111750',' 111751',' 111752',' 111753',' 111754',' 111755',' 111756',' 111757',' 111758',' 111759',' 111760',' 111761',' 111762',' 111763',' 111764',' 111765',' 111766',' 111767',' 111768',' 111769',' 111770',' 111771',' 111772',' 111773',' 111774',' 111775',' 111776',' 111777',' 111778',' 111779',' 111780',' 111781',' 111782',' 111783',' 111784',' 111785',' 111786',' 111787',' 111788',' 111789',' 111790',' 111791',' 111792',' 111793',' 111794',' 111795',' 111796',' 111797',' 111798',' 111799',' 111800',' 111801',' 111802',' 111803',' 111804',' 111805',' 111806',' 111807',' 111808',' 111809',' 111810',' 111811',' 111812',' 111813',' 111814',' 111815',' 111816',' 111817',' 111818',' 111819',' 111820',' 111821',' 111822',' 111823',' 111824',' 111825',' 111826',' 111827',' 111828',' 111829',' 111830',' 111831',' 111832',' 111833',' 111834',' 111835',' 111836',' 111837',' 111838',' 111839',' 111840',' 111841',' 111842',' 111843',' 111844',' 111845',' 111846',' 111847',' 111848',' 111849',' 111850',' 111851',' 111852',' 111853',' 111854',' 111855',' 111856',' 111857',' 111858',' 111859',' 111860',' 111861',' 111862',' 111863',' 111864',' 111865',' 111866',' 111867',' 111868',' 111869',' 111870',' 111871',' 111872',' 111873',' 111874',' 111875',' 111876',' 111877',' 111878',' 111879',' 111880',' 111881',' 111882',' 111883',' 111884',' 111885',' 111886',' 111887',' 111888',' 111889',' 111890',' 111891',' 111892',' 111893',' 111894',' 111895',' 111896',' 111897',' 111898',' 111899',' 111900',' 111901',' 111902',' 111903',' 111904',' 111905',' 111906',' 111907',' 111908',' 111909',' 111910',' 111911',' 111912',' 111913',' 111914',' 111915',' 111916',' 111917',' 111918',' 111919',' 111920',' 111921',' 111922',' 111923',' 111924',' 111925',' 111926',' 111927',' 111928',' 111929',' 111930',' 111931',' 111932',' 111933',' 111934',' 111935',' 111936',' 111937',' 111938',' 111939',' 111940',' 111941',' 111942',' 111943',' 111944',' 111945',' 111946',' 111947',' 111948',' 111949',' 111950',' 111951',' 111952',' 111953',' 111954',' 111955',' 111956',' 111957',' 111958',' 111959',' 111960',' 111961',' 111962',' 111963',' 111964',' 111965',' 111966',' 111967',' 111968',' 111969',' 111970',' 111971',' 111972',' 111973',' 111974',' 111975',' 111976',' 111977',' 111978',' 111979',' 111980',' 111983',' 111984',' 111985',' 111986',' 111987',' 111988',' 111989',' 111990',' 111991',' 111992',' 111993',' 111994',' 111995',' 112297',' 112298',' 112299',' 112389',' 112390',' 112391',' 112392',' 112393',' 112394',' 112395',' 112396',' 112397',' 112398',' 112399',' 112400',' 112401',' 112402',' 112403',' 112404',' 112405',' 112406',' 112407',' 112408',' 112409',' 112410',' 112411',' 112412',' 112413',' 112414',' 112415',' 112416',' 112417',' 112418',' 112419',' 112420',' 112421',' 112422',' 112423',' 112424',' 112425',' 112426',' 112427',' 112428',' 112429',' 112430',' 112431',' 112432',' 112433',' 112434',' 112435',' 112436',' 112437',' 112438',' 112439',' 112440',' 112441',' 112442',' 112443',' 112444',' 112445',' 112446',' 112447',' 112448',' 112449',' 112450',' 112451',' 112452',' 112453',' 112454',' 112455',' 112456',' 112457',' 112458',' 112459',' 112460',' 112461',' 112462',' 112463',' 112464',' 112465',' 112466',' 112467',' 112468',' 112469',' 112470',' 112471',' 112472',' 112473',' 112474',' 112475',' 112476',' 112477',' 112478',' 112479',' 112480',' 112481',' 112482',' 112483',' 112484',' 112485',' 112486',' 112487',' 112488',' 112489',' 112490',' 112491',' 112492',' 112493',' 112494',' 112495',' 112496',' 112497',' 112498',' 112499',' 112500',' 112501',' 112502',' 112503',' 112504',' 112505',' 112506',' 112507',' 112508',' 112509',' 112510',' 112511',' 112512',' 112513',' 112514',' 112515',' 112516',' 112517',' 112518',' 112519',' 112520',' 112521',' 112522',' 112523',' 112524',' 112525',' 112526',' 112527',' 112528',' 112529',' 112530',' 112531',' 112532',' 112533',' 112534',' 112535',' 112536',' 112537',' 112538',' 112539',' 112540',' 112541',' 112542',' 112543',' 112544',' 112545',' 112546',' 112547',' 112548',' 112554',' 112555',' 112556',' 112557',' 112558',' 112559',' 112560',' 112561',' 112562',' 112563',' 112564',' 112565',' 112566',' 112567',' 112568',' 112569',' 112570',' 112571',' 112572',' 112573',' 112574',' 112575',' 112576',' 112577',' 112578',' 112579',' 112580',' 112581',' 112582',' 112583',' 112584',' 112585',' 112586',' 112587',' 112588',' 112589',' 112590',' 112591',' 112592',' 112593',' 112594',' 112595',' 112596',' 112597',' 112598',' 112599',' 112600',' 112601',' 112602',' 112603',' 112604',' 112605',' 112606',' 112607',' 112608',' 112609',' 112610',' 112611',' 112612',' 112613',' 112614',' 112615',' 112616',' 112617',' 112618',' 112619',' 112620',' 112621',' 112622',' 112623',' 112624',' 112625',' 112626',' 112627',' 112628',' 112629',' 112630',' 112631',' 112632',' 112633',' 112634',' 112635',' 112636',' 112637',' 112638',' 112639',' 112640',' 112641',' 112642',' 112643',' 112644',' 112645',' 112646',' 112647',' 112648',' 112649',' 112650',' 112651',' 112652',' 112653',' 112654',' 112655',' 112656',' 112657',' 112658',' 112659',' 112660',' 112661',' 112662',' 112663',' 112664',' 112665',' 112666',' 112667',' 112668',' 112669',' 112670',' 112671',' 112672',' 112673',' 112674',' 112675',' 112676',' 112677',' 112678',' 112679',' 112680',' 112681',' 112682',' 112683',' 112684',' 112685',' 112686',' 112687',' 112688',' 112689',' 112690',' 112691',' 112692',' 112693',' 112694',' 112695',' 112696',' 112697',' 112698',' 112699',' 112700',' 112701',' 112702',' 112703',' 112704',' 112705',' 112706',' 112710',' 112711',' 112712',' 112713',' 112714',' 112715',' 112716',' 112717',' 112718',' 112719',' 112719',' 112720',' 112721',' 112722',' 112723',' 112724',' 112725',' 112726',' 112727',' 112728',' 112729',' 112730',' 112731',' 112732',' 112733',' 112734',' 112735',' 112736',' 112737',' 112738',' 112739',' 112740',' 112741',' 112742',' 112743',' 112745',' 112746',' 112747',' 112748',' 112749',' 112750',' 112751',' 112752',' 112753',' 112754',' 112755',' 112756',' 112758',' 112759',' 112760',' 112761',' 112762',' 112763',' 112764',' 112765',' 112766',' 112767',' 112769',' 112770',' 112771',' 112772',' 112773',' 112774',' 112775',' 112776',' 112777',' 112778',' 112779',' 112780',' 112781',' 112782',' 112783',' 112784',' 112785',' 112788',' 112789',' 112790',' 112792',' 112793',' 112794',' 112795',' 112796',' 112797',' 112798',' 112799',' 112800',' 112801',' 112802',' 112803',' 112804',' 112805',' 112806',' 112807',' 112808',' 112809',' 112810',' 112811',' 112814',' 112815',' 112816',' 112817',' 112818',' 112819',' 112820',' 112821',' 112822',' 112823',' 112824',' 112825',' 112826',' 112827',' 112828',' 112829',' 112830',' 112831',' 112832',' 112833',' 112834',' 112835',' 112836',' 112837',' 112838',' 112839',' 112840',' 112841',' 112842',' 112844',' 112845',' 112847',' 112848',' 112850',' 112853',' 112854',' 112855',' 112856',' 112857',' 112858',' 112859',' 112860',' 112861',' 112862',' 112863',' 112864',' 112865',' 112866',' 112867',' 112868',' 112869',' 112870',' 112871',' 112872',' 112873',' 112874',' 112875',' 112876',' 113003',' 113004',' 113022',' 113084',' 113085',' 113086',' 113087',' 113088',' 113089',' 113090',' 113091',' 113092',' 113093',' 113094',' 113095',' 113096',' 113097',' 113098',' 113099',' 113100',' 113101',' 113102',' 113103',' 113104',' 113105',' 113106',' 113107',' 113108',' 113109',' 113110',' 113111',' 113112',' 113113',' 113114',' 113115',' 113116',' 113117',' 113118',' 113119',' 113120',' 113121',' 113122',' 113123',' 113124',' 113125',' 113126',' 113127',' 113128',' 113129',' 113130',' 113131',' 113132',' 113133',' 113134',' 113135',' 113136',' 113137',' 113138',' 113140',' 113189',' 113190',' 113191',' 113192',' 113193',' 113194',' 113195',' 113196',' 113198',' 113199',' 113200',' 113201',' 113202',' 113203',' 113204',' 113205',' 113206',' 113207',' 113208',' 113209',' 113210',' 113211',' 113212',' 113221',' 113258',' 113263',' 113264',' 113265',' 113266',' 113267',' 113268',' 113269',' 113270',' 113271',' 113272',' 113273',' 113274',' 113275',' 113276',' 113277',' 113278',' 113279',' 113280',' 113281',' 113282',' 113283',' 113284',' 113285',' 113286',' 113287',' 113288',' 113289',' 113290',' 113291',' 113292',' 113293',' 113298',' 113299',' 113300',' 113301',' 113302',' 113305',' 113306',' 113307',' 113308',' 113309',' 113321',' 113322',' 113323',' 113334',' 113335',' 113336',' 113337',' 113338',' 113344',' 113345',' 113346',' 113348',' 113350',' 113351',' 113352',' 113353',' 113354',' 113355',' 113356',' 113373',' 113374',' 113396',' 113397',' 113398',' 113399',' 113400',' 113401',' 113402',' 113403',' 113404',' 113405',' 113406',' 113408',' 113409',' 113410',' 113411',' 113412',' 113432',' 113498',' 113499',' 113500',' 113501',' 113502',' 113503',' 113504',' 113505',' 113506',' 113507',' 113508',' 113509',' 113510',' 113511',' 113512',' 113513',' 113514',' 113515',' 113517',' 113518',' 113519',' 113520',' 113521',' 113523',' 113531',' 113532',' 113533',' 113534',' 113535',' 113536',' 113537',' 113610',' 113679',' 113685',' 113688',' 113697',' 113701',' 113707',' 113708',' 113709',' 113710',' 113711',' 113728',' 113762',' 113763',' 113764',' 113765',' 113766',' 113767',' 113768',' 113772',' 113775',' 113776',' 113777',' 113778',' 113779',' 113780',' 113781',' 113782',' 113783',' 113784',' 113785',' 113786',' 113787',' 113788',' 113794',' 113795',' 113796',' 113797',' 113798',' 113799',' 113800',' 113801',' 113802',' 113803',' 113804',' 113805',' 113806',' 113807',' 113823',' 113824',' 113825',' 113827',' 113833',' 113834',' 113916',' 113917',' 113918',' 113919',' 113920',' 113921',' 113934',' 113935',' 113936',' 113937',' 113938',' 113939',' 113947',' 113948',' 113951',' 113960',' 113961',' 114003',' 114004',' 114005',' 114025',' 114026',' 114027',' 114028',' 114029',' 114075',' 114082',' 114085',' 114089',' 114126',' 114130',' 114221',' 114229',' 114230',' 114231',' 114232',' 114233',' 114234',' 114235',' 114236',' 114237',' 114238',' 114239',' 114240',' 114242',' 114243',' 114244',' 114257',' 114258',' 114259',' 114260',' 114262',' 114285',' 114287',' 114288',' 114289',' 114290',' 114317',' 114339',' 114345',' 114368',' 114369',' 114382',' 114386',' 114389',' 114393',' 114395',' 114398',' 114430',' 114431',' 114432',' 114433',' 114434',' 114435',' 114439',' 114456',' 114506',' 114577',' 114578',' 114579',' 114580',' 114581',' 114582',' 114583',' 114584',' 114585',' 114586',' 114587',' 114588',' 114589',' 114592',' 114597',' 114598',' 114599',' 114600',' 114603',' 114604',' 114605',' 114606',' 114607',' 114608',' 114609',' 114610',' 114616',' 114617',' 114642',' 114645',' 114646',' 114647',' 114667',' 114668',' 114669',' 114670',' 114671',' 114672',' 114673',' 114699',' 114701',' 114702',' 114703',' 114704',' 114705',' 114706',' 114708',' 114710',' 114712',' 114713',' 114714',' 114728',' 114791',' 114792',' 114793',' 114795',' 114844',' 114871',' 114874',' 114899',' 114902',' 114907',' 114964',' 115157',' 115157',' 115204',' 115206',' 115208',' 115250',' 115256',' 115283',' 115330',' 115334',' 115335',' 115345',' 115347',' 115349',' 115350',' 115353',' 115365',' 115385',' 115419',' 115420',' 115422',' 115423',' 115450',' 115451',' 115482',' 115553',' 115583',' 115623',' 115682',' 115684',' 115699',' 115719',' 115725',' 115738',' 115739',' 115740',' 115837',' 115902',' 115903',' 115905',' 115924',' 115925',' 115926',' 115927',' 116156',' 116163',' 116167',' 116182',' 116257',' 116258',' 116259',' 116260',' 116262',' 116264',' 116265',' 116266',' 116274',' 116280',' 116283',' 116284',' 116285',' 116286',' 116288',' 116289',' 116290',' 116294',' 116296',' 116297',' 116335',' 116336',' 116347',' 116391',' 116393',' 116394',' 116403',' 116448',' 116449',' 116450',' 116451',' 116452',' 116453',' 116454',' 116455',' 116458',' 116459',' 116460',' 116461',' 116462',' 116483',' 116486',' 116487',' 116495',' 116502',' 116503',' 116504',' 116506',' 116509',' 116510',' 116511',' 116512',' 116513',' 116514',' 116515',' 116516',' 116517',' 116519',' 116520',' 116521',' 116535',' 116576',' 116577',' 116589',' 116617',' 116618',' 116620',' 116621',' 116622',' 116623',' 116636',' 116640',' 116641',' 116642',' 116643',' 116680',' 116681',' 116682',' 116683',' 116684',' 116685',' 116686',' 116687',' 116715',' 116716',' 116717',' 116718',' 116719',' 116721',' 116722',' 116723',' 116724',' 116725',' 116743',' 116744',' 116747',' 116748',' 116749',' 116765',' 116767',' 116780',' 116781',' 116782',' 116784',' 116785',' 116911',' 116926',' 116964',' 116966',' 117068',' 117069',' 117096',' 117098',' 117099',' 117100',' 117101',' 117102',' 117103',' 117132',' 117144',' 117157',' 117159',' 117163',' 117165',' 117166',' 117167',' 117168',' 117296',' 117297',' 117331',' 117341',' 117342',' 117343',' 117344',' 117345',' 117349',' 117351',' 117383',' 117384',' 117414',' 117415',' 117450',' 117451',' 117453',' 117454',' 117467',' 117470',' 117471',' 117472',' 117473',' 117474',' 117475',' 117476',' 117477',' 117481',' 117492',' 117493',' 117494',' 117495',' 117496',' 117497',' 117498',' 117520',' 117568',' 117572',' 117573',' 117574',' 117607',' 117641',' 117662',' 117688',' 117689',' 117692',' 117754',' 117770',' 117771',' 117772',' 117773',' 117774',' 117775',' 117776',' 117777',' 117782',' 117787',' 117788',' 117789',' 117790',' 117792',' 117794',' 117795',' 117796',' 117799',' 117800',' 117801',' 117818',' 117843',' 117844',' 117874',' 117875',' 117876',' 117879',' 117880',' 117881',' 117882',' 117883',' 117884',' 117885',' 117896',' 117898',' 117899',' 117901',' 117902',' 117903',' 117904',' 117905',' 117906',' 117908',' 117938',' 117967',' 117968',' 117969',' 117970',' 117972',' 117974',' 117975',' 117986',' 117987',' 117988',' 117989',' 118003',' 118043',' 118044',' 118045',' 118046',' 118049',' 118050',' 118051',' 118052',' 118053',' 118054',' 118055',' 118056',' 118057',' 118061',' 118065',' 118075',' 118076',' 118078',' 118080',' 118082',' 118083',' 118084',' 118090',' 118101',' 118116',' 118165',' 118166',' 118178',' 118185',' 118186',' 118189',' 118217',' 118218',' 118219',' 118261',' 118271',' 118272',' 118273',' 118274',' 118275',' 118276',' 118291',' 118292',' 118293',' 118335',' 118386',' 118387',' 118398',' 118410',' 118412',' 118413',' 118414',' 118416',' 118434']
    
# Loop over files in path
for x in files:
    # Use time to determine how long each loop takes
    start = time.time()
    
    
    z = x
    
    # Open PDF file and get objects 
    fp = open('Files/' + x, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)


    # Loop to get the y location of items to exclude, and the invoice number
    error = 0
    lis = []
    lis1 = []
    dic = {}
    
    # Count number of pages in PDF
    page_no = 1
    
    # Count number of instances an excluded item appears in PDF
    counter = 0
    
    # Loop over each page
    for page in pages:
        interpreter.process_page(page)
        layout = device.get_result()
        
        # Loop over each instance of a textbox
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                
                #Loop over each item that should be excluded
                for itstr in exclude:
                    if itstr in text:
                        lis.append(y)
                        lis1.append(y)
                        counter += 1
                if text[:10] == 'Invoice No':
                    Inv_name = text[11:24]
                    Inv_name1 = text[11:24] 
        dic.update({page_no:lis})
        lis = []
        page_no = page_no + 1

    
    # Not sure what oi.BytesIO does/is. BT to assist?
    packet = io.BytesIO()

    # Create a new PDF in Report lap, and add rectangle black space on y-15 line extracted for items to exclude 
    can = canvas.Canvas(packet, pagesize=letter)
    
    # Loop to add blacked out rectangle on PDF in location
    for k in dic:
        for v in dic[k]:
            can.rect(0.01*inch,v-15,20*inch,0.2*inch, fill=1)
        can.showPage() 

    can.save()


    #Dont know what this is for?
    packet.seek(0)
    new_pdf = PdfFileReader(packet)

    # Read existing PDF there is a duplication of code here, however it is working so dont want to remove
    existing_pdf = PdfFileReader(fp)
    output = PdfFileWriter()

    # Combine the new PDF created with rectangle lines and the existing PDF
    for k in dic:
        a = k
        k = existing_pdf.getPage(a-1)
        k.mergePage(new_pdf.getPage(a-1))
        output.addPage(k)

    # Save to real file, using invoice name
    try:
        outputStream = open('Output/' + str(z) + '-' + str(Inv_name) + ".pdf", "wb")
        output.write(outputStream)
        outputStream.close()
    except:
        error = 1
    # Create log of data being blacked out
    if error == 0:
        Log_Dict.update({str(z) + ' - ' + str(Inv_name1):{'Rectangles':counter,'Time':time.time()-start,'Complete':'True'}})
    else:
        Log_Dict.update({str(z) + ' - ' + str(Inv_name1):{'Rectangles':counter,'Time':time.time()-start,'Complete':'False'}})
    
    print('Inv ' + str(Inv_name) + ' Time ' + str(time.time()-start))
Log_DF = pd.DataFrame.from_dict(Log_Dict, orient = 'index')
Log_DF.to_csv('Log.csv')
print(Log_Dict)

