from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
#este codi
# Sample variables
name = "Joe Mama"
age = 30
city = "Cincinnati" 

# Create PDF
pdf_filename = "output.pdf"
c = canvas.Canvas(pdf_filename, pagesize=letter)
width, height = letter  # Get page size

# Add text
c.drawString(100, height - 100, f"Name: {name}")
c.drawString(100, height - 120, f"Age: {age}")
c.drawString(100, height - 140, f"City: {city}")

# Save PDF
c.save()

print(f"PDF '{pdf_filename}' created successfully!")