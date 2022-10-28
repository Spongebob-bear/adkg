# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys
import logging
from tkinter import E

from typing import List

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from AliyunConfig import ECSConfig
from AliyunConfig import RegionConfig


class ECSManager:

    ACCESS_KEY_ID = 'LTAI5tMuUWCcThf5SwAfVYcU'
    ACCESS_KEY_SECRET = 'gEpY3ILOiPMNidWRXOkDRHuy42fjt8'

    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
        config_endpoint: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = config_endpoint
        return Ecs20140526Client(config)

    @staticmethod
    def create_instance(region_id:str) -> None:
        """
            create one instance in the region identified by param:region_id.
        """

        client = ECSManager.create_client(ECSManager.ACCESS_KEY_ID, ECSManager.ACCESS_KEY_SECRET, 
            ECSConfig.REGION[region_id].CONFIG_ENDPOINT)
        system_disk = ecs_20140526_models.CreateInstanceRequestSystemDisk(
            category='cloud_essd'
        )
        create_instance_request = ecs_20140526_models.CreateInstanceRequest(
            region_id=region_id,
            image_id=ECSConfig.REGION[region_id].IMAGE_ID,
            instance_type=ECSConfig.REGION[region_id].INSTANCE_TYPE,
            security_group_id=ECSConfig.REGION[region_id].SECURITY_GROUP_IDS[0],
            instance_name=ECSConfig.INST_NAME,
            internet_charge_type=ECSConfig.INTERNET_CHARGE_TYPE,
            internet_max_bandwidth_out=ECSConfig.INTERNET_MAX_BANDWIDTH_OUT,
            internet_max_bandwidth_in=ECSConfig.INTERNET_MAX_BANDWIDTH_IN,
            password=ECSConfig.PASSWORD,
            system_disk=system_disk,
            instance_charge_type=ECSConfig.INSTANCE_CHARGE_TYPE,
            security_enhancement_strategy=ECSConfig.SECURITY_ENHANCEMENT_STRATEGY,
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            resp = client.create_instance_with_options(create_instance_request, runtime)
            print(vars(resp))

        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
            print(error)

    @staticmethod
    async def main_async() -> None:
        client = ECSManager.create_client('accessKeyId', 'accessKeySecret')
        system_disk = ecs_20140526_models.CreateInstanceRequestSystemDisk(
            category='cloud_essd'
        )
        create_instance_request = ecs_20140526_models.CreateInstanceRequest(
            region_id='cn-hongkong',
            image_id='m-j6calzsckaxjdy3o1iwd',
            instance_type='ecs.g7.large',
            security_group_id='sg-j6cgs979ky3jwqb2k322',
            instance_name='adkg-hongkong-01',
            internet_charge_type='PayByTraffic',
            internet_max_bandwidth_out=50,
            internet_max_bandwidth_in=50,
            password='adkg_test_666',
            system_disk=system_disk,
            instance_charge_type='PostPaid',
            security_enhancement_strategy='Deactive'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.create_instance_with_options_async(create_instance_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)



class RunCmdOnInst:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'ecs.cn-hongkong.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main() -> None:
        client = RunCmdOnInst.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        run_command_request = ecs_20140526_models.RunCommandRequest(
            region_id='cn-hongkong',
            name='touch',
            type='RunShellScript',
            command_content='touch helloword.txt',
            instance_id=[
                'i-j6c0q4b3lxkd5myuks8p'
            ],
            working_dir='/root/adkg'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.run_command_with_options(run_command_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = RunCmdOnInst.create_client(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        run_command_request = ecs_20140526_models.RunCommandRequest(
            region_id='cn-hongkong',
            name='touch',
            type='RunShellScript',
            command_content='touch helloword.txt',
            instance_id=[
                'i-j6c54tyfku5a9vq9u9z6'
            ],
            working_dir='/root/adkg'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.run_command_with_options_async(run_command_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

class RunInstances:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'ecs-cn-hangzhou.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-hongkong',
            image_id='123',
            instance_type='ecs.g7.large',
            security_group_id='123',
            internet_max_bandwidth_in=50,
            internet_max_bandwidth_out=50,
            instance_name='123',
            v_switch_id='123',
            host_name='123',
            unique_suffix=True,
            password='adkg_test_666',
            internet_charge_type='PayByTraffic',
            system_disk=system_disk,
            amount=10,
            security_enhancement_strategy='Deactive',
            instance_charge_type='PostPaid',
            security_group_ids=[
                '123'
            ],
            host_names=[
                '123'
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            client.run_instances_with_options(run_instances_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client('accessKeyId', 'accessKeySecret')
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd'
        )
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-hongkong',
            image_id='123',
            instance_type='ecs.g7.large',
            security_group_id='123',
            internet_max_bandwidth_in=50,
            internet_max_bandwidth_out=50,
            instance_name='123',
            v_switch_id='123',
            host_name='123',
            unique_suffix=True,
            password='adkg_test_666',
            internet_charge_type='PayByTraffic',
            system_disk=system_disk,
            amount=10,
            security_enhancement_strategy='Deactive',
            instance_charge_type='PostPaid',
            security_group_ids=[
                '123'
            ],
            host_names=[
                '123'
            ]
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.run_instances_with_options_async(run_instances_request, runtime)
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)

if __name__ == '__main__':
    ECSManager.create_instance('cn-chengdu')

