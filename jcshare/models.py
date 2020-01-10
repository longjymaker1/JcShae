from django.db import models
import django.utils.timezone as timezone


class Article_type(models.Model):
    """模块类型表"""
    article_type_name = models.CharField(max_length=32, verbose_name="板块类型")
    article_type_name2 = models.CharField(max_length=32, null=True, verbose_name="板块别称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class User(models.Model):
    """用户表"""
    login_name = models.CharField(max_length=32, verbose_name="登录账号")
    login_passwd = models.CharField(max_length=64, verbose_name="登录密码")
    name = models.CharField(max_length=32, null=True, default=None, verbose_name="用户昵称")
    email = models.EmailField(verbose_name="用户邮箱")
    integral = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="积分")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Central(models.Model):
    """地区表, 东北、华北、华中、华东、华南、西北、西南"""
    central_name = models.CharField(max_length=32, verbose_name="地区名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Provinces(models.Model):
    """省份表"""
    central = models.ForeignKey(
        Central,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cen_province",
        verbose_name="地区外键"
    )
    provices_name = models.CharField(max_length=32, verbose_name="省份、直辖市名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class City(models.Model):
    """城市表"""
    provinces = models.ForeignKey(
        Provinces,
        on_delete=models.SET_NULL,
        null=True,
        related_name="pro_city",
        verbose_name="省份外键"
    )
    city_name = models.CharField(max_length=32, verbose_name="城市、直辖市区名称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Article(models.Model):
    """帖子表"""
    title = models.CharField(max_length=128, verbose_name="标题")
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="act_user",
        verbose_name="用户外键"
    )
    content = models.TextField(verbose_name="正文")
    view_num = models.IntegerField(default=0, verbose_name="浏览量")
    comment_num = models.IntegerField(default=0, verbose_name="评论数")
    like_num = models.IntegerField(default=0, verbose_name="点赞数")
    collection_num = models.IntegerField(default=0, verbose_name="收藏数")
    provinces = models.ForeignKey(
        Provinces,
        on_delete=models.SET_NULL,
        null=True,
        related_name="provinces",
        verbose_name="省份、直辖市"
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        related_name="city",
        verbose_name="市、直辖市区"
    )
    article_type = models.ForeignKey(
        to=Article_type,
        on_delete=models.SET_NULL,
        related_name='acticle_type',
        null=True,
        default=1,
        verbose_name="article外键关联类型"
    )
    main_photo_path = models.CharField(max_length=128, verbose_name="主图路径", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class article_photo(models.Model):
    """信息-照片表"""
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="photo",
        verbose_name="帖子图片外键"
    )
    photo_path = models.CharField(max_length=256, null=True, verbose_name="图片path")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Comment(models.Model):
    """评论表，可以多级评论"""
    content = models.CharField(max_length=2048, null=False, verbose_name="评论正文")
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments"
    ),
    father_comment_id = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_com'
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.content


class Attention(models.Model):
    """关注表"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="att_user"
    )
    att_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="att_ed_user"
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Collect(models.Model):
    """收藏表"""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="col_user"
    )
    col_art = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="art_user"
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")


class Jc_html(models.Model):
    """老哥稳网站详情页编码"""
    html_id = models.CharField(max_length=32, null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
