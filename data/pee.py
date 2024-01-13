import csv
import webbrowser

def create_google_maps_link(latitude, longitude):
    return f"https://www.google.com/maps?q={latitude},{longitude}"

def open_csv_and_generate_links(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            place = row[0].strip()
            coordinates = row[1].strip().split(', ')
            latitude, longitude = coordinates

            google_maps_link = create_google_maps_link(latitude, longitude)
            
            print(f"Place: {place}")
            print(f"Coordinates: {latitude}, {longitude}")
            print(f"Google Maps Link: {google_maps_link}\n")

            # Open the link in the default web browser
            webbrowser.open(google_maps_link)

if __name__ == "__main__":
    csv_file_path = "D:\CodeRed\data\hills.csv"  # Replace with the path to your CSV file
    open_csv_and_generate_links(csv_file_path)
