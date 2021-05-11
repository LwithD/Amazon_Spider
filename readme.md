# 亚马逊美国站（或者别的什么站）的爬虫  

### 现在写的是对亚马逊美国站图书信息的爬虫  
<br>
<br>
<ul>项目结构:  
<li> Amazon_Spider  </li>
<li>　　—— Amazon_Spider </li>
<li>　　　　—— items　　　　解析到的数据存储的数据结构  </li>
<li>　　　　—— middleware　 中间件（UA伪装和代理池都写在这）</li>
<li>　　　　—— pipelines　　数据输出管道（暂只输出网页用于调试）  </li>
<li>　　　　—— settings　　　配置文件（启用cookie，刷新代理池方法）　</li>
<li>　　　　　　—— amazon　　爬虫本体
</ul>
    
## 已用反爬虫：  
<li>代理池
<li>UA伪装
