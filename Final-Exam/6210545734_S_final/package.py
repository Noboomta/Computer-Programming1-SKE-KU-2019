class Package:
    def __init__(self,package_id,from_office,to_office):
        self.id = package_id
        self.fromm = from_office
        self.to = to_office
        self.status = 1
        
    def statusstr(self):
        if self.status == 1:
            return 'to mail'
        elif self.status == 2:
            return 'on the way'
        elif self.status == 3:
            return 'delivered'
    def __str__(self):
        return f'packet id: {self.id}, from: {self.fromm}, to: {self.to}, current: 101, status: {self.statusstr()}'