#pragma once

#include <esphome.h>
#include <components/sensor/sensor.h>

namespace esphome {
namespace r60abd1 {

class R60ABD1Sensor : public sensor::Sensor, public PollingComponent {
 public:
  void setup() override;
  void update() override;
  void set_pin(GPIOPin* pin);

 protected:
  GPIOPin* pin_;  // 存储 GPIO 引脚对象
};

}  // namespace r60abd1
}  // namespace esphome
