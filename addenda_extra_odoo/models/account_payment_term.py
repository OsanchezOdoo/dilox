# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class AccountPaymentTerm(models.Model):
    _inherit = 'account.payment.term'

    term_day = fields.Integer(
        string="Numero",
        help='Valor correspondiente modelo:paymentTerms / modelo:netPayment / modelo:paymentTimePeriod / modelo:timePeriodDue / modelo:value',
    )
    