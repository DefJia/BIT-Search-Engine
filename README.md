# (附件) 项目研究报告

[TOC]

## 一、课题背景与现状

​	近年来，随着科技研究和学术水平的快速发展，机器学习算法开始走入更多人的视野当中。自然语言处理（Natural Language Processing，NLP）和计算语言学（Computational Linguistics）便是其中一个主要的分支。这个分支是一门跨学科的研究领域，它试图找出自然语言的规律，建立运算模型，最终让电脑能够像人类般分析，理解和处理自然语言。

​	在日常生活中，人们能接触到的与计算语言学相关性最大的产品，除了聊天机器人，就是如“百度”、“必应”、“Google”等人们耳熟能详的搜索引擎了。搜索引擎汇聚了互联网中庞大的网页数据，融合了爬虫、数据库等多种技术，以搜索引擎算法为支撑，获得网站网页资料，建立数据库并提供查询的系统，通过网络上的各种链接自动获取大量网页信息内容，并通过自然语言处理相关算法分析整理形成的。

​	目前，这一领域的研究方兴未艾，对自然语言的处理是现代计算机科学，包括语言学都在研究的课题，我们的项目实现了两方面的结合，联系实际需求，具有一定的理论意义和开拓性。

## 二、研究的目的和意义

​	北京理工大学（以下简称“北理”）校内网中有很多站点资源呈点状分布，有相当一部分网站没有互相链接，由于不能访问外网，这些站点不能被各大搜索引擎收录。所以，我们的研究旨在基于对相关自然语言处理算法的研究，建立一个北理内网搜索引擎，将所有内网资源联系起来，给师生查找资料提供便利，有很强的实用价值——北理师生可通过校园网访问该站点；同时，我们还公布了项目中关于自然语言处理的资料，包括分词模型，统计规则，处理算法等，以供交流研究。

## 三、方案设计和实施计划

### 方案前期设计

1. 利用网络爬虫（Network Spider）下载网页，通过Python的BeautifulSoup库分析网页HTML结构。
2. 使用Sqlite3进行数据存储，将生成的语料库存入数据库。

2. 通过自然语言处理相关技术分析网页关键词，制成索引备用； 

3. 根据关键词和网页索引，按照相关性排序列出搜索结果；

4. 通过机器学习算法和隐马尔可夫模型（Hidden Markov Model，HMM）以及贝叶斯网络（Bayesian network），对搜索结果进行不断改进。

### 实施计划

- 2017.11 – 2017.12 撰写网络爬虫并进行初步爬取；
- 2017.12 – 2018.1 通过Python对现有数据进行分离处理生成语料库；
- 2018.1 – 2018.3 通过自然语言处理算法统计分析网页关键词，制成索引；
- 2018.3 – 2018.5根据关键词和网页索引，按照相关性排序列出搜索结果；
- 2018.5 – 2018.6 Web页面的设计与项目上线对外服务宣传；
- 2018.6– 2018.9 探究隐马尔科夫模型并搭建框架；
- 2018.9  利用机器学习算法结果语言学模型对搜索结果进行改进。
## 四、研究的主要内容

​	在搜索引擎中，影响搜索引擎质量的因素首先是用户的点击数据，除此之外还可归纳成下面的四大类：完备的索引、对网页质量的度量、用户偏好、确定一个网页和某个查询的相关性的方法。

​        然而，在搜索引擎创立初期，缺乏主要数据的情况下，我们优先研究的方向，主要对完备的索引、对网页质量的度量、确定一个网页和某个查询的相关性的方法进行了详细研究。

### 制作完备的索引

​	在对网页的HTML进行解析之后，接下来重要的一步便是分词，良好的分词系统是完备索引的基础，在这里我们选用了开源的jieba分词系统，并对其进行了改进。

> Python中文分词组件 "Jieba" 
>
> 支持三种分词模式：
>
> ​	精确模式，试图将句子最精确地切开，适合文本分析；
>
> ​	全模式，把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义；
>
> ​	搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率，适合用于搜索引擎分词。

​	对于校内网站的一些专有名词，我们在分词系统中进行了修改，调整了一些理工特色的词语的分类，以便在搜索时更加精确。

### 对网页质量的度量

​	对网页质量的度量，即PageRank算法。

> “PageRank”原理是通过民主表决的方式，如果一个网页被很多其他网页所链接，说明它价值就越高。同时，因为被那些排名更高的网站所链接更说明其价值，所以还要考虑网页排名越高的网站贡献的链接权重越大。

