# -*- coding: utf-8 -*-


class Project:
    def __init__(self, id, name, description, id_property_type, id_stage, id_profile, id_department,
                 id_province, id_district, id_urbanization, id_beach, address, reference, finished, towers, floors,
                 units, elevators, garages, date_delivery, date_publication, date_expire, state):
        self.id = id
        self.name = name
        self.description = description
        self.idPropertyType = id_property_type
        self.idStage = id_stage
        self.idProfile = id_profile
        self.idDepartment = id_department
        self.idProvince = id_province
        self.idDistrict = id_district
        self.idUrbanization = id_urbanization
        self.idBeach = id_beach
        self.address = address
        self.reference = reference
        self.finished = finished
        self.towers = towers
        self.floors = floors
        self.units = units
        self.elevators = elevators
        self.garages = garages
        self.dateDelivery = date_delivery
        self.datePublication = date_publication
        self.dateExpire = date_expire
        self.state = state
