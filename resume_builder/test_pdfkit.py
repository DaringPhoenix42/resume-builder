import pdfkit

html_content = "<h1>Hello from pdfkit</h1><p>This is a test PDF.</p>"
pdf_data = pdfkit.from_string(html_content, False)  # returns PDF bytes

with open("test.pdf", "wb") as f:
    f.write(pdf_data)

print("PDF generated successfully!")
