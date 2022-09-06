from odoo import models, fields


class DaftarSupplierXlsx(models.AbstractModel):
    _name = 'report.minimart.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_laporan = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('Daftar Supplier')
        bold = workbook.add_format({'bold': True})
        italic = workbook.add_format({'italic': True})
        row = 1
        col = 0
        sheet.write(0, 0, str(self.tgl_laporan))
        sheet.write(row, col, 'Nama Perusahaan', bold)
        sheet.write(row, col+1, 'Alamat', bold)
        sheet.write(row, col+2, 'Contact Person', bold)
        for obj in supplier:
            row += 1
            col = 0
            sheet.write(row, col, obj.name, italic)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.pic)
            for xxx in obj.barang_ids:
                sheet.write(row, col+3, xxx.name, italic)
                col += 1
