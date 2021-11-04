clear
import delimited "https://raw.githubusercontent.com/msn08/dev_eco/main/data_stata/stata_data.csv"

drop v1

gen modate=ym(year, month)

********
gen FARC=1 if ratio>0.75 & modate<666
replace FARC= 0 if missing(FARC)

// TO FIND FARC MUNICIPALITIES, COLLECT ID
preserve
collapse (sum) FARC , by(municipality) 
//collapse (sum) births FARC , by(municipality modate)
restore
//preserve
// DEFINE IF MUN ARE FARC RELATED

replace FARC=1 if municipality==5004 | municipality==5031 |municipality==5034 | municipality==5038 |municipality==5040 | municipality==5042 | municipality==5044 |municipality==5045 | municipality==5055 |municipality==5107 |municipality==5120 |municipality==5125 |municipality==5134 
replace FARC=1 if municipality==5138 |municipality==5147 |municipality==5148 |municipality==5154 |municipality==5172 |municipality==5212 |municipality==5234 |municipality==5250 |municipality==5284 |municipality==5310 |municipality==5313 |municipality==5315 | municipality== 5361 | municipality==5364 | municipality==    5475  | municipality== 5480 | municipality==5483  | municipality== 5495     | municipality==5541 | municipality==5543 | municipality==5585   | municipality==5604 | municipality==5628  | municipality==5642 | municipality==5647 | municipality==5649| municipality== 5652 | municipality==5658 | municipality==5660  | municipality==5664 | municipality==5667 | municipality== 95670 | municipality== 5686 | municipality== 5690 | municipality==5736   | municipality== 5756 | municipality==5790| municipality== 5819 | municipality==  5837| municipality==  5847| municipality== 5854 | municipality==5873 | municipality==5887 | municipality== 5893 | municipality== 5895  | municipality==8675 | municipality==11001| municipality==13042 | municipality==13160 | municipality==13212 | municipality==13244| municipality==13458 | municipality==13490| municipality==13654 | municipality==13670| municipality==13683 | municipality==13688 | municipality==13744 | municipality==15001 | municipality==15176 | municipality==15183 | municipality==15223 | municipality==15518| municipality==15533 | municipality==15550| municipality==15755 | municipality==15757| municipality==17013| municipality==17042 | municipality==17380 | municipality==17541 | municipality==17614 | municipality==17662 | municipality==18001 | municipality==18029 | municipality==18094 | municipality==18150 | municipality==18205 | municipality==18247 | municipality==18256 | municipality==18410 | municipality==18460 | municipality==18479| municipality==18592 | municipality==18610| municipality==18753 | municipality==18756| municipality==18785 | municipality==18860 | municipality==20013 | municipality==20045| municipality==20238 | municipality==20443 | municipality==20517 | municipality==20621 | municipality==20710 | municipality==20750 | municipality==23079 | municipality==23466 | municipality==23500 | municipality==23570 | municipality==23580 | municipality==23807 | municipality==25120 | municipality==25279| municipality==25290 | municipality==25307 | municipality==25339 | municipality==25372 | municipality==25386 | municipality==25506 | municipality==25513 | municipality==25649 | municipality==25785 | municipality==25799 | municipality==25815 | municipality==25845| municipality==25878 | municipality==27001 
replace FARC=1 if municipality==27006 | municipality==27050| municipality==27075 | municipality==27077 | municipality==27099 | municipality==27150 | municipality==27160 | municipality==27205 | municipality==27245 | municipality==27250 | municipality==27361 | municipality==27372 | municipality==27413 | municipality==27425 | municipality==27450 | municipality==27491 | municipality==27495 | municipality==27580| municipality==27615 | municipality==27660 | municipality==27745| municipality==27787 | municipality==27800 | municipality==41001 | municipality==41016 | municipality==41020 | municipality==41026 | municipality==41078 | municipality==41132| municipality==41206 | municipality==41298 | municipality==41306 | municipality==41349 | municipality==41357 | municipality==41359 | municipality==41378 | municipality==41396 | municipality==41483 | municipality==41524 | municipality==41530 | municipality==41548 | municipality==41551| municipality==41615 | municipality==41660 | municipality==41668 | municipality==41676| municipality==41770 | municipality==41797 | municipality==41799 | municipality==41801 | municipality==41807 | municipality==44035| municipality==44078| municipality==44090| municipality==44098 | municipality==44110 | municipality==44279 | municipality==44430 | municipality==44560 | municipality==44650 | municipality==44847 | municipality==44855 | municipality==44874 | municipality==47030 | municipality==47798 | municipality==50001 | municipality==50223 | municipality==50226 | municipality==50251 | municipality==50287 | municipality==50313| municipality==50325  | municipality==50330 | municipality==50350 | municipality==50370 | municipality==50400 | municipality==50450 | municipality==50568| municipality==50573 | municipality==50577 | municipality==50590 | municipality==50606 | municipality==50683 | municipality==50686 | municipality==50689 | municipality==50711 | municipality==52001 | municipality==52022 | municipality==52036 | municipality==52079 | municipality==52203 | municipality==52210| municipality==52215 | municipality==52227 | municipality==52250 | municipality==52256  | municipality==52260 | municipality==52317 | municipality==52320  | municipality==52356 | municipality==52378 | municipality==52381| municipality==52385| municipality==52390| municipality==52399| municipality==52405| municipality==52418| municipality==52427| municipality==52435
replace FARC=1 if municipality==52473| municipality==52490| municipality==52506| municipality==52520| municipality==52540| municipality==52560| municipality==52565| municipality==52573| municipality==52585| municipality==52612| municipality==52621| municipality==52678| municipality==52683| municipality==52696| municipality==52699| municipality==52720| municipality==52786| municipality==52835| municipality==52838| municipality==52885| municipality==54003| municipality==54051| municipality==54109| municipality==54174| municipality==54206| municipality==54223| municipality==54239| municipality==54245| municipality==54250| municipality==54261| municipality==54344| municipality==54377| municipality==54498| municipality==54553| municipality==54660| municipality==54670| municipality==54673| municipality==54720| municipality==54800| municipality==54810| municipality==54820| municipality==63001| municipality==63130| municipality==63212 | municipality==63302 | municipality==63548 | municipality==66088 | municipality==66383 | municipality==66456 | municipality==66572 | municipality==66594 | municipality==68101 | municipality==68207    | municipality==68575    | municipality==68655  | municipality==70221   | municipality==70230   | municipality==70713   | municipality==70742    | municipality==73001  | municipality== 73024    | municipality==73026   | municipality==73043 | municipality==73067  | municipality==73124  | municipality==73152| municipality== 73168    | municipality==73200 | municipality==73217   | municipality==73226 | municipality==73236  | municipality== 73268  | municipality==73275 | municipality==73349    | municipality==73352 | municipality==73411    | municipality==73449| municipality==   73461 | municipality==  73483 | municipality==73504 | municipality==  73520 | municipality== 73555  | municipality==73563 | municipality==73585   | municipality==73616   | municipality== 73622 | municipality== 73624  | municipality==73675| municipality==  73686  | municipality==73854 | municipality==73861  | municipality== 73870   | municipality== 73873 | municipality== 76001| municipality==   76036 | municipality==   76111  | municipality==76113 | municipality== 76122  | municipality==76126| municipality==   76130  | municipality==76233  | municipality== 76248  | municipality==76250  | municipality==76275    | municipality==76306  | municipality==76318  | municipality== 76364 | municipality==76520  | municipality== 76563  | municipality==76606  | municipality== 76616  | municipality==76622| municipality== 76670| municipality== 76736 | municipality==76834  | municipality== 76892  | municipality==81001  | municipality==81065 | municipality==81220 | municipality==81300 | municipality==81591 | municipality==81736 | municipality==81794 | municipality==85001 | municipality==85125 | municipality==85136| municipality==   85162 | municipality==85225 | municipality== 85230 | municipality==85250 | municipality==85279   | municipality==85315 | municipality==85400| municipality==86001 | municipality==86320 | municipality==86568 | municipality==86569 | municipality==86571 | municipality==86573 | municipality==86749 | municipality== 86757 | municipality==86865| municipality== 86885 | municipality== 91001 | municipality==91405 | municipality==94001 | municipality==94343 | municipality==94663 | municipality==94885 | municipality==95001| municipality== 95015 | municipality==95025 | municipality==    95200  | municipality==97001| municipality== 97161 | municipality==97511 | municipality==99001 | municipality==99773

