# -*- coding: utf-8 -*-
import dependency_injector.containers as containers
import dependency_injector.providers as providers

from project.application.services.home import HomeAppService
from project.application.services.doc import DocumentationAppService
from project.application.services.project import ProjectAppService
from project.application.services.contact import ContactAppService
from project.domain.services.project import ProjectDomainService
from project.domain.services.contact import ContactDomainService
from project.infrastructure.adapter.config.file_config import FileConfig
from project.infrastructure.adapter.sql.sqlalchemy import SqlAlchemyAdapter
from project.infrastructure.repository.mockup.project import MockProjectRepository
from project.infrastructure.repository.mockup.property_type import MockPropertyTypeRepository
from project.infrastructure.repository.mockup.contact import MockContactRepository
from project.infrastructure.repository.sqlalchemy.project import ProjectSqlAlchemyRepository
from project.infrastructure.adapter.log.logging import ConsoleLogger
from project.infrastructure.repository.sqlalchemy.contact import ContactSqlAlchemyRepository
from project.infrastructure.repository.sqlalchemy.service_project import ServiceProjectSqlAlchemyRepository
from project.domain.services.service_project import ServiceProjectDomainService
from project.application.services.service_project import ServiceProjectAppService
from project.infrastructure.repository.sqlalchemy.service import ServiceSqlAlchemyRepository
from project.domain.services.service import ServiceDomainService
from project.application.services.service import ServiceAppService
from project.application.services.property_type import PropertyTypeAppService
from project.domain.services.property_type import PropertyTypeDomainService
from project.infrastructure.repository.sqlalchemy.property_type import PropertyTypeSqlAlchemyRepository
from project.application.services.bank import BankAppService
from project.domain.services.bank import BankDomainService
from project.infrastructure.repository.sqlalchemy.bank import BankSqlAlchemyRepository
from project.infrastructure.repository.mockup.bank import MockBankRepository
from project.domain.services.ubigeo import UbigeoDomainService
from project.infrastructure.repository.rest.deparment import DepartmentMicroServiceRepository
from project.infrastructure.adapter.rest.request import ServicesAdapter
from project.infrastructure.repository.rest.province import ProvinceMicroServiceRepository
from project.infrastructure.repository.rest.district import DistrictMicroServiceRepository
from project.infrastructure.repository.rest.user import UserMicroServiceRepository
from project.infrastructure.repository.mockup.department import MockDepartmentRepository
from project.infrastructure.repository.mockup.province import MockProvinceRepository
from project.infrastructure.repository.mockup.district import MockDistrictRepository
from project.infrastructure.repository.mockup.user import MockUserProfileRepository
from project.application.services.stage import StageAppService
from project.domain.services.stage import StageDomainService
from project.infrastructure.repository.sqlalchemy.stage import StageSqlAlchemyRepository
from project.infrastructure.repository.mockup.stage import MockStageRepository
from project.application.services.multimedia import MultimediaAppService
from project.domain.services.multimedia import MultimediaDomainService
from project.infrastructure.repository.sqlalchemy.multimedia import MultimediaSqlAlchemyRepository
from project.infrastructure.repository.mockup.multimedia import MockMultimediaRepository
from project.infrastructure.repository.mockup.service_project import MockServiceProjectRepository
from project.infrastructure.adapter.aws.s3 import S3Service
from project.infrastructure.repository.aws.s3.multimedia_images import MultimediaImagesS3Repository
from project.application.services.multimedia_project import MultimediaProjectAppService
from project.domain.services.multimedia_project import MultimediaProjectDomainService
from project.infrastructure.repository.sqlalchemy.multimedia_project import MultimediaProjectSqlAlchemyRepository
from project.domain.services.multimedia_images import MultimediaImagesDomainService
from project.application.services.contact_persists import ContactPersistsAppService
from project.domain.services.contact_persists import ContactPersistsDomainService
from project.infrastructure.repository.sqlalchemy.contact_persists import ContactPersistsSqlAlchemyRepository
from project.infrastructure.repository.mockup.contact_persists import MockContactPersistsRepository
from project.application.services.operation_type import OperationTypeAppService
from project.domain.services.operation_type import OperationTypeDomainService
from project.infrastructure.repository.sqlalchemy.operation_type import OperationTypeSqlAlchemyRepository
from project.infrastructure.repository.mockup.operation_type import MockOperationTypeRepository


