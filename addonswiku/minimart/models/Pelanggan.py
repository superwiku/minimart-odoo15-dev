from odoo import api, fields, models


class Pelanggan(models.Model):
    _name = 'minimart.pelanggan'
    _inherit = 'minimart.manusia'
    _description = 'New Description'

    id_member = fields.Char(string='ID Member')
    
    level = fields.Selection(
        string='Level',
        selection=[('silver', 'Silver'),
                   ('gold', 'Gold'),
                   ('platinum', 'Patinum'),
                   ],
        required=True, readonly=True, default='silver')

    
    
