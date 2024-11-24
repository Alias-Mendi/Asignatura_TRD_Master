import pandas as pd
import openai
import os
import dotenv



def calculate_metrics(data):

    '''Adds a 'Buy' column to the input DataFrame based on trading decisions made by a language model.

    This function sends historical financial data to OpenAI's language model to determine 
    whether to 'Buy' or 'Not Buy' a financial asset for each row in the input data. 
    The decision is made based solely on the provided data without any additional metric calculations.

    Parameters:
    -----------
    data : pd.DataFrame
        A pandas DataFrame containing historical financial data with the following required columns:
        - 'Date' : datetime
        - 'open' : float
        - 'high' : float
        - 'low' : float
        - 'close' : float
        - 'volume' : float

    Returns:
    --------
    pd.DataFrame
        A pandas DataFrame identical to the input data but with an additional column:
        - 'Buy' : bool
          Indicates whether the model recommends buying the asset (True) or not (False) for each row.

    Notes:
    ------
    - The function relies on the OpenAI API to perform the decision-making process.
    - Ensure your OpenAI API key is set in the environment variable 'OPENAI_KEY' before using this function.
    - The decision-making process is based on the language model's understanding of trading principles and may not
      always reflect real-world market conditions.'''
    
    # Convertir el DataFrame a CSV (como texto)
    data_csv = data.to_csv(index=False)
    dotenv.load_dotenv()
    openai.api_key = os.getenv('OPENAI_KEY')

    # Crear el prompt
    
    prompt = f"""
    You are a professional financial analyst and an expert in trading. I will provide you with historical data for a financial asset 
    in CSV format with the following columns: ['Date', 'open', 'high', 'low', 'close', 'volume'].

    I need you to perform the following task:
    - For each row of data, decide whether to 'Buy' or 'Not Buy' the asset based on your expert knowledge of financial analysis and trading principles. 
    Use the following guidelines:
    - 'Buy' = True if the data suggests a good buying opportunity.
    - 'Buy' = False if the data does not suggest a good buying opportunity.

    Return the output in **CSV format** with the original columns and an additional column named 'Buy', which contains either True or False for each row.

    Here is the historical data in CSV format:
    {data_csv}

    Make sure to:
    - Base your decision solely on the provided data without performing additional metric calculations.
    - Provide the result in a valid CSV format including the original data and the new 'Buy' column.
    Return only the resulting CSV output, nothing else.
    """



    # Llamada a OpenAI
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional trader and financial analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )
        content = response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"Error al llamar a la API de OpenAI: {str(e)}")

    # Leer el contenido como un DataFrame directamente desde el texto CSV
    from io import StringIO
    try:
        result_df = pd.read_csv(StringIO(content))
    except Exception as e:
        raise ValueError("El texto devuelto no es un CSV válido.")

    return result_df


