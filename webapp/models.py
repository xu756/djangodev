from django.db import models

choices = (
    ('男', '男性'),
    ('女', '女性'),
)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100, default='user', verbose_name="用户名")
    password = models.CharField(max_length=100, default='123456', verbose_name="密码")
    email = models.EmailField(max_length=100, default='email@qq.com', verbose_name="邮箱")
    gender = models.CharField(max_length=2, choices=choices, default='男', verbose_name='性别')

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = 'user'
        verbose_name = '用户列表'
        verbose_name_plural = verbose_name
