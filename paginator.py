class Paginator:

    def __init__(self, objects, per_page) -> None:
        self.objects = objects
        self.per_page = per_page
        self.pages = self._gen_pages()
        self.length = len(self.pages)


    def _gen_pages(self) -> list:
        result = []
           
        list_aux, x = [], 1
        
        for obj in self.objects:
            if x <= self.per_page: 
                list_aux.append(obj)
            else:
                result.append(list_aux)
                list_aux = []
                list_aux.append(obj)
                x = 1
               
            x += 1
            
        result.append(list_aux)
                
        return result
            
            
 
    def get_page(self, page) -> object:
        try:
            self.pages[page - 1]
        except IndexError:
            raise IndexError('Invalid index')
        else:
            return Page(self.objects, page, self)
            
            
class Page:
    
    
    def __init__(self, object_list, number_page, paginator) -> None:
        self.object_list = object_list
        self.number_page = number_page
        self._paginator = paginator
            
            
    def has_next(self) -> bool:
        return self.number_page != len(self._paginator.pages)      
    
    
    def has_previous(self) -> bool:
        return self.number_page > 1
    
    
    def next_page_number(self) -> int:
        return self.number_page + 1  if self.has_next() else None
    
    
    def previous_page_number(self) -> int:
        return self.number_page - 1 if self.has_previous() else None
          
          
    
def main():

    objects = [{'name': 'Lucas', 'i': i + 1} for i in range(10)]
    
    pages = Paginator(objects, 2)

    page = pages.get_page(1)
    
    print(page.previous_page_number())
    
    


main()