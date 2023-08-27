import requests
import pyfiglet
from bs4 import BeautifulSoup

# Search query

banner = pyfiglet.figlet_format("YouCanFindIt", font = "big") 
print(banner)
print("                                 by Danilo Dias\n")

while True:

    try:
        option = int(input("""
        Options:

        0 - Exit
        1 - Make a search
    
        Chose: """))  

        if option == 1:

            search = input("Enter what you want to search: ")

            if search != "":
                query = requests.utils.quote(search)

                # Make the request to Google
                response = requests.get(f'https://www.google.com/search?q={query}')

                # Parse the HTML response
                soup = BeautifulSoup(response.text, 'html.parser')

                # Search for the specific name on the websites

                for result in soup.find_all("a"):
                    # Get the link of the search result
                    link = result.get('href')
                    
                    # Make a request to the website
                    try:
                        site_response = requests.get(f"https://www.google.com{link}")

                        site_soup = BeautifulSoup(site_response.text, 'html.parser')

                        results = site_soup.find_all(string=search)


                        # Print the number of occurrences of the name 
                        
                        if len(results) > 0:

                            print(f'''{search} was found {len(results)} times on: 
                            {link}
                            -----------------------------------------------------
                            ''')
                    except:
                        continue
            else: 
                print("Please, enter a valid query.")
        elif option == 0:
            print("\n\n     Exiting program...\n\n")
            break
        else:
            print("Please, enter a valid option.")
    except ValueError:
        print("Please, enter a valid option.")
    except KeyboardInterrupt:       
        print("\n\n     Exiting program...\n\n")
        break