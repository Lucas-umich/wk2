import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""



# Add character cards
for char in data["results"]:
    html_content += f"""
    <table>
        <tr>
            <td>
                <img src={char["image"]} width="200" alt="Attila Starwar">
            </td>
            <td>
                <h3><strong>Name: </strong>{char['name']}</h3>
                <p><strong>Status: </strong>{char['status']}</p>
                <p><strong>Species: </strong>{char['species']}</p>
                <p><strong>location: </strong>{char['location']['name']} <a herf=https://rickandmortyapi.com/api/location/6 ></a></p>
            </td>
        </tr>
    </table>
    """
# End character cards


html_content += """
</body>
</html>
"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

