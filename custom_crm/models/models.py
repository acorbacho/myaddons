# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api
import datetime


class Visit(models.Model):
    _name = 'custom.crm.visit'
    _description = 'Visit'

    name = fields.Char(string='Descripción')
    customer_id = fields.Many2one(string='Cliente', comodel_name="res.partner")
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'),
                             ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Imagen')

    def toggle_state(self):
        if self.done is False:
            self.done = True
        else:
            self.done = False

# ORM
    def f_create(self):
        visit = {
            'name': random.randrange(1000000),
            'customer_id': 1,
            'date': str(datetime.date(2020, 8, 6)),
            'type': 'P',
            'done': False
        }
        print(visit)
        self.env['custom.crm.visit'].create(visit)

    def f_search_update(self):
        visit = self.env['custom.crm.visit'].search([('name', '=', self.name)])
        print('search()', visit, visit.name)

        visit.write({
            'name': 'ORM test write'
        })

    def f_delete(self):
        visit = self.env['custom.crm.visit'].search([('name', '=', self.name)])
        visit.unlink()


class VisitReport(models.AbstractModel):

    _name = 'report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['custom.crm.visit'],
            'docs': self.env['custom.crm.visit'].browse(docids)
        }


class CustomSaleOrder(models.Model):

    _inherit = 'sale.order'

    zone = fields.Selection([('N', 'Norte'), ('C', 'Centro'), ('S', 'Sur')],
                            string='Zona comercial')
