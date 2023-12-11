from flask import url_for
class Bird:
    __tablename__ = 'birds'
    columns = ['id','class_id','file_path','labels','data_set','scientific_name']
    
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

    # display bird image located in data/bird-training-images
    def image_url(self):
        # url_root = '/Users/kielay/code/projects/flask-bird-api'
        # return url_for( '/data/bird-training-images/' + self.file_path, _external=True)
        return url_for('static',filename=self.file_path)
        
        # return request.url_root + '/Users/kielay/code/projects/flask-bird-api/data/bird-training-images/' + self.filepaths