    https://www.youtube.com/watch?v=_XTBGiMaVEg
    
    ***
    
    DEVELOPING AN EFFICIENT CRYPTOCURRENCY TRADING BOT
    Asrın ÖZTİN - BİLGİSAYAR MÜHENDİSLİĞİ - LİSANS TEZİ - Haziran 2022
    Asrın ÖZTİN - COMPUTER ENGINEERING - LICENSE THESIS - Haziran 2022

 
# ÖZET
Bu çalışmada teknik analiz, indikatörlerin çalışma prensipleri, ve kural bazlı alım-satımstratejilerinde dikkat edilmesi gereken hususlar açıklanmış, açıklanan strateji tasarımı özellikleri geçmişe yönelik test edilmiş, ve sonuçları kıyaslanmış; karar verilen tasarım üzerinden farklı indikatörler ile geçmişe yönelik testler yapılmış ve sonuçları kıyaslanarak görece en başarılı strateji tercih edilip python programlama dilinde Binance platformu API’leri aracılığıyla alım-satım işlemi yapan bir kripto para botu geliştirilmiştir.

Geçmişe yönelik testlerde veri çeşitliliği sağlanarak, deneyler olabildiğince yanlılık içermeyen bir şekilde tasarlanmıştır. Deneyler, rastgele seçilen ve 5erli gruplar halinde yatay piyasa, yükselen piyasa ve düşen piyasa şeklinde ayrıştırılan 15 sembol verisi üzerinden gerçekleştirilmiştir. Deneylerdeki başarı metrikleri, getiri yüzdesi, beklenen HODL getirisi yüzdesi, kayıp yaşatan işlem sayısı, kazanç getiren işlem sayısı ve kazançlı işlem sayısı / kayıplı işlem sayısı oranı olarak seçilmiştir.

Araştırmalar ile elde edilen bilgiler ve deneyler ile elde edilen destekleyici bulgular doğrultusunda, stratejilerin tasarımında bir filtre ve bir tetikleyici kullanımına karar verilmiştir. Geçmişe yönelik testlerde, filtreleme görevinde Ağırlıklı Hareketli Ortalama (WMA) göstergesi ve Parabolik Sar (PSAR) göstergesi; tetikleme görevinde Hareketli Ortalamaların Yakınsaması Iraksaması (MACD) göstergesi kullanılan stratejinin görece daha başarılı olduğu gözlemlenmiştir. Burada başarı metriği, getiri oranı olarak seçilerek ofansif bir strateji tercihi yapılmıştır.

Elde edilen çıktılar doğrultusunda seçilen strateji, python programlama dili kullanılarak hayata geçirilmiştir. Çalışmada ve geliştirilen yazılımda, piyasa verilerinin elde edilmesi, işlemlerin gerçekleştirilmesi, portföye erişilebilmesi gibi tüm broker işlemleri Binance API’lerini arka planda kullanan 3.parti python-binance kütüphanesi aracılığıyla sağlanmıştır.

Sonuç olarak, amaçlandığı üzere piyasanın üzerine çıkarak getiri elde edebilen stratejiler geliştirilerek, görece başarılı bulunan strateji ile çalışan bir kripto para alım-satım botu geliştirilmiştir.


    ANAHTAR KELİMELER: Algo-trading, Algoritmik trading, Binance, Borsa, Finans, Kripto para

 
# ABSTRACT
In this study, technical analysis, the working principles of indicators and the points to be considered in rule-based trading strategies were explained, the described strategy design features were backtested, and the results were compared; Based on the design that was decided on, backtests were made with different indicators and the results were compared, then the most successful strategy was preferred, and a cryptocurrency bot in python programming language that trades through Binance platform APIs was developed.

By providing data diversity in backtests, the experiments were designed in a way that is as bias-free as possible. Experiments were carried out on 15 symbol data, which were randomly selected, and separated into groups of 5 as horizontal market, rising market, and falling market. The success metrics in the experiments were chosen as the percentage of return, the percentage of expected HODL return, the number of losing transactions, the number of profitable transactions, and the number of profitable transactions / the number of losing transactions ratio.

In line with the information obtained from the researches and the supporting findings obtained from the experiments, it was decided to use a filter and a trigger in the design of the strategies. In backtests, it has been observed that the strategy which uses Weighted Moving Average (WMA) and Parabolic Sar (PSAR) indicators in the filtering task; Moving Average Convergence Divergence (MACD) indicator in the triggering task is relatively being more successful. Here, an offensive strategy was chosen by choosing the success metric as the rate of return.

The strategy chosen in line with the results obtained was implemented using the python programming language. In the study and the developed software, all broker operations such as obtaining market data, performing transactions, and accessing the portfolio are provided through the 3rd party python-binance library that uses Binance APIs in the background.

As a result, a cryptocurrency trading bot that works with a relatively successful strategy has been developed by developing strategies that are profitable by going above the market as intended.


    KEYWORDS: Algo-trading, Algorithmic Trading, Binance, Cryptocurrency, Finance, Stock
		
 
# ÖNSÖZ
İstatistik bilimine olan ilgim, grafikleri doğru yorumlayabileceğim düşüncesi ve maddi kazanç hevesim doğrultusunda, bu tezin hazırlanmasından yaklaşık olarak 2 yıl kadar önce Borsa İstanbul’da yer alan hisse senetleri üzerinde alım satım yapma kararı aldım. İlk aşama olarak teknik analizi olabildiğince öğrendim ve bir hisse senedinin değerlendirmesini yapmak, alıp satmaya karar vermek için gerekli olan tüm koşulları araştırdım. Bilgisayar mühendisliği bölümünün bana kazandırmış olduğu alışkanlıklardan biridir ki, bütün bu değerlendirme aşamalarını sistematik bir hale getirecek şekilde bir dosyaya not aldım ve her bir hisse senedi için aynı aşamaları, hiçbirini atlamadan her seferinde uygulayarak kazanç elde ettim. Günlük %10 değişim kotası bir yerden sonra az gelmeye başladığı için bu tarz kısıtlamaların olmadığı kripto para piyasasına yönlendim ve bu aşamada 7/24 takipte ve tetikte olmalıyım gibi endişelerim olduğu için hiçbir zaman bu piyasalarda yatırım yapamadım. Bu süreci nasıl yöneteceğime karar verebilmek için, görece iyi yönetebilen insanların fikirlerine internet üzerinden araştırmalar yaparak ulaştım ve hali hazırda sistematik hale getirmiş olduğum alım satım değerlendirme aşamalarının API’ler aracılığı ile kripto para piyasalarında tetikleyici olarak kullanılabildiğini gördüm. Teoride geriye kalan tüm aşamalar sadece biraz kodlama bilgisiydi, fakat kullandığım stratejilerin uzun vadedeki etkilerini kesin olarak kestiremediğim için deneyler yapmam gerekliydi. Bu aşamada üzerinde çalışmaya ve kendimi eğitmeye bugünden yaklaşık 1 yıl kadar öncesinde başladığım veri bilimi devreye girdi. Yine istatistik ilgimden kaynaklı ilgilendiğim bu alanda, sıkıcı olarak gördüğüm “ev fiyatı tahminleme” gibi standart uygulamalardan sıyrılarak, veri bilimi için kilit bir rolü olan, kendi projemi geliştirmek, veri setleri ile uzun bir zaman geçirmek, internette hazır çözümü olmayan bir problemi çözmek için çabalamak gibi konularda, üzerinde severek çalıştığım bu projeye sahip olmak kendimi geliştirmemde çok büyük katkı sağladı. İlk başta makine öğrenimi modellerini kullanarak fiyat bilgilerini tahminlemeye çalışırken, sonrasında bu tarz tahminlerin, değişim kotası olmayan kripto para piyasasında ani değişiklikleri yanlış öngördüğü taktirde büyük kayıplara yol açabileceklerini düşündüm. Finansta davranışsal analiz üzerine araştırmalar yaptım ve Etkin Piyasalar Hipotezinin ön koşullarından olan teorik piyasaların gerçek hayatta karşımıza çıkmadığını bir kez daha görmüş oldum. Ek olarak piyasa manipülasyonlarına her açıdan açık olan, örneğin atılan bir tweet üzerinden bile hızlı bir şekilde yüksek miktarlarda etkilenebilen bu piyasada, tahminlemelerin geçerli olabilmesi için çok büyük bir veriye gerek olması, yeterli veri elde olsa dahi veriyi işleyerek anlamlı sonuçlar elde etmenin zor olması ve bunlar sağlandığı taktirde bile öngörülen sonuçların yanlış öngörülme durumlarında büyük kayıplar yaşatacak olması üzerine, tahminleme üzerine kurulan modelleri kullanmaktan ve aylarca üzerinde uğraştığım veri bilimi ve makine öğrenimi çalışmalarından vazgeçtim. Tahminler ile değil, gecikmeli bile olsa göstergeler ile; yani gelecekteki olası veriler ile değil, şu anda elimizde olan reel veriler ile hareket edilmesini mantıklı bulduğum için, teknik analizin programlama dünyasında nasıl kullanıldığına dair araştırmalar yapmaya başladım. Aylarca süren bu araştırma ve geliştirme sürecinden sonra bu çalışmada yer alan bilgileri ve bulguları elde ettim. İlk kez bir tez hazırlamakta olduğum için araştırma geliştirme aşamalarımı bir dokümana aktarmakta sıkıntılar çektim, bir deneyin çıktısını biliyorken bile o deneyi burada kanıtlama gerekliliğimden kaynaklı, tekrar ve tekrar, hali hazırda bildiğim sonuçları elde etmek için çalışmalarımı düzgün birer deney haline getirip, daha sezgisel olan bilgi ve bulguları resmiyete dökmem gerekti. İyi yanı ise şu anda bu yazıyı okuyan sizlerin benim çalışmalarımı kullanarak daha iyi sistemler geliştirebileceğinizi biliyor olmak oldu. Faydalı olacağını düşündüğüm birçok bilgiyi ve benim için elde etmesi, tasarlaması zamanımı alan birçok kod parçasını ve mantalitelerini olabildiğince açık bir şekilde dokümana ekledim. Daha fazla bilgi edinmek, tanışmak, bir konuda danışmak, çalışmamda bulduğunuz bir hatayı düzeltmek için ve/veya herhangi bir sebepten, benim ile son kısımda bulabileceğiniz iletişim bilgilerim üzerinden temasa geçebilirsiniz. İyi çalışmalar dilerim.

