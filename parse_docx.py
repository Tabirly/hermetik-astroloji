import docx
import json
import re

def extract_sabian():
    doc = docx.Document("Hermetik Astroloji.docx")
    
    valid_tables = []
    
    for table in doc.tables:
        table_rows = []
        for row in table.rows:
            cells = [c.text.replace('\n', ' ').strip() for c in row.cells]
            if len(cells) >= 5:
                degree_text = cells[0].replace('°', '').strip()
                if degree_text.isdigit():
                    table_rows.append({
                        "degree": int(degree_text),
                        "symbol": cells[1],
                        "theme": cells[2],
                        "hermetic": cells[3],
                        "stage": cells[4]
                    })
        # If a table has exactly 10 rows, it's one of our data tables!
        if len(table_rows) == 10:
            valid_tables.append(table_rows)
            
    print(f"Total valid tables found: {len(valid_tables)}")
    
    if len(valid_tables) != 36:
        print("Warning: Expected 36 tables (12 signs * 3 decades). Found:", len(valid_tables))
        
    signs = [
        "Koç", "Boğa", "İkizler", "Yengeç", "Aslan", "Başak",
        "Terazi", "Akrep", "Yay", "Oğlak", "Kova", "Balık"
    ]
    
    final_data = []
    
    # We have 36 tables.
    # We assume they are in order: 
    # Tables 0-11: Signs 0-11 (Degrees 1-10)
    # Tables 12-23: Signs 0-11 (Degrees 11-20)
    # Tables 24-35: Signs 0-11 (Degrees 21-30)
    
    for i, t_rows in enumerate(valid_tables):
        sign_index = i % 12
        sign = signs[sign_index]
        sign_en = sign.lower().replace("ç", "c").replace("ğ", "g").replace("ı", "i").replace("ş", "s").replace("ö", "o").replace("ü", "u")
        
        for row in t_rows:
            row["sign"] = sign
            row["id"] = f"{sign_en}-{row['degree']}"
            final_data.append(row)
            
    final_data.sort(key=lambda x: (signs.index(x['sign']), x['degree']))
    
    js_content = "const sabianData = " + json.dumps(final_data, indent=2, ensure_ascii=False) + ";"
    with open("sabian_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"Exported {len(final_data)} items to sabian_data.js")

if __name__ == "__main__":
    extract_sabian()
