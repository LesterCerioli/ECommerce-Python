class EntitybaseWithTypedid(EntityBase):

    abstract = True
    id = db.Column(db.String(255), primary_key=True)

def __eq__(self, other):
    if not isinstance(other, EntityBaseWithTypedId):
        return False
    if self.id is None or other.id is None:
        return False
    return self.id == other.id

def __ne__(self, other):
    return not self.__eq__(other)

def __hash__(self):
    return hash(self.id) if self.id is not None else hash(super(EntityBaseWithTypedId, self).__hash__())
