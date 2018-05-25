# -*- coding: utf-8 -*-

from project.domain.entities.contact import Contact
from project.domain.valueObjects.contact import Id, IdProject, Name, LastName, Phone, PhoneSecond, Schedule, Email, EmailGroup, State


class ContactFactory:

    @staticmethod
    def create(id_project, **kwargs):
        id = Id(kwargs['id'] if 'id' in kwargs else None)
        id_project = IdProject(id_project)
        name = Name(kwargs['name'])
        last_name = LastName(kwargs['lastName'])
        phone = Phone(kwargs['phone'])
        phone_second = PhoneSecond(kwargs['phoneSecond'] if 'phoneSecond' in kwargs else None)
        schedule = Schedule(kwargs['schedule'] if 'schedule' in kwargs else None)
        email = Email(kwargs['email'])
        email_group = EmailGroup(kwargs['emailGroup'] if 'emailGroup' in kwargs else None)
        state = State(kwargs['state'] if 'state' in kwargs else 1)

        return Contact(id_project.value, name.value, last_name.value, phone.value, phone_second.value,  schedule.value, email.value, email_group.value, state.value, id.value)

    @staticmethod
    def get_contact(contact: Contact):
        return {
            'id': contact.id,
            'idProject': contact.idProject,
            'name': contact.name,
            'lastName': contact.lastName,
            'phone': contact.phone,
            'phoneSecond': "" if contact.phoneSecond is None else contact.phoneSecond,
            'schedule': contact.schedule,
            'email': contact.email,
            'emailGroup': "" if contact.emailGroup is None else contact.emailGroup,
            'state': contact.state
        }
