# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as ECS20140526Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ecs20140526 import models as ecs20140526_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_env.client import Client as EnvClient

ACCESS_KEY_ID = LTAI5tMuUWCcThf5SwAfVYcU
ACCESS_KEY_SECRET = gEpY3ILOiPMNidWRXOkDRHuy42fjt8


class CreateInstancesSample:
    def __init__(self):
        pass

    @staticmethod
    def initialization(
        access_key_id: str,
        access_key_secret: str,
        region_id: str,
    ) -> ECS20140526Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @param region_id:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config()
        # 您的AccessKey ID
        config.access_key_id = access_key_id
        # 您的AccessKey Secret
        config.access_key_secret = access_key_secret
        # 您的可用区ID
        config.region_id = region_id
        return ECS20140526Client(config)

    @staticmethod
    def create_instance_sample(
        client: ECS20140526Client,
        region_id: str,
        name: str,
        password: str,
        instance_type: str,
        zone_id: str,
        image_id: str,
        dry_run: bool,
    ) -> None:
        """
        创建实例
        @param client:
        @param region_id:
        @param name:
        @param password:
        @param instance_type:
        @throws Exception
        """
        try:
            request = ecs20140526_models.CreateInstanceRequest(
                instance_name=name,
                password=password,
                instance_type=instance_type,
                region_id=region_id,
                zone_id=zone_id,
                image_id=image_id,
                dry_run=dry_run
            )
            response = client.create_instance(request)
            ConsoleClient.log(f'创建实例成功，实例ID:{response.body.instance_id}')
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    async def create_instance_sample_async(
        client: ECS20140526Client,
        region_id: str,
        name: str,
        password: str,
        instance_type: str,
        zone_id: str,
        image_id: str,
        dry_run: bool,
    ) -> None:
        """
        创建实例
        @param client:
        @param region_id:
        @param name:
        @param password:
        @param instance_type:
        @throws Exception
        """
        try:
            request = ecs20140526_models.CreateInstanceRequest(
                instance_name=name,
                password=password,
                instance_type=instance_type,
                region_id=region_id,
                zone_id=zone_id,
                image_id=image_id,
                dry_run=dry_run
            )
            response = await client.create_instance_async(request)
            ConsoleClient.log(f'创建实例成功，实例ID:{response.body.instance_id}')
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def describe_instances_sample(
        client: ECS20140526Client,
        region_id: str,
    ) -> None:
        """
        查询实例列表
        @param client:
        @param region_id:
        @throws Exception
        """
        try:
            request = ecs20140526_models.DescribeInstancesRequest(
                region_id=region_id
            )
            response = client.describe_instances(request)
            instances = response.body.instances.instance
            for instance in instances:
                ConsoleClient.log(f'实例ID:{instance.instance_id}信息')
                ConsoleClient.log(f'  状态:{instance.status}')
                ConsoleClient.log(f'  CPU:{instance.cpu}')
                ConsoleClient.log(f'  内存:{instance.memory}MB')
                ConsoleClient.log(f'  规格:{instance.instance_type}')
                ConsoleClient.log(f'  系统:{instance.ostype}({instance.osname})')
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    async def describe_instances_sample_async(
        client: ECS20140526Client,
        region_id: str,
    ) -> None:
        """
        查询实例列表
        @param client:
        @param region_id:
        @throws Exception
        """
        try:
            request = ecs20140526_models.DescribeInstancesRequest(
                region_id=region_id
            )
            response = await client.describe_instances_async(request)
            instances = response.body.instances.instance
            for instance in instances:
                ConsoleClient.log(f'实例ID:{instance.instance_id}信息')
                ConsoleClient.log(f'  状态:{instance.status}')
                ConsoleClient.log(f'  CPU:{instance.cpu}')
                ConsoleClient.log(f'  内存:{instance.memory}MB')
                ConsoleClient.log(f'  规格:{instance.instance_type}')
                ConsoleClient.log(f'  系统:{instance.ostype}({instance.osname})')
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        # 区域ID
        region_id = args[0]
        # 实例名称
        instance_name = args[1]
        # 密码
        password = args[2]
        # 实例规格
        instance_type = args[3]
        # 可用区ID
        zone_id = args[4]
        # 镜像文件ID
        image_id = args[5]
        # 预检请求
        # true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回DryRunOperation错误。
        # false：发送正常请求，通过检查后直接创建实例。
        dry_run_str = args[6]
        dry_run = True
        if UtilClient.equal_string(dry_run_str, 'false'):
            dry_run = False
        client = Sample.initialization(EnvClient.get_env('ACCESS_KEY_ID'), EnvClient.get_env('ACCESS_KEY_SECRET'), region_id)
        # 1.创建实例
        ConsoleClient.log('--------------------创建实例--------------------')
        Sample.create_instance_sample(client, region_id, instance_name, password, instance_type, zone_id, image_id, dry_run)
        # 2.等待实例创建成功
        UtilClient.sleep(1000)
        # 2.查询实例列表
        ConsoleClient.log('--------------------查询实例列表--------------------')
        Sample.describe_instances_sample(client, region_id)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        # 区域ID
        region_id = args[0]
        # 实例名称
        instance_name = args[1]
        # 密码
        password = args[2]
        # 实例规格
        instance_type = args[3]
        # 可用区ID
        zone_id = args[4]
        # 镜像文件ID
        image_id = args[5]
        # 预检请求
        # true：发送检查请求，不会创建实例。检查项包括是否填写了必需参数、请求格式、业务限制和ECS库存。如果检查不通过，则返回对应错误。如果检查通过，则返回DryRunOperation错误。
        # false：发送正常请求，通过检查后直接创建实例。
        dry_run_str = args[6]
        dry_run = True
        if UtilClient.equal_string(dry_run_str, 'false'):
            dry_run = False
        client = Sample.initialization(EnvClient.get_env('ACCESS_KEY_ID'), EnvClient.get_env('ACCESS_KEY_SECRET'), region_id)
        # 1.创建实例
        ConsoleClient.log('--------------------创建实例--------------------')
        await Sample.create_instance_sample_async(client, region_id, instance_name, password, instance_type, zone_id, image_id, dry_run)
        # 2.等待实例创建成功
        await UtilClient.sleep_async(1000)
        # 2.查询实例列表
        ConsoleClient.log('--------------------查询实例列表--------------------')
        await Sample.describe_instances_sample_async(client, region_id)


if __name__ == '__main__':
    Sample.main(ACCESS_KEY_ID, ACCESS_KEY_SECRET, )