********
gen treatment=1 if FARC==1 & post15==1
replace treatment=0 if missing(treatment)

//Treatment when peace talk first began
gen treatment13=1 if FARC==1 & post13==1
replace treatment13=0 if missing(treatment13)


preserve

collapse (sum) births , by(FARC modate)
twoway (line births modate if  FARC==0, mcolor("red") tline(679)) (line births modate if  FARC==1 , mcolor("green"))
restore

///////////
//For when peace talk first began
preserve 

collapse (sum) births , by(FARC modate)
twoway (line births modate if  FARC==0, mcolor("red") tline(635)) (line births modate if  FARC==1 , mcolor("green"))
restore

///////////
**************
ssc install estout, replace
**************

preserve

collapse (sum) births totalviolence, by(treatment modate municipality)
gen treat_violence = treatment*totalviolence

//diff options
xtset municipality modate
xtreg births i.treatment treat_violence i.modate, fe

restore


// diff function
**************
ssc install diff, replace
**************
/// format: diff output_variable, t(treated) p(period)
/// where treated  dummy variable with the indicator of the control (treated==0) and treated (treated==1)
/// and period  dummy variable indicating the baseline (period==0) and a follow-up (period==1) periods

diff births, t(treatment) p(post15)
diff births, t(treatment13) p(post13)

