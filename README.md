# Assignment-4_Week-9

Step1: To do the assignment, I had to first install some libraries I did not have including requests, html5lib, pandas
and BeautifulSoup. I used the following commands to download and install them: pip install requests, 
pip install html5lib, pip install bs4, pip install pandas. From reading different sources on internet, the mentioned libraries
makes it easy to do web scraping.

**Why use the libraries**

1. _**Requests:**_ the requests' module helps us to get access to the webpage we want to scrap. It basically
                   allows us to exchange requests with the server/ on the web. I used it to access the amazon 
                   bestsellers page.
2. _**html5lib:**_ the html5lib module helps us to parse html i.e. analysing and converting a program into a format that
                   runtime environment can run. Since I was trying to access an html format page, with the html5lib
                   the runtime environment was able to provide the output of the program in the html format.

3. _**BeautifulSoup:**_ the BeautifulSoup module helped me to extract data from the amazon html page.

4. _**Pandas**_: I used Pandas to visualize the output of the program in a table for easy reading of the output.

Step 2: After understanding the use of the libraries, the next step was to find how to get the names, reviews and prices
        of the books. With the use of BeautifulSoup, I was able to navigate through the classes of the page and extract 
        some information I needed to find the top 10 expensive books.

Step 3: To extract the classes, I inspected them from the amazon website to access the Sources of the page. I started
        by extracting the name, reviews and prices of the first book then used 'for' loop to do extract the same info
        for all the books. I used built-in functions like (**.find/ .find_all**) to find the classes from the Sources of
        page. ('get_text()) to get the texts between the html tags (book names, reviews and prices)

Step 4: After inspecting the amazon webpage and using the BeautifulSoup to extract the required info from the classes
        I used Pandas to view the extracted information in a table. I used a built-in function called 
        (**pd.DataFrame**). Each extracted information was put in a column.

Step 5: To identify the 10 most expensive books in the list, I had to first change prices to float for easy comparison
        since the extracted ones were strings. By the use of **float()** function I changed the prices datatype then used
        **.replace()** function to remove the **'$'** sign. Then used **.sort_values()** to sort the prices in a 
        descending order.

Step 6: After sorting the prices, I wanted to select the 10 most expensive books in the list. With the help of 
        Pandas, I used .head(10) to print the top 10 expensive books in a table.

These are the steps, I went through to solve the problem. However, I face some challenges while finding classes to
use from the webpage Sources because some divisions <div> had more than one class in it. Also some errors that I could not 
understand and how to solve.
