from odoo import api, fields, models, _


class Pelanggan(models.Model):
    _name = 'minimart.pelanggan'
    _inherit = 'minimart.manusia'
    _description = 'New Description'
    _rec_name = 'id_member'

    id_member = fields.Char(string='ID Member', required=True, copy=False, readonly=True,
                       default=lambda self: _('New'))
    
    level = fields.Selection(
        string='Level',
        selection=[('silver', 'Silver'),
                   ('gold', 'Gold'),
                   ('platinum', 'Patinum'),
                   ],
        required=True, readonly=True, default='silver')

    @api.model
    def create(self, vals):
        if vals.get('id_member', _('New')) == _('New'):
            vals['id_member'] = self.env['ir.sequence'].next_by_code('minimart.datamember') or _('New')
        record = super(Pelanggan, self).create(vals)
        return record
    
