
import math
import matplotlib.pyplot as plt


lista_sensores=[-0.7828508615493774, -1.3559389114379883, -0.7803982496261597, -1.3596888780593872, -0.7734717130661011, -1.3556897640228271, -0.7709469795227051, -1.359452724456787, -0.7683971524238586, -1.3632665872573853, -0.7658176422119141, -1.3671245574951172, -0.7587703466415405, -1.36305570602417, -0.7561195492744446, -1.3669352531433105, -0.753433346748352, -1.3708528280258179, -0.7507196068763733, -1.3748241662979126, -0.7435471415519714, -1.370683193206787, -0.7407582998275757, -1.3746771812438965, -0.7379361987113953, -1.3787190914154053, -0.7350758910179138, -1.3828020095825195, -0.7277738451957703, -1.3785862922668457, -0.7248387932777405, -1.382700800895691, -0.7218677997589111, -1.386865496635437, -0.7188565135002136, -1.3910737037658691, -0.7114201188087463, -1.3867802619934082, -0.7083295583724976, -1.3910213708877563, -0.7052008509635925, -1.3953155279159546, -0.7020330429077148, -1.3996632099151611, -0.6944570541381836, -1.3952891826629639, -0.6911977529525757, -1.399656057357788, -0.6899216175079346, -1.408210277557373, 1.1967747211456299, -4.853013038635254, 1.2252857685089111, -4.775124549865723, 1.2532107830047607, -4.699089050292969, 1.2804927825927734, -4.624555587768555, 1.3213598728179932, -4.600960731506348, 1.3476595878601074, -4.528416633605957, 1.373361349105835, -4.457273483276367, 1.3985649347305298, -4.387754440307617, 1.4381473064422607, -4.364901542663574, 1.4623756408691406, -4.296934127807617, 1.4861485958099365, -4.230485916137695, 1.5093958377838135, -4.165268898010254, 1.5477707386016846, -4.143113136291504, 1.5702073574066162, -4.0795488357543945, 1.5921525955200195, -4.0171356201171875, 1.6137099266052246, -3.9560673236846924, 1.650949478149414, -3.9345669746398926, 1.6716763973236084, -3.874791383743286, 1.6920480728149414, -3.8162784576416016, 1.7120298147201538, -3.758884906768799, 1.748199701309204, -3.738002061843872, 1.7674126625061035, -3.681795597076416, 1.786311388015747, -3.626743793487549, 1.8048112392425537, -3.572622060775757, 1.8399701118469238, -3.55232310295105, 1.8578516244888306, -3.4994802474975586, 1.875357985496521, -3.4475128650665283, 1.8925952911376953, -3.396575927734375, 1.926798939704895, -3.37682843208313, 1.9433709383010864, -3.3268966674804688, 1.9596973657608032, -3.2779386043548584, 1.9756865501403809, -3.2297613620758057, 2.0089848041534424, -3.210536479949951, 2.0244529247283936, -3.163450241088867, 2.0396525859832764, -3.117177724838257, 2.054542064666748, -3.0716254711151123, 2.086982250213623, -3.05289626121521, 2.1013917922973633, -3.0083539485931396, 2.115506649017334, -2.9644908905029297, 2.1294360160827637, -2.921434164047241, 2.1610612869262695, -2.903175115585327, 2.174445867538452, -2.86091685295105, 2.1876602172851562, -2.8194210529327393, 2.200608968734741, -2.778538942337036, 2.2314586639404297, -2.760727882385254, 2.243997573852539, -2.7207157611846924, 2.256283760070801, -2.6812856197357178, 2.2684247493743896, -2.6425445079803467, 2.298536777496338, -2.625159502029419, 2.310248374938965, -2.5871684551239014, 2.3217244148254395, -2.549715995788574, 2.333073139190674, -2.512903928756714, 2.3624818325042725, -2.495924711227417, 2.3734283447265625, -2.4598116874694824, 2.384155035018921, -2.424199104309082, 2.3947701454162598, -2.389180898666382, 2.4235074520111084, -2.372589349746704, 2.4336934089660645, -2.338174819946289, 2.4437785148620605, -2.304325819015503, 2.4537136554718018, -2.2709801197052, 2.481809616088867, -2.254758834838867, 2.4913387298583984, -2.2219784259796143, 2.500779628753662, -2.1897242069244385, 2.5100317001342773, -2.1578948497772217, 2.5375139713287354, -2.1420280933380127, 2.546485185623169, -2.1108171939849854, 2.555328130722046, -2.0800540447235107, 2.563993453979492, -2.049686908721924, 2.590888500213623, -2.034158945083618, 2.599240303039551, -2.0043323040008545, 2.607527256011963, -1.9749646186828613, 2.6156463623046875, -1.9459670782089233, 2.6419787406921387, -1.9307641983032227, 2.6498546600341797, -1.9023116827011108, 2.6576223373413086, -1.8742501735687256, 2.6652326583862305, -1.84653639793396, 2.691025495529175, -1.831644892692566, 2.698408603668213, -1.8044428825378418, 2.7056407928466797, -1.7775733470916748, 2.7128281593322754, -1.7510974407196045, 2.738102912902832, -1.7365050315856934, 2.7450265884399414, -1.710477590560913, 2.75180721282959, -1.6847620010375977, 2.7585501670837402, -1.6594147682189941, 2.783327579498291, -1.6451096534729004, 2.7897701263427734, -1.6201565265655518, 2.79617977142334, -1.5955559015274048, 2.8024563789367676, -1.5712429285049438, 2.8267550468444824, -1.5572140216827393, 2.8328468799591064, -1.533329963684082, 2.8388614654541016, -1.5097496509552002, 2.8447489738464355, -1.4864394664764404, 2.8685879707336426, -1.472676157951355, 2.874302864074707, -1.449771523475647, 2.8798959255218506, -1.4271268844604492, 2.885470390319824, -1.4047880172729492, 2.9088659286499023, -1.3912804126739502, 2.9142279624938965, -1.3692994117736816, 2.919473648071289, -1.3475632667541504, 2.9247055053710938, -1.3261151313781738, 2.947674512863159, -1.3128540515899658, 2.9526543617248535, -1.2917230129241943, 2.9576239585876465, -1.2708678245544434, 2.9625349044799805, -1.2502617835998535, 2.9850921630859375, -1.2372381687164307, 2.9897608757019043, -1.216933250427246, 2.9944241046905518, -1.1968886852264404, 2.9989824295043945, -1.1770590543746948, 3.0211427211761475, -1.1642647981643677, 3.025568962097168, -1.1447609663009644, 3.029893398284912, -1.1254643201828003, 3.0342178344726562, -1.106408953666687, 3.0559945106506348, -1.0938361883163452, 3.0601444244384766, -1.0750709772109985, 3.0641980171203613, -1.0565025806427002, 3.0682544708251953, -1.0381615161895752, 3.089660882949829, -1.025802493095398, 3.0935020446777344, -1.0077214241027832, 3.097349166870117, -0.9898593425750732, 3.1011533737182617, -0.9721959829330444, 3.122201919555664, -0.9600436687469482, 3.125798225402832, -0.9426286220550537, 3.129403829574585, -0.925419807434082, 3.1329216957092285, -0.9083856344223022, 3.153623580932617, -0.8964334726333618, 3.157038688659668, -0.8796641826629639, 3.160367727279663, -0.8630634546279907, 3.1637096405029297, -0.8466547727584839, 3.1840763092041016, -0.8348958492279053, 3.1872730255126953, -0.8187264204025269, 3.190387487411499, -0.802716851234436, 3.193516731262207, -0.7868894338607788, 3.213559627532959, -0.7753176689147949, 3.2165021896362305, -0.7597068548202515, 3.219461441040039, -0.7442713975906372, 3.2223427295684814, -0.728986382484436, 3.2420711517333984, -0.7175960540771484, 3.2448673248291016, -0.7025396823883057, 3.247586250305176, -0.6876286268234253, 3.2503247261047363, -0.6728811264038086, 3.2697486877441406, -0.6616665124893188, 3.2723605632781982, -0.6471271514892578, 3.2748982906341553, -0.6327266693115234, 3.2774569988250732, -0.618480920791626, 3.296586036682129, -0.6074367761611938, 3.2989766597747803, -0.5933816432952881, 3.301389455795288, -0.5794761180877686, 3.3037307262420654, -0.5657011270523071, 3.32257342338562, -0.5548223257064819, 3.324845790863037, -0.5412460565567017, 3.3270480632781982, -0.5277963876724243, 3.329275369644165, -0.5144863128662109, 3.3478400707244873, -0.5037679672241211, 3.3499550819396973, -0.49064040184020996, 3.352003335952759, -0.4776339530944824, 3.354077100753784, -0.4647599458694458, 3.3723721504211426, -0.4541972875595093, 3.3742923736572266, -0.44149231910705566, 3.3762402534484863, -0.42891526222229004, 3.3781235218048096, -0.41645240783691406, 3.3961563110351562, -0.4060412645339966, 3.3979811668395996, -0.39375197887420654, 3.3997890949249268, -0.38157880306243896, 3.4015350341796875, -0.3695152997970581, 3.4193127155303955, -0.3592512607574463, 3.4210033416748047, -0.34735357761383057, 3.4226346015930176, -0.33556246757507324, 3.4242944717407227, -0.32388532161712646, 3.4418251514434814, -0.3137640953063965, 3.4433438777923584, -0.3022373914718628, 3.4448938369750977, -0.290820837020874, 3.4463844299316406, -0.2795048952102661, 3.4636735916137695, -0.26952290534973145, 3.4651167392730713, -0.25835907459259033, 3.4665465354919434, -0.24729681015014648, 3.467919111251831, -0.23633122444152832, 3.4849743843078613, -0.2264842987060547, 3.486302614212036, -0.21566450595855713, 3.4876182079315186, -0.20494139194488525, 3.488922595977783, -0.1943138837814331, 3.5057501792907715, -0.18459844589233398, 3.5069243907928467, -0.17410576343536377, 3.508131980895996, -0.16370820999145508, 3.5092852115631104, -0.15340006351470947, 3.525890588760376, -0.143812894821167, 3.5270047187805176, -0.13363873958587646, 3.5280654430389404, -0.12355172634124756, 3.529160499572754, -0.11355376243591309, 3.5455498695373535, -0.10409152507781982, 3.5465645790100098, -0.09422063827514648, 3.54752779006958, -0.0844336748123169, 3.548525094985962, -0.07473170757293701, 3.564704179763794, -0.0653907060623169, 3.5655808448791504, -0.05581057071685791, 3.5664937496185303, -0.04631233215332031, 3.5673558712005615, -0.03689396381378174, 3.58332896232605, -0.02767181396484375, 3.5841588973999023, -0.018372058868408203, 3.584982395172119, -0.009150266647338867, 3.6008219718933105, -5.364418029785156e-06, 3.613041400909424, -1.1920928955078125e-06, 3.624680519104004, 0.009244918823242188, 3.608665943145752, 0.018490910530090332, 3.620403289794922, 0.027951359748840332, 3.632279396057129, 0.037558674812316895, 3.6443417072296143, 0.04731643199920654, 3.627950668334961, 0.05677986145019531, 3.6400742530822754, 0.06676650047302246, 3.6524360179901123, 0.07691299915313721, 3.6649510860443115, 0.08722126483917236, 3.648164987564087, 0.09691262245178223, 3.6607460975646973, 0.10746622085571289, 3.6735799312591553, 0.11819338798522949, 3.6865766048431396, 0.1290954351425171, 3.6693763732910156, 0.13902592658996582, 3.6824469566345215, 0.150191068649292, 3.6957836151123047, 0.16154491901397705, 3.7092971801757812, 0.17308807373046875, 3.691661834716797, 0.18326985836029053, 3.705254554748535, 0.19509589672088623, 3.7190802097320557, 0.20712459087371826, 2.7207655906677246, 0.15987324714660645, 2.7075793743133545, 0.16748642921447754, 2.680607795715332, 0.1742037534713745, 2.665203094482422, 0.18162190914154053, 2.6555745601654053, 0.1894378662109375, 2.6424500942230225, 0.19701528549194336, 2.6327786445617676, 0.20486152172088623, 2.633080005645752, 0.21353912353515625, 2.63020920753479, 0.22203850746154785, 2.616947650909424, 0.22969508171081543, 2.614001512527466, 0.23829174041748047, 2.6135783195495605, 0.2471979856491089, 2.6152913570404053, 0.2564026117324829, 2.6018333435058594, 0.2641725540161133, 2.6034884452819824, 0.2735300064086914, 2.605161666870117, 0.2829974889755249, 2.606855869293213, 0.2925769090652466, 2.5931596755981445, 0.30048441886901855, 2.6006886959075928, 0.310929536819458, 2.6068968772888184, 0.3213697671890259, 2.6131744384765625, 0.33196938037872314, 2.5991504192352295, 0.34006619453430176, 2.6054441928863525, 0.35089945793151855, 2.619887113571167, 0.3630197048187256, 2.6323082447052, 0.3750762939453125, 2.6178717613220215, 0.3834112882614136, 2.630429267883301, 0.3958083391189575, 2.656282901763916, 0.41047918796539307, 2.6802220344543457, 0.42517805099487305, 2.6651930809020996, 0.43385517597198486, 2.7341196537017822, 0.45655155181884766, 3.710888385772705, 0.6354092359542847, 3.686323642730713, 0.6470317840576172, 3.6651782989501953, 0.6592400074005127, 3.640735626220703, 0.6708405017852783, 3.616337776184082, 0.6824202537536621, 3.5919833183288574, 0.6939789056777954, 3.570895195007324, 0.7061539888381958, 3.5465474128723145, 0.7176696062088013, 3.522301197052002, 0.7291756868362427, 3.4980976581573486, 0.740660548210144, 3.477066993713379, 0.7528026103973389, 3.45292592048645, 0.7642561197280884, 3.4288289546966553, 0.7756892442703247, 3.4047207832336426, 0.7870891094207764, 3.383747100830078, 0.7991982698440552, 3.359755516052246, 0.8105792999267578, 3.3358068466186523, 0.8219395875930786, 3.311901092529297, 0.8332797288894653, 3.2909841537475586, 0.8453562259674072, 3.2670881748199463, 0.8566519021987915, 3.2432875633239746, 0.8679404258728027, 3.2195286750793457, 0.8792089223861694, 3.1986677646636963, 0.8912529945373535, 3.1749706268310547, 0.9024906158447266, 3.1513144969940186, 0.913707971572876, 3.127652883529663, 0.9248913526535034, 3.1068482398986816, 0.9369028806686401, 3.0832958221435547, 0.9480694532394409, 3.0597853660583496, 0.9592163562774658, 3.0363171100616455, 0.9703434705734253, 3.0155677795410156, 0.9823230504989624, 2.992159366607666, 0.9934196472167969, 2.9687466621398926, 1.0044810771942139, 2.9454216957092285, 1.0155384540557861, 2.9247279167175293, 1.027485966682434, 2.9014625549316406, 1.0385128259658813, 2.8782379627227783, 1.049520492553711, 2.855010509490967, 1.060491919517517, 2.834372043609619, 1.072407603263855, 2.811248302459717, 1.0833659172058105, 2.788165330886841, 1.0943045616149902, 2.765123128890991, 1.1052238941192627, 2.7445390224456787, 1.1171081066131592, 2.721555709838867, 1.127997875213623, 2.6985714435577393, 1.1388509273529053, 2.675668716430664, 1.1497020721435547, 2.655139446258545, 1.1615548133850098, 2.6322953701019287, 1.1723765134811401, 2.6094913482666016, 1.183179259300232, 2.5866875648498535, 1.1939446926116943, 2.5662124156951904, 1.205765962600708, 2.5435070991516113, 1.2165205478668213, 2.520841121673584, 1.2272560596466064, 2.4982147216796875, 1.2379727363586426, 2.4777932167053223, 1.249763011932373, 2.4552245140075684, 1.2604509592056274, 2.4326577186584473, 1.2711007595062256, 2.410167932510376, 1.2817509174346924, 2.3898003101348877, 1.2935101985931396, 2.367367744445801, 1.3041318655014038, 2.3449740409851074, 1.314734935760498, 2.3225836753845215, 1.3252992630004883, 2.302269458770752, 1.3370275497436523, 2.2799715995788574, 1.347583532333374, 2.2577126026153564, 1.3581211566925049, 2.2354917526245117, 1.3686401844024658, 2.215230703353882, 1.3803379535675049, 2.193066120147705, 1.3908288478851318, 2.1709070205688477, 1.4012802839279175, 2.148819923400879, 1.4117345809936523, 2.1286113262176514, 1.4234018325805664, 2.1065800189971924, 1.4338281154632568, 0.9395995140075684, 0.6509697437286377, 0.9296935796737671, 0.6556460857391357, 0.920608639717102, 0.6608912944793701, 0.9107341766357422, 0.6655595302581787, 0.9368733167648315, 0.6969998478889465, 1.9768568277359009, 1.497274398803711, 1.9567532539367676, 1.5088810920715332, 1.934983730316162, 1.5191798210144043, 1.9132516384124756, 1.5294609069824219, 1.8915280103683472, 1.539700984954834, 1.8714765310287476, 1.551277756690979, 1.8498363494873047, 1.5615133047103882, 1.828233242034912, 1.571731448173523, 1.8066673278808594, 1.5819320678710938, 1.7866673469543457, 1.593479037284851, 1.7651288509368896, 1.603628158569336, 1.7436540126800537, 1.613783836364746, 1.7222157716751099, 1.6239221096038818, 1.7022674083709717, 1.635439395904541, 1.6808826923370361, 1.6455506086349487, 1.6595346927642822, 1.6556445360183716, 1.6381986141204834, 1.665696382522583, 1.618301510810852, 1.677183985710144, 1.597043514251709, 1.687233805656433, 1.5758213996887207, 1.6972661018371582, 1.4006489515304565, 1.538175344467163, 1.3827683925628662, 1.5484986305236816, 1.3637335300445557, 1.557503581047058, 1.492537021636963, 1.7386748790740967, 1.4714758396148682, 1.7486295700073242, 1.4516801834106445, 1.7600585222244263, 1.4306716918945312, 1.7699867486953735, 1.409698724746704, 1.7798984050750732, 1.388761043548584, 1.7897928953170776, 1.3690156936645508, 1.8011928796768188, 1.348110318183899, 1.8110344409942627, 1.3272602558135986, 1.8208857774734497, 1.306445598602295, 1.8307207822799683, 1.2867505550384521, 1.8420917987823486, 1.2659876346588135, 1.8519008159637451, 1.2452411651611328, 1.8616654872894287, 1.2245482206344604, 1.8714410066604614, 1.2049031257629395, 1.882783055305481, 1.1842615604400635, 1.8925325870513916, 1.1636546850204468, 1.9022659063339233, 1.143082618713379, 1.9119832515716553, 1.1234869956970215, 1.9232966899871826, 1.1029492616653442, 1.9329591989517212, 1.0824626684188843, 1.9426339864730835, 1.062010407447815, 1.952292561531067, 1.042464256286621, 1.9635775089263916, 1.0220625400543213, 1.9732105731964111, 1.0016947984695435, 1.9828274250030518, 0.981346845626831, 1.9923990964889526, 0.9618499279022217, 2.0036556720733643, 0.9415668249130249, 2.013230800628662, 0.9213175773620605, 2.0227904319763184, 0.90110182762146, 2.0323336124420166, 0.8816537261009216, 2.0435619354248047, 0.8614881038665771, 2.0530803203582764, 0.8413435220718384, 2.0625524520874023, 0.8212450742721558, 2.0720388889312744, 0.8018457293510437, 2.0832390785217285, 0.7817968130111694, 2.092700719833374, 0.7617810368537903, 2.1021463871002197, 0.7417985200881958, 2.1115763187408447, 0.722447395324707, 2.122748613357544, 0.7025036811828613, 2.132122755050659, 0.6826035976409912, 2.141512393951416, 0.6627365350723267, 2.1508865356445312, 0.643433690071106, 2.1620309352874756, 0.6236152648925781, 2.1713802814483643, 0.603829562664032, 2.1807141304016113, 0.5840679407119751, 2.190000534057617, 0.5648131966590881, 2.2011172771453857, 0.5451087951660156, 2.210411310195923, 0.5254369378089905, 2.2196900844573975, 0.5057973861694336, 2.2289531230926514, 0.48659008741378784, 2.2400424480438232, 0.4669986963272095, 2.249281167984009, 0.4474329352378845, 2.258472442626953, 0.4279060363769531, 2.267681121826172, 0.40874630212783813, 2.278743028640747, 0.3892672061920166, 2.2879271507263184, 0.36981987953186035, 2.2970964908599854, 0.3503994941711426, 2.306217670440674, 0.33128708600997925, 2.3172521591186523, 0.3119193911552429, 2.3263819217681885, 0.2925833463668823, 2.3354973793029785, 0.27327877283096313, 2.344597578048706, 0.2542131543159485, 2.355605125427246, 0.23495572805404663, 2.3646817207336426, 0.2157265543937683, 2.3737094402313232, 0.19653207063674927, 2.382755994796753, 0.1775132417678833, 2.3937366008758545, 0.15836560726165771, 2.4027600288391113, 0.13924908638000488, 2.411768674850464, 0.12016350030899048, 2.420762538909912, 0.10119110345840454, 2.431716203689575, 0.08215075731277466, 2.4406514167785645, 0.05792725086212158, 2.247267246246338, 0.0397908091545105, 2.215015411376953, 0.022739529609680176, 2.2248599529266357, 0.006308555603027344, 2.478393316268921, -0.012591958045959473, 2.4872968196868896, -0.031461358070373535, 2.496150493621826, -0.050341010093688965, 2.5070507526397705, -0.06916499137878418, 2.515916585922241, -0.08795833587646484, 2.524768114089966, -0.10672140121459961, 2.5336050987243652, -0.1255556344985962, 2.5444791316986084, -0.14427125453948975, 2.5532572269439697, -0.16295850276947021, 2.562056541442871, -0.181615948677063, 2.570842742919922, -0.20040428638458252, 2.5816900730133057, -0.21901631355285645, 2.5904531478881836, -0.23759853839874268, 2.5992019176483154, -0.25614726543426514, 2.6078994274139404, -0.2748901844024658, 2.618720769882202, -0.29339754581451416, 2.6274328231811523, -0.31187498569488525, 2.6361305713653564, -0.33032310009002686, 2.644814968109131, -0.3490208387374878, 2.6556100845336914, -0.36742448806762695, 2.664271354675293, -0.3857933282852173, 2.672882080078125, -0.4041377305984497, 2.6815152168273926, -0.42279052734375, 2.692284345626831, -0.4410909414291382, 2.7008960247039795, -0.4593619108200073, 2.709493637084961, -0.4775972366333008, 2.7180395126342773, -0.4962049722671509, 2.7287826538085938, -0.5144028663635254, 2.737344264984131, -0.5325716733932495, 2.74589204788208, -0.5507116317749023, 2.7544262409210205, -0.56927490234375, 2.765143871307373, -0.5873713493347168, 2.773655891418457, -0.6054304838180542, 2.782116174697876, -0.623469352722168, 2.7906014919281006, -0.6419882774353027, 2.8012936115264893, -0.65998375415802, 2.8097565174102783, -0.6779507398605347, 2.818206310272217, -0.6958892345428467, 2.8266427516937256, -0.7143641710281372, 2.8373093605041504, -0.7322498559951782, 2.845684766769409, -0.7501168251037598, 2.854085922241211, -0.7679557800292969, 2.862474203109741, -0.7863867282867432, 2.873115301132202, -0.8041826486587524, 2.881481885910034, -0.38481879234313965, 1.3529558181762695, -0.3880034387111664, 1.3391858339309692, -0.3964998424053192, 1.3440911769866943, -0.3994821310043335, 1.330629587173462, -0.4026971757411957, 1.3185536861419678, -0.4106474220752716, 1.32228684425354, -0.4189155399799347, 1.3270604610443115, -0.42684945464134216, 1.3307921886444092, -0.9645781517028809, 2.9607460498809814, -0.9821223020553589, 2.9689910411834717, -1.0004230737686157, 2.9795570373535156, -1.01792573928833, 2.987781047821045, -1.0353864431381226, 2.995950698852539, -1.052834153175354, 3.0041487216949463, -1.0710915327072144, 3.0146896839141846, -1.0884976387023926, 3.022866725921631, -1.1058766841888428, 3.031031370162964, -0.7659488320350647, 2.0724713802337646, -0.7783697247505188, 2.0796425342559814, -0.7815340757369995, 2.0623867511749268, -0.784210205078125, 2.0444486141204834, -0.7957136034965515, 2.0498437881469727, -0.8078312277793884, 2.056839942932129, -1.2286646366119385, 3.0925862789154053, -1.2458363771438599, 3.100615978240967, -1.262998342514038, 3.108675241470337, -1.2811274528503418, 3.1191422939300537, -1.298248529434204, 3.127180814743042, -1.3153431415557861, 3.135206937789917, -1.3324111700057983, 3.1432206630706787, -1.3504983186721802, 3.153663396835327, -1.3675072193145752, 3.1616132259368896, -1.3844895362854004, 3.169550895690918, -1.4014643430709839, 3.1775197982788086, -1.4195088148117065, 3.1879377365112305, -1.4364432096481323, 3.1958858966827393, -1.4533320665359497, 3.2037782669067383, -1.4702141284942627, 3.2117018699645996, -1.4882166385650635, 3.2220957279205322, -1.5050586462020874, 3.229998826980591, -1.5218751430511475, 3.2378900051116943, -1.5386654138565063, 3.2457687854766846, -1.5566262006759644, 3.256138324737549, -1.573355793952942, 3.26395320892334, -1.0874969959259033, 2.23766827583313, -1.0893306732177734, 2.2234580516815186, -1.1014792919158936, 2.2304720878601074, -1.1031745672225952, 2.2164833545684814, -1.1056108474731445, 2.2042946815490723, -1.1166810989379883, 2.209479808807373, -1.1286029815673828, 2.216362953186035, -1.7090266942977905, 3.331437349319458, -1.7255706787109375, 3.339195966720581, -1.7420896291732788, 3.3469431400299072, -1.759926676750183, 3.35724139213562, -0.9286502003669739, 1.759101152420044, -0.930611252784729, 1.7506420612335205, -0.9316367506980896, 1.7406232357025146, -0.9408003687858582, 1.7459139823913574, -0.9417287111282349, 1.736023187637329, -0.9426408410072327, 1.726302146911621, -0.9470069408416748, 1.7230592966079712, -0.9559693336486816, 1.728233814239502, -0.9641913175582886, 1.7320783138275146, -0.9724072217941284, 1.7359285354614258, -1.9427250623703003, 3.446730852127075, -1.9604400396347046, 3.456958532333374, -1.9766287803649902, 3.4645116329193115, -1.99281907081604, 3.4720985889434814, -2.0105068683624268, 3.4823105335235596]

