# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_ecs20140526.client import Client as EcsClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_darabonba_env.client import Client as EnvClient
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def initialization(
        region_id: str,
    ) -> EcsClient:
        """
        Initialization  初始化公共请求参数
        """
        config = open_api_models.Config()
        # 您的AccessKey ID
        config.access_key_id = EnvClient.get_env('ACCESS_KEY_ID')
        # 您的AccessKey Secret
        config.access_key_secret = EnvClient.get_env('ACCESS_KEY_SECRET')
        # 您的可用区ID
        config.region_id = region_id
        return EcsClient(config)

    @staticmethod
    def describe_cloud_assistant_status(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> str:
        """
        DescribeCloudAssistantStatus  查询是否安装了云助手客户端
        """
        req = ecs_models.DescribeCloudAssistantStatusRequest()
        # 所在的地域ID
        req.region_id = region_id
        # 实例ID列表
        req.instance_id = [
            instance_id
        ]
        resp = client.describe_cloud_assistant_status(req)
        ConsoleClient.log('--------------------查询是否安装了云助手客户端--------------------')
        status = resp.body.instance_cloud_assistant_status_set.instance_cloud_assistant_status[0]
        ConsoleClient.log(f'实例ID {status.instance_id} 是否安装云助手 {status.cloud_assistant_status}')
        return status.cloud_assistant_status

    @staticmethod
    async def describe_cloud_assistant_status_async(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> str:
        """
        DescribeCloudAssistantStatus  查询是否安装了云助手客户端
        """
        req = ecs_models.DescribeCloudAssistantStatusRequest()
        # 所在的地域ID
        req.region_id = region_id
        # 实例ID列表
        req.instance_id = [
            instance_id
        ]
        resp = await client.describe_cloud_assistant_status_async(req)
        ConsoleClient.log('--------------------查询是否安装了云助手客户端--------------------')
        status = resp.body.instance_cloud_assistant_status_set.instance_cloud_assistant_status[0]
        ConsoleClient.log(f'实例ID {status.instance_id} 是否安装云助手 {status.cloud_assistant_status}')
        return status.cloud_assistant_status

    @staticmethod
    def install_cloud_assistant(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> None:
        """
        InstallCloudAssistant  安装云助手客户端
        """
        req = ecs_models.InstallCloudAssistantRequest()
        # 实例ID列表
        req.instance_id = [
            instance_id
        ]
        # 可用区ID
        req.region_id = region_id
        client.install_cloud_assistant(req)
        ConsoleClient.log('--------------------安装云助手客户端--------------------')

    @staticmethod
    async def install_cloud_assistant_async(
        client: EcsClient,
        instance_id: str,
        region_id: str,
    ) -> None:
        """
        InstallCloudAssistant  安装云助手客户端
        """
        req = ecs_models.InstallCloudAssistantRequest()
        # 实例ID列表
        req.instance_id = [
            instance_id
        ]
        # 可用区ID
        req.region_id = region_id
        await client.install_cloud_assistant_async(req)
        ConsoleClient.log('--------------------安装云助手客户端--------------------')

    @staticmethod
    def reboot_instance(
        client: EcsClient,
        instance_id: str,
    ) -> None:
        """
        RebootInstance  重启实例
        """
        req = ecs_models.RebootInstanceRequest()
        # 指定实例的ID
        req.instance_id = instance_id
        client.reboot_instance(req)
        ConsoleClient.log('--------------------重启实例--------------------')

    @staticmethod
    async def reboot_instance_async(
        client: EcsClient,
        instance_id: str,
    ) -> None:
        """
        RebootInstance  重启实例
        """
        req = ecs_models.RebootInstanceRequest()
        # 指定实例的ID
        req.instance_id = instance_id
        await client.reboot_instance_async(req)
        ConsoleClient.log('--------------------重启实例--------------------')

    @staticmethod
    def run_command(
        client: EcsClient,
        content: str,
        instance_id: str,
        region_id: str,
    ) -> str:
        """
        RunCommand  执行脚本
        """
        req = ecs_models.RunCommandRequest()
        # ECS实例ID列表
        req.instance_id = [
            instance_id
        ]
        # 可用区ID
        req.region_id = region_id
        # 脚本的明文内容或者Base64编码后的内容
        req.command_content = content
        # 运维脚本的语言类型
        req.type = 'RunShellScript'
        resp = client.run_command(req)
        ConsoleClient.log('--------------------执行脚本--------------------')
        ConsoleClient.log(f'脚本ID {resp.body.command_id} 请求ID {resp.body.request_id}')
        return resp.body.command_id

    @staticmethod
    async def run_command_async(
        client: EcsClient,
        content: str,
        instance_id: str,
        region_id: str,
    ) -> str:
        """
        RunCommand  执行脚本
        """
        req = ecs_models.RunCommandRequest()
        # ECS实例ID列表
        req.instance_id = [
            instance_id
        ]
        # 可用区ID
        req.region_id = region_id
        # 脚本的明文内容或者Base64编码后的内容
        req.command_content = content
        # 运维脚本的语言类型
        req.type = 'RunShellScript'
        resp = await client.run_command_async(req)
        ConsoleClient.log('--------------------执行脚本--------------------')
        ConsoleClient.log(f'脚本ID {resp.body.command_id} 请求ID {resp.body.request_id}')
        return resp.body.command_id

    @staticmethod
    def describe_invocation_results(
        client: EcsClient,
        instance_id: str,
        command_id: str,
        region_id: str,
        content_encoding: str,
    ) -> bool:
        """
        DescribeInvocationResults  查看云助手命令的执行结果
        """
        req = ecs_models.DescribeInvocationResultsRequest()
        # 实例ID
        req.instance_id = instance_id
        # 可用区ID
        req.region_id = region_id
        # 脚本ID
        req.command_id = command_id
        # 设置返回数据中Output字段的编码方式
        req.content_encoding = content_encoding
        resp = client.describe_invocation_results(req)
        invocation_result = resp.body.invocation.invocation_results.invocation_result[0]
        if not UtilClient.is_unset(invocation_result.invocation_status) and UtilClient.equal_string(invocation_result.invocation_status, 'Aborted'):
            ConsoleClient.log(f'执行失败 错误信息 {invocation_result.error_info}')
            return True
        elif UtilClient.is_unset(invocation_result.exit_code):
            ConsoleClient.log('脚本执行中，请等待.......')
            return False
        else:
            if UtilClient.equal_string(f'{invocation_result.exit_code}', '0'):
                ConsoleClient.log(f'命令输出结果 {invocation_result.output}')
            else:
                ConsoleClient.log(f'错误码 {invocation_result.error_code} 错误信息 {invocation_result.error_info}')
            return True

    @staticmethod
    async def describe_invocation_results_async(
        client: EcsClient,
        instance_id: str,
        command_id: str,
        region_id: str,
        content_encoding: str,
    ) -> bool:
        """
        DescribeInvocationResults  查看云助手命令的执行结果
        """
        req = ecs_models.DescribeInvocationResultsRequest()
        # 实例ID
        req.instance_id = instance_id
        # 可用区ID
        req.region_id = region_id
        # 脚本ID
        req.command_id = command_id
        # 设置返回数据中Output字段的编码方式
        req.content_encoding = content_encoding
        resp = await client.describe_invocation_results_async(req)
        invocation_result = resp.body.invocation.invocation_results.invocation_result[0]
        if not UtilClient.is_unset(invocation_result.invocation_status) and UtilClient.equal_string(invocation_result.invocation_status, 'Aborted'):
            ConsoleClient.log(f'执行失败 错误信息 {invocation_result.error_info}')
            return True
        elif UtilClient.is_unset(invocation_result.exit_code):
            ConsoleClient.log('脚本执行中，请等待.......')
            return False
        else:
            if UtilClient.equal_string(f'{invocation_result.exit_code}', '0'):
                ConsoleClient.log(f'命令输出结果 {invocation_result.output}')
            else:
                ConsoleClient.log(f'错误码 {invocation_result.error_code} 错误信息 {invocation_result.error_info}')
            return True

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        try:
            region_id = args[0]
            instance_id = args[1]
            content = args[2]
            content_encoding = args[3]
            client = Sample.initialization(region_id)
            cloud_assistant_status = Sample.describe_cloud_assistant_status(client, instance_id, region_id)
            if UtilClient.equal_string(cloud_assistant_status, 'false'):
                Sample.install_cloud_assistant(client, instance_id, region_id)
                Sample.reboot_instance(client, instance_id)
            command_id = Sample.run_command(client, content, instance_id, region_id)
            while True:
                is_exit = Sample.describe_invocation_results(client, instance_id, command_id, region_id, content_encoding)
                if is_exit:
                    break
                UtilClient.sleep(2000)
        except Exception as error:
            ConsoleClient.log(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        try:
            region_id = args[0]
            instance_id = args[1]
            content = args[2]
            content_encoding = args[3]
            client = Sample.initialization(region_id)
            cloud_assistant_status = await Sample.describe_cloud_assistant_status_async(client, instance_id, region_id)
            if UtilClient.equal_string(cloud_assistant_status, 'false'):
                await Sample.install_cloud_assistant_async(client, instance_id, region_id)
                await Sample.reboot_instance_async(client, instance_id)
            command_id = await Sample.run_command_async(client, content, instance_id, region_id)
            while True:
                is_exit = await Sample.describe_invocation_results_async(client, instance_id, command_id, region_id, content_encoding)
                if is_exit:
                    break
                await UtilClient.sleep_async(2000)
        except Exception as error:
            ConsoleClient.log(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
