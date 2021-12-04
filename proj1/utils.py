import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, NamedStyle
from openpyxl.worksheet.table import Table, TableStyleInfo

def get_styles():

    bold_ = NamedStyle(name="bold_")
    bold_.font = Font(bold=True, size=18, name='Century')

    thin = Side(border_style="thin", color="000000")

    heading_ = NamedStyle(name="heading_")
    heading_.font = Font(bold=True, size=12, name='Century')
    heading_.alignment = Alignment(horizontal='center')
    heading_.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    correct_style = NamedStyle(name="correct_style")
    correct_style.font = Font(size=12, name='Century', color='FF299438')
    correct_style.alignment = Alignment(horizontal='center')
    correct_style.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    wrong_style = NamedStyle(name="wrong_style")
    wrong_style.font = Font(size=12, name='Century', color='FFFF0000')
    wrong_style.alignment = Alignment(horizontal='center')
    wrong_style.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    neut_style = NamedStyle(name="neut_style")
    neut_style.font = Font(size=12, name='Century')
    neut_style.alignment = Alignment(horizontal='center')
    neut_style.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    true_style = NamedStyle(name="true_style")
    true_style.font = Font(size=12, name='Century', color='FF0000FF')
    true_style.alignment = Alignment(horizontal='center')
    true_style.border = Border(top=thin, left=thin, right=thin, bottom=thin)

    return bold_, thin, heading_, correct_style, wrong_style, neut_style, true_style