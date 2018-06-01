# -*- coding: utf-8 -*-
# 20180107 #19 created by zhoujiang

from datetime import timedelta
from odoo import models, fields, api, exceptions


class WxUser(models.Model):
    _name = 'wx.user'
    name = fields.Char(string="姓名")
    description = fields.Text(string="描述")
    # responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)

    wx_openid = fields.Char(string="微信openid")
    wx_nickname = fields.Char(string="微信昵称")
    wx_avatarUrl = fields.Char(string="微信头像")
    wx_city = fields.Char(string="微信所在城市")
    phone = fields.Char(string="手机")
    addr = fields.Char(string="地址")


    user_id = fields.Many2one('res.users')

    _sql_constraints = [
        ('unique_wxuser_openid',
         'unique(wx_openid)', 'wx_openid should be unique per weixin_user!')]






