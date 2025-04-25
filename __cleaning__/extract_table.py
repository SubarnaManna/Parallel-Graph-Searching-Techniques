# import pdfplumber
# import pandas as pd

# # Load the PDF
# with pdfplumber.open("all_data.pdf") as pdf:
#     all_tables = []
#     for page in pdf.pages:
#         tables = page.extract_tables()
#         for table in tables:
#             df = pd.DataFrame(table[1:], columns=table[0])  # First row as header
#             all_tables.append(df)

# # Combine all tables
# final_df = pd.concat(all_tables, ignore_index=True)

# # Save to CSV
# final_df.to_csv("output.csv", index=False)


import pdfplumber

output_lines = []

with pdfplumber.open("all_data.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            lines = text.split('\n')
            output_lines.extend(lines)

# Save to a text file
with open("output.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line + '\n')
