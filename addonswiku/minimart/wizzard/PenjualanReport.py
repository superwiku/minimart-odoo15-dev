from odoo import fields, models, api


class PenjualanReport(models.TransientModel):
    _name = 'minimart.penjualanreport'
    _description = 'Description'

    pelanggan_id = fields.Many2one(
        comodel_name='minimart.pelanggan',
        string='Pelanggan',
        required=False)
    dari_tgl = fields.Date(
        string='Dari Tanggal',
        required=False)
    ke_tgl = fields.Date(
        string='Ke Tanggal',
        required=False)

    def action_reportpenjualan(self):
        member = []
        pelanggan_id = self.pelanggan_id
        dari_tgl = self.dari_tgl
        ke_tgl = self.ke_tgl
        if pelanggan_id:
            member += [('pelanggan_id', '=', pelanggan_id.id)]
        if dari_tgl:
            member += [('tgl_nota', '>=', dari_tgl)]
        if ke_tgl:
            member += [('tgl_nota', '<=', ke_tgl)]
        penjualan = self.env['minimart.penjualan'].search_read(member)
        data = {
            'form': self.read()[0],
            'penjualan': penjualan
        }
        return self.env.ref('minimart.report_penjualan_wizzardxx').report_action(self, data=data)
