class UsersRouter:
    """
    Маршрутизация для приложения users.
    """
    app_label = 'users'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'default'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == 'default'
        return None


class PostsRouter:
    """
    Маршрутизация для приложения posts.
    """
    app_label = 'posts'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'posts'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'posts'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == 'posts'
        return None


class CommentsRouter:
    """
    Маршрутизация для приложения comments.
    """
    app_label = 'comments'

    def db_for_read(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'comments'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == self.app_label:
            return 'comments'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == self.app_label:
            return db == 'comments'
        return None
