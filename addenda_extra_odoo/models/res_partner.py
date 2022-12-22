# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    shipping_gln = fields.Char(
        string="GLN",
        default="7500000000000",
        help='Valor correspondiente modelo:seller / modelo:gln',
    )
    
    shipping_number_provider = fields.Char(
        string="Numero de proveedor",
        help='Valor correspondiente modelo:seller / modelo:alternatePartyIdentification',
    )
