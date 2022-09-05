from odoo import fields, models, api


class Dagangan(models.Model):
    _inherit = 'product.product'
    _description = 'Description'
    
    name = fields.Char()
