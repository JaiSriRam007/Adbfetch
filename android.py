# Import the Shodan module
import shodan

# Ask the user for their Shodan API key
api_key = input('Enter your Shodan API key: ')

# Create a Shodan object using the user's API key
shodan_obj = shodan.Shodan(api_key)

# Search for ADB devices
results = shodan_obj.search('android debug bridge')  # This searches for devices that have "android debug bridge" in their banner

# Loop through the search results and print the IP address and port of each device
for result in results['matches']:  # The 'matches' field of the results object contains a list of search results
    print(f'IP: {result["ip_str"]}, Port: {result["port"]}')  # This prints the IP address and port of each device