Son olarak kaynaklarını referans göstererek çalışma boyunca teknik analize dair birçok kısımda kullandığım ve teknik analize attığım ilk adımlarda bana, herkese açık bir şekilde sundukları kaynaklar ile çok yardımcı olan Anıl ÖZEKŞİ’ye ve Kıvanç ÖZBİLGİÇ’e özellikle teşekkür ediyorum.

# PREFACE
In line with my interest in statistics, the thought that I can interpret the graphics correctly, and my enthusiasm for financial gain, I have decided to trade stocks in Borsa Istanbul approximately 2 years before the preparation of this very thesis. As a first step, I have learned as much technical analysis as possible and researched all the conditions necessary to evaluate a stock and decide to buy or sell. It is one of the habits that the computer engineering department has given me, that I took notes in a file to systematize all these evaluation stages, and I made profits by applying the same steps for each stock without skipping any of them. Since the daily 10% exchange quota started to become less after a while, I turned to the cryptocurrency market, where there are no such restrictions, and at this stage, I have never been able to invest in these markets, as I have concerns such as 24/7 monitoring and alertness. In order to decide how to manage this process, I have reached the ideas of people who can manage it relatively well by doing research on the internet and I saw that the trading evaluation stages that I have already systematized can be used as a trigger in the cryptocurrency markets through APIs. All the remaining steps in theory were just a little bit of coding knowledge, but I had to do experiments because I was not able to predict the long-term effects of the strategies I have been using. At this stage, data science, which I have started working on and educating myself about a year ago, came into play. Again, due to my interest in statistics, in this field I am interested in, having that project that I have been working on with pleasure, helped me a lot to improve myself on the subjects that are essential in data science such as spending a long time with a dataset, trying to solve a problem that has no direct answer on the web, and running my own project by getting rid of the standard applications such as “house price prediction” which I consider as boring. At first, I was trying to predict price information using machine learning models, but then I thought that such predictions could lead to huge losses if they incorrectly predicted sudden changes in the cryptocurrency market, which has no change quota. I have done research on the topic behavioral analysis in finance and once again, I have seen that theoretical markets, one of the prerequisites of the Efficient Market Hypothesis, do not appear in real life. In addition, in this market, which is open to market manipulations in all aspects, for example, which can be rapidly affected by a tweet, very large data is required for the predictions to be valid, even if sufficient data is available, it is difficult to obtain meaningful results by processing the data, and these I gave up on using models based on prediction and on data science and machine learning studies that I had been working on for months, as the predicted results would cause great losses in case of incorrect prediction even if it is provided. Since I find more logical that acting not with estimations but with indicators, that is not acting with possible future data but acting with real data that is available now, even with a delay, I have started to do research on how technical analysis is used in the programming world. After months of research and development, I have obtained the information and findings contained in this study. Since I was preparing a thesis for the first time, I had difficulties in documenting my research and development stages. Even when I knew the output of an experiment, I needed to prove the experiment here again and again and had to turn my studies into neat experiments and formalized the more intuitive information and findings in order to obtain the results I already know. The good thing is to know that you, who are reading this article right now can develop better systems using my work. I have included a lot of information that I think will be useful, and many pieces of code and mentalities that took my time to obtain and design, as clearly as possible. You can contact me via my contact information, which you can find in the last section, to learn more, to meet, to consult on a subject, to correct an error you find in my work and/or for any reason. I wish you good work.

Finally, I like to especially thank to Anıl ÖZEKŞİ and Kıvanç ÖZBİLGİÇ whose I have used sources in many parts of this study and helped me a lot with their open-to-everyone sources in my personal first steps in technical analysis.


# Table of Contents
    ÖZET
    ABSTRACT
    ÖNSÖZ
    PREFACE
    AKADEMİK BEYAN
    1.	Introduction
    2.	Technical Analysis
    2.1.	Dow Theory
    2.1.1.	The Markets Discount Everything
    2.1.2.	The Markets Have 3 Trends
    2.1.3.	The Market Trends Have 3 Phases
    2.1.4.	Indices Must Confirm Each Other
    2.1.5.	Volume Must Confirm the Trend
    2.1.6.	A Trend Is Said to Be Continuous Until a Reversal Is Confirmed
    2.2.	Indicators
    2.2.1.	Trend Indicators
    2.2.2.	Volatility
    3.	Methodology
    4.	Strategies
    4.1.	How To Create Strategies?
    4.1.1.	How To Choose Indicators?
    4.1.2.	How to Choose Indicator Parameters?
    4.1.3.	How To Choose Timeframes?
    4.2.	Backtest
    4.3.	Tests
    4.3.1.	Getting Historical Data
    4.3.2.	Preprocessing
    4.3.3.	Experiments
    4.3.4.	Findings
    5.	Source Code
    5.1.	Python-binance Library Documents
    5.1.1.	Wallet Endpoints
    5.1.2.	Market Data Endpoints
    5.1.3.	Spot Account Trade Endpoints
    5.2.	Code Design
    5.2.1.	Classes
    5.2.2.	UML    
    6.	References    
    7.	License
    8.	Disclaimer    


# 1.	Introduction
Cryptocurrency markets are platforms where real currencies and cryptocurrencies can be exchanged. Cryptocurrencies on cryptocurrency markets have equivalents in real currencies and in other cryptocurrencies. In this way, trading transactions, in other words, asset conversions, are executed (Cryptocurrency exchange, 2022).

In the cryptocurrency market, which is constantly alive and open to high changes, gaining and/or not losing money, requires constant monitoring as long as you are in any position. As can be foreseen, being on the market 24/7 remains utopian when applied to daily life. In this case, it is a necessity for people to work with an investment company and/or follow the markets with a team, in order to protect their own psychology, to make the right decisions, and to continue their life comfortably (Palmer, 2022). Another method that can be shown as an example of solving this problem is algorithmic trading, or in short, algo-trading, which is the conversion of the transaction and market-following processes into an automatic form, and is built on computers to perform certain transactions under certain conditions (Seth, 2021). According to studies, this method, which is getting more common day by day, constitutes the market by %70 to 80 in America (Graham, 2021). 

The advantages of algorithmic trading can be listed as being free from the feelings and thoughts of the investor, having a rule-based progress and not causing errors by going beyond the rules, having the correct setting of trading timings, having the chance to pre-testing strategies, and not allowing manual errors. The most common algo-trading strategies are indicator-based trend tracking strategies. This kind of strategies are easier and simpler to implement compared to other algo-trading variations. Requirements to develop such a trading algorithm, and to profit from this developed system can be listed as having programming knowledge, a cryptocurrency exchange platform (API-supported broker) to trade and get the data to be used, historical data which is required for strategy tests, and having a network connection for routing orders (Seth, 2021).

As aimed in this study, in order to develop an efficient cryptocurrency trading bot that is indicator-based and works with a trend-following strategy, which will go over the market by bringing more returns than the HODL strategy which stands for “Hold On For Dear Life”, that is based on holding what you have, the first thing done is researching on technical analysis and the working principles of indicators; then the historical data are obtained and examined with a data science approach, backtests needed on strategies are executed, and the relatively successful strategy that the aimed success is achieved is implemented.

In Section 2, "Technical Analysis", it is mentioned what technical analysis is, the Dow Theory put forward by Charles Dow, the indicators used in technical analysis, the classification of these indicators and their mentalities, how to use them, their weaknesses and how to eliminate these weaknesses.

In section 3, “Methodology”, it is mentioned how this study was carried out by explaining the design of this study; stating the test conditions, tools, and environments, the steps on getting and preparing data; And is given all the information needed to validate the results of this study.

In Section 4, “Strategies”, it is mentioned how the strategies should be created and how did the validity tests of the strategies are executed; And for last, it is shown that, how did the tests make to see which strategy is more profitable to be used in the cryptocurrency trading bot, that is developed as a result of these studies, are done; the results, the meanings of the results, success metrics. Before all of these, the process of getting and preparing the data is explained which is the first step that lets all these to be executed.

In Section 5, “Source Code”, firstly, the python-binance library, which enables the developed cryptocurrency trading bot work; which obtains, and processes the necessary data, and sends orders when needed; which briefly communicates with the Binance account is explained. Then, information is given about the classes consisting of the developed program in python programming language and how these classes are designed.

