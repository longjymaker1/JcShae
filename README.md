# 网站简介
娱乐信息分享平台, 主要分享楼凤,站街, SPA, KTV, 洗浴中心, 足疗店.
通过鼓励分享实现信息的互通有无

# 基本功能
1. 信息展示
2. 会员功能
3. 发帖评论功能
4. 充值功能 -- 创建简易购物网站(游戏币)
5. 购买功能

# 页面
## 首页
1. 导航栏
2. 选择城市
3. 选择板块
4. 模块精选信息
    1. 新上传TOP10
    2. 好评TOP10
    3. 楼凤TOP10
    4. 站街TOP10
    5. SPA TOP10
    6. KTV TOP10
    7. 洗浴中心TOP10
    8. 足疗店TOP10
5. 会员基本信息

# 数据模型
## 文章主表 -- article
* `id` -- id (primary key)
* 文章标题 -- title
* 用户id -- user_id
* 类型 -- article_type.id
* 正文 -- content
* 文章-评论id -- article_comment.id
* 浏览量 -- view_num
* 评论数 -- comment_num
* 当然浏览量 -- hot_num
* 点赞数 -- like_num
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)
* 省份 -- provinces (varchar(32))
* 城市 -- city (varchar(32))
* 主图path -- main_photo_path  (varchar(128))

## 帖子信息子表 -- article_message
* `id` -- id (primary key)
* `article_id`
* 小姐数量 -- hooker_num (varchar(64))
* 小姐年龄 -- hooker_age (varchar(64))
* 小姐素质 -- hooker_quality (varchar(128))
* 小姐外形 -- hooker_shape (varchar(128))
* 服务项目 -- service_content (varchar(128))
* 营业时间 -- business_hours (varchar(128))
* 环境设备 -- equipment (varchar(128))
* 安全评估 -- security (varchar(128))
* `详细地址` -- address (varchar(128))
* `联系方式` -- contact_way (varchar(128))
* 综合评价 -- evaluation (varchar(128))
* 图片列表 -- pic_lst (longtext)
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)
* 价格P -- price_p
* 价格PP -- price_pp
* 价格包夜 -- price_y

## 图片表 -- photo
* `id` -- id (primary key)
* `article_message` -- 帖子信息子表id
* 图片path -- photo_path

## 用户表 -- user
* `id` -- id (primary key)
* 登录名 -- login_name
* 登录密码 -- login_passwd
* 昵称 -- name
* 邮箱 -- email
* 状态 -- status
* 积分 -- integral
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)

## 板块类型 -- article_type
* `id` -- id (primary key)
* 板块名称 -- article_type_name
* 帖子id -- article_id
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)


## 评论表 -- comment
* `id`
* 评论正文 -- content
* 文章id -- article_id
* 父级评论id -- father_comment_id
* 评论用户id -- user_id
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)

## 关注表 -- attention
* id
* 关注人id -- user_id
* 被关注人id -- att_user_id
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)

## 收藏表 -- collect
* id
* 收藏用户id -- col_user_id
* 收藏文章id -- col_art_id
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)

## 基础配置信息表 -- configs_msg
基础配置信息，包括区域、省份、城市、地区等

* id
* 值信息(区域信息-- 一级包括省、直辖市; 二级 市、直辖市的区等信息) -- value_name
* 类型id -- type_id
* 类型名 -- type_name
* 创建时间 -- create_time (datetime)
* 修改时间 -- edit_time (datetime)




> 翻页功能  -- django-pure-pagination