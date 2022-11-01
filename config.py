import os

BASE_DIR = os.path.dirname(__file__)

# db접속 주소. sqlite db 사용. db파일은 홈디렉터리에 pybo.db로 저장됨
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# sqlAlchemy 이벤트 처리
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