In Section 6, “References”, all the sources that contributed to this study are listed.

In Section 7, “License”, it is stated that the rights of the software developed in line with this study and the works done are protected with MIT License.

In Section 8, “Disclaimer”, it is stated clearly that, any market transaction that executed by any individual, institution, or organization, in line with this study, is not the responsibility of any individuals that names take place in this study; but the responsibility of the individual, institution, or organization that executed the transaction.


# 2.	Technical Analysis
In cryptocurrency markets, which are based on the balance of supply and demand, one investor's gain is another investor's loss. In order to be on the winning side, investments must be made at the right time and in the right way. While fundamental analysis has the right to speak about doing it in the right way; The method that can be considered more sensitive about doing it at the right time is technical analysis (Özekşi, Teknik Analize Giriş, 2013).

The purpose of technical analysis is to predict the next move in the market. Technical analysis works by considering only the price data, namely the supply and demand of the stock, by leaving aside company and industry information, economic situation, and balance sheets. Here, the supply can be considered as the desired stock to be sold while demand can be considered as the part that is wanted to be bought (Özekşi, Teknik Analize Giriş, 2013).

The reason why technical analysis only deals with price information and is simple, yet working well, is that stock values are basically priced according to the current supply and demand balance of that stock. This supply and demand may have occurred for one reason or another, but since it will naturally be reflected in prices, it is not needed to evaluate it separately. The price is nothing but the value that people place; However, considering how unstable human psychology can be, the data obtained as a result of technical analysis, cannot offer more than “high probability”, that is, certainty. In addition, it is a type of analysis with a high accuracy rate, as the majority of share suppliers and demanders will give similar reactions in accordance with the concept called "herd psychology" in common language (Özekşi, Teknik Analize Giriş, 2013).

Technical analysis not only gives all of the information in a simpler way that are given by fundamental analysis which is a validation method and which the market value is evaluated by examining balance sheets and investments, but also provides the information about the time of transactions to be made. What is important, and therefore the data to be considered, is what the prices are; not why such it is as fundamental analysis is concerned (Özekşi, Teknik Analize Giriş, 2013).

## 2.1.	Dow Theory
Dow Theory is a set of generally accepted rules that are the fundamentals of technical analysis, which was put forward by Charles Dow, who is seen as the founder of modern technical analysis. The purpose of this theory is to predict the direction of the stock market (Özekşi, Dow Kuramı, 2013).

Dow Theory tries to discover the current trend in the market by filtering short-term price movements. It does this by adhering to 6 principles. These:
    
    •	The markets discount everything
    •	The markets have 3 trends
    •	The market trends have 3 phases
    •	Indices must confirm each other 
    •	Volume must confirm the trend
    •	A trend is said to be continuous until a reversal is confirmed (Özekşi, Dow Kuramı, 2013).

### 2.1.1.	The Markets Discount Everything
As mentioned under the title of "Technical Analysis", the basic logic of technical analysis is that all situations, such as a situation in the market, investments of the shareholder company, the situation of the competitor will affect the price, and as a result, regardless of whether this is due to one reason or another, the supply and demand will be affected. The logic that explained, emerged from the part “The Markets Discount Everything” of the Dow Theory. For example, when company A starts to reap the fruits of an investment it made a long time ago, company value will start to rise. People who hear, examine, and realize this, do fundamental analysis and/or think that the value of the company will increase in various ways, invest in company stocks. In that way, since there is an increase in demand, there will also be an increase in supply, and therefore the value of the stock will increase. As a result, the data that investors are interested in analyzing the charts within the framework of technical analysis, took everything into account and appeared as a result chart (Özekşi, Teknik Analize Giriş, 2013).

### 2.1.2.	The Markets Have 3 Trends

#### 2.1.2.1.	Main (Primary) Trend
Usually, the duration is longer than 1 year. It is the long-term rising and falling movements in which rising (bull) markets and falling (bear) markets are defined, increases and decreases that can be called abysses occur (Özekşi, Dow Kuramı, 2013).

#### 2.1.2.2.	Secondary Trend
Usually, the duration varies from 1 month to several months. Their feature is that they are trends that develop in the opposite direction to the main trend (Özekşi, Dow Kuramı, 2013). 

#### 2.1.2.3.	Minor Trend
These moments, which can only reach a period of a few week durations, were evaluated as meaningless price movements by Charles Dow. Because they cover a short period of time, they are susceptible to minor changes and therefore can be misleading (Özekşi, Dow Kuramı, 2013).

### 2.1.3.	The Market Trends Have 3 Phases

#### 2.1.3.1.	Uptrend (Bull) Phases

##### 2.1.3.1.1.	Recovery
It is very similar to the last part of the downtrend (bear) formation. Stock prices are far below their values and although they experience minor fluctuations, they cannot fully rise. Smart investors buy shares with long-term thinking at these levels (Özekşi, Dow Kuramı, 2013).

##### 2.1.3.1.2.	Ascension and Participation
It is a phase that takes longer than the other two phases. Prices begin to rise rapidly. As this increase maintains, the thoughts supporting that the increase will maintain, gets stronger and this causes the prices to continue to increase. People who want to secure themselves, also start buying at this stage (Özekşi, Dow Kuramı, 2013).

##### 2.1.3.1.3.	Exaggeration and Distribution
The strong climb of the stock with media support and word of mouth attracts many people to this stock and trading volumes begin to occur at record levels. In this phase, which is similar to the last part of the bear market, the increased prices due to the excess buyers, have exceeded the required market price. Smart investors who buy at the first stage, start to sell at this stage when demand and therefore supply are high (Özekşi, Dow Kuramı, 2013).

#### 2.1.3.2.	Downtrend (Bear) Phases
##### 2.1.3.2.1.	Distribution
In this part, which is similar to the last stage of the bull market, smart investors are selling. Unconscious investors continue to buy due to media manipulation and market gossip, but as mentioned, the prices at this stage are much higher than they should be (Özekşi, Dow Kuramı, 2013).

##### 2.1.3.2.2.	Collapse
As in an uptrend, this phase lasts longer than the other two phases. With the participation of trend followers in the sale, prices continue to decrease rapidly (Özekşi, Dow Kuramı, 2013).

##### 2.1.3.2.3.	Desperation and Recovery
It is a time of frustration for unconscious investors such as investors who act on what they hear from others. This phase is similar to the first phase of the uptrend (Özekşi, Dow Kuramı, 2013).

### 2.1.4.	Indices Must Confirm Each Other
The pricing of two companies related to each other should also overlap with each other. Dow did this by taking the Dow Jones Transportation Index and the Dow Jones Industrial Average. Dow says that producing more industrial materials requires faster transportation, and so they are interrelated, and as a result, their prices overlap. This logic is used for confirmation and verification in case of trend changes (Özekşi, Dow Kuramı, 2013).

### 2.1.5.	Volume Must Confirm the Trend
Dow says that, regardless of its type, for a trend to continue, the trading volume must be high (Özekşi, Dow Kuramı, 2013).

### 2.1.6.	A Trend Is Said to Be Continuous Until a Reversal Is Confirmed
For the trend to change, the change needs to be confirmed, and until and/or not, the current trend is expected to continue (Özekşi, Dow Kuramı, 2013).

## 2.2.	Indicators
By using certain mathematical functions and calculations, indicators process and visualize the available data such as price and volume, and thus they enable this data to be interpreted better, faster, and more accurately. In short, they make complex data interpretable. They do this in a heuristic or pattern-based way (Chen, Technical Indicator, 2021).

Indicators are basically examined in 2 types as leading and lagging indicators. The best use of lagging indicators is to determine the trend direction. Another name for leading indicators is “predictive” indicators (Jeff Drake, 2003).

Regardless of their type, indicators are examined in 4 main classes in terms of the way they are calculated, the values they take into account and their purpose. It should be underlined that, the most important point in using indicators is to understand how they are interpreted and the mathematical nature of them (Jeff Drake, 2003).

In this study, since it is aimed to develop an indicator-based strategy that will make transaction decisions with trend tracking, only 2 (trend, volatility) of the 4 main indicator types (momentum, volume, trend, volatility) are included in the study. This is because, as will be explained in the “Trend Indicators” section, the situations that is the weakness of trend indicators to be used, and therefore cause them give false signals, can be filtered with volatility indicators. It also should be underlined that, in this study, not all the indicators belonging to a class are examined, but the ones that are commonly used and preferred, and also easy to implement are.

### 2.2.1.	Trend Indicators

#### 2.2.1.1.	Moving Averages (MA)
Moving averages (MA) is an indicator that helps to show the rate of increase or decrease, by averaging the prices on the chart and comparing them with the current value. To use it effectively, the 3 main variables must be understood. These can be listed as the time interval (period) to be used, the calculation method, and the data type to be used. The generally accepted period selection of moving averages, which can be used by making changes in the direction that is thought to be beneficial, is as follows:

    • 5-13 days ==> very short term
    • 14-22 days ==> short term
    • 23-49 days ==> medium term
    • 50-99 days ==> medium – long term
    • 100-300 days ==> long term

