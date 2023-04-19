#strings
import logging
import os
import sys

import dotenv

logger = logging.getLogger('myapp')
dotenv.load_dotenv()

def get_env_variable(var_name):
    value = os.getenv(var_name)
    if not value or value == "":
        logger.error("错误：又尼玛的狗日的没设置环境变量是不是？？？？   %r",var_name)
        exit()
    return value


OPENAI_API_KEY = get_env_variable("OPENAI_API_KEY")
