# #imports for extrastion data from limeservey
# import requests
# import base64
# import json
# import pandas as pd

# #imports for the creation of the pdf document
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# import chardet
# import pandas as pd
# from reportlab.lib.colors import red, blue, green, black
# from reportlab.lib.colors import Color



# from reportlab.lib.pagesizes import letter
# from reportlab.lib.colors import Color, blue, black
# from reportlab.pdfgen import canvas

# def make_and_save_pdf(Raw_df):

#     # Function to create a PDF document
#     def create_pdf(df, filename):
#         row = df.iloc[0]
#         Name = row["id"]

#         c = canvas.Canvas(filename, pagesize=letter)
#         width, height = letter
#         c.setFont("Helvetica", 12)

#         # Set the background color (for example, light gray)
#         background_color = Color(0.4, 0.5, 0.6)  # RGB values for grayish-blue

#         # Draw the background rectangle
#         c.setFillColor(background_color)
#         c.rect(0, 0, width, height, stroke=0, fill=1)

#         # Setting up height var
#         current_height = height - 50  # Starting height for the header

#         # Add sections to the PDF
#         current_height = add_header(c, current_height, Name)

#         current_height = FundRecomendation(c, current_height, row)
#         current_height = add_risk_tolerance(c, current_height, row)
#         current_height = Risk_capacity(c, current_height, row)
#         current_height = investment_knowledge(c, current_height, row)
#         current_height = composere(c, current_height, row)
        
#         current_height = add_assets_breakdown(c, current_height, row)
#         current_height = add_liabilities_breakdown(c, current_height, row)
#         current_height = add_income_expenses(c, current_height, row)
#         current_height = add_free_assets(c, current_height, row)
#         current_height = add_sustainability_preferences(c, current_height, row)

#         # Add logo and border
#         add_logo(c, width, height)
#         add_border(c, width, height)

#         c.save()

#     def add_header(c, current_height, Name):
#         c.setFont("Helvetica-Bold", 16)
#         c.setFillColor(blue)
#         c.drawString(200, current_height, f"{Name}'s Risk Tolerance Report")
#         c.setFillColor(black)
#         return current_height - 15
    
#     def FundRecomendation(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Fund Recomendataion")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"Risk tolerance: {row['Risk_Tolerance']}")
#         return current_height - 30

#     def add_risk_tolerance(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Risk Tolerance")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"Risk tolerance: {row['Risk_Tolerance']}")
#         return current_height - 30
    
#     def Risk_capacity(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Risk capacity")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"Risk tolerance: {row['Risk_Tolerance']}")
#         return current_height - 30
    
#     def investment_knowledge(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "investment knowledge")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"Risk tolerance: {row['Risk_Tolerance']}")
#         return current_height - 30
    
#     def composere(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "composere")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"Risk tolerance: {row['Risk_Tolerance']}")
#         return current_height - 30


    


#     def add_assets_breakdown(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Assets Breakdown")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         assets = [
#             f"- Liquid assets with UBS: {row['Assets: Liquid assets with UBS']} {row['Entry of Currency']}",
#             f"- Liquid assets with other: {row['Assets: Liquid Assets with other']} {row['Entry of Currency']}",
#             f"- Real estate assets: {row['Assets: Real Estate']} {row['Entry of Currency']}",
#             f"- Pension assets: {row['Assets: Pension Assets']} {row['Entry of Currency']}",
#             f"- Other assets: {row['Assets: Other assets']} {row['Entry of Currency']}",
#             f"- Total assets: {row['Assets: Total Assets']} {row['Entry of Currency']}"
#         ]
#         for asset in assets:
#             c.drawString(30, current_height, asset)
#             current_height -= 15
#         return current_height - 15

#     def add_liabilities_breakdown(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Liabilities Breakdown")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         liabilities = [
#             f"- Lombard loans with UBS: {row['Liabilities: Lombard loans with UBS']} {row['Entry of Currency']}",
#             f"- Other loans: {row['Liabilities: Other loans']} {row['Entry of Currency']}",
#             f"- Mortgages: {row['Liabilities: Mortgages']} {row['Entry of Currency']}",
#             f"- Total Liabilities: {row['Liabilities: Total Liabilities']} {row['Entry of Currency']}"
#         ]
#         for liability in liabilities:
#             c.drawString(30, current_height, liability)
#             current_height -= 15
#         return current_height - 15

