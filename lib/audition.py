class Audition:

    all = []

    def __init__(self, role, actor, location, phone, hired=False):
        self.role = role
        self.actor = actor
        self.location = location
        self.phone = phone
        self.hired = hired
        Audition.all.append(self)

    def __repr__(self):
        return f'(Role:{self.role}), (Actor:{self.actor}), (Location:{self.location}), (Phone:{self.phone}), (Hired:{self.hired})'

    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, role):
        from lib.role import Role
        if isinstance(role, Role):
            self._role = role
        else: raise Exception('Role must be role instance.')

    @property
    def actor(self):
        return self._actor
    
    @actor.setter
    def actor(self, actor):
        if isinstance(actor, str) and 3 < len(actor) < 20:
            self._actor = actor
        else: raise Exception('Actor must be string between 3 and 20 characters.')

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, location):
        if isinstance(location, str):
            self._location = location
        else: raise Exception('Location must be string.')

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if isinstance(phone, str):
            self._phone = phone
        else: raise Exception('Phone must be string.')

    @property
    def hired(self):
        return self._hired
    
    @hired.setter
    def hired(self, hired):
        if isinstance(hired, bool):
            self._hired = hired
        else: raise Exception('Hired must be boolean value.')

    def call_back(self):
        self._hired = True

    pass
