import data_fetcher


def generate_website(animal_data):
    """
    Generates a website from the fetched animal data and saves it as animals.html.
    """
    html_content = "<html><head><title>Animal Info</title></head><body>"

    if animal_data:
        # Iterate over each animal in the response
        for animal in animal_data:
            html_content += f"<h1>{animal['name']}</h1>"
            # Safely get taxonomy data
            taxonomy = animal.get('taxonomy', {})
            html_content += f"<p><strong>Scientific Name:</strong> {taxonomy.get('scientific_name', 'N/A')}</p>"
            html_content += f"<p><strong>Kingdom:</strong> {taxonomy.get('kingdom', 'N/A')}</p>"
            html_content += f"<p><strong>Phylum:</strong> {taxonomy.get('phylum', 'N/A')}</p>"
            html_content += f"<p><strong>Class:</strong> {taxonomy.get('class', 'N/A')}</p>"
            html_content += f"<p><strong>Order:</strong> {taxonomy.get('order', 'N/A')}</p>"
            html_content += f"<p><strong>Family:</strong> {taxonomy.get('family', 'N/A')}</p>"
            html_content += f"<p><strong>Genus:</strong> {taxonomy.get('genus', 'N/A')}</p>"

            html_content += f"<p><strong>Locations:</strong> {', '.join(animal.get('locations', []))}</p>"

            # Characteristics
            characteristics = animal.get('characteristics', {})
            html_content += "<h2>Characteristics</h2>"
            html_content += f"<p><strong>Prey:</strong> {characteristics.get('prey', 'N/A')}</p>"
            html_content += f"<p><strong>Name of Young:</strong> {characteristics.get('name_of_young', 'N/A')}</p>"
            html_content += f"<p><strong>Group Behavior:</strong> {characteristics.get('group_behavior', 'N/A')}</p>"
            html_content += f"<p><strong>Estimated Population Size:</strong> {characteristics.get('estimated_population_size', 'N/A')}</p>"
            html_content += f"<p><strong>Biggest Threat:</strong> {characteristics.get('biggest_threat', 'N/A')}</p>"
            html_content += f"<p><strong>Most Distinctive Feature:</strong> {characteristics.get('most_distinctive_feature', 'N/A')}</p>"
            html_content += f"<p><strong>Gestation Period:</strong> {characteristics.get('gestation_period', 'N/A')}</p>"
            html_content += f"<p><strong>Habitat:</strong> {characteristics.get('habitat', 'N/A')}</p>"
            html_content += f"<p><strong>Diet:</strong> {characteristics.get('diet', 'N/A')}</p>"
            html_content += f"<p><strong>Average Litter Size:</strong> {characteristics.get('average_litter_size', 'N/A')}</p>"
            html_content += f"<p><strong>Lifestyle:</strong> {characteristics.get('lifestyle', 'N/A')}</p>"
            html_content += f"<p><strong>Common Name:</strong> {characteristics.get('common_name', 'N/A')}</p>"
            html_content += f"<p><strong>Number of Species:</strong> {characteristics.get('number_of_species', 'N/A')}</p>"
            html_content += f"<p><strong>Location:</strong> {characteristics.get('location', 'N/A')}</p>"
            html_content += f"<p><strong>Slogan:</strong> {characteristics.get('slogan', 'N/A')}</p>"
            html_content += f"<p><strong>Group:</strong> {characteristics.get('group', 'N/A')}</p>"
            html_content += f"<p><strong>Color:</strong> {characteristics.get('color', 'N/A')}</p>"
            html_content += f"<p><strong>Skin Type:</strong> {characteristics.get('skin_type', 'N/A')}</p>"
            html_content += f"<p><strong>Top Speed:</strong> {characteristics.get('top_speed', 'N/A')}</p>"
            html_content += f"<p><strong>Lifespan:</strong> {characteristics.get('lifespan', 'N/A')}</p>"
            html_content += f"<p><strong>Weight:</strong> {characteristics.get('weight', 'N/A')}</p>"
            html_content += f"<p><strong>Height:</strong> {characteristics.get('height', 'N/A')}</p>"
            html_content += f"<p><strong>Age of Sexual Maturity:</strong> {characteristics.get('age_of_sexual_maturity', 'N/A')}</p>"
            html_content += f"<p><strong>Age of Weaning:</strong> {characteristics.get('age_of_weaning', 'N/A')}</p>"

            html_content += "<hr>"  # Add a separator between animals
    else:
        html_content += "<h2>No animals found.</h2>"

    html_content += "</body></html>"

    # Save the HTML content to a file
    with open('animals.html', 'w') as file:
        file.write(html_content)

    print("Website was successfully generated to the file animals.html.")


# Main function
if __name__ == "__main__":
    # Ask for the animal name from the user
    animal_name = input("Please enter an animal: ")

    # Fetch the data from the API
    data = data_fetcher.fetch_data(animal_name)

    # Print the fetched data for testing
    print("Fetched Data for testing:")
    print(data)

    # Generate the website using the fetched data
    generate_website(data)