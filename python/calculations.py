import pandas as pd


def calculations(df):



    def generic_calc(df):
        # Get data from the first row
        row = df.iloc[0]

        # Extract and convert necessary data

        # Extract and convert necessary data
        nameold = row.get('CLusername', '')

        name = decrypt_data(nameold)

        currency = row.get('A1', '')

        Confidence = (pd.to_numeric(row.get('B1', 0), errors='coerce') + 
                    pd.to_numeric(row.get('B2', 0), errors='coerce') + 
                    pd.to_numeric(row.get('B3', 0), errors='coerce') + 
                    pd.to_numeric(row.get('B4', 0), errors='coerce') + 
                    pd.to_numeric(row.get('B5', 0), errors='coerce') + 
                    pd.to_numeric(row.get('B6', 0), errors='coerce')) / 6

        Impulsivity = (pd.to_numeric(row.get('C1', 0), errors='coerce') + 
                    pd.to_numeric(row.get('C2', 0), errors='coerce') + 
                    pd.to_numeric(row.get('C3', 0), errors='coerce') + 
                    pd.to_numeric(row.get('C4', 0), errors='coerce')) / 4

        Familiarity_preferences = (pd.to_numeric(row.get('D1', 0), errors='coerce') + 
                                pd.to_numeric(row.get('D2', 0), errors='coerce') + 
                                pd.to_numeric(row.get('D3', 0), errors='coerce') + 
                                pd.to_numeric(row.get('D4', 0), errors='coerce')) / 4

        Risk_tolerance = (Confidence + Impulsivity + Familiarity_preferences) / 4

        E1 = (pd.to_numeric(row.get("E1a", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1b", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1c", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1d", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1e", 0), errors='coerce')) / 5

        Composure = (E1 + 
                    pd.to_numeric(row.get('E2', 0), errors='coerce') + 
                    pd.to_numeric(row.get('E3', 0), errors='coerce') + 
                    pd.to_numeric(row.get('E4', 0), errors='coerce')) / 4

        if Composure >= 3:
            discount = 0
        elif Composure < 3 and Composure >= 2:
            discount = 0.25
        else:
            discount = 0.5

        Overall_Wealth = (
            pd.to_numeric(row.get('A2', 0), errors='coerce') + 
            pd.to_numeric(row.get('A4', 0), errors='coerce') + 
            pd.to_numeric(row.get('A5', 0), errors='coerce') - 
            pd.to_numeric(row.get('A6', 0), errors='coerce') -
            pd.to_numeric(row.get('A8', 0), errors='coerce') + 
            pd.to_numeric(row.get('A9', 0), errors='coerce') - 
            pd.to_numeric(row.get('A10', 0), errors='coerce') + 
            pd.to_numeric(row.get('A12', 0), errors='coerce') - 
            pd.to_numeric(row.get('A13', 0), errors='coerce')
        )

        A2 = pd.to_numeric(row.get('A2', 0), errors='coerce')
        
        A4 = pd.to_numeric(row.get('A4', 0), errors='coerce')
        A5 = pd.to_numeric(row.get('A5', 0), errors='coerce')
        A6 = pd.to_numeric(row.get('A6', 0), errors='coerce')
        
        A8 = pd.to_numeric(row.get('A8', 0), errors='coerce')
        A9 = pd.to_numeric(row.get('A9', 0), errors='coerce')
        A10 = pd.to_numeric(row.get('A10', 0), errors='coerce')
        A11 = pd.to_numeric(row.get('A11', 0), errors='coerce')
        A12 = pd.to_numeric(row.get('A12', 0), errors='coerce')
        A13 = pd.to_numeric(row.get('A13', 0), errors='coerce')


        Risk_capacity = (pd.to_numeric(row.get('A2', 0), errors='coerce') +
                        pd.to_numeric(row.get('A4', 0), errors='coerce')) / Overall_Wealth

        Suitability_rating = Risk_capacity * Risk_tolerance * (1 - discount)


        Liquidity_and_money_market_products = str(row.get('F1a', ''))
        Bonds = str(row.get('F1b', ''))  # Bonds (including bond funds)
        Equity = str(row.get('F1c', ''))  # Equity (including equity funds)
        Multi_asset_class_funds = str(row.get('F1d', ''))  # Multi asset class funds (including strategy funds)
        Precious_metals_and_commodities = str(row.get('F1e', ''))  # Precious metals and commodities (including funds)
        Hedge_funds = str(row.get('F1f', ''))  # Hedge funds
        Private_markets = str(row.get('F1g', ''))  # Private markets
        Real_estate = str(row.get('F1h', ''))  # Real estate (including funds)
        Structured_products = str(row.get('F1i', ''))  # Structured products (protection, optimisation...)
        Other_derivatives = str(row.get('F1j', ''))  # Other derivatives


        # Count the number of non-empty F1a to F1j fields
        investment_count = sum(bool(value) for value in [
            Liquidity_and_money_market_products,
            Bonds,
            Equity,
            Multi_asset_class_funds,
            Precious_metals_and_commodities,
            Hedge_funds,
            Private_markets,
            Real_estate,
            Structured_products,
            Other_derivatives
        ])

        # Determine the investment history based on the count
        if investment_count <= 3:
            Investment_history = 1
        elif 4 <= investment_count <= 7:
            Investment_history = 2
        else:
            Investment_history = 3



        # Extract values for the knowledge fields
        Course_or_Degree = str(row.get('F2a', ''))
        Professional_Experience = str(row.get('F2b', ''))
        Personal_Investing = str(row.get('F2c', ''))
        Reading_books_websites_articles = str(row.get('F2d', ''))

        # Count the number of non-empty F2a to F2d fields
        knowledge_count = sum(bool(value) for value in [
            Course_or_Degree,
            Professional_Experience,
            Personal_Investing,
            Reading_books_websites_articles
        ])


        Objective_knowledge = (pd.to_numeric(row.get('F3', 0), errors='coerce') + 
                            pd.to_numeric(row.get('F4', 0), errors='coerce') + 
                            pd.to_numeric(row.get('F6', 0), errors='coerce') + 
                            pd.to_numeric(row.get('F7', 0), errors='coerce')) / 4


        # Calculate the numerical average
        Objective_experience = (Objective_knowledge + Investment_history) / 2

    

        self_Identification_of_knowledge = pd.to_numeric(row.get('F5', 0), errors='coerce')

        Impact_desire = (pd.to_numeric(row.get('G1', 0), errors='coerce') + 
                        pd.to_numeric(row.get('G2', 0), errors='coerce') + 
                        pd.to_numeric(row.get('G3', 0), errors='coerce')) / 3

        Impact_apprehension = (pd.to_numeric(row.get('H1', 0), errors='coerce') + 
                            pd.to_numeric(row.get('H2', 0), errors='coerce')) / 2

        Impact_tradeoff = pd.to_numeric(row.get('I1', 0), errors='coerce')

        need_for_evidence = pd.to_numeric(row.get('J1', 0), errors='coerce')

        Level_of_sustainable_assets = (Impact_desire + Impact_apprehension + Impact_tradeoff + need_for_evidence) / 4

        # Create a new dictionary to store the calculated values
        calculated_data = {
            'name': name,
            'currency': currency,
            'Confidence': Confidence,
            'Impulsivity': Impulsivity,
            'Familiarity_preferences': Familiarity_preferences,
            'Risk_tolerance': Risk_tolerance,
            'Composure': Composure,
            'Overall_Wealth': Overall_Wealth,
            'Risk_capacity': Risk_capacity,
            'Suitability_rating': Suitability_rating,
            'Objective_experience': Objective_experience,
            'Investment_history': Investment_history,
            'Objective_knowledge': Objective_knowledge,
            'self_Identification_of_knowledge': self_Identification_of_knowledge,
            'Impact_desire': Impact_desire,
            'Impact_apprehension': Impact_apprehension,
            'Impact_tradeoff': Impact_tradeoff,
            'need_for_evidence': need_for_evidence,
            'Level_of_sustainable_assets': Level_of_sustainable_assets,
            'A2': A2,
            'A4': A4,
            'A5': A5,
            'A6': A6,
            'A8': A8,
            'A9': A9,
            'A10': A10,
            'A11': A11,
            'A12': A12,
            'A13': A13,
            'Liquidity_and_money_market_products': Liquidity_and_money_market_products,
            'Bonds': Bonds,
            'Equity': Equity,
            'Multi_asset_class_funds': Multi_asset_class_funds,
            'Precious_metals_and_commodities': Precious_metals_and_commodities,
            'Hedge_funds': Hedge_funds,
            'Private_markets': Private_markets,
            'Real_estate': Real_estate,
            'Structured_products': Structured_products,
            'Other_derivatives': Other_derivatives,
            'Course_or_Degree': Course_or_Degree,
            'Professional_Experience': Professional_Experience,
            'Personal_Investing': Personal_Investing,
            'Reading_books_websites_articles': Reading_books_websites_articles,
            'knowledge_count': knowledge_count

        }

        return calculated_data

    calculated_data = generic_calc(df)

    newdf = pd.DataFrame([calculated_data])


    #csv_file = "toby.csv"
    #df.to_csv(csv_file, index=False)

    print("Went")

    


    return newdf




