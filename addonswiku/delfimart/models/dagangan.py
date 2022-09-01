from odoo import models, fields, api


class Dagangan(models.Model):
    _inherit = 'product.product'
    _description = 'Dagangan'
    name = fields.Char()
