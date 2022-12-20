import csv
import requests

# Your Google Maps API key
API_KEY = "YOUR_API_KEY"

# URL template for the Geocoding API
GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json?key={}&address={}"

# Input file path
INPUT_FILE = "input.csv"

# Output file path
OUTPUT_FILE = "output.csv"

# Read the input CSV file
with open(INPUT_FILE, "r") as input_file:
  reader = csv.reader(input_file)
  
  # Skip the header row
  next(reader)
  
  # Open the output CSV file for writing
  with open(OUTPUT_FILE, "w") as output_file:
    writer = csv.writer(output_file)
    
    # Write the header row to the output CSV file
    writer.writerow(["Address", "Latitude", "Longitude"])
    
    # Loop through each address in the input CSV file
    for row in reader:
      address = row[0]
      
      # Make a request to the Geocoding API
      response = requests.get(GEOCODING_URL.format(API_KEY, address)).json()
      
      # Get the latitude and longitude of the address
      latitude = response["results"][0]["geometry"]["location"]["lat"]
      longitude = response["results"][0]["geometry"]["location"]["lng"]
      
      # Write the address, latitude, and longitude to the output CSV file
      writer.writerow([address, latitude, longitude])
      
print("Geocoding complete!")
