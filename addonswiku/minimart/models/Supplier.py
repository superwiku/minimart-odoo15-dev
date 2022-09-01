from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'minimart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='')
    pic = fields.Char(string='Contact Person')
    no_pic = fields.Char(string='No.Telp Contact')  
    
    barang_ids = fields.Many2many(comodel_name='minimart.barang', string='Supply Barang')
    