​	我们的研究中，将这个计算问题转换为二维矩阵相乘的问题，用迭代的方式和数据库关联的方式解决了相关性问题。我们对此设计了两种方案：

- 初始化时，可以假定所有网站的排名都是相同的，算出第一次迭代排名，再往下继续算出几次的迭代排名。可以从理论上证明，排名值能够收敛到真实值。而且这迭代次数大概是10次，就能达到收敛的效果。
- 初始化时，假定只有几个网站的权重为1，如[北京理工大学官网](http://www.bit.edu.cn)、[北理人网址导航](http://bitren.com)，这些网站中附带的所有链接权重为(k+1)，以此类推；灵感来源与数据结构中图的最短路径Floyd算法和Dijkstra算法。

### 确定一个网页和某个查询的相关性

​	这一点相对与以上两点，理论性更强一些，我们利用隐含马尔可夫模型（Hidden Markov Model）和贝叶斯公式（Bayes' theorem）来解决了这些问题。

​	当我们接受到输入词 (o1,o2,o3) 时，我们要根据这组信号推测出发送的句子 (s1,s2,s3)。用数学语言来描述，就是在已知 o1,o2,o3,…的情况下，求使得条件概率P (s1,s2,s3,…|o1,o2,o3….) 达到最大值的那个句子 (s1,s2,s3)。但是，这个概率不容易直接求出，于是我们可以间接地利用贝叶斯公式：

> P(o1,o2,o3,…|s1,s2,s3….) * P(s1,s2,s3,…) 

拟合出了用户最可能的搜索结果，以此来加强搜索精度。

## 五、创新点和结论

​	基于我们对搜索引擎的研究和搜索引擎相关算法，主要是**搜索关键词权重的科学度量TF-IDF**——词频（TF, Term Frequency）和逆文本频率指数（IDF, Inverse Document Frequency）的度量，我们设计并优化了校内搜索引擎的网页排名分数。

- 词频计算

  - 一个词预测主题的能力越强权重越大
  - 停止词的权重为零

- 逆文本频率指数

  - 公式为 log(D/Dw)

    其中D指全部网页数，Dw指一个关键词w在Dw个网页中出现过

  由此，我们的排名公式：

> 网页分数 =（相关关键词分数 x 0.37）+（域名权重 X 0.11）+（外链分数 X 0.25）+（内容质量分数 X 0.02）+（人工加分）-（自动或人工降分）

​	基于此公式，我们得以得到网页权重的计算方法，并将其运用到了实际的网站中，相关的技术博客也已经发布到了个人博客当中，也可在开源网站上看到[项目部分代码及文档](https://github.com/DefJia/BIT-Search-Engine)。

## 六、成果的应用前景

​	最终，本项目在校内服务器上，基于搭建的微型开发板Rapiberry 3B和自行配置的一套网络环境，网站可通过校园网访问，网址为[https://so.defjia.top/](https://so.defjia.top/)——这个网站名为“北湖之道”，取“北湖知道”的谐音，“北湖”融合北理元素，“知道”体现网站作为搜索引擎的特点，首页设计图：

![](document/index.png)

​	该项目是整合了北京理工大学校内网络资源的第一个搜索网站，是一次对搜索引擎算法的创新实践，也是基于语言学和计算机科学之间学科交叉的一次探索与创新。方便同学门查找校内资源的入口，具有极强的现实意义与使用价值。

## 七、参考资料

- 沈健. 基于统计模型的搜索引擎查询纠错系统[D].大连理工大学,2017.
- 张伟哲,张宏莉,许笑,何慧.分布式搜索引擎系统效能建模与评价[J].软件学报,2012,23(02):253-265.
- 漆志辉. 基于隐马尔科夫模型的主题爬虫性能提高与应用[D].暨南大学,2011.
- 《数学之美》 吴军 人民邮电出版社 (重点为7 - 11章)
  - 《布尔代数和搜索引擎的索引》
  - 《贾里尼克和现代语言处理》
  - 《图论和网络爬虫》
  - 《PageRank——Google的民主表决式网页排名技术》
  - 《如何确定网页和查询的相关性》
- [简易搜索引擎(Python)]->(http://blkstone.github.io/2015/12/06/PySearchEngine/)
- [python搜索引擎实现]->(http://www.voidcn.com/article/p-hjpmifud-ss.html)
- [Python中文分词组件 jieba]->(https://www.oschina.net/p/jieba)
- [SQLite教程 - 菜鸟论坛]->(http://www.runoob.com/sqlite)

------

北京理工大学 BIT-2017-047 大创小组 [联系我们](mailto:code@defjia.top)
