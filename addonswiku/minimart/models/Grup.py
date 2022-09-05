from odoo import fields, models, api


class MinimartGrup(models.Model):
    _name = 'minimart.grup'
    _description = 'Description'
  
    name = fields.Selection([
        ('makananbasah', 'Makanan Basah'),
        ('makanankering', 'Makanan Kering'),
        ('minuman', 'Minuman'),
        ('bahanmakananbasah', 'Bahan Makanan Basah'),
        ('bahanmakanankering', 'Bahan Makanan Kering'),
        ], string='Nama Grup', ondelete='cascade')

    kode_grup = fields.Char(string='Kode Grup')
    
    produk_ids = fields.One2many(
        comodel_name='minimart.produk',
        inverse_name='grup_id',
        string='Produk-produk',
        required=False)

    @api.onchange('name')
    def _onchange_namagrup(self):
        if (self.name == 'makananbasah'):
            self.kode_grup = 'mak0123'
        elif (self.name == 'makanankering'):
            self.kode_grup = 'mak2345'
        elif (self.name == 'minuman'):
            self.kode_grup = 'min9999'
        elif (self.name == 'bahanmakanankering'):
            self.kode_grup = 'bhnmak2345'
        elif (self.name == 'bahanmakananbasah'):
            self.kode_grup = 'bhnmak0123'