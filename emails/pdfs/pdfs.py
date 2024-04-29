from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image #Flowables. Used by report lab to arrange and make a complete report
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

#~~~~~~~~~~main body of pdf~~~~~~~~~~
style = getSampleStyleSheet()
report = SimpleDocTemplate('emails/pdfs/report.pdf')
title = Paragraph('My inventory of Fruits', style['h1'])

#~~~~~~~~~~Table~~~~~~~~~~
table_data = []
for k, v in fruit.items():
    table_data.append([k,v])

table_style = [('GRID', (0,0), (-1,-1), 1, colors.pink)]
report_table = Table(data=table_data, style=table_style, hAlign='LEFT')

#~~~~~~~~~~adding a pie chart~~~~~~~~~~
report_pie = Pie(width=500, height=500)
report_pie.data = []
report_pie.labels = []

for name in sorted(fruit):
    report_pie.data.append(fruit[name])
    report_pie.labels.append(name)


report_chart = Drawing()
report_chart.add(report_pie)

report.build([title, report_table, report_chart])
# report.build([title])
