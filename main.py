import pandas
from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pandas.read_csv("topics.csv")

for index, rows in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=rows["Topic"], ln=1, align="L", border=0)
    pdf.line(10, 21, 200, 21)

    for i in range(rows["Pages"]-1):
        pdf.add_page()


pdf.output("output.pdf")




