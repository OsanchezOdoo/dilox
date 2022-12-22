from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_repr


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    pedidoAdicional = fields.Integer(
        string="pedidoAdicional",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / Detalle:pedidoAdicional',
    )
    remision = fields.Char(
        string="remision",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / Detalle:remision',
    )
    crTienda = fields.Char(
        string="crTienda",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / Detalle:crTienda',
    )

    nombreTienda = fields.Char(
        string="nombreTienda",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / Detalle:nombreTienda',
    )