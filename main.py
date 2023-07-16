from module.book import Book
from module.magazine import Magazine
from module.dvd import Dvd
from module.catalog import Catalog

book1=Book('Title Test','Ini subject test',None,'1344-4566','Singgih','088888888')
book2=Book('Title Test','Ini subject test',None,'1344-4566','Singgih','088888888')
book3=Book('Title Test','Ini subject test',None,'1344-4566','Singgih','088888888')

magazine1=Magazine('media cnn','edisi 14 juli 2023',None,'volume 1',23)
magazine2=Magazine('media cnn','edisi 14 juli 2023',None,'volume 1',24)

dvd1=Dvd('DVD','Ini subject test dvd',None,None,'comedy','war')


#collect data per jenis
book=[book1,book2,book3]
magazine=[magazine1,magazine2]
dvd=[dvd1]

#collect all data
catalog_all=[book,magazine,dvd]

#search
input_search='media'
results=Catalog(catalog_all).search(input_search)
if results:
    for index,result in enumerate(results):
        print (f'result ke-{index+1}| {result}')
else:
    print('no result')