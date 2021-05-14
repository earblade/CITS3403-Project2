import unittest, os
from app import app, db

TEST_DB = 'test.db'

class UserTests(unittest.TestCase):

  ## setUp and tearDown
  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, TEST_DB)
    self.app = app.test_client() #setting up testing environment
    db.drop_all()
    db.create_all()

  def tearDown(self):
    db.drop_all()

  ## Testing methods
  def test_login(self):
    response = self.login('a@hotmail.com', 'a1234567', True)
    self.assertIn(b'Invalid Username or Password', response.data)
    response = self.login('a@hotmail.com', 'a', False)
    self.assertIn(b'Field must be between 8 and 80 characters long.', response.data)

  def test_registration(self):
    response = self.register('aaaa', 'a', '12345678')
    self.assertIn(b'Invalid email', response.data)

  def test_logout(self):
    self.register('aaaa', 'a@hotmail.com', '12345678')
    self.login('a@hotmail.com', '12345678', False)
    response = self.logout()
    self.assertEquals(response.status_code, 200)
  
  ## Helper methods
  def login(self, email, password, remember):
    return self.app.post(
      '/login', 
      data=dict(email=email, password=password, remember=remember), 
      follow_redirects = True
    )
  
  def register(self, username, email, password):
    return self.app.post(
      '/signup',
      data=dict(username=username, email=email, password=password),
      follow_redirects = True
    )
  
  def logout(self):
    return self.app.get(
      '/logout',
      follow_redirects = True
    )