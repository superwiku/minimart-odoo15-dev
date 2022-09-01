from pyexpat import model
from odoo import models, fields, api

class Produk(models.Model):
    _name = 'delfimart.produk'
    _description = 'Ini produk delfimart'
    # _rec_name = 'nomor_kode_produk'

    nomor_kode_produk = fields.Char(
        string='Kode Produk')
    
    name = fields.Char(
        string='Nama Produk')
    
    kode_grup_id = fields.Many2one(
        comodel_name='delfimart.grup', 
        string='Grup')

    barang_ids = fields.One2many(
        comodel_name='delfimart.barang', 
        inverse_name='kode_produk_id', 
        string='Barang')

    # produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Produk')

    # kode_produk_id = fields.Many2one(
    #     comodel_name='delfimart.produk', 
    #     string='Kode Produk')