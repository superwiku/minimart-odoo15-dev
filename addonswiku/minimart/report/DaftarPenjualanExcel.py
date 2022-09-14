from odoo import models


class PenjualanXlsx(models.AbstractModel):
    _name = 'report.minimart.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Laporan Penjualan')
        sheet.write(0, 0, 'KODE TRANSAKSI')
        sheet.write(0, 1, 'NAMA')
        sheet.write(0, 2, 'MEMBERSHIP')
        col = 0
        row = 1
        for obj in penjualan:
            sheet.write(row, col, obj.kode)
            if obj.nama_nonmember:
                sheet.write(row, col+1, obj.nama_nonmember)
            else:
                sheet.write(row, col+1, obj.pelanggan_id.name)
            if obj.membership:
                label = 'member'
            else:
                label = 'non member'
            sheet.write(row, col+2, label)

            row += 1