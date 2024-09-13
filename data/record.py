import uuid


class Record():

    def __init__(self, record_src, record_bytes):
        self.record_bytes = record_bytes 
        self.record_src = record_src 
        self.id = uuid.uuid4()
        
    def get_id(self):
        return self.id 

    def get_record_bytes(self):
        return self.record_bytes

    def get_record_src(self):
        return self.record_src

    def get_record_hexstring(self):
        return self.get_record_bytes().hex()

    def to_list(self):
        return [
            self.get_record_hexstring(),
            self.get_record_src()
        ]