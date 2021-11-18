class Page:
    
    def __init__(self, elements, page, paginator) -> None:
        self.elements = elements
        self.page = page
        self.paginator = paginator
        self.length = len(self.elements)


    def has_next(self) -> bool:
        return self.page != len(self.paginator.pages) 
    
    
    def has_previous(self):
        return self.page > 1
    
    
    def next_page_number(self):
        return self.page + 1 if self.has_next() else None
    
    
    def previous_page_number(self):
        return self.page - 1 if self.has_previous() else None


    def get_first_value(self):
        return self.elements[0]


    def get_last_value(self):
        return self.elements[-1]
    
    
    
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
            objectList = self.pages[int(page) - 1]
        except (TypeError, ValueError):
            raise ValueError('Inteiro esperado, recebido: ', type(page))
        except IndexError:
            raise IndexError('Valor de índice incorreto.')
        else:
            return Page(objectList, page, self)


