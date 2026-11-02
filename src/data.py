# Hanzi tree data.
# Each tree: root char, then 3 branches. Each branch: compound word, the linked
# character it introduces, and 3 leaf words built on that linked character.
# Word entry: (word, pinyin, meaning, example sentence, sentence English)

TREES = [
 ("火", [
  (("火车","huǒchē","train","我坐火车去北京。","I'm taking the train to Beijing."), "车", [
    ("汽车","qìchē","car","他买了一辆新汽车。","He bought a new car."),
    ("车站","chēzhàn","station","车站离这儿不远。","The station isn't far from here."),
    ("车票","chēpiào","(bus/train) ticket","我的车票在包里。","My ticket is in my bag.")]),
  (("火山","huǒshān","volcano","这座火山很多年没有喷发了。","This volcano hasn't erupted for many years."), "山", [
    ("上山","shàng shān","go up a mountain","我们早上六点上山。","We go up the mountain at six in the morning."),
    ("下山","xià shān","go down a mountain","天黑以前我们要下山。","We have to come down the mountain before dark."),
    ("山上","shān shang","on the mountain","山上有一个小庙。","There is a small temple on the mountain.")]),
  (("火星","huǒxīng","Mars","火星是红色的行星。","Mars is the red planet."), "星", [
    ("星星","xīngxing","star","今天晚上星星很多。","There are lots of stars tonight."),
    ("星期","xīngqī","week","这个星期我很忙。","I'm very busy this week."),
    ("明星","míngxīng","celebrity, star","她是一个电影明星。","She is a movie star.")]),
 ]),
 ("人", [
  (("人口","rénkǒu","population","中国人口很多。","China has a large population."), "口", [
    ("门口","ménkǒu","doorway, entrance","我在门口等你。","I'll wait for you at the entrance."),
    ("出口","chūkǒu","exit; export","出口在左边。","The exit is on the left."),
    ("口语","kǒuyǔ","spoken language","我的中文口语不太好。","My spoken Chinese isn't very good.")]),
  (("人生","rénshēng","life (one's life)","人生很短。","Life is short."), "生", [
    ("学生","xuésheng","student","我是大学学生。","I am a university student."),
    ("生日","shēngrì","birthday","祝你生日快乐！","Happy birthday to you!"),
    ("医生","yīshēng","doctor","我妈妈是医生。","My mother is a doctor.")]),
  (("人心","rénxīn","popular feeling, people's hearts","这件事很得人心。","This won broad public support."), "心", [
    ("小心","xiǎoxīn","careful","过马路要小心。","Be careful crossing the road."),
    ("开心","kāixīn","happy","今天我很开心。","I'm very happy today."),
    ("中心","zhōngxīn","center","购物中心在城市中心。","The shopping mall is in the city center.")]),
 ]),
 ("水", [
  (("水果","shuǐguǒ","fruit","我每天都吃水果。","I eat fruit every day."), "果", [
    ("苹果","píngguǒ","apple","这个苹果很甜。","This apple is very sweet."),
    ("果汁","guǒzhī","fruit juice","你想喝果汁吗？","Would you like some juice?"),
    ("结果","jiéguǒ","result; as a result","考试结果出来了。","The exam results are out.")]),
  (("水平","shuǐpíng","level, standard","他的中文水平很高。","His Chinese is at a high level."), "平", [
    ("平安","píng'ān","safe and sound","祝你一路平安。","Have a safe journey."),
    ("和平","hépíng","peace","大家都希望和平。","Everyone hopes for peace."),
    ("平时","píngshí","ordinarily, usually","我平时七点起床。","I usually get up at seven.")]),
  (("水电","shuǐdiàn","water and electricity, utilities","这个月的水电费很贵。","This month's utility bill is expensive."), "电", [
    ("电话","diànhuà","telephone; phone call","晚上给我打电话。","Give me a call tonight."),
    ("电脑","diànnǎo","computer","我的电脑坏了。","My computer is broken."),
    ("电影","diànyǐng","film, movie","我们去看电影吧。","Let's go see a movie.")]),
 ]),
 ("日", [
  (("日本","Rìběn","Japan","他明年要去日本工作。","He's going to work in Japan next year."), "本", [
    ("本来","běnlái","originally","我本来想去，后来没时间。","I originally wanted to go, but then had no time."),
    ("书本","shūběn","book(s)","不要只看书本上的知识。","Don't rely only on book knowledge."),
    ("基本","jīběn","basic; basically","这是最基本的问题。","This is the most basic question.")]),
  (("日记","rìjì","diary","她每天晚上写日记。","She writes in her diary every night."), "记", [
    ("记得","jìde","remember","你还记得我吗？","Do you still remember me?"),
    ("忘记","wàngjì","forget","我忘记带钥匙了。","I forgot to bring my keys."),
    ("记者","jìzhě","journalist, reporter","他是一名新闻记者。","He is a news reporter.")]),
  (("日期","rìqī","date","请写上今天的日期。","Please write today's date."), "期", [
    ("学期","xuéqī","school term, semester","新学期九月开始。","The new semester starts in September."),
    ("假期","jiàqī","holiday, vacation","假期你打算做什么？","What are you planning to do over the holiday?"),
    ("期待","qīdài","look forward to","我很期待和你见面。","I'm really looking forward to meeting you.")]),
 ]),
 ("月", [
  (("月亮","yuèliang","the moon","今晚的月亮又大又圆。","Tonight's moon is big and round."), "亮", [
    ("明亮","míngliàng","bright","这个房间很明亮。","This room is very bright."),
    ("漂亮","piàoliang","pretty, beautiful","你的衣服很漂亮。","Your clothes are very pretty."),
    ("亮光","liàngguāng","light, glow","远处有一点亮光。","There's a faint light in the distance.")]),
  (("月饼","yuèbing","mooncake","中秋节我们吃月饼。","We eat mooncakes at the Mid-Autumn Festival."), "饼", [
    ("饼干","bǐnggān","biscuit, cracker","孩子们喜欢吃饼干。","The children like eating biscuits."),
    ("煎饼","jiānbing","jianbing (savory crepe)","我早饭吃了一个煎饼。","I had a jianbing for breakfast."),
    ("大饼","dàbǐng","flatbread","这家店的大饼很好吃。","This shop's flatbread is delicious.")]),
  (("月份","yuèfèn","month (of the year)","哪个月份最热？","Which month is the hottest?"), "份", [
    ("身份","shēnfèn","identity, status","请出示你的身份证。","Please show your ID card."),
    ("省份","shěngfèn","province","中国有很多省份。","China has many provinces."),
    ("股份","gǔfèn","share, stock","他有这家公司的股份。","He holds shares in this company.")]),
 ]),
 ("大", [
  (("大学","dàxué","university","她在北京上大学。","She goes to university in Beijing."), "学", [
    ("学习","xuéxí","study, learn","我在学习中文。","I'm learning Chinese."),
    ("学校","xuéxiào","school","学校八点上课。","School starts at eight."),
    ("数学","shùxué","mathematics","我的数学不太好。","I'm not very good at maths.")]),
  (("大家","dàjiā","everyone","大家好！","Hello, everyone!"), "家", [
    ("国家","guójiā","country, nation","你去过几个国家？","How many countries have you been to?"),
    ("家人","jiārén","family members","周末我和家人在一起。","I spend weekends with my family."),
    ("回家","huí jiā","go home","我们回家吧。","Let's go home.")]),
  (("大小","dàxiǎo","size","这双鞋大小正合适。","These shoes are just the right size."), "小", [
    ("小时","xiǎoshí","hour","我每天工作八个小时。","I work eight hours a day."),
    ("小孩","xiǎohái","child","那个小孩很可爱。","That child is very cute."),
    ("小说","xiǎoshuō","novel","我在看一本小说。","I'm reading a novel.")]),
 ]),
 ("天", [
  (("天气","tiānqì","weather","今天天气很好。","The weather is nice today."), "气", [
    ("生气","shēngqì","angry","别生气了。","Don't be angry."),
    ("空气","kōngqì","air","这里的空气很新鲜。","The air here is very fresh."),
    ("客气","kèqi","polite; to stand on ceremony","不客气。","You're welcome.")]),
  (("天下","tiānxià","the world, all under heaven","天下没有免费的午餐。","There's no such thing as a free lunch."), "下", [
    ("下午","xiàwǔ","afternoon","下午我们去公园。","We're going to the park in the afternoon."),
    ("下雨","xià yǔ","to rain","外面下雨了。","It's raining outside."),
    ("下班","xià bān","get off work","你几点下班？","What time do you get off work?")]),
  (("天空","tiānkōng","sky","天空很蓝。","The sky is very blue."), "空", [
    ("空调","kōngtiáo","air conditioner","请把空调打开。","Please turn on the air conditioning."),
    ("有空","yǒu kòng","have free time","你明天有空吗？","Are you free tomorrow?"),
    ("太空","tàikōng","outer space","他想去太空旅行。","He wants to travel to outer space.")]),
 ]),
 ("手", [
  (("手机","shǒujī","mobile phone","我的手机没电了。","My phone is out of battery."), "机", [
    ("飞机","fēijī","airplane","我们坐飞机去上海。","We're flying to Shanghai."),
    ("机场","jīchǎng","airport","我去机场接你。","I'll pick you up at the airport."),
    ("司机","sījī","driver","出租车司机很友好。","The taxi driver is very friendly.")]),
  (("手表","shǒubiǎo","wristwatch","这块手表是我爸爸送的。","My father gave me this watch."), "表", [
    ("表示","biǎoshì","express, indicate","他点头表示同意。","He nodded to show agreement."),
    ("代表","dàibiǎo","represent; representative","她代表公司去开会。","She went to the meeting on behalf of the company."),
    ("表演","biǎoyǎn","perform; performance","孩子们的表演很精彩。","The children's performance was wonderful.")]),
  (("手工","shǒugōng","handmade; handicraft","这些杯子都是手工做的。","These cups are all handmade."), "工", [
    ("工作","gōngzuò","work, job","你在哪儿工作？","Where do you work?"),
    ("工人","gōngrén","worker","工厂里有很多工人。","There are many workers in the factory."),
    ("工厂","gōngchǎng","factory","他在一家工厂上班。","He works at a factory.")]),
 ]),
 ("中", [
  (("中国","Zhōngguó","China","我想去中国旅游。","I want to travel to China."), "国", [
    ("外国","wàiguó","foreign country","他是外国人。","He is a foreigner."),
    ("国王","guówáng","king","国王住在城堡里。","The king lives in a castle."),
    ("美国","Měiguó","USA","我住在美国。","I live in the USA.")]),
  (("中文","Zhōngwén","Chinese (language)","你会说中文吗？","Can you speak Chinese?"), "文", [
    ("文化","wénhuà","culture","我对中国文化很感兴趣。","I'm very interested in Chinese culture."),
    ("英文","Yīngwén","English (language)","这本书是英文的。","This book is in English."),
    ("文字","wénzì","writing, script","汉字是很古老的文字。","Chinese characters are a very ancient script.")]),
  (("中午","zhōngwǔ","noon","我们中午一起吃饭吧。","Let's have lunch together at noon."), "午", [
    ("上午","shàngwǔ","morning (before noon)","我上午有课。","I have class in the morning."),
    ("午饭","wǔfàn","lunch","午饭你想吃什么？","What do you want for lunch?"),
    ("午睡","wǔshuì","afternoon nap","我习惯午睡。","I usually take an afternoon nap.")]),
 ]),
 ("上", [
  (("上班","shàng bān","go to work","我每天坐地铁上班。","I take the subway to work every day."), "班", [
    ("班级","bānjí","class (group of students)","我们班级有三十个学生。","There are thirty students in our class."),
    ("加班","jiā bān","work overtime","今天晚上我要加班。","I have to work overtime tonight."),
    ("航班","hángbān","flight (scheduled)","我的航班晚点了。","My flight is delayed.")]),
  (("上网","shàng wǎng","go online","我每天晚上上网。","I go online every evening."), "网", [
    ("网站","wǎngzhàn","website","这个网站很有用。","This website is very useful."),
    ("网球","wǎngqiú","tennis","他喜欢打网球。","He likes playing tennis."),
    ("网络","wǎngluò","network; internet","今天网络很慢。","The internet is very slow today.")]),
  (("马上","mǎshàng","immediately","我马上就来。","I'll be right there."), "马", [
    ("马路","mǎlù","road, street","马路上车很多。","There are a lot of cars on the road."),
    ("骑马","qí mǎ","ride a horse","你会骑马吗？","Can you ride a horse?"),
    ("马虎","mǎhu","careless, sloppy","做作业不能马虎。","You can't be careless with homework.")]),
 ]),
 ("吃", [
  (("吃饭","chī fàn","eat (a meal)","我们去吃饭吧。","Let's go eat."), "饭", [
    ("米饭","mǐfàn","cooked rice","我要一碗米饭。","I'd like a bowl of rice."),
    ("饭店","fàndiàn","restaurant; hotel","这家饭店很有名。","This restaurant is very famous."),
    ("早饭","zǎofàn","breakfast","你吃早饭了吗？","Have you had breakfast?")]),
  (("好吃","hǎochī","tasty, delicious","这个菜真好吃！","This dish is really delicious!"), "好", [
    ("你好","nǐ hǎo","hello","你好，很高兴认识你。","Hello, nice to meet you."),
    ("好看","hǎokàn","good-looking; interesting (to watch)","这部电影很好看。","This movie is really good."),
    ("好像","hǎoxiàng","seem, as if","他好像不太高兴。","He doesn't seem very happy.")]),
  (("吃惊","chī jīng","be startled, surprised","听到这个消息，我很吃惊。","I was shocked to hear the news."), "惊", [
    ("惊喜","jīngxǐ","pleasant surprise","我给你准备了一个惊喜。","I've prepared a surprise for you."),
    ("震惊","zhènjīng","shocked; shock","这个消息让大家很震惊。","The news shocked everyone."),
    ("惊讶","jīngyà","amazed, astonished","她惊讶地看着我。","She looked at me in astonishment.")]),
 ]),
 ("看", [
  (("看见","kànjiàn","see, catch sight of","你看见我的钥匙了吗？","Have you seen my keys?"), "见", [
    ("再见","zàijiàn","goodbye","明天见，再见！","See you tomorrow, bye!"),
    ("见面","jiàn miàn","meet (face to face)","我们在哪儿见面？","Where shall we meet?"),
    ("意见","yìjiàn","opinion; objection","你有什么意见？","What's your opinion?")]),
  (("看书","kàn shū","read (a book)","我喜欢在床上看书。","I like reading in bed."), "书", [
    ("书店","shūdiàn","bookstore","学校旁边有一家书店。","There's a bookstore next to the school."),
    ("读书","dú shū","study; read books","他在国外读书。","He is studying abroad."),
    ("书包","shūbāo","schoolbag","我的书包很重。","My schoolbag is very heavy.")]),
  (("看病","kàn bìng","see a doctor","我下午要去医院看病。","I'm going to the hospital to see a doctor this afternoon."), "病", [
    ("病人","bìngrén","patient, sick person","医生正在给病人看病。","The doctor is examining a patient."),
    ("生病","shēng bìng","fall ill","她生病了，没来上课。","She got sick and didn't come to class."),
    ("毛病","máobìng","fault, problem, bad habit","我的车有点儿毛病。","My car has a bit of a problem.")]),
 ]),
 ("说", [
  (("说话","shuō huà","speak, talk","请慢一点儿说话。","Please speak a bit more slowly."), "话", [
    ("笑话","xiàohua","joke","他讲了一个笑话。","He told a joke."),
    ("对话","duìhuà","dialogue, conversation","请读这段对话。","Please read this dialogue."),
    ("话题","huàtí","topic of conversation","我们换个话题吧。","Let's change the subject.")]),
  (("说明","shuōmíng","explain; instructions","请说明一下原因。","Please explain the reason."), "明", [
    ("明天","míngtiān","tomorrow","明天见！","See you tomorrow!"),
    ("明白","míngbai","understand; clear","你明白我的意思吗？","Do you understand what I mean?"),
    ("聪明","cōngming","clever, smart","这个孩子很聪明。","This child is very clever.")]),
  (("听说","tīngshuō","hear (it said) that","听说你要结婚了？","I hear you're getting married?"), "听", [
    ("听见","tīngjiàn","hear","你听见了吗？","Did you hear that?"),
    ("好听","hǎotīng","pleasant to listen to","这首歌很好听。","This song sounds great."),
    ("听力","tīnglì","listening comprehension; hearing","我的听力还不太好。","My listening skills still aren't very good.")]),
 ]),
 ("钱", [
  (("钱包","qiánbāo","wallet","我的钱包丢了。","I lost my wallet."), "包", [
    ("面包","miànbāo","bread","早饭我吃面包。","I eat bread for breakfast."),
    ("包子","bāozi","steamed stuffed bun","这家的包子很好吃。","The buns here are delicious."),
    ("红包","hóngbāo","red envelope (gift money)","过年的时候孩子们收红包。","Children receive red envelopes at New Year.")]),
  (("金钱","jīnqián","money, wealth","金钱不能买到幸福。","Money can't buy happiness."), "金", [
    ("黄金","huángjīn","gold","黄金的价格涨了。","The price of gold has gone up."),
    ("金色","jīnsè","golden","她有一头金色的头发。","She has golden hair."),
    ("现金","xiànjīn","cash","可以用现金付款吗？","Can I pay in cash?")]),
  (("价钱","jiàqian","price","这个价钱太贵了。","This price is too high."), "价", [
    ("价格","jiàgé","price","这里的价格很便宜。","The prices here are cheap."),
    ("减价","jiǎn jià","reduce prices, discount","商店正在减价。","The shop is having a sale."),
    ("物价","wùjià","cost of living, prices","这个城市的物价很高。","The cost of living in this city is high.")]),
 ]),
 ("木", [
  (("木头","mùtou","wood, timber","这张桌子是木头做的。","This table is made of wood."), "头", [
    ("头发","tóufa","hair (on the head)","她的头发很长。","Her hair is very long."),
    ("头疼","tóuténg","headache; troublesome","我今天有点儿头疼。","I have a bit of a headache today."),
    ("石头","shítou","stone, rock","河边有很多石头。","There are many stones by the river.")]),
  (("树木","shùmù","trees","公园里的树木很多。","There are many trees in the park."), "树", [
    ("树叶","shùyè","leaf (of a tree)","秋天树叶变黄了。","In autumn the leaves turn yellow."),
    ("大树","dà shù","big tree","我们在大树下休息。","We rested under the big tree."),
    ("树林","shùlín","woods, grove","房子后面有一片树林。","There's a stretch of woods behind the house.")]),
  (("木耳","mù'ěr","wood ear fungus","我喜欢吃木耳炒肉。","I like wood ear stir-fried with pork."), "耳", [
    ("耳朵","ěrduo","ear","兔子的耳朵很长。","Rabbits have long ears."),
    ("耳机","ěrjī","earphones, headphones","我坐地铁的时候戴耳机。","I wear headphones on the subway."),
    ("耳环","ěrhuán","earring","这对耳环很漂亮。","This pair of earrings is very pretty.")]),
 ]),
 ("白", [
  (("白色","báisè","white (colour)","我喜欢白色的衣服。","I like white clothes."), "色", [
    ("颜色","yánsè","colour","你最喜欢什么颜色？","What's your favourite colour?"),
    ("红色","hóngsè","red","中国人过年喜欢红色。","Chinese people favour red at New Year."),
    ("特色","tèsè","characteristic, distinctive feature","这是本地的特色菜。","This is a local specialty dish.")]),
  (("白菜","báicài","Chinese cabbage","今天的白菜很便宜。","The cabbage is cheap today."), "菜", [
    ("点菜","diǎn cài","order food","服务员，我们要点菜。","Waiter, we'd like to order."),
    ("菜单","càidān","menu","请给我看一下菜单。","Please let me see the menu."),
    ("蔬菜","shūcài","vegetables","多吃蔬菜对身体好。","Eating more vegetables is good for your health.")]),
  (("白酒","báijiǔ","baijiu (Chinese spirit)","白酒很烈。","Baijiu is very strong."), "酒", [
    ("啤酒","píjiǔ","beer","来两瓶啤酒。","Two bottles of beer, please."),
    ("酒店","jiǔdiàn","hotel","我们住在机场附近的酒店。","We're staying at a hotel near the airport."),
    ("喝酒","hē jiǔ","drink alcohol","开车不能喝酒。","You mustn't drink and drive.")]),
 ]),
 ("门", [
  (("开门","kāi mén","open the door; open for business","商店九点开门。","The shop opens at nine."), "开", [
    ("开始","kāishǐ","begin, start","电影七点开始。","The movie starts at seven."),
    ("开车","kāi chē","drive (a car)","我爸爸每天开车上班。","My dad drives to work every day."),
    ("离开","líkāi","leave, depart","他昨天离开了北京。","He left Beijing yesterday.")]),
  (("门票","ménpiào","admission ticket","博物馆的门票多少钱？","How much is the museum admission?"), "票", [
    ("机票","jīpiào","plane ticket","我已经买好机票了。","I've already bought my plane ticket."),
    ("邮票","yóupiào","postage stamp","他喜欢收集邮票。","He likes collecting stamps."),
    ("投票","tóu piào","vote, cast a ballot","明天大家要投票。","Everyone votes tomorrow.")]),
  (("专门","zhuānmén","specially; specialized","我是专门来看你的。","I came specially to see you."), "专", [
    ("专业","zhuānyè","major (field of study); professional","你大学学什么专业？","What did you major in at university?"),
    ("专家","zhuānjiā","expert","他是这方面的专家。","He is an expert in this field."),
    ("专心","zhuānxīn","concentrate, focused","上课要专心听讲。","Pay close attention in class.")]),
 ]),
 ("爱", [
  (("爱好","àihào","hobby, interest","你有什么爱好？","What are your hobbies?"), "好", [
    ("好处","hǎochu","benefit, advantage","运动有很多好处。","Exercise has many benefits."),
    ("好人","hǎorén","good person","他是一个好人。","He is a good person."),
    ("友好","yǒuhǎo","friendly","这里的人很友好。","People here are very friendly.")]),
  (("可爱","kě'ài","cute, lovely","这只小狗真可爱！","This puppy is so cute!"), "可", [
    ("可以","kěyǐ","can, may; okay","我可以进来吗？","May I come in?"),
    ("可能","kěnéng","possible; maybe","明天可能会下雨。","It may rain tomorrow."),
    ("可是","kěshì","but, however","我想去，可是没有时间。","I'd like to go, but I don't have time.")]),
  (("爱情","àiqíng","romantic love","这是一部关于爱情的电影。","This is a film about love."), "情", [
    ("事情","shìqing","matter, thing, affair","我有一件事情要告诉你。","I have something to tell you."),
    ("感情","gǎnqíng","feelings, affection","他们的感情很好。","They're very close."),
    ("心情","xīnqíng","mood","今天我的心情不错。","I'm in a good mood today.")]),
 ]),
 ("时", [
  (("时间","shíjiān","time","你有时间吗？","Do you have time?"), "间", [
    ("房间","fángjiān","room","我的房间很小。","My room is small."),
    ("中间","zhōngjiān","middle, between","坐在我们中间吧。","Sit between us."),
    ("空间","kōngjiān","space, room","这个车的空间很大。","This car is very roomy.")]),
  (("时候","shíhou","time, moment, when","你什么时候来？","When are you coming?"), "候", [
    ("气候","qìhòu","climate","这里的气候很温和。","The climate here is mild."),
    ("问候","wènhòu","send regards, greet","请替我问候你父母。","Please give my regards to your parents."),
    ("等候","děnghòu","wait (for)","请在这里等候。","Please wait here.")]),
  (("同时","tóngshí","at the same time","他们同时到了。","They arrived at the same time."), "同", [
    ("同学","tóngxué","classmate","他是我的大学同学。","He was my university classmate."),
    ("同意","tóngyì","agree","我同意你的看法。","I agree with your view."),
    ("相同","xiāngtóng","identical, the same","我们的爱好相同。","We have the same hobbies.")]),
 ]),
 ("行", [
  (("银行","yínháng","bank","我要去银行取钱。","I need to go to the bank to withdraw money."), "银", [
    ("银色","yínsè","silver (colour)","她穿了一条银色的裙子。","She wore a silver skirt."),
    ("银子","yínzi","silver (metal, money)","古代人用银子买东西。","In ancient times people paid with silver."),
    ("银河","yínhé","Milky Way","夏天晚上可以看见银河。","You can see the Milky Way on summer nights.")]),
  (("旅行","lǚxíng","travel, journey","我们打算去云南旅行。","We're planning a trip to Yunnan."), "旅", [
    ("旅游","lǚyóu","tourism; to tour","很多人来这里旅游。","Many people come here as tourists."),
    ("旅馆","lǚguǎn","inn, small hotel","我们住在一家小旅馆。","We stayed at a small inn."),
    ("旅客","lǚkè","traveler, passenger","旅客们请上车。","Passengers, please board.")]),
  (("不行","bù xíng","no good; won't do","这样做不行。","Doing it this way won't work."), "不", [
    ("不错","búcuò","not bad, pretty good","你的中文说得不错。","Your Chinese is pretty good."),
    ("不用","búyòng","no need to","不用谢。","No need to thank me."),
    ("不同","bùtóng","different","我们的想法不同。","Our ideas are different.")]),
 ]),
 ("东", [
  (("东西","dōngxi","thing, stuff","我去超市买东西。","I'm going to the supermarket to buy things."), "西", [
    ("西红柿","xīhóngshì","tomato","我想买一斤西红柿。","I'd like to buy half a kilo of tomatoes."),
    ("西装","xīzhuāng","Western-style suit","他今天穿了一套西装。","He's wearing a suit today."),
    ("西北","xīběi","northwest","西北地区很干燥。","The northwest is very dry.")]),
  (("东方","dōngfāng","the East; east","太阳从东方升起。","The sun rises in the east."), "方", [
    ("地方","dìfang","place","这是什么地方？","What place is this?"),
    ("方便","fāngbiàn","convenient","住在这里交通很方便。","Transport is convenient living here."),
    ("方法","fāngfǎ","method, way","你有什么好方法？","Do you have a good method?")]),
  (("东北","dōngběi","northeast; Northeast China","东北的冬天很冷。","Winters in Northeast China are very cold."), "北", [
    ("北京","Běijīng","Beijing","北京是中国的首都。","Beijing is the capital of China."),
    ("北方","běifāng","the north","北方人喜欢吃面。","Northerners like eating noodles."),
    ("南北","nánběi","north and south","这条路是南北方向的。","This road runs north–south.")]),
 ]),
 ("女", [
  (("女儿","nǚ'ér","daughter","他有一个女儿。","He has a daughter."), "儿", [
    ("儿子","érzi","son","我儿子今年五岁。","My son is five this year."),
    ("儿童","értóng","children","这是儿童乐园。","This is a children's playground."),
    ("婴儿","yīng'ér","baby, infant","婴儿在睡觉。","The baby is sleeping.")]),
  (("美女","měinǚ","beautiful woman","她是有名的美女。","She is a famous beauty."), "美", [
    ("美丽","měilì","beautiful","这里的风景很美丽。","The scenery here is beautiful."),
    ("美食","měishí","fine food, delicacies","成都有很多美食。","Chengdu has lots of great food."),
    ("美元","Měiyuán","US dollar","一美元是多少人民币？","How many RMB is one US dollar?")]),
  (("妇女","fùnǚ","woman, women","三月八号是妇女节。","March 8th is Women's Day."), "妇", [
    ("夫妇","fūfù","married couple","那对夫妇很恩爱。","That couple is very devoted to each other."),
    ("主妇","zhǔfù","housewife","她是一个家庭主妇。","She is a housewife."),
    ("媳妇","xífu","daughter-in-law; wife (colloq.)","她是我们家的媳妇。","She married into our family.")]),
 ]),
 ("子", [
  (("桌子","zhuōzi","table, desk","桌子上有一本书。","There's a book on the table."), "桌", [
    ("书桌","shūzhuō","desk","我的书桌很乱。","My desk is messy."),
    ("饭桌","fànzhuō","dining table","全家人坐在饭桌旁。","The whole family sat around the dining table."),
    ("桌布","zhuōbù","tablecloth","这块桌布是新的。","This tablecloth is new.")]),
  (("鞋子","xiézi","shoes","这双鞋子很舒服。","These shoes are very comfortable."), "鞋", [
    ("皮鞋","píxié","leather shoes","他穿着黑色的皮鞋。","He's wearing black leather shoes."),
    ("拖鞋","tuōxié","slippers","进门请换拖鞋。","Please change into slippers when you come in."),
    ("鞋店","xiédiàn","shoe shop","那家鞋店在打折。","That shoe shop is having a sale.")]),
  (("房子","fángzi","house","他们买了一套新房子。","They bought a new house."), "房", [
    ("厨房","chúfáng","kitchen","妈妈在厨房做饭。","Mum is cooking in the kitchen."),
    ("书房","shūfáng","study (room)","爸爸在书房工作。","Dad is working in the study."),
    ("房东","fángdōng","landlord","房东人很好。","The landlord is very nice.")]),
 ]),
 ("路", [
  (("走路","zǒu lù","walk","我每天走路上学。","I walk to school every day."), "走", [
    ("走开","zǒukāi","go away","请你走开！","Please go away!"),
    ("走进","zǒujìn","walk into","她走进了教室。","She walked into the classroom."),
    ("逃走","táozǒu","escape, run away","小偷逃走了。","The thief ran away.")]),
  (("一路","yílù","all the way; the whole journey","一路上我们聊了很多。","We chatted a lot along the way."), "一", [
    ("一起","yìqǐ","together","我们一起去吧。","Let's go together."),
    ("一样","yíyàng","the same","我们的书一样。","Our books are the same."),
    ("一定","yídìng","certainly, must","我一定会来。","I'll definitely come.")]),
  (("道路","dàolù","road, path","这条道路很宽。","This road is very wide."), "道", [
    ("知道","zhīdào","know","我不知道他是谁。","I don't know who he is."),
    ("味道","wèidao","taste, flavour","这个汤味道很好。","This soup tastes great."),
    ("道理","dàoli","reason, principle, sense","你说得很有道理。","What you say makes a lot of sense.")]),
 ]),
 ("雨", [
  (("雨伞","yǔsǎn","umbrella","别忘了带雨伞。","Don't forget your umbrella."), "伞", [
    ("打伞","dǎ sǎn","hold up an umbrella","下雨了，快打伞。","It's raining—put up your umbrella."),
    ("阳伞","yángsǎn","parasol, sunshade","夏天她总是带着阳伞。","She always carries a parasol in summer."),
    ("伞兵","sǎnbīng","paratrooper","他以前是伞兵。","He used to be a paratrooper.")]),
  (("雨衣","yǔyī","raincoat","骑车的时候穿上雨衣。","Put on a raincoat when you ride your bike."), "衣", [
    ("衣服","yīfu","clothes","我去买衣服。","I'm going to buy clothes."),
    ("大衣","dàyī","overcoat","冬天要穿大衣。","You need an overcoat in winter."),
    ("毛衣","máoyī","sweater","这件毛衣很暖和。","This sweater is very warm.")]),
  (("雨季","yǔjì","rainy season","这里的雨季是六月到八月。","The rainy season here runs June to August."), "季", [
    ("季节","jìjié","season","你最喜欢哪个季节？","Which season do you like best?"),
    ("四季","sìjì","the four seasons","昆明四季如春。","Kunming is like spring all year round."),
    ("春季","chūnjì","spring (season)","春季是旅游的好时候。","Spring is a good time to travel.")]),
 ]),
 ("身", [
  (("身体","shēntǐ","body; health","祝你身体健康。","I wish you good health."), "体", [
    ("体育","tǐyù","sports, physical education","他很喜欢体育。","He loves sports."),
    ("体重","tǐzhòng","body weight","我的体重增加了。","I've gained weight."),
    ("具体","jùtǐ","specific, concrete","请说得具体一点儿。","Please be a bit more specific.")]),
  (("身边","shēnbiān","at one's side","我会一直在你身边。","I'll always be by your side."), "边", [
    ("旁边","pángbiān","beside, next to","银行在超市旁边。","The bank is next to the supermarket."),
    ("这边","zhèbiān","this side, over here","请往这边走。","This way, please."),
    ("海边","hǎibiān","seaside","我们去海边玩吧。","Let's go to the seaside.")]),
  (("身高","shēngāo","height (of a person)","你的身高是多少？","How tall are you?"), "高", [
    ("高兴","gāoxìng","happy, glad","认识你很高兴。","Nice to meet you."),
    ("高中","gāozhōng","senior high school","我弟弟在上高中。","My younger brother is in high school."),
    ("高铁","gāotiě","high-speed rail","坐高铁去上海很快。","Taking high-speed rail to Shanghai is fast.")]),
 ]),
 ("力", [
  (("能力","nénglì","ability, capability","她的工作能力很强。","She's very capable at her job."), "能", [
    ("能够","nénggòu","be able to","我希望能够帮助你。","I hope I can help you."),
    ("功能","gōngnéng","function, feature","这个手机有很多功能。","This phone has many features."),
    ("能源","néngyuán","energy (source)","我们要节约能源。","We should conserve energy.")]),
  (("力量","lìliang","strength, power, force","团结就是力量。","Unity is strength."), "量", [
    ("数量","shùliàng","quantity, amount","数量不够。","The quantity isn't enough."),
    ("质量","zhìliàng","quality","这家店的东西质量很好。","This shop's goods are high quality."),
    ("商量","shāngliang","discuss, consult","我们商量一下吧。","Let's talk it over.")]),
  (("压力","yālì","pressure, stress","最近工作压力很大。","Work has been very stressful lately."), "压", [
    ("血压","xuèyā","blood pressure","医生给我量了血压。","The doctor took my blood pressure."),
    ("气压","qìyā","air pressure","山上的气压比较低。","Air pressure is lower on the mountain."),
    ("压缩","yāsuō","compress","请把文件压缩一下。","Please compress the file.")]),
 ]),
 ("公", [
  (("公司","gōngsī","company, firm","他在一家大公司工作。","He works at a big company."), "司", [
    ("上司","shàngsi","boss, superior","我的上司很严格。","My boss is very strict."),
    ("司令","sīlìng","commander","他是部队的司令。","He is the commander of the troops."),
    ("司法","sīfǎ","judiciary, justice","司法要公正。","The judiciary must be impartial.")]),
  (("公园","gōngyuán","park","我们去公园散步吧。","Let's go for a walk in the park."), "园", [
    ("花园","huāyuán","garden","她家有一个小花园。","Her home has a small garden."),
    ("校园","xiàoyuán","campus","大学的校园很漂亮。","The university campus is beautiful."),
    ("果园","guǒyuán","orchard","秋天果园里有很多苹果。","In autumn the orchard is full of apples.")]),
  (("公里","gōnglǐ","kilometre","这里离机场二十公里。","It's twenty kilometres from here to the airport."), "里", [
    ("这里","zhèlǐ","here","这里的风景很好。","The scenery here is lovely."),
    ("哪里","nǎlǐ","where","你住在哪里？","Where do you live?"),
    ("心里","xīnli","in one's heart, inwardly","我心里很着急。","I was anxious inside.")]),
 ]),
 ("花", [
  (("花茶","huāchá","flower tea","我喜欢喝花茶。","I like drinking flower tea."), "茶", [
    ("喝茶","hē chá","drink tea","我们去喝茶吧。","Let's go have some tea."),
    ("茶叶","cháyè","tea leaves","这是今年的新茶叶。","These are this year's new tea leaves."),
    ("红茶","hóngchá","black tea","你要红茶还是绿茶？","Would you like black tea or green tea?")]),
  (("鲜花","xiānhuā","fresh flowers","他送了我一束鲜花。","He gave me a bunch of fresh flowers."), "鲜", [
    ("新鲜","xīnxiān","fresh","这些鱼很新鲜。","This fish is very fresh."),
    ("海鲜","hǎixiān","seafood","我对海鲜过敏。","I'm allergic to seafood."),
    ("鲜艳","xiānyàn","bright-coloured, vivid","她穿了一件鲜艳的裙子。","She wore a brightly coloured dress.")]),
  (("花瓶","huāpíng","vase","桌子上有一个花瓶。","There's a vase on the table."), "瓶", [
    ("瓶子","píngzi","bottle","瓶子里没有水了。","There's no water left in the bottle."),
    ("酒瓶","jiǔpíng","wine/liquor bottle","地上有很多空酒瓶。","There are lots of empty bottles on the floor."),
    ("瓶盖","pínggài","bottle cap","我打不开这个瓶盖。","I can't open this bottle cap.")]),
 ]),
 ("海", [
  (("海洋","hǎiyáng","ocean","地球上大部分是海洋。","Most of the Earth is ocean."), "洋", [
    ("西洋","xīyáng","the West (Western countries)","他在研究西洋音乐。","He studies Western music."),
    ("洋葱","yángcōng","onion","切洋葱的时候我会流眼泪。","I cry when I cut onions."),
    ("洋装","yángzhuāng","Western-style dress","她穿着一件白色洋装。","She's wearing a white dress.")]),
  (("海关","hǎiguān","customs (at a border)","过海关的时候要检查行李。","Your luggage is checked at customs."), "关", [
    ("关心","guānxīn","care about","谢谢你的关心。","Thank you for your concern."),
    ("关系","guānxi","relationship; connection","我们的关系很好。","We get along very well."),
    ("关门","guān mén","close the door; close (shop)","超市十点关门。","The supermarket closes at ten.")]),
  (("海报","hǎibào","poster","墙上贴着电影海报。","There's a movie poster on the wall."), "报", [
    ("报纸","bàozhǐ","newspaper","爷爷每天看报纸。","Grandpa reads the newspaper every day."),
    ("报名","bào míng","sign up, register","我报名参加了比赛。","I signed up for the competition."),
    ("报告","bàogào","report","明天我要交报告。","I have to hand in a report tomorrow.")]),
 ]),
]

