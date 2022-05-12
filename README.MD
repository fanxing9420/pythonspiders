# Python爬虫实战项目源码(新人练手项目)

这是我在自学爬虫时候根据老师讲的做的，部分我写了注释，我上传的这几个项目也是比较经典的项目。

爬取腾讯招聘，豆瓣TOP250，爬取58同城住房信息，爬取读书网并写入数据库等等项目

这些项目改动链接就可以使用，写入数据库还需要建表，我没有上传数据库文件，

建表语句如下，自己看看空格啥的，别照着复制

```mysql
CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `src` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
```

后续我还会上传相关源代码，持续更新中......

如果有问题可以去我主页查看我的联系方式咨询我。

我的博客网：（我的学习笔记，技术相关，软件资源都在更新中...）

www.fanxingw.cn
