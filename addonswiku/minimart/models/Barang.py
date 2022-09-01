from odoo import fields, models, api


class MinimartBarang(models.Model):
    _name = 'minimart.barang'
    _description = 'Description'

    name = fields.Char(string="Nama Barang")
    kode_spec = fields.Char(string='Kode Spec')    
    kode_barang = fields.Char(
        string='Kode Barang',
        required=False)
    satuan = fields.Char(
        string='Satuan',
        required=False)
    harga_jual = fields.Integer(
        string='Harga Jual', 
        required=False)
    harga_beli = fields.Integer(
        string='Harga Beli', 
        required=False)
    stok = fields.Integer(
        string='Stok', 
        required=False)
    produk_id = fields.Many2one(
        comodel_name='minimart.produk',
        string='ID Produk',
        required=False)
    jenis = fields.Selection([('minuman', 'Minuman'),('makanan', 'Makanan'),('bahanmakanan', 'Bahan Makanan')], string='Jenis')
    supplier_ids = fields.Many2many(comodel_name='minimart.supplier', string='Daftar Supplier')
    
    @api.onchange('produk_id','kode_spec')
    def _onchange_produk(self):
        self.kode_barang = str(self.produk_id.kode_produk)+' '+str(self.kode_spec)