# Character glosses. Pinyin with "/" marks characters with more than one reading;
# READINGS gives the contexts for those.
CHARS = {
"火":("huǒ","fire"),"车":("chē","vehicle"),"山":("shān","mountain"),"星":("xīng","star"),
"汽":("qì","steam, gas"),"站":("zhàn","station; to stand"),"票":("piào","ticket"),
"上":("shàng","up, above; to go up"),"下":("xià","down, below; to go down"),
"期":("qī","period of time"),"明":("míng","bright; next (day/year)"),
"人":("rén","person"),"口":("kǒu","mouth; opening"),"生":("shēng","life; be born; raw"),
"心":("xīn","heart, mind"),"门":("mén","door, gate"),"出":("chū","go out"),"语":("yǔ","language, speech"),
"学":("xué","study, learn"),"日":("rì","sun, day"),"医":("yī","medicine, doctor"),
"小":("xiǎo","small"),"开":("kāi","open; start; drive"),"中":("zhōng","middle, center"),
"水":("shuǐ","water"),"果":("guǒ","fruit; result"),"苹":("píng","apple (in 苹果)"),"汁":("zhī","juice"),
"结":("jié","tie, knot; conclude"),"平":("píng","flat, level, calm"),"安":("ān","peaceful, safe"),
"和":("hé","and; harmony, peace"),"时":("shí","time, hour"),"电":("diàn","electricity"),
"话":("huà","speech, words"),"脑":("nǎo","brain"),"影":("yǐng","shadow, image"),
"本":("běn","root, origin; measure word for books"),"来":("lái","come"),"书":("shū","book"),
"基":("jī","base, foundation"),"记":("jì","record, remember"),"得":("dé/de","obtain; (complement particle)"),
"忘":("wàng","forget"),"者":("zhě","one who (suffix)"),"假":("jiǎ/jià","false / holiday"),
"待":("dài","wait; treat"),"月":("yuè","moon, month"),"亮":("liàng","bright, light"),
"漂":("piào/piāo","pretty (in 漂亮) / float"),"光":("guāng","light, ray"),"饼":("bǐng","round flat cake"),
"干":("gān/gàn","dry / to do"),"煎":("jiān","pan-fry"),"大":("dà","big"),"份":("fèn","portion, share"),
"身":("shēn","body"),"省":("shěng","province; save"),"股":("gǔ","share, stock; strand"),
"家":("jiā","home, family"),"习":("xí","practice"),"校":("xiào","school"),"数":("shù/shǔ","number / to count"),
"国":("guó","country"),"回":("huí","return"),"孩":("hái","child"),"说":("shuō","speak, say"),
"天":("tiān","sky, heaven; day"),"气":("qì","air, gas, energy, spirit"),"空":("kōng/kòng","empty; sky / free time"),
"客":("kè","guest"),"午":("wǔ","noon"),"雨":("yǔ","rain"),"班":("bān","shift; class, team"),
"调":("tiáo/diào","adjust / tune, transfer"),"有":("yǒu","have, there is"),"太":("tài","too; extremely; great"),
"手":("shǒu","hand"),"机":("jī","machine; opportunity"),"飞":("fēi","fly"),"场":("chǎng","field, venue"),
"司":("sī","manage; department"),"表":("biǎo","surface; show; meter, watch"),"示":("shì","show, indicate"),
"代":("dài","replace; generation"),"演":("yǎn","perform, act"),"工":("gōng","work, labour"),
"作":("zuò","do, make"),"厂":("chǎng","factory"),"外":("wài","outside, foreign"),"王":("wáng","king"),
"美":("měi","beautiful; America"),"文":("wén","writing, culture"),"化":("huà","change, transform"),
"英":("yīng","hero; England"),"字":("zì","character, word"),"饭":("fàn","cooked rice, meal"),"睡":("shuì","sleep"),
"网":("wǎng","net, web"),"站":("zhàn","station; to stand"),"球":("qiú","ball"),"络":("luò","net-like, network"),
"马":("mǎ","horse"),"路":("lù","road"),"骑":("qí","ride (astride)"),"虎":("hǔ","tiger"),
"级":("jí","level, grade"),"加":("jiā","add"),"航":("háng","navigate, sail"),"吃":("chī","eat"),
"米":("mǐ","rice (uncooked); metre"),"店":("diàn","shop"),"早":("zǎo","early, morning"),
"好":("hǎo/hào","good / to like"),"你":("nǐ","you"),"看":("kàn","look, see, read"),"像":("xiàng","resemble, like"),
"惊":("jīng","startle, alarm"),"喜":("xǐ","happy; like"),"震":("zhèn","shake, quake"),"讶":("yà","surprised"),
"见":("jiàn","see, meet"),"再":("zài","again"),"面":("miàn","face; surface; noodles"),"意":("yì","meaning, idea"),
"读":("dú","read aloud, study"),"包":("bāo","bag; wrap"),"病":("bìng","illness"),"毛":("máo","hair, fur"),
"笑":("xiào","laugh, smile"),"对":("duì","correct; facing; pair"),"题":("tí","topic, question"),
"白":("bái","white; clear"),"聪":("cōng","clever; acute hearing"),"听":("tīng","listen, hear"),"力":("lì","strength, power"),
"钱":("qián","money"),"子":("zi/zǐ","(noun suffix) / child, seed"),"红":("hóng","red"),"金":("jīn","gold, metal"),
"黄":("huáng","yellow"),"色":("sè","colour"),"现":("xiàn","present, now; appear"),"价":("jià","price, value"),
"格":("gé","grid; standard"),"减":("jiǎn","reduce, subtract"),"物":("wù","thing, matter"),
"木":("mù","tree, wood"),"头":("tóu","head; (noun suffix)"),"发":("fā/fà","send out / hair"),"疼":("téng","ache, hurt"),
"石":("shí","stone"),"树":("shù","tree"),"叶":("yè","leaf"),"林":("lín","forest, grove"),"耳":("ěr","ear"),
"朵":("duǒ","(measure word for flowers, clouds)"),"环":("huán","ring, loop"),"颜":("yán","face; colour"),
"特":("tè","special"),"菜":("cài","vegetable; dish"),"点":("diǎn","point, dot; o'clock; to order"),"单":("dān","single; list"),
"蔬":("shū","vegetables"),"酒":("jiǔ","alcohol, wine"),"啤":("pí","beer (in 啤酒)"),"喝":("hē","drink"),
"始":("shǐ","begin"),"离":("lí","leave; be apart from"),"邮":("yóu","post, mail"),"投":("tóu","throw, cast"),
"专":("zhuān","special, focused"),"业":("yè","line of work, trade"),"爱":("ài","love"),"处":("chù/chǔ","place / handle"),
"友":("yǒu","friend"),"可":("kě","can, may; but"),"以":("yǐ","by means of"),"能":("néng","able, can; energy"),
"是":("shì","to be"),"情":("qíng","feeling, emotion; situation"),"事":("shì","matter, affair"),"感":("gǎn","feel, sense"),
"间":("jiān","room; between; interval"),"房":("fáng","house, room"),"候":("hòu","wait; season, time"),
"问":("wèn","ask"),"等":("děng","wait; etc."),"同":("tóng","same; together"),"相":("xiāng","mutual, each other"),
"行":("xíng/háng","walk, go; OK / row, firm"),"银":("yín","silver"),"河":("hé","river"),"旅":("lǚ","travel"),
"游":("yóu","swim; tour"),"馆":("guǎn","hall, building (public)"),"不":("bù","not"),"错":("cuò","wrong, mistake"),
"用":("yòng","use"),"东":("dōng","east"),"西":("xī","west"),"瓜":("guā","melon"),"方":("fāng","direction; square; method"),
"餐":("cān","meal"),"地":("dì","earth, ground, place"),"便":("biàn/pián","convenient / cheap (in 便宜)"),
"法":("fǎ","law, method"),"北":("běi","north"),"京":("jīng","capital"),"南":("nán","south"),
"女":("nǚ","woman, female"),"儿":("ér","son, child; (diminutive suffix)"),"童":("tóng","child"),
"婴":("yīng","infant"),"丽":("lì","beautiful"),"食":("shí","food; eat"),"元":("yuán","yuan, dollar; first"),
"妇":("fù","woman, wife"),"夫":("fū","husband, man"),"主":("zhǔ","master, main"),"媳":("xí","daughter-in-law"),
"桌":("zhuō","table"),"布":("bù","cloth"),"鞋":("xié","shoe"),"皮":("pí","skin, leather"),"拖":("tuō","drag, pull"),
"厨":("chú","kitchen"),"走":("zǒu","walk, leave"),"进":("jìn","enter"),"逃":("táo","flee, escape"),
"一":("yī","one"),"起":("qǐ","rise, get up"),"样":("yàng","appearance, kind"),"定":("dìng","fix, decide, certain"),
"道":("dào","way, road; principle; say"),"知":("zhī","know"),"味":("wèi","taste, flavour"),"理":("lǐ","reason, logic"),
"伞":("sǎn","umbrella"),"打":("dǎ","hit; (general action verb)"),"阳":("yáng","sun; yang"),"兵":("bīng","soldier"),
"衣":("yī","clothing"),"服":("fú","clothes; serve; obey"),"季":("jì","season"),"节":("jié","festival; section, joint"),
"四":("sì","four"),"春":("chūn","spring"),"体":("tǐ","body; form, style"),"育":("yù","educate, raise"),
"重":("zhòng/chóng","heavy / again"),"具":("jù","tool; concrete"),"边":("biān","side, edge"),"旁":("páng","beside"),
"这":("zhè","this"),"海":("hǎi","sea"),"高":("gāo","tall, high"),"兴":("xìng/xīng","interest, mood / prosper"),
"铁":("tiě","iron"),"够":("gòu","enough"),"功":("gōng","merit, effect"),"源":("yuán","source"),
"量":("liàng/liáng","quantity / to measure"),"质":("zhì","quality, nature"),"商":("shāng","trade; discuss"),
"压":("yā","press, pressure"),"血":("xuè","blood"),"缩":("suō","shrink"),"公":("gōng","public; male"),
"令":("lìng","order, command"),"园":("yuán","garden, park"),"花":("huā","flower; spend"),"里":("lǐ","inside; Chinese mile"),
"哪":("nǎ","which, where"),"茶":("chá","tea"),"鲜":("xiān","fresh"),"新":("xīn","new"),"艳":("yàn","colourful, gorgeous"),
"瓶":("píng","bottle, vase"),"盖":("gài","lid; cover"),"洋":("yáng","ocean; foreign"),"葱":("cōng","scallion, onion"),
"装":("zhuāng","clothing; install; pretend"),"关":("guān","close; pass; concern"),"系":("xì","system; relate"),
"报":("bào","report; newspaper"),"纸":("zhǐ","paper"),"名":("míng","name"),"告":("gào","tell, inform"),
"爸":("bà","dad"),
}