As the period gets smaller, the probability of giving false signals increases as data can change rapidly in short periods. As the period increases, the delay rate of the signals increases. Therefore, choosing the right period is important to maximize the gain. As with all other indicators, one can find which period is appropriate by looking at the past and analyzing at what point the MA used gives the correct signals (Özekşi, Hareketli Ortalamalar, 2013).

Values that go above their average are considered to be on the rise, that is, in an uptrend, as can be understood. Therefore, while triggering the transactions, the price values breaking their own averages upwards should be considered as a buy signal; And breaking downwards should be considered as a sell signal.

There are basically 3 types of moving averages, and they differ from each other in the way they are calculated.

##### 2.2.1.1.1.	Simple Moving Average (SMA)
The Simple Moving Average (SMA) indicator gives the average of the selected price data over the selected period. While doing so, it accepts the coefficient of all times, that is, its importance in this case, the same. Because of the fact that, the longer the period during which it is considered to invest means that there is the higher probability of a change being occurred in the market respectively to the first day, there is a greater possibility of giving false signals. Therefore, it should not be preferred especially in the long-term investing. (Özekşi, Hareketli Ortalamalar, 2013).

Figure 2-1 shows the application of the Simple Moving Average indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172856813-287f2259-9fb1-460d-be23-8e3ee3de73c8.png)

##### 2.2.1.1.2.	Weighted Moving Average (WMA)
Ignoring recent changes in the SMA indicator can be corrected using the Weighted Moving Average (WMA) indicator. As it gets closer to the present day, the coefficient of price data, that is, its importance, increases. It gives faster signals than the SMA indicator, but it is also relatively more likely to produce false signals due to the speed increase (Özekşi, Hareketli Ortalamalar, 2013).

Figure 2-2 shows the application of the Weighted Moving Average indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172857104-120aa048-7167-435d-aa44-7589bd209c5e.png)


##### 2.2.1.1.3.	Exponential Moving Average (EMA)
The importance of the last days neglected in SMA indicator is eliminated by using WMA indicator; but this time, the first days were almost completely ignored. These omissions are corrected by determining a general coefficient in the Exponential Moving Average (EMA). Period and coefficient information is required for its calculation. While the coefficient is always set to 2, the period can be changed depending on the situation (Özekşi, Hareketli Ortalamalar, 2013).

Figure 2-3 shows the application of the Exponential Moving Average indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172857145-7621f069-99bd-4f18-aef7-8330f0a5621f.png)


#### 2.2.1.2.	 Parabolic Stop and Reversal (PSAR)
The Parabolic Stop and Reversal (PSAR) indicator checks whether there is a bullish continuum or a bearish continuum by looking at the change from the previous value. As soon as the indicator appeared below the price chart intersects with the price chart, it moves up, changes area and also should be interpreted as a sell signal. Likewise, when the indicator above the price chart intersects with the price chart, it goes down, changes area and should be interpreted as a buy signal. The PSAR indicator that is on default settings uses step variable as 0.2 and max step variable also as 0.2 (Özekşi, Parabolic Sar, 2013).

Because of the mathematical background difference in the up and down trend in its calculation, its usage within a solid trend is more consistent. While the indicator gives accurate results in a trending environment, it gives false signals in horizontal markets, that is, in markets where trends are not clear. It is effective to use together with indicators such as MA in eliminating this deficiency (Murphy, 2022).

Figure 2-4 shows the application of the Parabolic Stop and Reversal indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172857176-40231c77-1bcd-453f-b196-85de0e72f73c.png)


#### 2.2.1.3.	Moving Average Convergence Divergence (MACD)
Moving Average Convergence Divergence (MACD) is an indicator that shows in which direction the price movements tend to go. MACD visualizes this by calculating 2 different time-period EMAs and their differences from each other (Özekşi, Macd, 2013).

It is calculated, over the default settings, by taking the difference of the 12-day exponential moving average and the 26-day exponential moving average values, so the MACD chart is positive if the 12-day value is greater than the 26-day value; It is negative if the 26-day value is greater than the 12-day value, and 0 in case of equality. In addition, the 9-day exponential moving average of the values formed as a result of this calculation, namely the MACD line, is taken to smoothen the graph. This makes it easier to interpret at intersections (Özekşi, Macd, 2013).

It should be interpreted as a buy signal when the MACD indicator crosses its own average up; And a sell signal when the indicator crosses down. The reason for this is, that if the indicator values formed as we approach the last periods are higher than the values that have been formed for a long time that is the indicator's own average, the prices will have exceeded its own average from the moment of this intersection, that is, it is on the rise (Özekşi, Macd, 2013).

As with all other indicators, the default periods may not match with the stock being analyzed, and as with all other indicators, the surest way is to try and find the right period specific to the stock. Otherwise, it will either provide early signals and overbought; or the expected gain cannot be obtained by providing late signals (Özekşi, Macd, 2013).

Figure 2-5 shows the application of the Moving Average Convergence Divergence indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172857239-f240224b-cd90-4fb5-aa0b-93286eeed575.png)


### 2.2.2.	Volatility

#### 2.2.2.1.	Average Directional Index (ADX)
ADX indicator, which stands for Average Directional Index, provides information about how strongly the price is in a trend. ADX calculations are based on the moving average of price range expansion over a given period of time. The default setting is 14 periods, but as with all other indicators, other time periods can be used (Schaap, 2022).

It takes values between 0 and 100. The point to be underlined in the ADX indicator is that the indicator shows the strength of the current trend, not the direction of the trend. Therefore, for both downtrend and uptrend, if the trend strength is high, the ADX value is high; otherwise, the ADX value will be low (Schaap, 2022).

It is commonly interpreted that values above 25 indicate the presence of a partially high-power trend, and it is known that the success of trend indicators decreases for ADX values below 25. Low ADX is also a sign of accumulation or dispersal phases (Schaap, 2022).

Figure 2-6 shows the application of the Average Directional Index indicator on real data via the Tradingview platform as an example. Since it is a visualization just to give an example of the indicator being applied, symbol data and timeframe chosen is out of context, thus not mentioned additionally.

