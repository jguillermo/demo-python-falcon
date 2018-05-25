import boto3
from concurrent.futures import as_completed
from concurrent.futures import ThreadPoolExecutor
from ..config.base import BaseConfig
from .base import BaseS3


class S3Service(BaseConfig, BaseS3):

    def __init__(self, config):
        self._config = config.get_key('aws')['s3']

    def copy_tmp_to_origin(self, images, id_project, id_user, id_model=None):
        self.create_resource()
        self.get_bucket()
        data = self.__prepare_data_origin(images, id_project, id_user, id_model)
        return self.send(data)

    def copy_origin_to_redim(self, images, id_project, id_user, id_model=None):
        self.create_resource()
        self.get_bucket()
        data = self.__prepare_data_redim(images, id_project, id_user, id_model)
        return self.send(data)

    def send(self, data):
        try:
            def copy(obj, bucket, key):
                result = obj.copy_from(CopySource={'Bucket': bucket, 'Key': key})
                return (result['ResponseMetadata']['HTTPStatusCode'])

            with ThreadPoolExecutor(max_workers=len(data)) as executor:
                todo = []

                for image in data:
                    dest_obj = self.s3.Object(image['bucketDestination'], key = image['keyDestination'])
                    future = executor.submit(copy, dest_obj, image['bucketOrigin'], key = image['keyOrigin'])
                    todo.append(future)
                results = []
                for future in as_completed(todo):
                    res = future.result()
                    results.append(res)
            return results
        except Exception as e:
            print(e)
            return False

    def __prepare_data_origin(self, images, id_project, id_user, id_model=None):
        self.id_project = id_project
        self.id_user = id_user

        data = []

        for image in images:
            image_name = image['name']
            alias_type = image['type']
            key_origin = 'tmp/'+image_name

            key_destination = self.create_key('origin', image_name) if alias_type == 'image' else self.create_key(alias_type, 'origin', image_name)
            key_destination = self.create_key('model', 'origin', image_name) if id_model is not None else key_destination

            data.append({
                'bucketOrigin': self.get_cde(), 'keyOrigin': key_origin,
                'bucketDestination': self.get_cde(), 'keyDestination': key_destination
             })
        return data

    def __prepare_data_redim(self, images, id_project, id_user, id_model=None):
        self.id_project = id_project
        self.id_user = id_user

        data = []

        for image in images:
            image_name = image['name']
            alias_type = image['type']

            key_origin = self.create_key('origin', image_name) if alias_type == 'image' else self.create_key(alias_type, 'origin', image_name)
            key_origin = self.create_key('model', 'origin', image_name) if id_model is not None else key_origin

            key_destination = self.create_key(image_name) if alias_type == 'image' else self.create_key(alias_type, image_name)
            key_destination = self.create_key('model', image_name) if id_model is not None else key_destination

            data.append({
                'bucketOrigin': self.get_cde(), 'keyOrigin': key_origin,
                'bucketDestination': self.get_redim(), 'keyDestination': key_destination
            })
        return data
