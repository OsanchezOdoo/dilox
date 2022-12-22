# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    buyer_gln = fields.Char(
        string="GLN",
        default="7504001186019",
        help='Valor correspondiente modelo:buyer / modelo:gln',
    )

    buyer_personOrDepartmentName_text = fields.Char(
        string="Persona o nombre del departamento",
        default="7502",
        help='Valor correspondiente modelo:buyer / contactInformation / personOrDepartmentName / modelo:text',
    )

