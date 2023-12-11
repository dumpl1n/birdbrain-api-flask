from flask import url_for

class Bird:
    __tablename__ = 'birds'
    columns = ['id','class_id','file_path','labels','data_set','scientific_name']
    
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    # display bird image located in data/bird-training-images
    def image_url(self):
        return url_for('static',filename=self.file_path)
        