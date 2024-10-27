import os
import data_fetcher

def generate_website(animal_data):
    """Generates a website from fetched animal data, saves it as animals.html, and fills in template placeholders."""
    try:
        with open('animals_template.html', 'r', encoding='utf-8') as template_file:
            html_template = template_file.read()
    except FileNotFoundError:
        print("Template file 'animals_template.html' not found.")
        return

    # Populate animal data in the HTML
    animal_info = ""
    for animal in animal_data:
        animal_info += f"<li class='cards__item'><h1>{animal['name']}</h1>"

        # Taxonomy details
        taxonomy = animal.get('taxonomy', {})
        animal_info += f"<p><strong>Scientific Name:</strong> {taxonomy.get('scientific_name', 'N/A')}</p>"
        animal_info += f"<p><strong>Kingdom:</strong> {taxonomy.get('kingdom', 'N/A')}</p>"
        animal_info += f"<p><strong>Phylum:</strong> {taxonomy.get('phylum', 'N/A')}</p>"
        animal_info += f"<p><strong>Class:</strong> {taxonomy.get('class', 'N/A')}</p>"
        animal_info += f"<p><strong>Order:</strong> {taxonomy.get('order', 'N/A')}</p>"
        animal_info += f"<p><strong>Family:</strong> {taxonomy.get('family', 'N/A')}</p>"
        animal_info += f"<p><strong>Genus:</strong> {taxonomy.get('genus', 'N/A')}</p>"

        # Locations
        animal_info += f"<p><strong>Locations:</strong> {', '.join(animal.get('locations', []))}</p>"

        # Characteristics
        characteristics = animal.get('characteristics', {})
        animal_info += "<h2>Characteristics</h2>"
        animal_info += f"<p><strong>Diet:</strong> {characteristics.get('diet', 'N/A')}</p>"
        animal_info += f"<p><strong>Lifespan:</strong> {characteristics.get('lifespan', 'N/A')}</p>"

        animal_info += "</li>"

    # Replace placeholder in template and write to file
    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_info)
    with open('animals.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

    print("Website successfully generated in animals.html.")

if __name__ == "__main__":
    animal_name = input("Enter an animal name: ")
    data = data_fetcher.fetch_data(animal_name)
    generate_website(data)