# Polyphonic characters: all readings with an example of each.
READINGS = {
"行":"xíng — walk; OK (旅行, 不行) · háng — row; firm (银行, 航班行业)",
"好":"hǎo — good (好吃, 你好) · hào — to like (爱好)",
"空":"kōng — empty; sky (天空, 空气) · kòng — free time (有空)",
"得":"dé — obtain (得到) · de — complement particle (说得好) · děi — must (我得走了)",
"假":"jiǎ — false (假的) · jià — holiday (假期)",
"调":"tiáo — adjust (空调) · diào — tune; transfer (调查)",
"干":"gān — dry (饼干, 干净) · gàn — to do (干活)",
"数":"shù — number (数学) · shǔ — to count (数一数)",
"发":"fā — send, emit (发现) · fà — hair (头发, said fa)",
"处":"chù — place (好处) · chǔ — handle (处理)",
"便":"biàn — convenient (方便) · pián — cheap (便宜)",
"重":"zhòng — heavy (体重) · chóng — again (重复)",
"兴":"xìng — mood (高兴) · xīng — prosper (兴奋)",
"量":"liàng — quantity (数量, 力量) · liáng — measure (量血压)",
"漂":"piào — pretty (漂亮) · piāo — float (漂流)",
"子":"zi — neutral noun suffix (桌子) · zǐ — child, seed (孔子)",
"长":"cháng — long · zhǎng — grow",
"乐":"lè — happy · yuè — music",
"觉":"jué — feel · jiào — sleep",
"还":"hái — still · huán — return",
}

