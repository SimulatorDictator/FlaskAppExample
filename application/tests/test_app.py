from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Todos, Lists

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="Test_Example_Key",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setup(self):
        db.create_all()
        list1 = Lists(name="TestList1")
        todo1 = Todos(tasks="TestTask1", fk_lid=1)
        db.session.add(list)
        db.session.add(todo1)
        db.session.commit

class TestViews(TestBase):
    def test_index(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestList1", response.data)
        self.assertIn(b"TestTask1", response.data)