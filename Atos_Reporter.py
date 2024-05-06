from Function_Service import process_csv_files
from Function_Service import apply_inverse_transformation

process_csv_files()

input_excel = "C:/Users/alika/Desktop/Reporter_Project/Outputs/merged_data.xlsx"
output_excel = "C:/Users/alika/Desktop/Reporter_Project/Outputs/merged_data.xlsx"  # Aynı dosya üzerine kaydedilecek
apply_inverse_transformation(input_excel, output_excel)

