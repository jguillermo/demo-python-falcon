# -*- coding: utf-8 -*-


class MultimediaProject:
    def __init__(self, id, idMultimedia, idProject):
        self.id = id
        self.idMultimedia = idMultimedia
        self.idProject = idProject

    def to_dict(self, *args, **kwargs):
        self.dict = dict(*args, **kwargs)
