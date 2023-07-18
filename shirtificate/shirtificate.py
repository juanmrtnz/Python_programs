from fpdf import FPDF

class PDF(FPDF):
    def set_auto_page_break(self, auto=False, margin=0):
        self.auto_page_break = auto
        self.b_margin = margin
        self.page_break_trigger = self.h - self.b_margin



def main():
    name = input("Name: ")

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('helvetica', 'B', 50)
    pdf.cell(190, 50, "CS50 Shirtificate", align='C')
    pdf.image("shirtificate.png", x=0, y=70)
    pdf.set_font('helvetica', '', 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-190, 260, f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()