TREES.append(
 ("瓜", [
  (("西瓜","xīguā","watermelon","夏天吃西瓜最舒服。","Watermelon is perfect in summer."), "西", [
    ("西边","xībian","west side","太阳从西边落下。","The sun sets in the west."),
    ("西方","xīfāng","the West; west","他研究西方哲学。","He studies Western philosophy."),
    ("西餐","xīcān","Western food","今天我们吃西餐吧。","Let's have Western food today.")]),
  (("南瓜","nánguā","pumpkin","万圣节的时候人们做南瓜灯。","People make pumpkin lanterns at Halloween."), "南", [
    ("南方","nánfāng","the south","南方的冬天不太冷。","Winters in the south aren't very cold."),
    ("南边","nánbian","south side","学校在公园南边。","The school is south of the park."),
    ("南方人","nánfāngrén","southerner","他是南方人，喜欢吃米饭。","He's a southerner and likes rice.")]),
  (("瓜子","guāzǐ","melon seeds","过年的时候大家一边聊天一边吃瓜子。","At New Year people chat and crack melon seeds."), "子", [
    ("孩子","háizi","child","他们有两个孩子。","They have two children."),
    ("儿子","érzi","son","我儿子今年五岁。","My son is five this year."),
    ("桌子","zhuōzi","table, desk","桌子上有一本书。","There's a book on the table.")]),
 ]))