#     def add_income_expenses(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Income and Expenses")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         incomes_expenses = [
#             f"- Average annual income: {row['Recurring income: Average annual income']} {row['Entry of Currency']}",
#             f"- Average annual expenses: {row['Recurring expenses: Average annual expenses']} {row['Entry of Currency']}",
#             f"- Non-recurring income: {row['Non-recurring income']} {row['Entry of Currency']}",
#             f"- Non-recurring expenses: {row['Non-recurring expenses']} {row['Entry of Currency']}"
#         ]
#         for item in incomes_expenses:
#             c.drawString(30, current_height, item)
#             current_height -= 15
#         return current_height - 15

#     def add_free_assets(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Free Assets")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"- Free assets: {row['Free assets']} {row['Entry of Currency']}")
#         current_height -= 15
#         c.drawString(30, current_height, f"- Free asset ratio: {row['Free asset ratio']}")
#         return current_height - 30

#     def add_sustainability_preferences(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Sustainability Preferences")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         c.drawString(30, current_height, f"- Sustainability preferences with UBS: {row['Sustainability preference with UBS methodology']}")
#         return current_height - 100

#     def add_logo(c, width, height):
#         image_width = 150
#         image_height = 50
#         x_position = width - image_width - 20  # 20 points margin from the right
#         y_position = height - image_height - 20  # 20 points margin from the top
#         c.drawImage("logo.JPG", x_position, y_position, width=image_width, height=image_height)

#     def add_border(c, width, height):
#         margin = 15
#         c.rect(margin, margin, width - 2 * margin, height - 2 * margin, stroke=1, fill=0)

#     # Create the PDF
#     pdf_file_path = '/Users/Toby/Desktop/Patch/OUTPUT5.pdf'
#     create_pdf(Raw_df, pdf_file_path)

#     print(f"PDF created: {pdf_file_path}")





# #imports for extrastion data from limeservey
# import requests
# import base64
# import json
# import pandas as pd

# #imports for the creation of the pdf document
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.colors import blue, black
# from reportlab.lib.pagesizes import letter

# def make_and_save_pdf(Raw_df):

#     # Function to create a PDF document
#     def create_pdf(df, filename):
#         row = df.iloc[0]
#         Name = row.get("name", "Client")  # Default to "Client" if "currency" is not available

#         c = canvas.Canvas(filename, pagesize=letter)
#         width, height = letter
#         c.setFont("Helvetica", 12)

#         # Set the background color (for example, light gray)
#         background_color = colors.Color(0.4, 0.5, 0.6)  # RGB values for grayish-blue

#         # Draw the background rectangle
#         c.setFillColor(background_color)
#         c.rect(0, 0, width, height, stroke=0, fill=1)

#         # Setting up height var
#         current_height = height - 50  # Starting height for the header

#         # Add sections to the PDF
#         current_height = add_header(c, current_height, Name)
#         current_height = add_currenccy(c, current_height, row)

#         current_height = add_overall_wealth(c, current_height, row)
#         current_height = add_risk_capacity(c, current_height, row)
#         current_height = add_risk_tolerance(c, current_height, row)
#         current_height = add_suitability_rating(c, current_height, row)
#         current_height = add_future_cashflow(c, current_height, row)
#         current_height = add_composure_discount(c, current_height, row)

#         current_height = add_assets_breakdown(c, current_height, row)
#         current_height = add_liabilities_breakdown(c, current_height, row)

#         # Add logo and border
#         add_logo(c, width, height)
#         add_border(c, width, height)

#         c.save()

#     def add_header(c, current_height, Name):
#         c.setFont("Helvetica-Bold", 16)
#         c.setFillColor(blue)
#         c.drawString(200, current_height, f"{Name}'s Risk Tolerance Report")
#         c.setFillColor(black)
#         return current_height - 15
    
#     def add_currenccy(c, current_height, row):
#         c.setFont("Helvetica-Bold", 16)
#         c.setFillColor(blue)
#         c.drawString(200, current_height, f"All ammounts are in: {row.get('currency', '')}")
#         c.setFillColor(black)
#         return current_height - 15

