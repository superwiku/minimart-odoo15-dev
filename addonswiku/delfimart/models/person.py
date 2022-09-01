from odoo import models, fields, api


class Person(models.Model):
    # _inherit = 'res.partner'
    _name = 'delfimart.person'
    _description = 'orang'

    alamat = fields.Char(
        string='Alamat')
    no_telepon = fields.Char(
        string='No Telepon')

class Pemasok(models.Model):
    _inherit = 'delfimart.person'
    _name = 'delfimart.pemasok'
    _description = 'pemasok barang'
    # _rec_name = 'kode_pemasok'

    kode_pemasok = fields.Char(
        string='Kode Pemasok')
    name = fields.Char(
        string='Nama Pemasok')
    kota = fields.Char(
        string='Kota')
    provinsi = fields.Char(
        string='Provinsi')
    no_fax = fields.Char(
        string='No Fax')
    kontak = fields.Char(
        string='Kontak')

class Pelanggan(models.Model):
    _inherit = 'delfimart.person'
    _name = 'delfimart.pelanggan'
    _description = 'pemasok barang'
    # _rec_name = 'kode_pelanggan'

    kode_pelanggan = fields.Char(
        string='Kode Pelanggan')
    name = fields.Char(
        string='Nama Pelanggan')