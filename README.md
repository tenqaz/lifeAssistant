### 简介

生活助手

### 接口

* 增加

接口: /article

方法: post

参数:  都是可选.
    category: 分类1
    category: 分类2
    header: 标题
    content:
    publisher:
    publisher_time: 
    
* 删除

接口: /article/{id}

方法: delete
    

* 通过分类查询文章

接口: /article/

方法: get

参数:
    category: 分类
    page: 当前页数
    per_page: 每一页显示几条数据

```json5

{
    "code": 0,
    "msg": "success",  
    "data": [{
        "_id": "",
        "category": "",   // 分类
        "category2": "",   // 分类2 
        "title": "",    // 标题
        "publisher": "", //发布者
        "publish_time": "",  //发布时间
        "create_time": "",  //创建时间
    },{
        "_id": "",
        "category": "",   // 分类
        "category2": "",   // 分类2 
        "title": "",    // 标题
        "publisher": "", //发布者
        "publish_time": "",  //发布时间
        "create_time": "",  //创建时间
    },
    ]
}

```

* 通过id查找文章

接口： /article/{id}

方法: get

```json5
{
  code: 0,
  msg: "success",
  data: {
    "_id": "",
    "content": "",  // 内容
  }
}
```


### 需要增加的功能

1. 自动生成文档
2. 单元测试

### 改进

1. 将爬虫部分移动到MagicPool项目中.
