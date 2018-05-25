# -*- coding: utf-8 -*-
import boto3


class BaseS3(object):

    bucket = None
    s3 = None

    def create_resource(self):
        self.s3 = boto3.resource('s3')

    def get_bucket(self):
        self.bucket = self.get_key('bucket')

    def get_cde(self):
        return self.bucket['cde']

    def get_redim(self):
        return self.bucket['redim']

    def create_key(self, *args):
        params = list(args)
        params.insert(0, str(self.id_project))
        params.insert(0, 'project')
        params.insert(0, str(self.id_user))
        return '/'.join(params)

