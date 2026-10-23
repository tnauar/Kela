import pandas as pd
import re

def count_occurrence(text: str, pattern: str)-> int:
    """Counts the occurences of the pattern "kohtelia". Meaning some form of "kohtelias" word.
        
    Args:
        text: Contents of the free_text column. In this case a string.
        pattern: A string containing the pattern to search.  
            
    Returns: Length of the findings list.
    """
    findings = []
    findings = re.findall(pattern, str(text), flags=re.IGNORECASE)
    return len(findings)

def main():
    
    file = "./random_data/palvelu.csv"
    df = pd.read_csv(file)

    """ Search pattern. We are looking for a raw string "kohtelia".""" 
    pattern = r"kohtelia"

    """ We go through each row of the "palauteteksti" column."""
    kohtelia_match = []
    for text in df["palauteteksti"]:
        kohtelia_match.append(count_occurrence(text, pattern))

    df["kohtelia_match"] = kohtelia_match

    """ The total amount of hits for the whole file."""
    total_count = df["kohtelia_match"].sum()

    """ The row count of hits."""
    rows_with_match = (df["kohtelia_match"] > 0).sum()

    print(f"Total hits: {total_count}")
    print(f"Rows hit: {rows_with_match}")

if __name__ == "__main__":
    main()