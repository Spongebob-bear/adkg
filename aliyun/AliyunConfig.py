from distutils.command.config import config
import json
import os
import sys


class RegionConfig(object):
    def __init__(self, inst_amount, sg_ids, image_id, config_endpoint, instance_type):
        self.INST_AMOUT = inst_amount
        self.SECURITY_GROUP_IDS = sg_ids
        self.IMAGE_ID = image_id
        self.CONFIG_ENDPOINT = config_endpoint
        self.INSTANCE_TYPE = instance_type


class MPCConfig(object):
    def __init__(self, command, t, k, port, n, num_faulty_nodes):
        self.COMMAND = command
        self.T = t
        self.K = k
        self.PORT = port
        self.N = n
        self.NUM_FAULTY_NODES = num_faulty_nodes


def read_environment_variable(key):
    try:
        value = os.environ[key]
    except KeyError:
        print(f">>> {key} environment variable not set.")
        sys.exit(1)
    return value


class ECSConfig:
    config = json.load(open("aliyun/aliyun-config.json"))

    mpc_config = config["mpc"]

    assert (
        mpc_config["num_faulty_nodes"] <= mpc_config["t"]
    ), "`num_faulty_nodes` \
        cannot be greater than `t`"

    MPC_CONFIG = MPCConfig(
        mpc_config["command"],
        mpc_config["t"],
        mpc_config["k"],
        mpc_config["port"],
        mpc_config["n"],
        mpc_config["num_faulty_nodes"],
    )

    ecsConfig = config["aliyunECS"]
    # SETUP_FILE_PATH = ecsConfig["setup_file_path"]

    REGION = {}
    TOTAL_INST_AMOUNT = 0
    for region, value in ecsConfig["region"].items():
        REGION[region] = RegionConfig(
            value["inst_amount"],
            value["security_group_ids"],
            value["image_id"],
            value["config_endpoint"],
            value["instance_type"]
        )
        TOTAL_INST_AMOUNT += value["inst_amount"]

    INST_NAME = ecsConfig["inst_name"]
    INTERNET_CHARGE_TYPE = ecsConfig["internet_charge_type"]
    INTERNET_MAX_BANDWIDTH_OUT = ecsConfig["internet_max_bandwidth_out"]
    INTERNET_MAX_BANDWIDTH_IN = ecsConfig["internet_max_bandwidth_in"]
    PASSWORD = ecsConfig["password"]
    INSTANCE_CHARGE_TYPE = ecsConfig["instance_charge_type"]
    SECURITY_ENHANCEMENT_STRATEGY = ecsConfig["security_enhancement_strategy"]

    # INSTANCE_USER_NAME = ecsConfig["instance_user_name"]
    # BUCKET_NAME = ecsConfig["bucket_name"]
    # DOCKER_IMAGE_PATH = config["docker"]["image_path"]
