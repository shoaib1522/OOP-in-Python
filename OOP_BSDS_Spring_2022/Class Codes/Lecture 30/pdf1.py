from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("times", size = 16)
pdf.cell(200, 10, txt = "My PDF File", ln = 1, align = 'C')
pdf.set_font("times", size = 14)
pdf.cell(100, 10, txt = "This is line 1.", ln = 1, align = 'R')
pdf.cell(100, 10, txt = "This is line 2.", ln = 1, align = 'L')
pdf.cell(200, 10, txt = "This is line 3.", ln = 1, align = 'C')
pdf.cell(100, 10, txt = "This is end of document.", ln = 1, align = 'L')
pdf.output('test.pdf')
