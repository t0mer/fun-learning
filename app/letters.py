class Letter(object):
    Id: int
    LetterId: int
    Letter: str
    
    def __init__(self, Id: int, LetterId: int, Letter: str):
        self.Id = Id
        self.LetterId = LetterId
        self.Letter = Letter
        
        
class Number(object):
    Id: int
    NumberId: int
    Number: str
    
    def __init__(self, Id: int, NumberId: int, Number: str):
        self.Id = Id
        self.NumberId: NumberId
        self.Number: Number