class ConfigInjector(containers.DeclarativeContainer):
    # spring_config = providers.Singleton(SpringConfig)
    app_config = providers.Singleton(FileConfig)


class AdapterInjector(containers.DeclarativeContainer):
    sql_alchemy = providers.Factory(SqlAlchemyAdapter, config=ConfigInjector.app_config)
    services = providers.Factory(ServicesAdapter, config=ConfigInjector.app_config)


class RepositoryInjector(containers.DeclarativeContainer):
    operation_type = providers.Singleton(OperationTypeSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    contact_persists = providers.Singleton(ContactPersistsSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    multimedia_project = providers.Singleton(MultimediaProjectSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    multimedia = providers.Singleton(MultimediaSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    stage = providers.Singleton(StageSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    bank = providers.Singleton(BankSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    home = providers.Singleton(ProjectSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    project = providers.Singleton(ProjectSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    contact = providers.Singleton(ContactSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    service_project = providers.Singleton(ServiceProjectSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    service = providers.Singleton(ServiceSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    property_type = providers.Singleton(PropertyTypeSqlAlchemyRepository, adapter=AdapterInjector.sql_alchemy)
    department = providers.Singleton(DepartmentMicroServiceRepository, adapter=AdapterInjector.services)
    province = providers.Singleton(ProvinceMicroServiceRepository, adapter=AdapterInjector.services)
    district = providers.Singleton(DistrictMicroServiceRepository, adapter=AdapterInjector.services)
    user = providers.Singleton(UserMicroServiceRepository, adapter=AdapterInjector.services)


class DomainServicesInjector(containers.DeclarativeContainer):
    operation_type = providers.Singleton(OperationTypeDomainService, repository=RepositoryInjector.operation_type)
    contact_persists = providers.Singleton(ContactPersistsDomainService, repository=RepositoryInjector.contact_persists)
    home = providers.Singleton(ProjectDomainService, repository=RepositoryInjector.home)
    multimedia = providers.Singleton(MultimediaDomainService, repository=RepositoryInjector.multimedia)
    stage = providers.Singleton(StageDomainService, repository=RepositoryInjector.stage)
    bank = providers.Singleton(BankDomainService, repository=RepositoryInjector.bank)
    project = providers.Singleton(ProjectDomainService, repository=RepositoryInjector.project)
    property_type = providers.Singleton(PropertyTypeDomainService, repository=RepositoryInjector.property_type)
    service_project = providers.Singleton(ServiceProjectDomainService, repository=RepositoryInjector.service_project)
    service = providers.Singleton(ServiceDomainService, repository=RepositoryInjector.service)
    contact = providers.Singleton(ContactDomainService, repository=RepositoryInjector.contact)
    ubigeo = providers.Singleton(UbigeoDomainService, department_repository=RepositoryInjector.department,
                                 province_repository=RepositoryInjector.province, district_repository=RepositoryInjector.district,
                                 user_repository=RepositoryInjector.user)
    multimedia_project = providers.Singleton(MultimediaProjectDomainService, repository=RepositoryInjector.multimedia_project)
    multimedia_images = providers.Singleton(MultimediaImagesDomainService, repository=RepositoryInjector.multimedia_images)


class LoggerInjector(containers.DeclarativeContainer):
    console = providers.Singleton(ConsoleLogger)


class AppServicesInjector(containers.DeclarativeContainer):
    operation_type = providers.Singleton(OperationTypeAppService, domain_service=DomainServicesInjector.operation_type)
    contact_persists = providers.Singleton(ContactPersistsAppService, domain_service=DomainServicesInjector.contact_persists)
    home = providers.Singleton(HomeAppService, domain_service=DomainServicesInjector.home, domain_ubigeo=DomainServicesInjector.ubigeo)
    multimedia = providers.Singleton(MultimediaAppService, domain_service=DomainServicesInjector.multimedia)
    stage = providers.Singleton(StageAppService, domain_service=DomainServicesInjector.stage)
    bank = providers.Singleton(BankAppService, domain_service=DomainServicesInjector.bank)
    project = providers.Singleton(ProjectAppService, domain_service=DomainServicesInjector.project)
    property_type = providers.Singleton(PropertyTypeAppService, domain_service=DomainServicesInjector.property_type)
    service_project = providers.Singleton(ServiceProjectAppService, domain_service=DomainServicesInjector.service_project)
    service = providers.Singleton(ServiceAppService, domain_service=DomainServicesInjector.service)
    contact = providers.Singleton(ContactAppService, domain_service=DomainServicesInjector.contact)
    doc = providers.Singleton(DocumentationAppService)
    multimedia_project = providers.Singleton(MultimediaProjectAppService, domain_service=DomainServicesInjector.multimedia_project,
                                             domain_multimedia=DomainServicesInjector.multimedia, domain_images=DomainServicesInjector.multimedia_images)


'''
Mock Class
'''


class MockRepositoryInjector(containers.DeclarativeContainer):
    operation_type = providers.Factory(MockOperationTypeRepository)
    contact_persists = providers.Factory(MockContactPersistsRepository)
    multimedia = providers.Factory(MockMultimediaRepository)
    stage = providers.Factory(MockStageRepository)
    bank = providers.Factory(MockBankRepository)
    project = providers.Factory(MockProjectRepository)
    property_type = providers.Factory(MockPropertyTypeRepository)
    home = providers.Factory(MockProjectRepository)
    contact = providers.Factory(MockContactRepository)
    department = providers.Factory(MockDepartmentRepository)
    province = providers.Factory(MockProvinceRepository)
    district = providers.Factory(MockDistrictRepository)
    user = providers.Factory(MockUserProfileRepository)
    service_project = providers.Factory(MockServiceProjectRepository)


class MockDomainServicesInjector(containers.DeclarativeContainer):
    operation_type = providers.Factory(OperationTypeDomainService, repository=MockRepositoryInjector.operation_type)
    contact_persists = providers.Factory(ContactPersistsDomainService, repository=MockRepositoryInjector.contact_persists)
    multimedia = providers.Factory(MultimediaDomainService, repository=MockRepositoryInjector.multimedia)
    stage = providers.Factory(StageDomainService, repository=MockRepositoryInjector.stage)
    bank = providers.Factory(BankDomainService, repository=MockRepositoryInjector.bank)
    project = providers.Factory(ProjectDomainService, repository=MockRepositoryInjector.project)
    property_type = providers.Factory(PropertyTypeDomainService, repository=MockRepositoryInjector.property_type)
    home = providers.Factory(ProjectDomainService, repository=MockRepositoryInjector.home)
    contact = providers.Factory(ContactDomainService, repository=MockRepositoryInjector.contact)
    ubigeo = providers.Factory(UbigeoDomainService, department_repository=MockRepositoryInjector.department,
                               province_repository=MockRepositoryInjector.province,
                               district_repository=MockRepositoryInjector.district,
                               user_repository=MockRepositoryInjector.user)
    service_project = providers.Factory(ServiceProjectDomainService, repository=MockRepositoryInjector.service_project)


class MockAppServicesInjector(containers.DeclarativeContainer):
    operation_type = providers.Singleton(OperationTypeAppService, domain_service=MockDomainServicesInjector.operation_type)
    contact_persists = providers.Singleton(ContactPersistsAppService, domain_service=MockDomainServicesInjector.contact_persists)
    home = providers.Singleton(HomeAppService, domain_service=MockDomainServicesInjector.home, domain_ubigeo=MockDomainServicesInjector.ubigeo)
    multimedia = providers.Singleton(MultimediaAppService, domain_service=MockDomainServicesInjector.multimedia)
    stage = providers.Singleton(StageAppService, domain_service=MockDomainServicesInjector.stage)
    bank = providers.Singleton(BankAppService, domain_service=MockDomainServicesInjector.bank)
    project = providers.Singleton(ProjectAppService, domain_service=MockDomainServicesInjector.project)
    property_type = providers.Singleton(PropertyTypeAppService, domain_service=MockDomainServicesInjector.property_type)
    contact = providers.Singleton(ContactAppService, domain_service=MockDomainServicesInjector.contact)
    service_project = providers.Singleton(ServiceProjectAppService, domain_service=MockDomainServicesInjector.service_project)
