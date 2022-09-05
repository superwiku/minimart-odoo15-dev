from odoo import fields, models, api


class MinimartProduk(models.Model):
    _name = 'minimart.produk'
    _description = 'Description'

    name = fields.Char(string='Nama Produk')

    kode_spec = fields.Char(string='Kode Spec')    

    kode_produk = fields.Char(
        string='Kode Produk')

    grup_id = fields.Many2one(
        comodel_name='minimart.grup',
        string='ID Grup',
        required=False)
        
    barang_ids = fields.One2many(
        comodel_name='minimart.barang',
        inverse_name='produk_id',
        string='ID Barang',
        required=False)   

    @api.onchange('grup_id','kode_spec')
    def _onchange_grup(self):
        if (self.grup_id.kode_grup):
            self.kode_produk = str(self.grup_id.kode_grup) +' '+ str(self.kode_spec)
        else:
            self.kode_produk = ""
    
   
    

