# 亚马逊美国站（或者别的什么站）的爬虫  

### 现在写的是对亚马逊美国站图书信息的爬虫  
<br>
<br>
<ul>项目结构:  
<li> Amazon_Spider  </li>
<li>　　—— Amazon_Spider </li>
<li>　　　　—— items　　　　解析到的数据存储的数据结构  </li>
<li>　　　　—— middleware　 中间件（UA伪装和代理池都写在这）</li>
<li>　　　　—— pipelines　　数据输出管道（使用Mysql数据库进行存储）  </li>
<li>　　　　—— settings　　　配置文件（启用cookie，刷新代理池方法）　</li>
<li>　　　　　　—— amazon　　爬虫本体
</ul>
    
## 已用反爬虫：  
<li>代理池(代理到期，暂未更新)
<li>UA伪装
<li>启用了cookie，因为亚马逊会自动检测cookie，不使用cookie会弹机器人检测  
<br>
<br>
<br>

## 其他：  
使用了RedisCrawlSpider，爬虫本体为分布式爬虫，服务器在settings中设置<br>
使用了Redis指纹去重(更新：Redis指纹去重效果差，书本不同的售出载体对应不同的链接，待更新)<br>
未设置分布式管道，暂时使用Mysql管道进行存储<br>


## 暂未解决:  
书本名去重，爬取的数据重复较多<br>
代理池删除代理的接口未实现，想改成超时便删除代理池，若代理池空则进行刷新的方案<br>
name个别时候获取不到，不知道是封IP了还是解析方法没写好<br>
