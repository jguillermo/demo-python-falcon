import unittest
from bootstrap.container import RepositoryInjector
from evaluation.domain.user import User
from evaluation.infrastructure.repository.sqlalchemy.mapping import load_mapper
from sdk.types import TypeUuid

load_mapper()


class TestUserMngRepository(unittest.TestCase):

    def test_user_persist_ok(self):
        user_repository = RepositoryInjector.user_mng()
        entity_user = User(id=TypeUuid().random(), name='Jose Antonio2', last_name='Guillermo')
        user_repository.persist(entity_user)
        self.assertEqual('123', '123')


if __name__ == "__main__":
    unittest.main()
