from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MinimartPenjualan(models.Model):
    _name = 'minimart.penjualan'
    _description = 'New Description'

    membership = fields.Boolean(string='Apakah member')

    name = fields.Char(string='No. Nota')

    nama_nonmember = fields.Char(string='Nama')

    pelanggan_id = fields.Many2one(comodel_name='minimart.pelanggan')

    id_member = fields.Char(compute='_compute_id_member', string='ID Member')

    gender = fields.Selection([
        ('male', 'Male'), ('female', 'Female')
    ], string='Gender', required='True')

    tgl_nota = fields.Datetime(string='Tanggal Nota', required='True',
                               default=fields.Datetime.now())

    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Bayar')

    detailpenjualan_ids = fields.One2many(comodel_name='minimart.detailpenjualan',
                                          inverse_name='penjualan_id',
                                          string='List Barang')

    state = fields.Selection(
        string='State',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancel', 'Cancel'),
                   ],
        required=True, readonly=True, default="draft")

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('pelanggan_id')
    def _compute_id_member(self):
        for rec in self:
            rec.id_member = rec.pelanggan_id.id_member

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for record in self:
            a = sum(self.env['minimart.detailpenjualan'].search([('penjualan_id', '=', record.id)]).mapped('subtotal'))
            record.total_bayar = a

    @api.onchange('pelanggan_id')
    def _onchange_pelanggan(self):
        if self.pelanggan_id.gender:
            self.gender = self.pelanggan_id.gender
        else:
            self.gender = ""

    # @api.ondelete(at_uninstall=False)
    # def _ondelete_penjualandetail(self):
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:  
    #             a = self.env['minimart.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for i in a:
    #             print(str(i.barang_id.name) + ' ' + str(i.qty))
    #             i.barang_id.stok += i.qty

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError('Tidak dapat menghapus selain yang masih DRAFT')
        else:
            if self.detailpenjualan_ids:
                a = []
                for wiku in self:
                    a = self.env['minimart.detailpenjualan'].search([('penjualan_id', '=', wiku.id)])
                    print(a)
                for i in a:
                    print(str(i.barang_id.name) + ' ' + str(i.qty))
                    i.barang_id.stok += i.qty
        record = super(MinimartPenjualan, self).unlink()

    def write(self, vals):
        for rec in self:
            a = self.env['minimart.detailpenjualan'].search([('penjualan_id', '=', rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name) + " " + str(data.qty) + ' ' + str(data.barang_id.stok))
                data.barang_id.stok = data.barang_id.stok + data.qty
        record = super(MinimartPenjualan, self).write(vals)
        for rec in self:
            b = self.env['minimart.detailpenjualan'].search([('penjualan_id', '=', rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name) + " " + str(databaru.qty) + " " + str(databaru.barang_id.stok))
                    databaru.barang_id.stok = databaru.barang_id.stok - databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_nota_unik', 'unique(name)', 'No. Nota harus unik yaaa...')
    ]


class MinimartDetailPenjualan(models.Model):
    _name = 'minimart.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')

    penjualan_id = fields.Many2one(comodel_name='minimart.penjualan', string='Penjualan')

    barang_id = fields.Many2one(comodel_name='minimart.barang', string='Barang')

    harga_satuan = fields.Integer(string='Harga Satuan')

    satuan = fields.Char(string='Satuan')

    qty = fields.Integer(string='QTY')

    subtotal = fields.Integer(compute='_compute_subtotal', string='subtotal')



    @api.onchange('barang_id')
    def _onchange_satuan(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual
        else:
            self.harga_satuan = ''

    @api.onchange('barang_id')
    def _compute_satuan(self):
        self.satuan = self.barang_id.satuan

    @api.depends('qty', 'harga_satuan')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.qty * record.harga_satuan

    @api.model
    def create(self, vals):
        record = super(MinimartDetailPenjualan, self).create(vals)
        if record.qty:
            self.env['minimart.barang'].search([('id', '=', record.barang_id.id)]).write(
                {'stok': record.barang_id.stok - record.qty})
        return record

    @api.constrains('qty')
    def _checkQuantity(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError('Mau belanja {} brp biji sihh...'.format(rec.barang_id.name))
            elif (rec.qty > rec.barang_id.stok):
                raise ValidationError(
                    'Stok {} tidak mencukupi, hanya tersedia {} {}'.format(rec.barang_id.name, rec.barang_id.stok,
                                                                           rec.barang_id.satuan))
