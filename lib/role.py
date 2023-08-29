from lib.audition import Audition


class Role:

    all = []

    def __init__(self, character_name):
        self.character_name = character_name
        Role.all.append(self)

    def __repr__(self):
        return f'(Role: {self.character_name})'

    @property
    def character_name(self):
        return self._character_name
    
    @character_name.setter
    def character_name(self, character_name):
        if isinstance(character_name, str) and 0 < len(character_name):
            self._character_name = character_name
        else: raise Exception('Must be a string more than 0 characters.')

    def auditions(self):
        return [aud for aud in Audition.all if aud.role == self]
    
    def actors(self):
        return [aud.actor for aud in Audition.all if aud.role == self]
    
    def locations(self):
        return [aud.location for aud in Audition.all if aud.role == self]
    
    def hires(self):
        return [aud for aud in Audition.all if aud.role == self and aud.hired]
    
    def lead(self):
        hires = self.hires()
        if len(hires) == 0:
            return 'No actor has been hired for this role'
        else: return hires[0]
            
    def understudy(self):
        hires = self.hires()
        if len(hires) <= 1:
            return 'No actor has been hired for understudy for this role'
        else: return hires[1]
    
    @classmethod
    def not_cast(cls):
        uncast = cls.all.copy()
        for audition in Audition.all:
            if audition.role in uncast and audition.hired == True:
                uncast.remove(audition.role)
        return uncast