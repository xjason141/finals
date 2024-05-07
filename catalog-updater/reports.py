#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, additional_info):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    title = Paragraph(title, style['h1'])
    info = Paragraph(additional_info, style=['BodyText'])
    white_spaces = Spacer(1, 20)
    
    report.build([title, white_spaces, info])