![image](https://user-images.githubusercontent.com/58219688/172857277-f4756a81-afb5-406a-8d20-ab89aaab5a52.png)


# 3.	Methodology
This study can be examined in two stages as developing an effective strategy and developing the source code. Throughout the study, the Python programming language was used due to its effective use on datasets and its large library. During the study, all broker transactions such as trading, and data acquisition were carried out using the Binance platform through the python-binance library. The python ta library, which uses the pandas library in the background, is used to implement the indicators. The ipynb file format was used during the stages of obtaining the data and testing the strategies. The reason for this is ease of use.

As detailed in the “Strategies” section, an indicator-based strategy was preferred within the scope of the study. The reason for this, is the ease of execution compared to other methods, as explained in the "Introduction" section. Therefore, all trading conditions to be used throughout the study are triggered by using at least one indicator and the main indicator type used in these conditions are trend indicators since trend-following strategy type is selected as also explained why it is chosen in the section “Introduction”.

Since the cryptocurrency trading bot, which has developed in this study, trade on more than one symbols, not on a single symbol, parameter optimization has not been made and thus, parameters have not been customized for a single symbol. Thus, the possibility of overfitting the states for a single symbol is eliminated by using the default indicator parameters in all strategies being considered and tested.

The timeframe that is used in filtering in this study, that is, that have a role in determining the main trend, was selected as 1 hour; The timeframe to be used in trading decisions, that is, to be used in the relatively smaller timeframe, was selected as 15 minutes and “day trading” was applied.

Symbol data is obtained at 1-hour and 15-minute timeframes, depending on the day trading choice. The resulting symbol data are the values of cryptocurrencies against the fixed dollar rate (USDT). For this, firstly, all the symbol data available for spot trading on the Binance platform were obtained. These data are separated as horizontal market, rising market and falling market. The decomposition process was made by considering the difference between the last market value and the first market value in the time period in which the data was obtained. The selected threshold value is 10% change. In short, symbol data with less than 10% change in plus or minus direction is considered a horizontal market; Which has more than 10% change in the positive direction is considered as bullish market; With more than 10% in the negative direction is classified as a bearish market. From the classified data obtained as a result of the decomposition, groups of 5 were randomly selected with the help of the random library and the sample to be considered was created. The reason for this is to observe the results of the strategy aimed to be developed in different market conditions more accurately and as close to reality as possible. Thus, the data set used in the experiments was chosen bias-free as much as possible.

By comparing the results obtained as a result of the experiments, the relatively successful model was implemented to the trading bot that was aimed to be developed. By using the python-binance library in the developed program, all broker transactions were carried out on Binance platform which is the selected broker for this study.

# 4.	Strategies
A strategy is needed in order to decide when to buy and when to sell in algorithmic trading. Strategy is a set of objectives, absolute rules that define when a trader will trade. Strategies typically include filters and triggers. While “filters” determine the trading environment; “triggers” directly determine which type of transaction to do in which situations (Folger, 2022).

## 4.1.	How To Create Strategies?
A strategy should and is used in this study, after its success has been confirmed by passing the tests that measure the success of the strategy on the historical data, and that called backtesting, as is detailed in the "Backtest" section. Thus, in the face of real market data, retrospective question of “What would be the result of trading, in the selected range, using this strategy?” is answered (Chen, Backtesting, 2021).

### 4.1.1.	How To Choose Indicators?
One of the important points to be considered when creating an indicator-based strategy is to use only one indicator from each of the indicator classes. The purpose of this is to prevent misperceptions. For example, if a strategy is created using MACD belonging to the trend indicator class and PSAR, also belonging to the same class, both indicators will generate buy and sell signals at very similar times and situations. Indicators with the same basic purpose and built on the similar mathematical background, provide a second layer of validation, but generally do not affect the success of the strategy (Jeff Drake, 2003).

### 4.1.2.	How to Choose Indicator Parameters?
Correct selection of indicator parameters has a key role to a strategy to be successful. Default settings are the choices of the person/people who used and/or developed the indicator for the first time in history and are generally accepted parameters. In general, when the parameters are selected small, the indicator reacts faster, prevents delays, but can give false signals due to the fast responses and are quickly affected by market fluctuations; On the other hand, when parameters are selected large, indicators react relatively late, but are less affected by market fluctuations and small movements, and give more reliable signals. In addition, with which parameters the indicators work correctly, it is closely related to the price chart on which it is applied. It also must be underlined that a strategy can be successful or not depending on the data it is applied (Woods, 2012).

### 4.1.3.	How To Choose Timeframes?
As mentioned in the section “Dow Theory”, trends are divided into primary, secondary and minor trends. The timeframes are changed in order to observe these trends more easily by separating them from each other. For example, the same symbol data can be in a downtrend on 1-hour charts and in an uptrend on 1-day charts in the same time interval vice versa. Therefore, the right timeframe should be used in investments so that gains can be obtained in the expected time. As a result, making a profit in the developed strategy directly depends on the correct selection of the selected timeframe. (Fundora, 2022). 

Depending on the type of them, traders/investors use different timeframes to examine price charts. While swing traders make transaction decisions using daily charts and identify the main trend using weekly charts; Day traders use 15-minute charts on transaction decisions and 1-hour charts to identify the main trend; And position traders that can be considered as investors rather than traders, make these decision with respectively weekly charts and monthly charts (Fundora, 2022).

## 4.2.	 Backtest
Testing how successful a strategy is by using real market data from the past is called backtesting, and it shows the usability of the strategies by giving results on selected success metrics. Its premise is that a strategy that has been successful in the past will also be successful in the future. The step of backtesting is a must since backtesting before trading with real money prepares the user for possible outcomes (Chen, Backtesting, 2021). 

An ideal backtest should be attempted on several datasets, since a strategy that succeeds on one symbol data may fail on another symbol data. Diversity is also important to observe whether the success or failure is not by chance; but is real. In addition, transaction fees must be considered in backtesting. While all other inputs and outputs are constant, the strategy that exhibits the same return performance with fewer transactions must be considered relatively more successful (Chen, Backtesting, 2021).

## 4.3.	Tests
In this section, as explained in detail in the “Methodology” section, the data to be used in the tests were obtained and pre-processed; Experiments were carried out and the results were compared.

### 4.3.1.	Getting Historical Data
This section explains how the historical market data that needed to run the tests are obtained. In addition, as mentioned in section “Methodology”, how 15 different symbol data are classified as rising, falling and horizontal markets is also explained.

In Figure 4-1, the functions, that are required to establish communication with the Binance platform from which the data will be drawn to be obtained, and to be organized, are coded in the python language in an object-oriented manner.

![image](https://user-images.githubusercontent.com/58219688/172857414-26c9adc9-e933-487b-8f79-f23d6c19d1b5.png)


Figure shows how the intended symbol data was obtained, with 5 horizontal, 5 vertical, and 5 rising. The code is written in Python programming language. To explain briefly, firstly, all symbols open for spot trading on the Binance platform were obtained and the historical values of these symbols were compared with their current values, the HODL strategy's return in the selected range was classified as bullish, bearish, or horizontal. This classification is necessary to observe the success of strategy tests by separating them from market characteristics. Finally, these symbols, whose historical data were obtained, were randomly separated to create 5 samples with the help of the random library, and the selected sample data was saved as a csv file with the naming of timeframe_symbolName. Here, in the process of classifying the markets as bullish, bearish, and horizontal, the threshold value is taken as %10 change as stated in section “Methodology” and it also can be seen in figure 4-2.

![image](https://user-images.githubusercontent.com/58219688/172857572-f5375ad0-8d4f-4e04-b6a5-de3d96ef34e2.png)


### 4.3.2.	Preprocessing
In this section, the preliminary preparation steps required to work on the historical data obtained are listed, explained, and coded in Python programming language. Historical market data, which is the main dataset used throughout the chapter, was read from the file, and the data were taken glance at and visualized to have an idea. Then, the indicators were defined; were obtained from the main data set and appended to the data set. The data set was made ready by eliminating the None values that emerged with the addition of the indicators.

#### 4.3.2.1.	Main Dataset

##### 4.3.2.1.1.	Import
Figure 4-3 shows how historical market data, which is the main data set throughout the study, was added to the program flow from the recorded files. Dataframe data structures are used and dynamically named using the names of the symbol data, in order to prevent possible index confusions during operation and to facilitate processing.

![image](https://user-images.githubusercontent.com/58219688/172857625-a58d7eb7-c73f-45c3-b87d-4a41793fb283.png)


##### 4.3.2.1.2.	First Glance
Initial ideas and observations about the main dataset were obtained with the piece of code shown in Figure 4-4.

![image](https://user-images.githubusercontent.com/58219688/172857685-9e0cac23-131d-4a3a-8636-51f31d8982c0.png)

 
##### 4.3.2.1.3.	Visualization
Figure 4-5 shows how the visualization process, which will be used many times throughout the study, is functionalized in accordance with the Dataframe data structure and the main dataset.

![image](https://user-images.githubusercontent.com/58219688/172857725-252bf8c9-475c-4293-8f79-2f29379e6768.png)

 
Figure 4-6 is the 1-hour chart visualization of the symbol data to be worked on.

![image](https://user-images.githubusercontent.com/58219688/172857816-5b2dfe9d-7c30-45b1-92a1-1be467e61e07.png)


Figure 4-7 is the 15-minute chart visualization of the symbol data to be worked on.

![image](https://user-images.githubusercontent.com/58219688/172857864-15ab044b-4c84-44f7-9f4c-1b27048c521e.png)


#### 4.3.2.2.	Indicators

##### 4.3.2.2.1.	Defining Helper Functions
Figure 4-8 shows the functionalization of the operations to be used in the visualization of the indicators. Depending on the type of the indicator, 2 different functions have been prepared, since the visualization process, which makes sense and is widely used, is in 2 different ways as on the graph and outside the graph.

![image](https://user-images.githubusercontent.com/58219688/172857920-bed4d149-6ba2-40d9-831e-c24f91acd5ac.png)


##### 4.3.2.2.2.	Implementation
In this section, the indicators were coded in python language; the indicator values were obtained by using the historical market data in the main dataset and appended as a new variable to the main dataset.

###### 4.3.2.2.2.1.	Volatility

###### *4.3.2.2.2.1.1.	ADX*
Figure 4-9 shows how the ADX indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172857951-f32e7bbc-00ca-4f89-aa85-bd949a2fa2bf.png)


Figure 4-10 shows the results obtained with 1-hour price data of the ADX indicator.

![image](https://user-images.githubusercontent.com/58219688/172857989-df6abdf2-13d2-462b-9b02-422be10001d4.png)

 
Figure 4-11 shows the results obtained with the 15-minute price data of the ADX indicator.

![image](https://user-images.githubusercontent.com/58219688/172858026-ce7f0105-de14-4cee-b0a8-cc5269d842e1.png)


###### 4.3.2.2.2.2.	Trend

###### *4.3.2.2.2.2.1.	MACD*
Figure 4-12 shows how the MACD indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172858066-10cfb294-d177-4aeb-ab1b-9eb475446c29.png)


Figure 4-13 shows the results obtained with the 1-hour price data of the MACD indicator.

![image](https://user-images.githubusercontent.com/58219688/172858091-dfb34e7b-e7d6-4f21-98a1-7e74bf9d6b25.png)


Figure 4-14 shows the results obtained with the 15-minute price data of the MACD indicator.

![image](https://user-images.githubusercontent.com/58219688/172858113-23c0c665-1104-4981-9876-9cb816eb7c6e.png)


###### *4.3.2.2.2.2.2.	Parabolic SAR*
Figure 4-15 shows how the PSAR indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172858177-9b38411a-00db-43af-95b7-097a6b779386.png)


Figure 4-16 shows the results obtained with the 1-hour price data of the PSAR indicator.

![image](https://user-images.githubusercontent.com/58219688/172858200-640a4c27-07d7-42f4-97e5-1b1e4d1b4909.png)


Figure 4-17 shows the results obtained with the 15-minute price data of the PSAR indicator.

![image](https://user-images.githubusercontent.com/58219688/172858214-156dd6a8-8664-46f4-a0d0-157388521fbe.png)


###### *4.3.2.2.2.2.3.	SMA*
Figure 4-18 shows how the SMA indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172858284-0fbb1a0e-87e4-4379-8d85-efd83738c663.png)


Figure 4-19 shows the results obtained with the 1-hour price data of the SMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858301-b4cb5d0b-d4dc-4238-b552-ea41ed41af0c.png)


Figure 4-20 shows the results obtained with the 15-minute price data of the SMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858320-5ca08a9a-ef1d-4b06-9269-0da1b8f6ad73.png)


###### *4.3.2.2.2.2.4.	WMA*
Figure 4-21 shows how the WMA indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172858391-0fd11d51-0a6b-431f-abda-c05fcb8c056b.png)


Figure 4-22 shows the results obtained with the 1-hour price data of the WMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858402-8f348606-2b22-4a61-a31d-622c56701591.png)


Figure 4-23 shows the results obtained with the 15-minute price data of the WMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858420-073e18d1-7cb5-47b9-ba4f-699f9010fd45.png)


###### *4.3.2.2.2.2.5.	EMA*
Figure 4-24 shows how the EMA indicator is defined and appended to the dataset.

![image](https://user-images.githubusercontent.com/58219688/172858493-52ad4c8e-07bc-4f96-b5f5-44ef42d8818e.png)


Figure 4-25 shows the results obtained with the 1-hour price data of the EMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858509-5f2e1508-1b51-4966-a2e2-eb64ace9df30.png)


Figure 4-26 shows the results obtained with the 1-minute price data of the EMA indicator.

![image](https://user-images.githubusercontent.com/58219688/172858535-9fd52501-c1a8-4d0b-812f-f0d1ffcc7485.png)


#### 4.3.2.3.	Get Dataset Ready to Test

##### 4.3.2.3.1.	Handling Missing Values
None values formed after the operations were removed from the data set as shown in figure 4-27. The reason for these None values is that, for example, a 14-day moving average returns the first 13 values None because there is not enough data to calculate for the first 13 timeframes.

![image](https://user-images.githubusercontent.com/58219688/172858591-bf91bcb1-e992-4341-95a2-227763353067.png)


##### 4.3.2.3.2.	Define Helper Functions

###### 4.3.2.3.2.1.	Heikin-Ashi
Heikin-ashi is a chart technique that aims to reduce market noise and visualizes the trend direction better than a standard chart. It is used by investors to distinguish a trend more easily. The Heikin-Ashi technique makes it easy to detect trends, price patterns and reversal points, as it corrects price information over two periods. Candles in a traditional candlestick chart often change from top to bottom, which can make them difficult to interpret. Heikin-Ashi charts typically have more consecutive-colored candles, helping traders easily identify past price movements (Mitchell, 2021).

Figure 4-28 shows how the steps required to convert historical data to Heikin-ashi data are functionalized using the main data set. Figure 4-29 shows how this function generates new values using the main dataset and appends them to the dataset as new variables.

![image](https://user-images.githubusercontent.com/58219688/172858640-caefc380-7706-4920-a51b-3404fc73b36b.png)

![image](https://user-images.githubusercontent.com/58219688/172858661-cabf1cb5-9fc8-46eb-a71f-941d3b573384.png)



### 4.3.3.	Experiments

#### 4.3.3.1.	Defining Backtest Templates
In order to facilitate the experiments and eliminate the margin of error, a template has been prepared that provides backtesting. The only changes on this template throughout the experiments are the indicators being used and therefore the trading conditions. Even using “filter” and “trigger” steps in a strategy is found out that being much more successful by the researches done as mentioned in the section “Strategies”, just to prove that by experiments, a strategy with no filtering function is also implemented as shown in figure 4-30. On the other hand, the main template being used, that is with filtering functionality is shown in figure 4-31.

Success metrics were determined as total profit, total HODL return, total number of losing trades, total number of profitable trades and total number of winning trades / total number of losing trades ratio.

![image](https://user-images.githubusercontent.com/58219688/172858743-69c8aada-e4e8-44d6-83ab-1c102125b2ca.png)

![image](https://user-images.githubusercontent.com/58219688/172858813-0417b8e1-90c4-4f3f-85c0-bac61da7788b.png)


 
#### 4.3.3.2.	HODL Strategy Expected Returns
As mentioned in the “Introduction” section, the aim of this study is to go beyond the HODL strategy, which is holding what is owned. In order to make comparisons, HODL performances of the symbols in the data sets on which transactions will be performed in the selected time interval are shown.

Figure 4-32 shows how the HODL return is calculated over the 15-minute data that will be traded. Figure 4-33 shows the results calculated as a result of this process. It is also shown that the market classifications made as 5 rising, 5 bullish, and 5 bearish in figure 4-33.

![image](https://user-images.githubusercontent.com/58219688/172858845-3724261e-566c-459a-aa3f-ada598317360.png)

![image](https://user-images.githubusercontent.com/58219688/172858859-92ab7fab-180b-4dac-ac73-62d4beaeef66.png)



#### 4.3.3.3.	Confirmations
In this section, the accuracy of the information about the design of strategies, obtained from the researches mentioned in the study, has been tested with the selected data sets and their accuracy has been proven.

##### 4.3.3.3.1.	Effect of Using a Filter
As can be seen in Figure 4-34, an additional filtering step used in addition to the buy-sell stage increased the expected overall earnings, reduced the number of trades, and increased the profitable trade rate. As mentioned earlier in the “Strategies” section, the application of filters has been shown to be beneficial.

![image](https://user-images.githubusercontent.com/58219688/172858959-13e5cb98-7290-425f-8005-3386f6803804.png)


##### 4.3.3.3.2.	Effect of Using More Than One Indicators Belonging to The Same Class
As seen in Figure 4-35, an additional indicator belonging to the same class, used in the trading phase, decreased the expected total earnings, the number of trading transactions and the profitable transaction rate. But these are very minor changes. As mentioned earlier in the section “How to Choose Indicators”, it has been shown that indicators in the same class confirm each other, but do not cause major changes. The reason for the decrease in the earnings and the number of transactions is due to the longer delays as the approval of both indicators is awaited.

![image](https://user-images.githubusercontent.com/58219688/172858973-b1165b53-f04d-4e59-991a-8dac6f6d4a1b.png)


##### 4.3.3.3.3.	Effect of using moving averages to confirm trend indicators
As seen in Figure 4-36, an additional moving average used in the filtering stage increased the expected total earnings and decreased the number of buy-sell transactions; increased the rate of profitable transactions.

![image](https://user-images.githubusercontent.com/58219688/172858987-72bbc131-f148-4476-be5a-8ae280f4451b.png)


##### 4.3.3.3.4.	Effect of using volatility indicators to confirm trend indicators
As seen in Figure 4-37, an additional ADX used in the filtering stage reduced the expected total earnings and the number of trades; slightly increased the rate of profitable transactions. The use of the ADX indicator as an additional indicator has eliminated the sideways markets that are the weakness of trend indicators, thus reducing the number of trades and increasing the accuracy; but as a more defensive strategy, it yielded less profit with less risk. This is due to the fact that the ADX indicator is a lagging indicator and it is below the value of 25 because it has a return in trend returns, that is, in places where gains can be made by taking early positions, and therefore it filters the signals. 

![image](https://user-images.githubusercontent.com/58219688/172859005-5517ba55-7a9f-4f0d-a250-ecf423b01342.png)


##### 4.3.3.3.5.	Effect of using moving averages while triggering
As can be seen in Figure 4-38, an additional moving average used in the trading phase reduced the expected total earnings, the number of trading transactions and the rate of profitable transactions, albeit slightly. The reason for this is that these delayed working indicators are working as confirmatory with each other and at the same time they are blocking each other. As a result of less purchase conditions, less profit has been obtained, while the loss-making situations have decreased, the gain-making situations have also decreased.

![image](https://user-images.githubusercontent.com/58219688/172859034-4a31d122-36f9-4836-9764-27e75e08d523.png)


##### 4.3.3.3.6.	Effect of using volatility indicators while triggering
As seen in Figure 4-39, an additional ADX used in the trading phase has reduced the expected total earnings and the number of trading transactions; reduced the rate of profitable transactions. This is because the ADX indicator is a lagging indicator, thus it eliminates potential buy trades at the low levels of trend reversals, and avoiding profitable buy trades.

![image](https://user-images.githubusercontent.com/58219688/172859056-3a93f8ca-d8e2-4477-a02a-01ef856c1692.png)


#### 4.3.3.4.	Strategy combinations chosen
In line with the experiments, it was decided to use the filtering section, and to use trend indicators and an additional moving average in this filtering process; In the triggering part, it has been decided to use a single trend indicator, including moving average types. All possible combinations have been tested in order to go into more detail. Volatility indicators, which were shown to prevent the weaknesses of trend indicators throughout the study, were not used in the rest of the study as they constitute a defensive investment strategy and reduce the risk as well as the profit. It should be underlined that this is a preference, it may vary depending on what kind of strategy that investors want to follow, and the risk/reward ratio they aim for.

##### 4.3.3.4.1.	Eliminate via SMA + PSAR & Determine via PSAR
Figure 4-40 shows the test results of a strategy that uses SMA and PSAR to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859087-e66b99a1-ad94-4b00-b141-12c0a62b4817.png)


##### 4.3.3.4.2.	Eliminate via SMA + MACD & Determine via PSAR
Figure 4-41 shows the test results of a strategy that uses SMA and MACD to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859105-8799dda9-b63e-47c2-8c3b-835bb6c3b9ef.png)


##### 4.3.3.4.3.	Eliminate via WMA + PSAR & Determine via PSAR
Figure 4-42 shows the test results of a strategy that uses SMA and PSAR to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859126-32420d99-41ed-4c28-8e94-60758c178cb9.png)


##### 4.3.3.4.4.	Eliminate via WMA + MACD & Determine via PSAR
Figure 4-43 shows the test results of a strategy that uses WMA and MACD to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859146-2f1f74d7-7002-4b31-b6d7-0dae5640ddd3.png)


##### 4.3.3.4.5.	Eliminate via EMA + PSAR & Determine via PSAR
Figure 4-44 shows the test results of a strategy that uses EMA and PSAR to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859155-b3b5606d-ca37-4c78-9044-e887874fb0ee.png)


##### 4.3.3.4.6.	Eliminate via EMA + MACD & Determine via PSAR
Figure 4-45 shows the test results of a strategy that uses EMA and MACD to filter the markets and PSAR as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859174-6f1430f1-2682-4bbd-86cc-ba9a57ae13bd.png)


##### 4.3.3.4.7.	Eliminate via SMA + PSAR & Determine via MACD
Figure 4-46 shows the test results of a strategy that uses SMA and PSAR to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859196-acd4e288-52c4-4262-a66a-ea9dccf0b97a.png)


##### 4.3.3.4.8.	Eliminate via SMA + MACD & Determine via MACD
Figure 4-47 shows the test results of a strategy that uses SMA and MACD to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859230-0ce1691e-ac6e-4c91-b425-c27eb3d90efe.png)


##### 4.3.3.4.9.	Eliminate via WMA + PSAR & Determine via MACD
Figure 4-48 shows the test results of a strategy that uses WMA and PSAR to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859254-4ebd4255-106b-4a01-beeb-b03d380226b8.png)


##### 4.3.3.4.10.	Eliminate via WMA + MACD & Determine via MACD
Figure 4-49 shows the test results of a strategy that uses WMA and MACD to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859280-181978ac-2ca9-4be7-806d-471cdef36a37.png)


##### 4.3.3.4.11.	Eliminate via EMA + PSAR & Determine via MACD
Figure 4-50 shows the test results of a strategy that uses EMA and PSAR to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859291-d8f3bbef-89aa-47d6-ba3a-4630ac3052d6.png)


##### 4.3.3.4.12.	Eliminate via EMA + MACD & Determine via MACD
Figure 4-51 shows the test results of a strategy that uses EMA and MACD to filter the markets and MACD as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859306-9dd0cc47-043d-4e59-833d-059378a5e206.png)


##### 4.3.3.4.13.	Eliminate via SMA + PSAR & Determine via SMA
Figure 4-52 shows the test results of a strategy that uses SMA and PSAR to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859329-03ffbbd7-79d5-4cf8-926d-f6d9a043e4af.png)


##### 4.3.3.4.14.	Eliminate via SMA + MACD & Determine via SMA
Figure 4-53 shows the test results of a strategy that uses SMA and MACD to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859359-e008f8bf-561a-4250-83ff-b6fce6cee2a7.png)


##### 4.3.3.4.15.	Eliminate via WMA + PSAR & Determine via SMA
Figure 4-54 shows the test results of a strategy that uses WMA and PSAR to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859375-3a03ffe3-6437-4bc0-84ab-776c11be79ea.png)


##### 4.3.3.4.16.	Eliminate via WMA + MACD & Determine via SMA
Figure 4-55 shows the test results of a strategy that uses WMA and MACD to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859414-3eda3640-0d98-4435-a282-0f2c4b6080f9.png)


##### 4.3.3.4.17.	Eliminate via EMA + PSAR & Determine via SMA
Figure 4-56 shows the test results of a strategy that uses EMA and PSAR to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859440-e4011ab0-8d63-4c72-83ea-856e991de3bc.png)


##### 4.3.3.4.18.	Eliminate via EMA + MACD & Determine via SMA
Figure 4-57 shows the test results of a strategy that uses EMA and MACD to filter the markets and SMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859472-a7f0b9de-1c61-4671-bb8e-c271e16cbd87.png)


##### 4.3.3.4.19.	Eliminate via SMA + PSAR & Determine via WMA
Figure 4-58 shows the test results of a strategy that uses SMA and PSAR to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859495-a4058967-f95a-4bcb-a6d6-9c1d05e5365e.png)


##### 4.3.3.4.20.	Eliminate via SMA + MACD & Determine via WMA
Figure 4-59 shows the test results of a strategy that uses SMA and MACD to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859531-4639dc7f-56af-4ece-bd7a-6987e49b7eb1.png)


