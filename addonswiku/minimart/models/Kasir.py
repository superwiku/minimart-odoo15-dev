from odoo import api, fields, models


class Kasir(models.Model):
    _name = 'minimart.kasir'
    _inherit = 'minimart.manusia'
    _description = 'New Description'

    id_pegawai = fields.Char(string='ID Pegawai')
    status_pegawai = fields.Selection([
        ('kontrak', 'Pegawai Kontrak'),
        ('tetap', 'Pegawai Tetap'),
        ('magang', 'Pegawai Magang'),
    ], string='status_pegawai')
    