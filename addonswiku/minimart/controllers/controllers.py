
from odoo import http, models, fields
from odoo.http import request
import json


class Minimart(http.Controller):
    @http.route('/minimart/get_barang', auth='public', method=['GET'])
    def getBarang(self, **kw):
        barang = request.env['minimart.barang'].search([])
        isi = []
        for b in barang:
            isi.append({
                'nama_barang' : b.name,
                'hrg_beli' : b.harga_beli,
                'hrg_jual' : b.harga_jual
            })
        return json.dumps(isi)

    @http.route('/minimart/get_produk', auth='public', method=['GET'])
    def getProduk(self, **kw):
        prod = request.env['minimart.produk'].search([])
        produk = []
        for p in prod:
            produk.append({
                'nama_produk' : p.name,
                'kode_produk' : p.kode_produk
            })
        return json.dumps(produk)


    
