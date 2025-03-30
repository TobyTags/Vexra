import pandas as pd


def calculations(df):



    def generic_calc(df):
        # Get data from the first row
        row = df.iloc[0]

        # Extract and convert necessary data

        name = row.get('A', '')

        currency = row.get('A1', '')


        # Convert strings to numeric values, coerce errors to NaN
        liquid_assets_Vexra = pd.to_numeric(row.get('A2', 0), errors='coerce')
        liquid_assets_Other = pd.to_numeric(row.get('A3', 0), errors='coerce')
        liquid_assets_total = liquid_assets_Vexra + liquid_assets_Other

        real_estate = pd.to_numeric(row.get('A4', 0), errors='coerce')

        # Print debugging information
        print("1")

        Investible_Asset = liquid_assets_Vexra + liquid_assets_Other + pd.to_numeric(row.get('A5', 0), errors='coerce')
        print("2")

        net_non_investible_assets = real_estate
        print("3")

        current_liabilities = pd.to_numeric(row.get('A6', 0), errors='coerce') + pd.to_numeric(row.get('A7', 0), errors='coerce') + pd.to_numeric(row.get('A8', 0), errors='coerce')
        print("4")

        # Calculate Future_cashflow
        Future_cashflow = (pd.to_numeric(row.get('A9', 0), errors='coerce') - 
                        pd.to_numeric(row.get('A10', 0), errors='coerce') - 
                        pd.to_numeric(row.get('A11', 0), errors='coerce') + 
                        pd.to_numeric(row.get('A12', 0), errors='coerce') - 
                        pd.to_numeric(row.get('A13', 0), errors='coerce'))
        print("5")

        Total_of_points_throughout_risk_questions = (pd.to_numeric(row.get('B3', 0), errors='coerce') + 
                                                    pd.to_numeric(row.get('B4', 0), errors='coerce') + 
                                                    pd.to_numeric(row.get('B5', 0), errors='coerce'))
        print("6")

        Number_of_risk_questions = 3  # Assuming B3, B4, and B5 are the risk questions
        print("7")

        E1 = (pd.to_numeric(row.get("E1a", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1b", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1c", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1d", 0), errors='coerce') + 
            pd.to_numeric(row.get("E1e", 0), errors='coerce')) / 5
        print("7.5")
        print(E1)

        E2 = pd.to_numeric(row.get('E2', 0), errors='coerce')
        E3 = pd.to_numeric(row.get('E3', 0), errors='coerce')
        E4 = pd.to_numeric(row.get('E4', 0), errors='coerce')

        Composure_discount = 1 - (E1 + E2 + E3 + E4) / 4
        print("8")

        # Calculating new data to add to clean df
        Overall_Wealth = Investible_Asset + net_non_investible_assets + current_liabilities + Future_cashflow
        print("12")

        Risk_Capacity = Overall_Wealth / Investible_Asset if Investible_Asset != 0 else float('inf')
        print("13")

        Risk_Tolerance = Total_of_points_throughout_risk_questions / Number_of_risk_questions

        print(f"{Risk_Tolerance} that is risk tollererance!!")
        print("14")

        Suitability_rating = Risk_Capacity * (Risk_Tolerance * Composure_discount)
        print("15")

        print("10")

        # Create a new dictionary to store the calculated values
        calculated_data = {
            'name': name,
            'currency': currency,
            'liquid_assets_total': liquid_assets_total,
            'real_estate': real_estate,
            'Overall_Wealth': Overall_Wealth,
            'Risk_Capacity': Risk_Capacity,
            'Risk_Tolerance': Risk_Tolerance,
            'Suitability_rating': Suitability_rating,
            'Investible_Asset': Investible_Asset,
            'net_non_investible_assets': net_non_investible_assets,
            'current_liabilities': current_liabilities,
            'Future_cashflow': Future_cashflow,
            'Total_of_points_throughout_risk_questions': Total_of_points_throughout_risk_questions,
            'Number_of_risk_questions': Number_of_risk_questions,
            'Composure_discount': Composure_discount
        }



       

        return calculated_data

    calculated_data = generic_calc(df)

    newdf = pd.DataFrame([calculated_data])


    #csv_file = "toby.csv"
    #df.to_csv(csv_file, index=False)

    print("Went - gone")

    


    return newdf
































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


