#include "r60abd1.h"

namespace esphome {
namespace r60abd1 {

void R60ABD1Sensor::setup() {
  this->pin_->setup();  // 初始化 GPIO 引脚
}

void R60ABD1Sensor::update() {
  bool value = this->pin_->digital_read();  // 读取引脚状态
  this->publish_state(value ? 1.0 : 0.0);    // 发布传感器值（0/1）
}

void R60ABD1Sensor::set_pin(GPIOPin* pin) {
  this->pin_ = pin;  // 绑定引脚到组件
}

}  // namespace r60abd1
}  // namespace esphome
