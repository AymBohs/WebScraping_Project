#-------------------------------------
# Webscraping Project by Ayman Bohsali
#-------------------------------------
import requests
from bs4 import BeautifulSoup
#----------------------------

def get_store(listing):

    store_element_retailer = listing.select_one('.topictitle_retailer')
    store_element = listing.select_one('.topictitle')

    if store_element_retailer:
        return store_element_retailer.text.strip()
    elif store_element:
        # Extract store from the square brackets, if available
        store_text = store_element.text.strip()
        return store_text.split(']')[0][1:].strip() if ']' in store_text else store_text
    else:
        return "N/A"
            
def main(option1, option2, option3, option4): # This method is called in every case, with different boolean parameters depending on the option
    """
    Main function to scrape and display deal information from the RedFlagDeals forum.
    """
    url = "https://forums.redflagdeals.com/"
    response = requests.get("https://forums.redflagdeals.com/hot-deals-f9/")
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "html.parser")

    # Extracting information from HTML elements
    # Base URL
    base_url = "https://forums.redflagdeals.com/"
    
    totalDeals = 0
    
    for listing in soup.find_all("li", class_="row topic"):
        totalDeals += 1
        
    if option1 == True:
        print(f"\nTotal deals found: {totalDeals}\n") 
        
    categoryList = []
    dealList = []
    storeList = []
    storeDeals = []
    urlCategList = [[0,""]] # The 2-dimensional list for the URL and category of each deal, used in option 4

    for listing in soup.find_all("li", class_="row topic"):
        
        store = get_store(listing)

        item_element = listing.select_one('.topic_title_link')
        item = item_element.text.strip() if item_element else "N/A"
        
        votes_element = listing.select_one('.total_count_selector')
        votes = votes_element.text.strip() if votes_element else "N/A"
        
        username_element = listing.select_one('.thread_meta_author')
        username = username_element.text.strip() if username_element else "N/A"
        
        timestamp_element = listing.select_one('.first-post-time')
        timestamp = timestamp_element.text.strip() if timestamp_element else "N/A"
        
        category_element = listing.select_one('.thread_category a')
        category = category_element.text.strip() if category_element else "N/A"
        
        replies_element = listing.select_one('.posts')
        replies = replies_element.text.strip() if replies_element else "N/A"
        
        views_element = listing.select_one('.views')
        views = views_element.text.strip() if views_element else "N/A"
        
        # Extract the URL and prepend the base URL
        url_element = item_element['href'] if item_element else "N/A"
        url = base_url + url_element

        urlCategList.append([url, category])
        
        # Filling the two pairs of parallel arrays: categoryList and dealList, then storeList and storeDeals
        
        if category not in categoryList:
            categoryList.append(category)
            dealList.append(1)
        else:
            for i in range(len(categoryList)):
                if categoryList[i] == category:
                    dealList[i] += 1
                    
        if store not in storeList:
            storeList.append(store)
            storeDeals.append(1)
        else:
            for i in range(len(storeList)):
                if storeList[i] == store:
                    storeDeals[i] += 1
        
        # Printing information for the deal
        
        if option1 == True:
            
            print(f"Store: {store}")
            print(f"Title: {item}")
            print(f"Votes: {votes}")
            print(f"Username: {username}")
            print(f"Timestamp: {timestamp}")
            print(f"Category: {category}")
            print(f"Replies: {replies}")
            print(f"Views: {views}")
            print(f"Url: {url}")
            print("-------------------------")
                
    if option2 == True:
        
        print("\nDeals by Category:\n")
        
        for i in range(len(categoryList)):
            output1 = f"{categoryList[i]}:"
            output2 = f"{dealList[i]} deals"
            print(output1.rjust(24)+output2.ljust(2))
            
        print()
        
    if option3 == True:
        
        numStores = int(input("Enter the number of top stores to display: "))
        
        mergedList = [[0,""]]   # A 2-dimensional list that merges storeList and storeDeals

        for i in range(len(storeDeals)):
            mergedList.append([storeDeals[i], storeList[i]])

        mergedList.sort(reverse = True)

        for i in range(numStores):
            output1 = f"{mergedList[i][1]}: "
            output2 = f"{mergedList[i][0]} deals"
            print(output1.rjust(25)+output2.ljust(5))
            
        print("----------------------------------------------------")

    if option4 == True:
        
        print("\nList of Categories: \n")
        
        for i in range(len(categoryList)):
            print(f"{i+1}. {categoryList[i]}")
            
        categNum = int(input("Enter the number corresponding to the category: ")) - 1
        
        targetCateg = categoryList[categNum]
        
        f = open("log.txt", "a")
        
        f.write("\n"+targetCateg+" URL List: \n---------------------------------\n")
        
        for j in range(len(urlCategList)):
            if urlCategList[j][1] == targetCateg:
                f = open("log.txt", "a")
                f.write(urlCategList[j][0]+"\n***\n")
        f.close()
        print("All links have been logged successfully.\n")

def menu():
    print("***** Web Scraping Adventure *****")
    print("1. Display Latest Deals")
    print("2. Analyze Deals by Category")
    print("3. Find Top Stores")
    print("4. Log Deal Information")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    match choice:
        
        case '1':
            if __name__ == "__main__":
                main(True, False, False, False)
            menu()
        
        case '2':
            if __name__ == "__main__":
                main(False, True, False, False)
            menu()
        
        case '3':
            if __name__ == "__main__":
                main(False, False, True, False)
            menu()
            
        case '4':
            if __name__ == "__main__":
                main(False, False, False, True)
            menu()
        
        case '5':
            print("Exiting the program. Goodbye!")
            
        case _:
            print("\nInvalid choice, program will restart.\n")
            menu()
            
menu()