def descompress_data(lista_sensores, posx, posy, orientation):
    matrix = []
    x = []
    y = []
    for i in range(0, len(lista_sensores), 2):
        fila = [lista_sensores[i], lista_sensores[i + 1]]
        lx = lista_sensores[i]
        ly = lista_sensores[i + 1]
        xt, yt = transform_coordinates(lx, ly, posx, posy, orientation)
        x.append(xt)
        y.append(yt)
        matrix.append(fila)
    return matrix, x, y

def transform_coordinates(lx, ly, posx, posy, orientation):
    cth = math.cos(orientation)
    sth = math.sin(orientation)
    x_transformated = cth * lx - sth * ly + posx
    y_transformated = sth * lx + cth * ly + posy
    return x_transformated, y_transformated

# Datos de ejemplo (debes reemplazarlos con tus datos reales)

positionx = 9
positiony = 7

# Generar datos para cada orientación
orientation0 = 0
orientation90 = math.pi / 2
orientation180 = math.pi
orientation270 = 3 * math.pi / 2

laser_data0, x0, y0 = descompress_data(lista_sensores, positionx, positiony, orientation0)
laser_data90, x90, y90 = descompress_data(lista_sensores, positionx, positiony, orientation90)
laser_data180, x180, y180 = descompress_data(lista_sensores, positionx, positiony, orientation180)
laser_data270, x270, y270 = descompress_data(lista_sensores, positionx, positiony, orientation270)

# Crear subgráficas
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.scatter(positionx, positiony, color='red', label='posición')
plt.scatter(x0, y0, color='blue', label='paredes')
plt.title("Orientación 0 grados")
plt.legend()

plt.subplot(2, 2, 2)
plt.scatter(positionx, positiony, color='red', label='posición')
plt.scatter(x90, y90, color='blue', label='paredes')
plt.title("Orientación 90 grados")
plt.legend()

plt.subplot(2, 2, 3)
plt.scatter(positionx, positiony, color='red', label='posición')
plt.scatter(x180, y180, color='blue', label='paredes')
plt.title("Orientación 180 grados")
plt.legend()

plt.subplot(2, 2, 4)
plt.scatter(positionx, positiony, color='red', label='posición')
plt.scatter(x270, y270, color='blue', label='paredes')
plt.title("Orientación 270 grados")
plt.legend()

plt.tight_layout()
plt.show()