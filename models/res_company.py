
from odoo import api, fields, models, tools, _

class ResCompany(models.Model):
    _inherit = 'res.company'

    oxxo_gln = fields.Char(
        string="GLN oxxo",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:glnEmisor',
    )