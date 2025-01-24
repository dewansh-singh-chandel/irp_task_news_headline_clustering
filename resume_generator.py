import argparse
from fpdf import FPDF


font = "Times"
def hex_to_rgb(hex_color):
    """Convert hex color to RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def draw_line(pdf, y_offset=5, thickness=0.25, color=(0, 0, 0)):
    """Draw a horizontal line relative to the current Y position.
    Args:
        pdf (FPDF): The PDF instance.
        y_offset (float): Offset from the current Y position.
        thickness (float): Thickness of the line.
        color (tuple): RGB color of the line (default is black).
    """
    current_y = pdf.get_y()
    pdf.set_line_width(thickness)
    pdf.set_draw_color(*color)
    pdf.line(10, current_y + y_offset, 200, current_y + y_offset)


def color_name_to_hex(color_name):
    """Convert common color names to hex values."""
    colors = {
        "black": "#000000",
        "white": "#FFFFFF",
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF",
        "yellow": "#FFFF00",
        "gray": "#808080",
        "purple": "#800080",
        "cyan": "#00FFFF",
        "magenta": "#FF00FF",
    }
    return colors.get(color_name.lower(), color_name)


def create_resume(font_size, font_color, background_color):
    """Generate a customizable resume PDF."""
    pdf = FPDF()
    pdf.add_page()

    if font_color[0] != '#':
        font_color = color_name_to_hex(font_color)
    if background_color[0] != '#':
        background_color = color_name_to_hex(background_color)
    # Convert colors
    bg_r, bg_g, bg_b = hex_to_rgb(background_color)
    font_r, font_g, font_b = hex_to_rgb(font_color)

    # Set background color
    pdf.set_fill_color(bg_r, bg_g, bg_b)
    pdf.rect(0, 0, 210, 297, 'F')

    # Add content
    pdf.set_font(font, size=font_size)
    pdf.set_text_color(font_r, font_g, font_b)

    # Header Section
    pdf.set_xy(10, 10)
    pdf.set_font(font, style="B", size=font_size + 10)
    pdf.cell(0, 10, "Henrietta Mitchell", ln=True, align="C")
    pdf.set_font(font, size=font_size)
    pdf.cell(0, 5, "+123-456-7890 | hello@reallygreatsite.com | @reallygreatsite", ln=True, align="C")
    pdf.cell(0,5,"123 Anywhere St., Any City, ST 12345", ln=True,align="C")

    # Business management and analysis
    draw_line(pdf = pdf)
    pdf.ln(10)
    pdf.set_font(font, style="B", size=font_size)
    pdf.cell(0, 10, "Business Management & Analysis ", ln=True)
    pdf.set_font(font, size=font_size)
    pdf.multi_cell(0,5,"Motivated and results-driven Business School graduate seeking a challenging position within a largeorganisation as a Business Analyst or Project Manager. Offering a strong foundation in business strategy,data analysis, and project management, with a proven ability to drive efficiency, deliver successful outcomesand collaborate within cross-functional teams.")

    # Section: Key Competencies
    draw_line(pdf=pdf)
    
    pdf.ln(10)
    pdf.set_font(font, style="B", size=font_size)
    pdf.cell(0, 10, "KEY COMPETENCIES", ln=True)
    pdf.set_font(font, size=font_size)
    pdf.multi_cell(0, 5, 
    "Process improvement                Data-driven strategic planning    Cost-benefit analysis\n"
    "Report writing and presenting    Critical thinking skills                   Excellent communication skills\n"
    "Strong interpersonal skills          Proactive and self-motivated      Exceptional organisational skills")
    

    # Section: Professional Experience
    draw_line(pdf= pdf)
    pdf.ln(10)
    pdf.set_font(font, style="B", size=font_size)
    pdf.cell(0, 10, "PROFESSIONAL EXPERIENCE", ln=True)
    
    experiences = [
        {
            "company": "Arowwai Industries",
            "date": "Oct 2023 - Present",
            "role": "Business Analyst Intern",
            "details": (
                "Developed and implemented a streamlined process for gathering business requirements, reducing project delivery time by 15%. Developed and implemented a standardised reporting framework, resulting in improved visibility of key performance metrics and enabling data-driven decision-making at all levels of the organisation."
            )
        },
        {
            "company": "Hanover and Tyke",
            "date": "Jan 2022 - Aug 2023",
            "role": "Project Management Assistant",
            "details": (
                "Assisted project managers in planning and executing various projects, ensuring adherence to projecttimelines and deliverables. Monitored project budgets, tracked expenses, and prepared financial reports to ensure cost-effectiveness and adherence to financial guidelines."
            )
        },
        {
            "company": "Giggling Platypus Co.",
            "date": "July 2020 - Jan 2022",
            "role": "Barista",
            "details": (
                "Prepared and served a variety of beverages with precision and creativity, consistently meeting or exceeding quality standards, and receiving compliments for latte art and presentation."
            )
        }
    ]

    for exp in experiences:
        pdf.set_font(font, style="B", size=font_size)
        pdf.cell(0, 10, f"{exp['company']} ({exp['date']})", ln=True)
        pdf.set_font(font, style="I", size=font_size)
        pdf.cell(0, 5, exp['role'], ln=True)
        pdf.set_font(font, size=font_size)
        pdf.multi_cell(0, 5, exp['details'])
        pdf.ln(5)

    # Section: Education
    
    
    draw_line(pdf = pdf)
    pdf.ln(10)
    pdf.set_font(font, style="B", size=font_size)
    pdf.cell(0, 10, "EDUCATION & CERTIFICATIONS", ln=True)
    pdf.set_font(font, size=font_size)
    pdf.multi_cell(0, 5, "- Bachelor of Business Administration\n- Graduate Project Management Certification\n- Impact Evaluation Methods 3-Day Short Course")

    # Save PDF
    pdf.output("customized_resume.pdf")
    print("Resume generated successfully as 'customized_resume.pdf'!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a customizable resume PDF.")
    parser.add_argument("--font-size", type=int, default=12, help="Font size for the text.")
    parser.add_argument("--font-color", type=str, default="#000000", help="Font color in hex code (e.g., #000000).")
    parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Background color in hex code (e.g., #FFFFFF).")

    args = parser.parse_args()
    create_resume(args.font_size, args.font_color, args.background_color)
