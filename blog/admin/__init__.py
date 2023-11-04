def register_views():
    from blog.models import models
    from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView, AuthorsAdminView
    from blog.models.database import db
    from blog.extensions import admin

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.User, db.session, category='Models'))
    admin.add_view(AuthorsAdminView(models.Author, db. session, category='Models'))