##### 4.3.3.4.21.	Eliminate via WMA + PSAR & Determine via WMA
Figure 4-60 shows the test results of a strategy that uses WMA and PSAR to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859554-a14cdcd3-1b47-4275-8107-ac708d966591.png)


##### 4.3.3.4.22.	Eliminate via WMA + MACD & Determine via WMA
Figure 4-61 shows the test results of a strategy that uses WMA and MACD to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859571-2d075705-b4c4-4f8e-b332-de8f6336281a.png)


##### 4.3.3.4.23.	Eliminate via EMA + PSAR & Determine via WMA
Figure 4-62 shows the test results of a strategy that uses EMA and PSAR to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859580-9fa067a6-db1a-4e86-b026-59ae8d282d49.png)


##### 4.3.3.4.24.	Eliminate via EMA + MACD & Determine via WMA
Figure 4-63 shows the test results of a strategy that uses EMA and MACD to filter the markets and WMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859598-2044aba5-112f-43f6-b0d2-74ec71d0cf9a.png)


##### 4.3.3.4.25.	Eliminate via SMA + PSAR & Determine via EMA
Figure 4-64 shows the test results of a strategy that uses SMA and PSAR to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859614-624d8d81-e95f-4cfa-bae6-d622661e56a5.png)


##### 4.3.3.4.26.	Eliminate via SMA + MACD & Determine via EMA
Figure 4-65 shows the test results of a strategy that uses SMA and MACD to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859637-15826d96-8d73-4741-af07-d05ae5818cef.png)