#     def add_overall_wealth(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Overall Wealth")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         overall_wealth = row.get('Overall_Wealth', 'N/A')
#         currency = row.get('currency', '')
#         c.drawString(30, current_height, f"Overall Wealth: {overall_wealth} {currency}")
#         return current_height - 30

#     def add_risk_capacity(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Risk Capacity")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         risk_capacity = row.get('Risk_Capacity', 'N/A')
#         c.drawString(30, current_height, f"Risk Capacity: {risk_capacity}")
#         return current_height - 30
    
#     def add_risk_tolerance(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Risk Tolerance")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         risk_tolerance = row.get('Risk_Tolerance', 'N/A')
#         c.drawString(30, current_height, f"Risk Tolerance: {risk_tolerance}")
#         return current_height - 30
    
#     def add_suitability_rating(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Suitability Rating")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         suitability_rating = row.get('Suitability_rating', 'N/A')
#         c.drawString(30, current_height, f"Suitability Rating: {suitability_rating}")
#         return current_height - 30
    
#     def add_future_cashflow(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Future Cashflow")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         future_cashflow = row.get('Future_cashflow', 'N/A')
#         currency = row.get('currency', '')
#         c.drawString(30, current_height, f"Future Cashflow: {future_cashflow} {currency}")
#         return current_height - 30

#     def add_composure_discount(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Composure Discount")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         composure_discount = row.get('Composure_discount', 'N/A')
#         c.drawString(30, current_height, f"Composure Discount: {composure_discount}")
#         return current_height - 30

#     def add_assets_breakdown(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Assets Breakdown")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         assets = [
#             f"- Liquid assets total: {row.get('liquid_assets_total', 'N/A')} {row.get('currency', '')}",
#             f"- Real estate: {row.get('real_estate', 'N/A')} {row.get('currency', '')}",
#             f"- Investible assets: {row.get('Investible_Asset', 'N/A')} {row.get('currency', '')}",
#             f"- Net non-investible assets: {row.get('net_non_investible_assets', 'N/A')} {row.get('currency', '')}",
#             f"- Overall wealth: {row.get('Overall_Wealth', 'N/A')} {row.get('currency', '')}"
#         ]
#         for asset in assets:
#             c.drawString(30, current_height, asset)
#             current_height -= 15
#         return current_height - 15

#     def add_liabilities_breakdown(c, current_height, row):
#         c.setFont("Helvetica-Bold", 14)
#         c.drawString(30, current_height, "Liabilities Breakdown")
#         current_height -= 16
#         c.setFont("Helvetica", 12)
#         liabilities = [
#             f"- Current liabilities: {row.get('current_liabilities', 'N/A')} {row.get('currency', '')}"
#         ]
#         for liability in liabilities:
#             c.drawString(30, current_height, liability)
#             current_height -= 15
#         return current_height - 15

#     def add_logo(c, width, height):
#         image_width = 150
#         image_height = 50
#         x_position = width - image_width - 20  # 20 points margin from the right
#         y_position = height - image_height - 20  # 20 points margin from the top
#         #c.drawImage({{ url_for('static', filename="logo.JPG") }}, x_position, y_position, width=image_width, height=image_height)

#     def add_border(c, width, height):
#         margin = 15
#         c.rect(margin, margin, width - 2 * margin, height - 2 * margin, stroke=1, fill=0)

#     # Create the PDF
#     pdf_file_path = 'OUTPUT5.pdf'
#     create_pdf(Raw_df, pdf_file_path)

#     print(f"PDF created: {pdf_file_path}")












#imports for extrastion data from limeservey
import requests
import base64
import json
import pandas as pd

#imports for the creation of the pdf document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import letter


from google.cloud import storage
import os

# Imports for extracting data from LimeSurvey
import requests
import base64
import json
import pandas as pd

# Imports for the creation of the PDF document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.colors import blue, black
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics








# Michle here is the list of vairbles to use

    # 'name': name,
    # 'currency': currency,
    # 'Confidence': Confidence,
    # 'Impulsivity': Impulsivity,
    # 'Familiarity_preferences': Familiarity_preferences,
    # 'Risk_tolerance': Risk_tolerance,
    # 'Composure': Composure,
    # 'Overall_Wealth': Overall_Wealth,
    # 'Risk_capacity': Risk_capacity,
    # 'Suitability_rating': Suitability_rating,
    # 'Objective_experience': Objective_experience,
    # 'Investment_history': Investment_history,
    # 'Objective_knowledge': Objective_knowledge,
    # 'self_Identification_of_knowledge': self_Identification_of_knowledge,
    # 'Impact_desire': Impact_desire,
    # 'Impact_apprehension': Impact_apprehension,
    # 'Impact_tradeoff': Impact_tradeoff,
    # 'need_for_evidence': need_for_evidence,
    # 'Level_of_sustainable_assets': Level_of_sustainable_assets










