from odoo import models


class PenjualanXlsx(models.AbstractModel):
    _name = 'report.minimart.report_penjualan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    def generate_xlsx_report(self, workbook, data, penjualan):
        sheet = workbook.add_worksheet('Laporan Penjualan')
        col = 0
        row = 1
        for obj in penjualan:
            sheet.write(row, col, obj.name)
            if obj.membership:
                label = 'member'
            else:
                label = 'non member'
            sheet.write(row, col+1, label)
            row += 1