##### 4.3.3.4.27.	Eliminate via WMA + PSAR & Determine via EMA
Figure 4-66 shows the test results of a strategy that uses WMA and PSAR to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859661-6c6edb30-8242-46a6-94c9-3329b49c4737.png)


##### 4.3.3.4.28.	Eliminate via WMA + MACD & determine via EMA
Figure 4-67 shows the test results of a strategy that uses WMA and MACD to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859693-45f582d5-2753-4865-b65c-8fd89778a447.png)


##### 4.3.3.4.29.	Eliminate via EMA + PSAR & Determine via EMA
Figure 4-68 shows the test results of a strategy that uses EMA and PSAR to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859720-4abdd6df-0822-43e7-832a-79bfdd133e14.png)


##### 4.3.3.4.30.	Eliminate via EMA + MACD & Determine via EMA
Figure 4-69 shows the test results of a strategy that uses EMA and MACD to filter the markets and EMA as a trigger.

![image](https://user-images.githubusercontent.com/58219688/172859753-6e62ec09-21e4-41a4-b055-391acf45bea1.png)


### 4.3.4.	Findings
In line with the experiments performed, it is decided that to use WMA and PSAR indicators in the filtering process; And MACD indicator in the triggering process. The reason for is that, as seen in the results, it has yielded results as the most profitable strategy relatively. It should be underlined that it is a choice and “the best” strategy is relative to the needs and aims of the investor. For example, a strategy with a less profit but higher the number of profitable transactions / the number of losing transactions ratio can be selected as well as a more defensive strategy. The test results of the chosen strategy are again shown in Figure 4-70.

![image](https://user-images.githubusercontent.com/58219688/172859770-bd99880f-95fc-4dd8-b796-1c9aac45e2b4.png)


# 5.	Source Code 
As mentioned as the aim of this study in the “Introduction” section, a cryptocurrency trading bot is developed in the scope of this study. While all the information given so far are about developing a successful strategy, the parts from now are about applying the strategy in the markets. The subjects included in this section are relatively, the used part of the document of python-binance library, the design of the program developed, and the program itself.

## 5.1.	Python-binance Library Documents
In this section, root functions that are used directly, indirectly or by derivation in the program are listed. It has been collected by the python-binance library under three titles as wallet endpoints, market data endpoints, spot account/trade endpoints and has been classified and transferred to this study in the same way. All information shown throughout the chapter is taken exactly from the python-binance library (Binance Api, 2022). 

The Python-binance library is a 3rd party library that enables communication with the Binance platform, which is selected as the broker in this study, via APIs by using the official Binance API functions that are relatively lower-level (Change Log, 2022).

### 5.1.1.	Wallet Endpoints

#### 5.1.1.1.	Get Asset Balance
    Get current asset balance.

    Parameters:
    •	asset (str) – required
    •	recvWindow (int) – the number of milliseconds the request is valid for
    
    Returns:	dictionary or None if not found

### 5.1.2.	Market Data Endpoints

#### 5.1.2.1.	Get Klines
    Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.
    https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-data

    Parameters:
    •	symbol (str) – required
    •	interval (str) –
    •	limit (int) –
    •	Default 500; max 1000.
    •	startTime (int) –
    •	endTime (int) –
    
    Returns:	API response

#### 5.1.2.2.	Get Symbol Ticker
    Latest price for a symbol or symbols.

    https://binance-docs.github.io/apidocs/spot/en/#symbol-price-ticker

    Parameters:
    • symbol (str) –

    Returns:	API response

#### 5.1.2.3.	Get Symbol Info
    Return information about a symbol
    
    Parameters:
    • symbol (str) – required e.g BNBBTC

    Returns:	Dict if found, None if not

#### 5.1.2.4.	Get Exchange Info
    Return rate limits and list of symbols

    Returns:
    • list - List of product dictionaries

### 5.1.3.	Spot Account Trade Endpoints

#### 5.1.3.1.	Create Order
    Send in a new order
    
    Any order with an icebergQty MUST have timeInForce set to GTC.
    https://binance-docs.github.io/apidocs/spot/en/#new-order-trade
    
    Parameters:
    •	symbol (str) – required
    •	side (str) – required
    •	type (str) – required
    •	timeInForce (str) – required if limit order
    •	quantity (decimal) – required
    •	quoteOrderQty (decimal) – amount the user wants to spend (when buying) or receive (when selling) of the quote asset, applicable to MARKET orders
    •	price (str) – required
    •	newClientOrderId (str) – A unique id for the order. Automatically generated if not sent.
    •	icebergQty (decimal) – Used with LIMIT, STOP_LOSS_LIMIT, and TAKE_PROFIT_LIMIT to create an iceberg order.
    •	newOrderRespType (str) – Set the response JSON. ACK, RESULT, or FULL; default: RESULT.
    •	recvWindow (int) – the number of milliseconds the request is valid for

    Returns:	API response

#### 5.1.3.2.	Get Account
    Get current account information.
    
    https://binance-docs.github.io/apidocs/spot/en/#account-information-user_data
    
    Parameters:
    • recvWindow (int) – the number of milliseconds the request is valid for
    
    Returns:		API response

## 5.2.	Code Design
In this section, there is descriptive information about the design of the developed software.

### 5.2.1.	Classes
In this section, object-oriented program design choices are explained about the classes used in the designed program and the features of the classes; And on which subjects they differ from each other and why they are necessary.

    •	Root Functions*: Functions that directly and ONLY using Binance-Client module


    •	Class IWalletEndPoints: Has ONLY Root Functions related to Binance-Client module/Wallet.

    •	Class IMarketDataEndPoints: Has ONLY Root Functions related to Binance-Client module/MarketData.

    •	Class ISpotAccountTradeEndPoints: Has ONLY Root Functions related to Binance-Client module/SpotAccountTrade.

    •	Class IDerivedEndPoints: Has functions that are derived from the Root Functions. Such as changing the data type of the returned value of the Root Function. The functions included are all can be considered as a bridge in between the Root Functions and the program itself.

    •	Class IBinanceClientModuleBehaviors: Has functions that are used directly in the main Program. They differ from the functions in IDerivedEndPoints not by being dependent on the Root Functions but being directly used in the program. Basically, as an example, Root Functions get the data needed and IBinanceClientModuleBehaviors functions lets us use them in the program flow by using the IDerivedEndPoints functions as a bridge.

    •	Class IBinanceClientClassBehaviors: Has functions to maintain the main flow of the program. The functions included are all essential to use BinanceClient class itself and class instance objects.

    •	Class Config holds the essential personal information required to construct BinanceClient.

    •	Class BinanceClient: The key class of the whole program. It uses all other classes at some level.

    •	Class Coin: The class to represent a basic Coin objects’ attributes in real life. It also has the mission to notify the upTrendCoin and downTrendCoin classes’ symbol lists. Observer pattern is applied.

    •	Class upTrendCoin: The class to store and get coins in uptrend which are determined with the Strategy class whenever needed. It is continuously notified by the Coin class and is triggered in the main flow of the program.

    •	Class downTrendCoin: The class to store and get coins in downtrend which are determined with the Strategy class whenever needed. It is continuously notified by the Coin class and is triggered in the main flow of the program.

    •	Class Indicator: The class is a premature class for now. It will be useful if there will be lots of indicator types.

    •	Class Sar: The class is a premature class for now. It will be useful if there will be lots of Sar indicator types.

    •	Class Sar02_02: The class is a class with embed attributes and methods. The attributes that are used in the class are chosen with the studies based on algorithmic trading.

    •	Class Wma: The class is a premature class for now. It will be useful if there will be lots of Wma indicator types.

    •	Class Wma14: The class is a class with embed attributes and methods. The attributes that are used in the class are chosen with the studies based on algorithmic trading.

    •	Class Macd: The class is a premature class for now. It will be useful if there will be lots of Macd indicator types

    •	Class Macd26_12_9: The class is a class with embed attributes and methods. The attributes that are used in the class are chosen with the studies based on algorithmic trading.

    •	Class Strategy: The class is a premature class now. It will be useful if there will be lots of Strategy types.

    •	Class Strategy01: The class is a class with embed attributes and methods. The attributes that are used in the class are chosen with the data science studies based on algorithmic trading that are explained and tested in that very study.

### 5.2.2.	UML
The relationship between the classes, the methods and attributes being used in these classes of the designed source code is as shown in Figure 5-1.

![WhatsApp Image 2022-06-05 at 14 39 58](https://user-images.githubusercontent.com/58219688/172860481-ee30766f-d7b4-42e4-924f-9d8446856929.jpeg)


# 6.	References
Binance Api. (2022). Retrieved from python-binance: https://python-binance.readthedocs.io/en/latest/binance.html#

Change Log. (2022). Retrieved from Binance-docs: https://binance-docs.github.io/apidocs/spot/en/#change-log

Chen, J. (2021, 8 18). Backtesting. Retrieved from Investopedia: https://www.investopedia.com/terms/b/backtesting.asp

Chen, J. (2021, 9 29). Technical Indicator. Retrieved from Investopedia: https://www.investopedia.com/terms/t/technicalindicator.asp#:~:text=Technical%20indicators%20are%20heuristic%20or,to%20predict%20future%20price%20movements.

Cryptocurrency exchange. (2022, 5 1). Retrieved from wikipedia: https://en.wikipedia.org/wiki/Cryptocurrency_exchange

Folger, J. (2022, 1 5). Using Technical Indicators to Develop Trading Strategies. Retrieved from Investopedia: https://www.investopedia.com/articles/trading/11/indicators-and-strategies-explained.asp

Fundora, J. (2022, 2 9). Multiple Timeframes Can Multiply Returns. Retrieved from Investopedia: https://www.investopedia.com/articles/trading/07/timeframes.asp

Graham, T. Y. (2021, 7 22). How many people in the US are using algorithmic trading in crypto market? Retrieved from Quora: https://www.quora.com/How-many-people-in-the-US-are-using-algorithmic-trading-in-crypto-market

Hayes, A. (2021, 4 29). Average True Range. Retrieved from Investopedia: https://www.investopedia.com/terms/a/atr.asp

Jeff Drake, E. D. (2003). Profi ting with Indicators. Austin, Texas.

Kenton, W. (2021, 10 4). Monte Carlo Simulation. Retrieved from Investopedia: https://www.investopedia.com/terms/m/montecarlosimulation.asp

Mitchell, C. (2021, 9 29). Heikin-Ashi Technique. Retrieved from Investopedia: https://www.investopedia.com/terms/h/heikinashi.asp

Murphy, C. (2022, 2 17). Introduction to the Parabolic SAR. Retrieved from Investopedia: https://www.investopedia.com/trading/introduction-to-parabolic-sar/

Özekşi, A. (2013). Dow Kuramı. Retrieved from Teknik Analiz Sanatı: http://www.teknikanalizsanati.com/dowkurami.aspx

Özekşi, A. (2013). Hareketli Ortalamalar. Retrieved from Teknik Analiz Sanatı: http://www.teknikanalizsanati.com/hareketliortalamalar.aspx

Özekşi, A. (2013). Macd. Retrieved from Teknik Analiz Sanatı: http://www.teknikanalizsanati.com/macd.aspx

Özekşi, A. (2013). Parabolic Sar. Retrieved from Teknik Analiz Sanatı: http://www.teknikanalizsanati.com/parabolicsar.aspx

Özekşi, A. (2013). Teknik Analize Giriş. Retrieved from Teknik Analiz Sanatı: http://www.teknikanalizsanati.com/teknikanalizegiris.aspx

Palmer, G. (2022, 4 8). Major Challenges with Cryptocurrency Investment. Retrieved from Valiant CEO: https://valiantceo.com/major-challenges-with-cryptocurrency-investment/

Schaap, C. (2022, 5 1). ADX: The Trend Stregth Indicator. Retrieved from Investopedia: https://www.investopedia.com/articles/trading/07/adx-trend-indicator.asp

Seth, S. (2021, 5 5). Basics of Algorithmic Trading: Concepts and Examples. Retrieved from investopedia: https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp

Woods, G. (2012, 12 8). Best Settings For Trading Indicators. Retrieved from Trading Setups Review: https://www.tradingsetupsreview.com/best-settings-trading-indicators/

# 7.	License
MIT License

Copyright (c) 2022 Asrın Öztin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# 8.	Disclaimer
The USER is responsible for any purchase and sale transactions to be made based on this study in any way. The study does NOT guarantee success in any situation and does NOT accept any kind of responsibility for any matter. All actions to be taken are in only and only responsibility of the user, NOT any of the individuals that names take place in this study.