# Function to create and save a PDF document
def make_and_save_pdf(Raw_df):


    print("------------------------------------------")

    # Register Hoefler Text fonts
    pdfmetrics.registerFont(TTFont('HoeflerText-Regular', 'static/fonts/FontPackages/hoefler-text.ttf'))
    pdfmetrics.registerFont(TTFont('HoeflerText-Italic', 'static/fonts/FontPackages/hoefler-text-italic.ttf'))
    pdfmetrics.registerFont(TTFont('HoeflerText-Black', 'static/fonts/FontPackages/hoefler-text-black.ttf'))

    # Function to create a PDF document
    def create_pdf(df, filename):
        # Extract the first row of the dataframe
        row = df.iloc[0]
        # Get the client's name or default to "Client" if not available
        Name = row.get("name", "Client")

        # Create a canvas object for the PDF
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        c.setFont("HoeflerText-Regular", 12)

        # Set the background color to a grayish-blue
        background_color = colors.Color(255, 255, 255)
        
        # Draw the background rectangle
        c.setFillColor(background_color)
        c.rect(0, 0, width, height, stroke=0, fill=1)

        # Initial height setting for the header
        current_height = height - 50

        # Add sections to the PDF
        current_height = add_header(c, current_height, Name)
        current_height = add_currency(c, current_height, row)
        current_height = add_overall_wealth(c, current_height, row)
        current_height = add_risk_capacity(c, current_height, row)
        current_height = add_risk_tolerance(c, current_height, row)
        current_height = add_suitability_rating(c, current_height, row)
        current_height = add_future_cashflow(c, current_height, row)
        current_height = add_composure_discount(c, current_height, row)
        current_height = add_assets_breakdown(c, current_height, row)
        current_height = add_liabilities_breakdown(c, current_height, row)
        current_height = add_financial_summary(c, current_height, row)

        # Add logo and border to the PDF
        add_logo(c, width, height)
        add_border(c, width, height)

        # Save the PDF document
        c.save()

    # Function to add the header to the PDF
    def add_header(c, current_height, Name):
        c.setFont("HoeflerText-Black", 16)
        c.setFillColorRGB(14/255, 28/255, 50/255)
        c.drawString(200, current_height, f"{Name}'s Risk Tolerance Report")
        c.setFillColor(black)
        return current_height - 15

    # Function to add the currency information to the PDF
    def add_currency(c, current_height, row):
        c.setFont("HoeflerText-Black", 16)
        c.setFillColorRGB(14/255, 28/255, 50/255)
        c.drawString(200, current_height, f"All amounts are in: {row.get('currency', '')}")
        c.setFillColor(black)
        return current_height - 15

    # Function to add the overall wealth information to the PDF
    def add_overall_wealth(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Overall Wealth")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        overall_wealth = row.get('Overall_Wealth', 'N/A')
        currency = row.get('currency', '')
        c.drawString(30, current_height, f"Overall Wealth: {overall_wealth} {currency}")
        return current_height - 30

    # Function to add the risk capacity information to the PDF
    def add_risk_capacity(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Risk Capacity")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        risk_capacity = row.get('Risk_Capacity', 'N/A')
        c.drawString(30, current_height, f"Risk Capacity: {risk_capacity}")
        return current_height - 30

    # Function to add the risk tolerance information to the PDF
    def add_risk_tolerance(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Risk Tolerance")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        risk_tolerance = row.get('Risk_Tolerance', 'N/A')
        c.drawString(30, current_height, f"Risk Tolerance: {risk_tolerance}")
        return current_height - 30

    # Function to add the suitability rating information to the PDF
    def add_suitability_rating(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Suitability Rating")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        suitability_rating = row.get('Suitability_rating', 'N/A')
        c.drawString(30, current_height, f"Suitability Rating: {suitability_rating}")
        return current_height - 30

    # Function to add the future cashflow information to the PDF
    def add_future_cashflow(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Future Cashflow")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        future_cashflow = row.get('Future_cashflow', 'N/A')
        currency = row.get('currency', '')
        c.drawString(30, current_height, f"Future Cashflow: {future_cashflow} {currency}")
        return current_height - 30

    # Function to add the composure discount information to the PDF
    def add_composure_discount(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Composure Discount")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        composure_discount = row.get('Composure_discount', 'N/A')
        c.drawString(30, current_height, f"Composure Discount: {composure_discount}")
        return current_height - 30

    # Function to add the assets breakdown to the PDF
    def add_assets_breakdown(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Assets Breakdown")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        assets = [
            f"- Liquid assets total: {row.get('liquid_assets_total', 'N/A')} {row.get('currency', '')}",
            f"- Real estate: {row.get('real_estate', 'N/A')} {row.get('currency', '')}",
            f"- Investible assets: {row.get('Investible_Asset', 'N/A')} {row.get('currency', '')}",
            f"- Net non-investible assets: {row.get('net_non_investible_assets', 'N/A')} {row.get('currency', '')}",
            f"- Overall wealth: {row.get('Overall_Wealth', 'N/A')} {row.get('currency', '')}"
        ]
        for asset in assets:
            c.drawString(30, current_height, asset)
            current_height -= 15
        return current_height - 15

    # Function to add the liabilities breakdown to the PDF
    def add_liabilities_breakdown(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Liabilities Breakdown")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        liabilities = [
            f"- Current liabilities: {row.get('current_liabilities', 'N/A')} {row.get('currency', '')}"
        ]
        for liability in liabilities:
            c.drawString(30, current_height, liability)
            current_height -= 15
        return current_height - 15

    # Function to add the financial summary to the PDF
    def add_financial_summary(c, current_height, row):
        c.setFont("HoeflerText-Black", 14)
        c.drawString(30, current_height, "Financial Summary")
        current_height -= 16
        c.setFont("HoeflerText-Regular", 12)
        fields = [
            f"Name: {row.get('name', 'N/A')}",
            f"Currency: {row.get('currency', 'N/A')}",
            f"Liquid Assets Total: {row.get('liquid_assets_total', 'N/A')} {row.get('currency', '')}",
            f"Real Estate: {row.get('real_estate', 'N/A')} {row.get('currency', '')}",
            f"Overall Wealth: {row.get('Overall_Wealth', 'N/A')} {row.get('currency', '')}",
            f"Risk Capacity: {row.get('Risk_Capacity', 'N/A')}",
            f"Risk Tolerance: {row.get('Risk_Tolerance', 'N/A')}",
            f"Suitability Rating: {row.get('Suitability_rating', 'N/A')}",
            f"Investible Assets: {row.get('Investible_Asset', 'N/A')} {row.get('currency', '')}",
            f"Net Non-Investible Assets: {row.get('net_non_investible_assets', 'N/A')} {row.get('currency', '')}",
            f"Current Liabilities: {row.get('current_liabilities', 'N/A')} {row.get('currency', '')}",
            f"Future Cashflow: {row.get('Future_cashflow', 'N/A')} {row.get('currency', '')}",
            f"Total Points Throughout Risk Questions: {row.get('Total_of_points_throughout_risk_questions', 'N/A')}",
            f"Number of Risk Questions: {row.get('Number_of_risk_questions', 'N/A')}",
            f"Composure Discount: {row.get('Composure_discount', 'N/A')}"
        ]
        for field in fields:
            c.drawString(30, current_height, field)
            current_height -= 15
        return current_height - 15

    # Function to add a logo to the PDF
    def add_logo(c, width, height):
        image_width = 150
        image_height = 50
        x_position = width - image_width - 20
        y_position = height - image_height - 20
        # Uncomment and update the path to the logo if available
        # c.drawImage("logo.JPG", x_position, y_position, width=image_width, height=image_height)

    # Function to add a border to the PDF
    def add_border(c, width, height):
        margin = 15
        c.rect(margin, margin, width - 2 * margin, height - 2 * margin, stroke=1, fill=0)

    # Create the PDF
    pdf_file_path = 'OUTPUT5.pdf'
    create_pdf(Raw_df, pdf_file_path)

    print(f"PDF created: {pdf_file_path}")

