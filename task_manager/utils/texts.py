from django.utils.translation import gettext as _


class MessagesForUser:
    def __init__(self):
        self.login = _("You need to authenticated")
        self.no_rigths_for_user = _("You don't have the rights "
                                    "to change another user.")
        self.status_delete = _('The status successfully deleted')
        self.status_create = _('The status successfully created')
        self.status_update = _('The status successfully updated')
        self.no_delete_status = _("This status is used, you can't delete it")
        self.label_delete = _('The label successfully deleted')
        self.label_create = _('The label successfully created')
        self.label_update = _('The label successfully updated')
        self.no_delete_label = _("This label is used, you can't delete it")

        self.user_delete = _("The user deleted! You need to log in again")
        self.user_create = _('The user successfully created')
        self.user_update = _('The user successfully updated')
        self.no_delete_user = _("It is not possible to delete a user "
                                "because it is being used")
        self.task_delete = _('The task successfully deleted')
        self.task_create = _('The task successfully created')
        self.task_update = _('The task successfully updated')
        self.no_delete_task = _("The task can only be deleted by its author")


class TitlesName:
    def __init__(self):
        self.save = _('Save')
        self.delete = _('Delete')
        self.reg = _('Registration')
        self.to_reg = _('To register')
        self.create_label = _('Create label')
        self.create_task = _('Create task')
        self.create_status = _('Create status')
        self.update_label = _('Update label')
        self.update_task = _('Update task')
        self.update_status = _('Update status')
        self.update_user = _('Update user')
        self.update = _('Update')
        self.create = _('Create')
        self.to_del_task = _('To delete task')
        self.to_del_user = _('To delete user')
        self.to_del_label = _('To delete label')
        self.to_del_status = _('To delete status')


class FieldsName:
    def __init__(self):
        self.name = _('Name')
        self.descr = _('Description')
        self.label = _('Label')
        self.status = _('Status')
        self.executor = _('Executor')
        self.date = _('Date')
        self.task = _('Task')
        self.author = _('Author')
        self.labels = _('Labels')