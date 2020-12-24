
class Office:
    
    def __init__(self, idd):
        # print('a')
        self.mail_in_package = []
        self.mail_out_package = []
        self.office_id = idd
    
    def __str__(self):
        return str(f'office id: {self.office_id}' + '\n' + f'Mail-in Package:' +'\n' + self.show_mail_in() + '\n' + f'Mail-out Package:' +'\n' + self.show_mail_out())
    def show_mail_in(self):
        data = ''
        for pac in self.mail_in_package:
            data += str(pac) +'\n'
        return data
    def show_mail_out(self):
        data = ''
        for pac in self.mail_out_package:
            data += str(pac)+'\n'
        return data
    def add_package_to_mailout(self, package):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office101.add_package_to_mailout(pack1)
            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: to mail
            
        '''
        self.mail_out_package.append(package)

    def add_package_to_mailin(self, package):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office102 = Office(102)
            >>> office102.add_package_to_mailin(pack1)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: to mail
                Mail-out Packages:

        '''
        self.mail_in_package.append(package)
        pass
    
    def transfer(self,dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages: 
                packet id: 1, from: 101, to: 102, current: 101, status: on the way

        '''
        for pac in self.mail_out_package:
            pac.status+=1
            dest_office.mail_in_package.append(pac)
        self.mail_out_package = []
        pass

    def deliver(self, dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> office101.deliver(office102)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 102, status: delivered
                Mail-out Packages: 

            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages:
                
        '''        
        for pac in dest_office.mail_in_package:
            pac.status +=1
        pass

    def clear(self):
        self.mail_in_package = []
        self.mail_out_package = []
        pass

    ### for level 3
    def deliver2(self, dest_office):
        ''' 
            >>> pack1 = Package(1,101,102)
            >>> office101 = Office(101)
            >>> office102 = Office(102)
            >>> office101.add_package_to_mailout(pack1)
            >>> office101.transfer(office102)
            >>> office101.deliver(office102)
            >>> print(office102)
                Office id: 102
                Mail-in Packages: 
                packet id: 1, from: 101, to: 102, current: 102, status: delivered
                Mail-out Packages: 

            >>> print(office101)
                Office id: 101
                Mail-in Packages: 
                Mail-out Packages:
                
        '''
        # fill in your own code
        pass
    

    
