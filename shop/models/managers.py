from django.db.models.query import QuerySet

class TestimonialQuerySet(QuerySet):
    def public_posts(self):
        return self.filter(is_public=True)

TestimonialManager = TestimonialQuerySet.as_manager