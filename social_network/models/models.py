# -*- coding: utf-8 -*-

from odoo import models, fields


class SocialNetwork(models.Model):

    _name = 'social.network'
    _description = 'Social Network'

    name = fields.Char(string='Name')


class SocialNetworkAccount(models.Model):
    _name = 'social.network.account'
    _description = 'Social Network Accounts'

    name = fields.Char(string='Username', required=True)
    password = fields.Char(string='Password', required=True,)
    date = fields.Date(string='Registry date', readonly=True, default=fields.Datetime.now)
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')


class ResPartner(models.Model):

    _inherit = 'res.partner'

    social_id = fields.One2many(comodel_name='social.network.account', inverse_name='customer_id',
                                string='Social Network')
