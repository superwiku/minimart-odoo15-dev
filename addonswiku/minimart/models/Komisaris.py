from odoo import api, fields, models


class Komisaris(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    jabatan = fields.Selection([
        ('komut', 'Komisaris Utama'),
        ('anggota', 'Komisaris'),
    ], string='Jabatan')
