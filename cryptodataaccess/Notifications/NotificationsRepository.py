from cryptomodel.operations import OPERATIONS

from cryptodataaccess.Memory import NOTIFICATIONS_MEMORY_KEY
from cryptodataaccess.Repository import Repository
from cryptomodel.sent_notification import sent_notification


DATE_FORMAT = "%Y-%m-%d"


class NotificationsRepository(Repository):

    def __init__(self, notifications_store):
        self.notifications_store = notifications_store
        super(NotificationsRepository, self).__init__()

    def add_sent_notification(self, user_id, user_name, user_email, notification_type, check_every, is_active,
                                  start_date, end_date, channel_type, threshold_value, source_id, computed_date, result,
                                  sent=False):
        n = sent_notification(
            user_id=user_id, user_name=user_name, user_email=user_email,
            notification_type=notification_type,
            check_every=check_every,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active,
            channel_type=channel_type, threshold_value=threshold_value, source_id=source_id,
            operation=OPERATIONS.ADDED.name, computed_date=computed_date, result=result, sent=sent)

        self.memories[NOTIFICATIONS_MEMORY_KEY].items.append(n)
        return n
