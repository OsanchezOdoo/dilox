from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_repr


class AccountMove(models.Model):
    _inherit = 'account.move'

    claseDoc = fields.Char(
        string="claseDoc",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:claseDoc',
    )
    plaza = fields.Char(
        string="plaza",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:plaza',
    )
    tipoProv = fields.Char(
        string="tipoProv",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:tipoProv',
    )
    locType = fields.Char(
        string="locType",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:locType',
    )
    folioPago = fields.Char(
        string="folioPago",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:folioPago',
    )
    ordCompra = fields.Char(
        string="ordCompra",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:ordCompra',
    )
    tipoValidacion = fields.Integer(
        string="tipoValidacion",
        default="1",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:tipoValidacion',
    )
    fuenteNota = fields.Integer(
        string="fuenteNota",
        default="1",
        help='Addenda Oxxo, Valor correspondiente oxxo:AddendaOXXO / oxxo:fuenteNota',
    )
    