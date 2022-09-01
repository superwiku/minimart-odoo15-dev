from odoo import models, fields, api


class Grup(models.Model):
    _name = 'delfimart.grup'
    _description = 'Grup Delfimart'
    # _rec_name = 'nomor_kode_grup'

    nomor_kode_grup = fields.Char(
        string='Kode Grup')
        
    name = fields.Char(
        string='Nama Grup')

    produk_ids = fields.One2many(
        comodel_name='delfimart.produk', 
        inverse_name='kode_grup_id', 
        string='Produk')

    # produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Produk')