class Bird:
    __tablename__ = 'birds'
    columns = ['id','class_id','filepaths','labels','data_set','scientific_name']
    
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))
    