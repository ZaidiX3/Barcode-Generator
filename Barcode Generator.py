import barcode
from barcode.writer import ImageWriter

def generate_barcode(data, barcode_type='code128', output_file='barcode'):
    try:
        # Create a barcode object
        code = barcode.get(barcode_type, data, writer=ImageWriter())

        # Save the barcode to a file
        filename = code.save(output_file)

        print(f"Barcode generated and saved as {filename}")

    except barcode.errors.BarcodeError as e:
        print(f"Error: {e}")

# Example usage:
data_to_encode = "123456789"
generate_barcode(data_to_encode)  # Using default options

# Example with custom options:
custom_data = "ABC123XYZ"
custom_barcode_type = "code39"
custom_output_file = "custom_barcode"
generate_barcode(custom_data, barcode_type=custom_barcode_type, output_file=custom_output_file)
