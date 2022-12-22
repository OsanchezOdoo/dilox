# -*- coding: utf-8 -*-


from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError, UserError
from odoo.tools.float_utils import float_repr


class AccountMove(models.Model):
    _inherit = 'account.move'

    entityType = fields.Selection([
        ('FA', 'Factura o Nota de Cargo'),
        ('AN', 'Anticipo'),
        ('ND', 'Nota de Crédito x devolución'),
        ('NA', 'Nota de Crédito por ajuste en precio'),
        ('NE', 'Nota de Crédito por descuento'),
        ('CO', 'Mercancías en Consignación')],
        string='Tipo',
        default='FA',
        help='Valor correspondiente modelo:entityType',
        copy=False)

    specialInstructioncode = fields.Selection([
        ('AAB', 'Condiciones de pag'),
        ('DUT', 'Información de impuestos (Pedimentos'),
        ('PUR', 'Información de compra'),
        ('ZZZ', 'Importe con letra')],
        string='Tipo', default='PUR',
        help='Valor correspondiente modelo:specialInstruction code=',
        copy=False)

    specialInstruction = fields.Text(
        string="Especial instruccion",
        help='Valor correspondiente modelo:text',
        copy=False
    )

    referenceIdentification = fields.Char(
        string="referencia Identificación",
        help='Valor correspondiente modelo:referenceIdentification',
        copy=False
    )

    alternatePartyIdentification = fields.Selection([
        ('VA', 'Identificación Tributaria'),
        ('IA', 'Numero interno del proveedor')],
        string='Identificación de parte alternativa', default='IA',
        help='Valor correspondiente modelo:InvoiceCreator / modelo:alternatePartyIdentification type=',
        copy=False)