from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("topics.csv")

for index, rows in df.iterrows():

    # Adds the parent page
    pdf.add_page()

    # Creates the Header with a line below it
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=rows["Topic"], ln=1, align="L", border=0)
    pdf.line(10, 21, 200, 21)

    # Creates footer
    pdf.ln(265)  # Breaks line by 260 mm or takes you 260 mm down
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=8, txt=rows['Topic'], ln=1, align='R')

    for i in range(rows["Pages"]-1):
        pdf.add_page()

        # Creates footer
        pdf.ln(277)  # Breaks line by 260 mm or takes you 260 mm down
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=8, txt=rows['Topic'], ln=1, align='R')



pdf.output("output.pdf")




