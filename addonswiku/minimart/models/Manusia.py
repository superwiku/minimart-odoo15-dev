from odoo import api, fields, models


class Manusia(models.Model):
    _name = 'minimart.manusia'
    _description = 'New Description'

    name = fields.Char(string='Nama', required='True')

    gender = fields.Selection([
        ('male', 'Male'),('female','Female')
    ], string='Gender', required='True')
    
    alamat = fields.Char(string='Alamat')
    
