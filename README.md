#  项目说明

该项目目标：
- 采用爬虫、自然语言处理、机器学习的办法，快速获取某领域关键论文
- 采用人工智能分析 + 人工打分的办法，自动判断某篇论文“是否有用”
------
1. 建立爬虫环境
  * [ ] 项目定时启动、关闭、操作自动化
  * [x] 采用selenium + phantomjs方案 
  * [ ] 采用反爬虫机制：agent，IP
  * [ ] 多线程爬虫
  * [ ] 采用flask搭建可视化界面

2. 自动根据关键词、关键词组合或者搜索符等工作抓取PubMed上相关文献信息 
  * [x] 抓取：题目、期刊、年份、作者、机构、摘要、关键词、全文链接
  * [x] 自动补齐：期刊影响因子及杂志分区信息
  * [ ] 自动补齐：该机构在全球范围的影响力或者排名

3. 储存抓取回到的信息
  * [x] 标准储存在CSV文件中，阅读友好
  * [ ] 储存改为MongoDB
  * [ ] Redis作为中间件

4. 对抓取回的文本信息做清洗
  * [ ] 去除所有标签；清除特殊字符或者非英文字母；合并段落
  * [ ] 抓取的str生成规范list
     
5. 文本强化，便于阅读
  * [ ] 搜索关键词突出：包含本项目所涉及所有关键词
  * [ ] 机构中国家名突出
  * [ ] 自定义关键词突出：自定义添加关注词

6. 输出成阅读格式：MD、HTML静态文件，web输出
  * [ ] 使用jinja生成MD，HTML静态文件
  * [ ] 使用flask实现动态查询输出

7. 自然语言处理
  * [ ] 文本清洗：停用词，词格
  * [ ] 分词
  * [ ] 词频统计与向量分析
  * [ ] 多文章聚类分析

8.1 深度学习模型建立：根据打分训练
  * [ ] 搭建文本、期刊资质、团队资质、作者资质等与人工打分之间联系的模型
  * [ ] 根据人工评分重新计算文章分数，重新排序

8.2 阅读后人工评分、更新
  * [ ] 人工多维度评论文章：主题相关度、文章质量、文章有用性
  * [ ] 对重拍的文章进行打分
  
9. 根据建立的模型，提供每篇文章有用的可能性
