
from odoo import models, fields, api


class Pembelian(models.Model):
    
    _name = 'delfimart.pembelian'
    _description = 'Pembelian'
    # _rec_name = 'kode_pemasok_id'

    
    pembeliandetail_ids = fields.One2many(
        comodel_name='delfimart.pembeliandetail', 
        inverse_name='no_masuk_id', 
        string='Pembelian Detail')

    no_masuk = fields.Char(
        string='No Masuk')
    tgl_masuk = fields.Date(
        string='Tgl Masuk')
    total_bayar = fields.Integer(
        compute='_compute_total',
        string='Total Bayar')
    kode_pemasok_id = fields.Many2one(
        comodel_name='delfimart.pemasok', 
        string='Kode Pemasok')
    user_id = fields.Char(
        string='User ID')
    
    @api.depends('pembeliandetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['delfimart.pembeliandetail'].search([('no_masuk_id', '=', record.id)]).mapped('sub_total'))
            record.total_bayar = a

    
    
    
class PembelianDetail(models.Model):
    _name = 'delfimart.pembeliandetail'
    _description = 'Pembelian Detail'

    no_masuk_id = fields.Many2one(
        comodel_name='delfimart.pembelian', 
        string='No Masuk')
    kode_barang_id = fields.Many2one(
        comodel_name='delfimart.barang', 
        string='Barang')
        # domain=[('kode_produk_id', '=', 'kode_produk_id.nama_barang')])

    # harga_beli_satuan = fields.Integer(
    #     string='Harga Satuan')

    harga_beli_satuan = fields.Integer(
        compute='_compute_hargasatuan',
        string='Harga Satuan')

    jumlah = fields.Integer(
        compute ='_compute_jumlah_stok',
        string='Jumlah')
    sub_total= fields.Integer(
        compute='_compute_total',
        string='Total')

    # barang_ids = fields.One2many(
    #     comodel_name='delfimart.barang', 
    #     inverse_name='kode_produk_id', 
    #     string='Pembelian Detail')

    @api.model
    def create(self, vals):
        record = super(PembelianDetail, self).create(vals)
        if record.jumlah:
            self.env['delfimart.barang'].search([('id', '=', record.kode_barang_id.id)]).write({
                'stok': record.kode_barang_id.stok+record.jumlah})
            return record

    @api.depends()
    def _compute_jumlah_stok(self):
        for record in self:
            record.jumlah = record.kode_barang_id.stok

    @api.depends('kode_barang_id')
    def _compute_hargasatuan(self):
        for record in self:
            record.harga_beli_satuan = record.kode_barang_id.harga_beli

    @api.depends('jumlah')
    def _compute_total(self):
        for record in self:
            if record.jumlah:
                record.sub_total = record.jumlah * record.harga_beli_satuan
            else:
                record.sub_total = 0