from flask import Flask, request, jsonify
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Function to read the secret key from a file
def read_secret_key(file_path):
    try:
        with open(file_path, 'r') as file:
            hex_key = file.read().strip()
            print(f"Hex Key: {hex_key}")  # Debugging print
            return bytes.fromhex(hex_key)
    except Exception as e:
        print(f"Error reading key file: {e}")
        return None

SECRET_KEY = read_secret_key('tokeny.key')  # Read the key once at startup


# Function to decrypt data using ECB mode (deterministic)
def decrypt_data(hex_data):
    key = SECRET_KEY
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    # Convert hexadecimal data back to bytes
    encrypted_data = bytes.fromhex(hex_data)
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode().rstrip('\x00')  # Remove padding


























# Convert strings to numeric values, coerce errors to NaN
        # liquid_assets_Vexra = pd.to_numeric(row.get('A2', 0), errors='coerce')
        # liquid_assets_Other = pd.to_numeric(row.get('A3', 0), errors='coerce')
        # liquid_assets_total = liquid_assets_Vexra + liquid_assets_Other

        # real_estate = pd.to_numeric(row.get('A4', 0), errors='coerce')

        # # Print debugging information
        # print("1")

        # Investible_Asset = liquid_assets_Vexra + liquid_assets_Other + pd.to_numeric(row.get('A5', 0), errors='coerce')
        # print("2")

        # net_non_investible_assets = real_estate
        # print("3")

        # current_liabilities = pd.to_numeric(row.get('A6', 0), errors='coerce') + pd.to_numeric(row.get('A7', 0), errors='coerce') + pd.to_numeric(row.get('A8', 0), errors='coerce')
        # print("4")

        # # Calculate Future_cashflow
        # Future_cashflow = (pd.to_numeric(row.get('A9', 0), errors='coerce') - 
        #                 pd.to_numeric(row.get('A10', 0), errors='coerce') - 
        #                 pd.to_numeric(row.get('A11', 0), errors='coerce') + 
        #                 pd.to_numeric(row.get('A12', 0), errors='coerce') - 
        #                 pd.to_numeric(row.get('A13', 0), errors='coerce'))
        # print("5")

        # Total_of_points_throughout_risk_questions = (pd.to_numeric(row.get('B3', 0), errors='coerce') + 
        #                                             pd.to_numeric(row.get('B4', 0), errors='coerce') + 
        #                                             pd.to_numeric(row.get('B5', 0), errors='coerce'))
        # print("6")

        # Number_of_risk_questions = 3  # Assuming B3, B4, and B5 are the risk questions
        # print("7")

        # E1 = (pd.to_numeric(row.get("E1a", 0), errors='coerce') + 
        #     pd.to_numeric(row.get("E1b", 0), errors='coerce') + 
        #     pd.to_numeric(row.get("E1c", 0), errors='coerce') + 
        #     pd.to_numeric(row.get("E1d", 0), errors='coerce') + 
        #     pd.to_numeric(row.get("E1e", 0), errors='coerce')) / 5
        # print("7.5")
        # print(E1)

        # E2 = pd.to_numeric(row.get('E2', 0), errors='coerce')
        # E3 = pd.to_numeric(row.get('E3', 0), errors='coerce')
        # E4 = pd.to_numeric(row.get('E4', 0), errors='coerce')

        # Composure_discount = 1 - (E1 + E2 + E3 + E4) / 4
        # print("8")

        # # Calculating new data to add to clean df
        # Overall_Wealth = Investible_Asset + net_non_investible_assets + current_liabilities + Future_cashflow
        # print("12")

        # Risk_Capacity = Overall_Wealth / Investible_Asset if Investible_Asset != 0 else float('inf')
        # print("13")

        # Risk_Tolerance = Total_of_points_throughout_risk_questions / Number_of_risk_questions

        # print(f"{Risk_Tolerance} that is risk tollererance!!")
        # print("14")

        # Suitability_rating = Risk_Capacity * (Risk_Tolerance * Composure_discount)
        # print("15")

        # print("10")

        # # Create a new dictionary to store the calculated values
        # calculated_data = {
        #     'name': name,
        #     'currency': currency,
        #     'liquid_assets_total': liquid_assets_total,
        #     'real_estate': real_estate,
        #     'Overall_Wealth': Overall_Wealth,
        #     'Risk_Capacity': Risk_Capacity,
        #     'Risk_Tolerance': Risk_Tolerance,
        #     'Suitability_rating': Suitability_rating,
        #     'Investible_Asset': Investible_Asset,
        #     'net_non_investible_assets': net_non_investible_assets,
        #     'current_liabilities': current_liabilities,
        #     'Future_cashflow': Future_cashflow,
        #     'Total_of_points_throughout_risk_questions': Total_of_points_throughout_risk_questions,
        #     'Number_of_risk_questions': Number_of_risk_questions,
        #     'Composure_discount': Composure_discount
        # }