# Split trees: a word at the top, broken into its two characters,
# each of which branches into 3 words (the 你好 pattern).
SPLITS = [
 (("你好","nǐ hǎo","hello","你好，很高兴认识你。","Hello, nice to meet you."), [
   ("你", [("你们","nǐmen","you (plural)","你们好！","Hello, everyone!"),
           ("你的","nǐ de","your, yours","这是你的书吗？","Is this your book?"),
           ("你家","nǐ jiā","your home / your family","你家在哪儿？","Where is your home?")]),
   ("好", [("好吃","hǎochī","tasty, delicious","这个菜真好吃！","This dish is really delicious!"),
           ("好看","hǎokàn","good-looking; interesting (to watch)","这部电影很好看。","This movie is really good."),
           ("好朋友","hǎo péngyou","good friend","他是我的好朋友。","He is my good friend.")])]),
 (("老师","lǎoshī","teacher","我们的老师很有耐心。","Our teacher is very patient."), [
   ("老", [("老人","lǎorén","elderly person","我们要尊重老人。","We should respect the elderly."),
           ("老板","lǎobǎn","boss, shop owner","老板，这个多少钱？","Boss, how much is this?"),
           ("老家","lǎojiā","hometown","我老家在四川。","My hometown is in Sichuan.")]),
   ("师", [("师傅","shīfu","master; (polite address for skilled worker)","师傅，去火车站。","Driver, to the train station please."),
           ("律师","lǜshī","lawyer","她想当律师。","She wants to be a lawyer."),
           ("厨师","chúshī","chef, cook","这个饭店的厨师很有名。","This restaurant's chef is famous.")])]),
 (("喜欢","xǐhuan","like","我喜欢学中文。","I like learning Chinese."), [
   ("喜", [("恭喜","gōngxǐ","congratulations","恭喜你找到新工作！","Congratulations on your new job!"),
           ("喜爱","xǐ'ài","love, be fond of","这本书很受孩子们喜爱。","This book is loved by children."),
           ("喜事","xǐshì","happy occasion (esp. wedding)","他们家最近有喜事。","Their family has a happy occasion coming up.")]),
   ("欢", [("欢迎","huānyíng","welcome","欢迎来我家！","Welcome to my home!"),
           ("欢乐","huānlè","joyful, happy","节日里到处都很欢乐。","Everywhere is joyful during the holiday."),
           ("欢笑","huānxiào","laugh happily","房间里充满了欢笑声。","The room was full of laughter.")])]),
 (("汉字","Hànzì","Chinese character","汉字很难写。","Chinese characters are hard to write."), [
   ("汉", [("汉语","Hànyǔ","Chinese language","我在学习汉语。","I'm studying Chinese."),
           ("汉族","Hànzú","Han ethnicity","汉族是中国人口最多的民族。","The Han are China's largest ethnic group."),
           ("好汉","hǎohàn","hero, brave man","不到长城非好汉。","You're not a hero until you've climbed the Great Wall.")]),
   ("字", [("名字","míngzi","name","你叫什么名字？","What's your name?"),
           ("字典","zìdiǎn","(character) dictionary","我查了一下字典。","I looked it up in the dictionary."),
           ("写字","xiě zì","write (characters)","孩子正在学写字。","The child is learning to write.")])]),
 (("快乐","kuàilè","happy","祝你新年快乐！","Happy New Year!"), [
   ("快", [("快点","kuài diǎn","hurry up","快点，要迟到了！","Hurry up, we'll be late!"),
           ("快递","kuàidì","courier, express delivery","我的快递到了。","My delivery has arrived."),
           ("愉快","yúkuài","pleasant, cheerful","祝你周末愉快。","Have a pleasant weekend.")]),
   ("乐", [("音乐","yīnyuè","music","我喜欢听音乐。","I like listening to music."),
           ("乐观","lèguān","optimistic","她是一个很乐观的人。","She's a very optimistic person."),
           ("可乐","kělè","cola","我要一杯可乐。","I'll have a cola.")])]),
 (("觉得","juéde","feel, think","我觉得这个主意很好。","I think this is a good idea."), [
   ("觉", [("睡觉","shuì jiào","sleep, go to bed","我十一点睡觉。","I go to bed at eleven."),
           ("感觉","gǎnjué","feel; feeling","我感觉有点儿冷。","I feel a bit cold."),
           ("觉悟","juéwù","awareness, consciousness","他的觉悟很高。","He has a high level of awareness.")]),
   ("得", [("得到","dédào","get, obtain","他得到了一个好机会。","He got a good opportunity."),
           ("获得","huòdé","gain, win","她获得了第一名。","She won first place."),
           ("值得","zhídé","be worth","这本书值得一看。","This book is worth reading.")])]),
 (("长城","Chángchéng","the Great Wall","我们明天去爬长城。","We're climbing the Great Wall tomorrow."), [
   ("长", [("长短","chángduǎn","length","这条裤子长短正好。","These trousers are just the right length."),
           ("校长","xiàozhǎng","headmaster, principal","校长在开会。","The principal is in a meeting."),
           ("成长","chéngzhǎng","grow up, develop","孩子们成长得很快。","The children are growing up fast.")]),
   ("城", [("城市","chéngshì","city","上海是一个大城市。","Shanghai is a big city."),
           ("进城","jìn chéng","go into town","我明天要进城买东西。","I'm going into town tomorrow to shop."),
           ("城墙","chéngqiáng","city wall","西安的城墙很有名。","Xi'an's city wall is famous.")])]),
 (("还是","háishi","or (in questions); still, had better","你喝茶还是咖啡？","Would you like tea or coffee?"), [
   ("还", [("还有","hái yǒu","also, in addition","还有别的问题吗？","Are there any other questions?"),
           ("还钱","huán qián","repay money","他明天还钱。","He'll pay the money back tomorrow."),
           ("还书","huán shū","return a book","我要去图书馆还书。","I need to return a book to the library.")]),
   ("是", [("但是","dànshì","but","他很累，但是很开心。","He's tired but happy."),
           ("就是","jiùshì","precisely, exactly","对，就是他！","Yes, it's him!"),
           ("是的","shì de","yes, that's right","是的，我是老师。","Yes, I'm a teacher.")])]),
]

