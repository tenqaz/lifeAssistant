### 简介

生活助手

### 接口

* 增加

接口: /lifeAssistant/article

方法: post

参数:  都是可选.
    category: 分类1
    category: 分类2
    header: 标题
    content:
    publisher:
    publisher_time: 
    header_img:  上传图片
    
响应数据:
```json5
{
    "code": 0,
    "msg": "success",
    "data": {   //新增的数据
        "_id": "",
        "category": "",   // 分类
        "category2": "",   // 分类2 
        "header": "",    // 标题
        "publisher": "", //发布者
        "publisher_time": "",  //发布时间
        "create_time": "",  //创建时间
        "header_img": "",  //上传图片
    } 
}
```
    
* 删除

接口: /lifeAssistant/article/{id}

方法: delete

响应数据:
```json5

{
"code": 0,
"msg": "success",
"data": "",
}

```
    

* 通过分类查询文章

接口: /lifeAssistant/article/

方法: get

参数:
    category: 分类
    page: 当前页数
    per_page: 每一页显示几条数据

响应数据:
```json5

{
    "code": 0,
    "msg": "success",  
    "data": [{
        "_id": "",
        "category": "",   // 分类
        "category2": "",   // 分类2 
        "header": "",    // 标题
        "publisher": "", //发布者
        "publisher_time": "",  //发布时间
        "create_time": "",  //创建时间
        "header_img": "",  //上传图片
        "type": 1,        // 上传类型. 0爬虫上传. 1手动上传
        "click_num": 1,   // 点击数
    },{
        "_id": "",
        "category": "",   // 分类
        "category2": "",   // 分类2 
        "header": "",    // 标题
        "publisher": "", //发布者
        "publisher_time": "",  //发布时间
        "create_time": "",  //创建时间
        "header_img": "",  //上传图片
        "type": 1,        // 上传类型. 0爬虫上传. 1手动上传
        "click_num": 1,   // 点击数
    },
    ]
}

```

* 通过id查找文章

接口： /lifeAssistant/article/{id}

方法: get

响应数据:
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

* 访问图片

通过图片id直接访问接口

接口: /lifeAssistant_images/{图片id}

方法: get

响应数据: 图片

### 需要增加的功能

1. 自动生成文档
2. 单元测试
3. 日志

### 改进

1. 将爬虫部分移动到MagicPool项目中.


### 信息

ip: 39.108.102.90