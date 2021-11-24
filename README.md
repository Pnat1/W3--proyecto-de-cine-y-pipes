![](./Image/Taste of cinema.png)

# W3 Film Data Pipelines Project
​
# Objetive
The goal of the project is to ultimately create a data pipeline of a random database. The chosen database comes from the BoxOfficeMojo website, where I specifically selected the top 10 grossing films since 1978. After proper cleaning of the dataset it will be enriched with further data both from a new updated database and through a web scrapping process. Ultimately all the functions created must go into a pipeline document that transforms the data through functions into what I want. 
​
​
# Working plan 
​
First, find a proper working database in Kaggle.

Second, find other information in websites from which I can enrich my database. 

Third, decide wether to continue with an API request or web scrapping. In this case its webs scrapping.

Fourth, concat or merge the information and make it as clean as possible.

Fifth, following the plan of indentifying taste trends through top 10 most watch films trhough the years. Identify those correlations or trends with both calculations and visualizations.
​

​
The following resources have been used to achieve the objective of this project: 
​
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing.
​
​
### Structure of the project files
​
The structure of this project is composed of:
 1. A folder of notebooks: 
    
    a) **Explore_Companies.ipynb** -->with the preliminary analysis where I search for companies that meet the requirements established a priori to be able to pre-select locations. 
​
    b) **APIs.ipynb** --> the call is made to the Api of "Foursquare Developers", where we will get some preferred conditions where we want our company to be located. 
​
    c) **Geospatial queries.ipynb** --> we make the spatial queries to calculate the distance between each point obtained in the Foursquare API and the locations selected at the beginning.
​
    d) **Madrid vs Barcelona vs Bilbao vs Gijon.ipynb** --> the relationship between each selected parameter (train stations, bars, vegan restaurants, basketball courts, and children's schools) and the possible locations (Madrid, Barcelona, Gijon and Bilbao) is evaluated. For this purpose, a normalisation and categorisation has been used. 
​
 2. scr folder: folder where all the .py files are stored with all the explained functions used during the whole project. The .py files included are: 
    a) APIsFunctions used in the APIs.ipynb
    b) GeospatialFunctions used in the Gespatial queries.ipynb
    c) CleaningFunctions used in the Madrid vs Barcelona vs Bilbao vs Gijon.ipynb
​
 3. Output: all the dataframes imported and saved in csv format. 
​
​
# Libraries
​
[sys](https://docs.python.org/3/library/sys.html)
​
[requests](https://pypi.org/project/requests/2.7.0/)
​
[pandas](https://pandas.pydata.org/)
​
[dotenv](https://pypi.org/project/python-dotenv/)
​
[pymongo](https://www.mongodb.com/2)
​
[json](https://docs.python.org/3/library/json.html)
​
[os](https://docs.python.org/3/library/os.html)
​
[geopandas](https://geopandas.org/)
​
[shapely](https://pypi.org/project/Shapely/)
​
[reduce](https://docs.python.org/3/library/functools.html)
​
[operator](https://docs.python.org/3/library/operator.html)
​
[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)
​
[re](https://docs.python.org/3/library/re.html)