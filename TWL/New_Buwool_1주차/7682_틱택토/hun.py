'''
처음은 반드시 x 가 먼저 놓는다
--> x 갯수랑 o 갯수랑 차이가 2이상이 될수 없다
--> o 갯수가 많을 수 없다
--> x 랑 o 가 둘다 빙고인 경우는 나올 수 가 없다
--> x만 빙고, o 빙고 아님 가능 
--> x가 두개가 빙고가 나올수 있는 경웅DAEDFGJKLASDFHG;LKFHS;LGKJAD;LKFJGHL;DSKFJG;LKJ
DFKLBHSD;LFKGJHS;LDFHG
DZFXGJL;KH'ZLD;KFGJ
SHDF
HSFG\SFHTG
SFGH
SRTH
SHRT
SRTH
SRTH
SRTH
SRTH
SRTH
SRTH
STHR
SRTH
RSTJ
SRJY
HJKKHK;AKERGHJLKHJ;AFWRETHJKRWEH;WferthklrftljkfweJL;KWfiol;jgerjiolrgejirgejiol;gaerjl;i
geraljrgaejigaerlj;rga;ljergajl;i
agj'aergj'aergjlgaj'gera;jigraejigraejol;gerrgaej'gaerjiogeajol;i
garjp'iograepjo'rgeajp'gaerjop'rgaejop'
gaerjp'gaerp'joegarjp'oaergjop'
gaerp'jogaer'jopgaerj'opgrae'j;oaerg'j;o
agji'erga'jgr'jaergj'aerg'jiprga'jaergj'gaer'jgarj'rgaejl
gaeriljaergojerag;agerp'jergajiaergj'earjiaep'eajp'aj'aerjp'aergjp'agrjp'
gaeh;a;aej'twrfojiaegrj'dfgajgjp'gawrfjol'garj'aergp'jgarjp'
twji'wjaergj'garjp'oaergjop'gajp'argj'aegrj'agjop'awtgrjop'agjopgarjop'
arfgji'gaj'rfgaj'arfgp'joaerg'jopgarop'jrgajop'awrj'j'w'jopgarjol'
rgwj'gwP'GWRjo'gw;'jsd;flk'p;wgpdfg;lWGPCWWPWJPwgjopgjpwgpjorgpjo'gwjop'
grj'gpjgerpjWRGPJO'Gwrjp'owfjop'gWRP'GR'JOPWRFTGJP'OWGJWrgpjo'gwro'pjgWRJ'P
GWolWEFPJ'werejop'

xxx
oo.
xxx
-> invalid

xox
oxo
xox
-> valid

oxo
xox
oxo
-> invalid

xxo
oox
xox
-> valid

xo.
ox.
..x
-> valid

.xx
x.x
ooo
-> invalid

x.o
o..
x..
-> valid

oox
xxo
oxo
-> invalid
'''

def check():
    













cnt = 0
while cnt == 0:
    lst = []
    if input() == 'end':
        cnt += 1
    lst.append(input().split(''))
    print(lst)
