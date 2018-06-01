# -*- coding: utf-8 -*-
# 20180107 #19 created by zhoujiang

from datetime import timedelta
from odoo import models, fields, api, exceptions

#订单添加微信备注、账号关联、内部状态
class Order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'
    # 订单的备注
    memo = fields.Char('订单备注')

    # 微信的openid和昵称
    wx_openid = fields.Char('微信账户openId')
    wx_nickname = fields.Char('微信昵称')

    # 内部状态
    status = fields.Selection(
        [('1', 'uncheck'), ('2', 'checked'), ('3', 'done'), ('4', 'untake'),('5', 'taken'),('6','uncancel'),('7','canceled')],
        'status', default="1")

    # 二维码
    wx_aqrcode = fields.Binary('订单微信二维码base64')

    # 取餐号
    take_no = fields.Char('取餐号', default='')

    #取餐时间
    take_time = fields.Datetime('预约取餐时间')

    # _sql_constraints = [
    #     ('unique_weixinuser_openid',
    #      'unique(wx_openid)', 'wx_openid should be unique per weixin_user!')]

#订单明细添加内部状态
class Orderline(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'
    # description = fields.Text(string="两面时光订单明细")
    # responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)

    # 内部状态
    status = fields.Selection(
        [('1', 'todo'),('2', 'checked'), ('3', 'done')],
        'status', default="1")

#产品添加可订数量、预约日期范围
class Product(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    # 可定数量(每天)
    order_max_number = fields.Integer('日预定上限', default=999)

    # 预约日期范围
    order_date_start = fields.Date('预定开始日期', default='2018-01-01')
    order_date_end = fields.Date('预定结束日期', default='2050-01-01')