CHARS.update({
"瓜":("guā","melon, gourd"),"们":("men","(plural suffix for people)"),"的":("de/dí","(possessive particle) / true"),
"朋":("péng","friend"),"老":("lǎo","old; (prefix of familiarity)"),"板":("bǎn","board, plank"),
"师":("shī","teacher, master"),"傅":("fù","tutor, master"),"律":("lǜ","law, rule"),"欢":("huān","joyous"),
"迎":("yíng","welcome, greet"),"恭":("gōng","respectful"),"汉":("hàn","Han Chinese; man"),"族":("zú","clan, ethnic group"),
"典":("diǎn","canon, standard work"),"写":("xiě","write"),"快":("kuài","fast; happy; soon"),"递":("dì","hand over, deliver"),
"愉":("yú","pleasant"),"乐":("lè/yuè","happy / music"),"音":("yīn","sound"),"观":("guān","view, observe"),
"觉":("jué/jiào","feel; aware / sleep"),"悟":("wù","realize, awaken"),"获":("huò","obtain, win"),"值":("zhí","value; be worth"),
"长":("cháng/zhǎng","long / grow; chief"),"短":("duǎn","short"),"成":("chéng","become, accomplish"),"城":("chéng","city, city wall"),
"市":("shì","market, city"),"墙":("qiáng","wall"),"还":("hái/huán","still, also / return"),"但":("dàn","but"),"就":("jiù","just, then"),
"柿":("shì","persimmon"),"耐":("nài","endure"),
})
CHARS["到"]=("dào","arrive; to (a place)")
