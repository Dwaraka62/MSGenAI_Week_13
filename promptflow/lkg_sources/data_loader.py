from promptﬂow import tool
import pandas as pd
import os

@tool
def load_data():
    """
    Loads the DataCo CSV ﬁle and returns schema information.
    """
   
    ﬁle_path = "/data/DataCoSupplyChainDataset.csv"

    if not os.path.exists(ﬁle_path):
        return {
            "error": f"File not found: {ﬁle_path}",
            "schema": "",
            "sample_data": ""
        }
   
    try:
        # Load a sample to get schema
        df = pd.read_csv(ﬁle_path, encoding='ISO-8859-1')
       
        # Clean column names (remove spaces, special characters)
        df.columns = [col.replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_') for col in df.columns]

        schema = []
        for col in df.columns:
            dtype = str(df[col].dtype)
            sample_values = df[col].dropna().unique()[:3].tolist()
            schema.append(f"- {col} ({dtype}): e.g., {sample_values}")
     
        return {
           "ﬁle_path": ﬁle_path,
           "schema": "\n".join(schema),
           "sample_data": df.head(5).to_string(),
           "columns": df.columns.tolist()
        }
    except Exception as e:
        return {
          "error": str(e),
          "schema": "",
          "sample_data": ""
    }
