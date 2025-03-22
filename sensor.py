import esphome.codegen as cg
import esphome.config_validation as cv
from esphome import pins
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    CONF_PIN,
    CONF_UPDATE_INTERVAL,
)

# 定义命名空间和类
r60abd1_ns = cg.esphome_ns.namespace("r60abd1")
R60ABD1Sensor = r60abd1_ns.class_(
    "R60ABD1Sensor", sensor.Sensor, cg.PollingComponent
)

# 配置验证规则
CONFIG_SCHEMA = sensor.sensor_schema(R60ABD1Sensor).extend({
    cv.Required(CONF_ID): cv.declare_id(R60ABD1Sensor),
    cv.Required(CONF_PIN): pins.gpio_input_pin_schema,
    cv.Optional(CONF_UPDATE_INTERVAL, default="60s"): cv.positive_time_period_milliseconds,
}).extend(cv.polling_component_schema("60s"))  # 默认更新间隔

# 生成 C++ 代码
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
    
    # 绑定 GPIO 引脚
    pin = await cg.gpio_pin_expression(config[CONF_PIN])
    cg.add(var.set_pin(pin))
