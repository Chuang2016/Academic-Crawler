统一格式如下：
论文记录（完整）：
    项目名称（project）：与运行项目名保持一致
    搜索检索式（sstr）：搜索使用的关键词或者检索式
    采集时间（ttime）：task time项目运行时间，如先抓sum再抓abstract，抓到abstract后更新，
    记录状态（status）：统一便于调取。1=只有pmid（只抓了sum），2=有完整记录，3=已清洗，4-10保留（自然语言处理），11=已输出，12=已阅读，13=已完整评价，14-20保留（人工智能），整数
    来源（source）：文章来源于何处，pubmed = “pm”，字符串
    pmid（pmid）： pmid，整数
    标题（title）：文章标题，字符串
    作者（author）：为简化统一用单数，列表
    期刊（journal）：名称必须是在线搜索返回的标准名称（直接抓下来的不算），字符串
    影响因子（if）：通过在线搜索获取，浮点数
    期刊分区（jzone）：期刊中科院分区，整数
    年份（year）：只记录年份，不考虑出版时间，整数
    摘要（abstract）：即abstract，字符串
    关键词（keyword）：关键词，列表
    机构名（institue)：机构名，列表
    第一机构排名（irank）：第一个机构的世界排名（尚未找到靠谱材料）
    机构国家（country）：机构国家，列表
    全文链接（flink）：全文链接，列表
    文章质量
    与项目相关性
    

    
    