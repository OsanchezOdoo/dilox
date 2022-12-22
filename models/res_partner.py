from odoo import api, fields, models, tools, _


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    oxxo_gln = fields.Char(
        string="GLN oxxo",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:glnReceptor',
    )