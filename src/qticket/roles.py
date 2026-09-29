from rolepermissions.roles import AbstractUserRole

class Organizer(AbstractUserRole):
    available_permissions = {
        'create_events': True,
        'edit_events': True,
        'delete_events': True,
        'create_partners': True,
        'edit_partners': True,
        'delete_partners': True,
        'create_participants': True,
        'edit_participants': True,
        'delete_participants': True,

    }

class Partner(AbstractUserRole):
    available_permissions = {
        'create_participants': True,
        'edit_participants': True,
        'delete_participants': True, 
    }

