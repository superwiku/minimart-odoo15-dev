
from odoo import models, fields, api


class Penjualan(models.Model):
    _name = 'delfimart.penjualan'
    _description = 'Penjualan'
    # _rec_name = 'user_id'

    membership = fields.Boolean(string='Apakah member')
    nama_nonmember = fields.Char(string='Nama')
    pelanggan_id = fields.Many2one (comodel_name='delfimart.pelanggan')
    id_member = fields.Char(compute='_compute_id_member', string='ID Member')


    no_nota = fields.Char(
        string='No Nota')
    tgl_nota = fields.Datetime(
        string='Tgl Nota',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        compute='_compute_total',
        string='Total Bayar')
    # kode_pelanggan_id = fields.Many2one(
    #     comodel_name='delfimart.pelanggan', 
    #     string='Kode Pelanggan')
    user_id = fields.Char(
        string='User ID')

    penjualandetail_ids = fields.One2many(
        comodel_name='delfimart.penjualandetail', 
        inverse_name='no_nota_id', 
        string='Penjualan Detail')

    @api.depends('penjualandetail_ids')
    def _compute_total (self):
        for record in self:
            a = sum(self.env['delfimart.penjualandetail'].search([('no_nota_id', '=', record.id)]).mapped('sub_total'))
            record.total_bayar = a

    @api.depends('pelanggan_id')
    def _compute_id_member(self):
        for record in self:
            record.id_member = record.pelanggan_id.name

class Penjualan_Detail(models.Model):
    _name = 'delfimart.penjualandetail'
    _description = 'Penjualan Detail'

    no_nota_id = fields.Many2one(
        comodel_name='delfimart.penjualan', 
        string='No Nota')
    
    kode_barang_id = fields.Many2one(
        comodel_name='delfimart.barang', 
        string='Barang')

    harga_jual = fields.Integer(
        # compute='_compute_hargasatuan',
        string='Harga Jual',
        related='kode_barang_id.harga_jual')

    jumlah = fields.Integer(
        string='Jumlah')

    sub_total = fields.Integer(
        compute='_compute_total',
        string='Sub Total')


    @api.depends('jumlah')
    def _compute_total(self):
        for record in self:
            if record.jumlah:
                record.sub_total = record.jumlah * record.harga_jual
            else:
                record.sub_total = 0
    
    @api.model
    def create(self, vals):
        record = super(Penjualan_Detail, self).create(vals)
        if record.jumlah:
            self.env['delfimart.barang'].search([('id', '=', record.kode_barang_id.id)]).write({
                'stok': record.kode_barang_id.stok+record.jumlah})
            return record

