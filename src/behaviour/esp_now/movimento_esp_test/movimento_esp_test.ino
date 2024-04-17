#include <micro_ros_arduino.h>
#include <stdio.h>
#include <unistd.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <std_msgs/msg/int64_multi_array.h>
#include <std_msgs/msg/int32.h>
#include <std_msgs/msg/multi_array_dimension.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <WiFi.h>
#include <esp_now.h>
#define BUFFER_SIZE 15
#define STRING_SIZE 30
#define N_POT 8

#ifdef ESP_PLATFORM
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#endif

#define RCCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) { \
      printf("Failed status on line %d: %d. Aborting.\n", __LINE__, (int)temp_rc); \
      vTaskDelete(NULL); \
    } \
  }
#define RCSOFTCHECK(fn) \
  { \
    rcl_ret_t temp_rc = fn; \
    if ((temp_rc != RCL_RET_OK)) { printf("Failed status on line %d: %d. Continuing.\n", __LINE__, (int)temp_rc); } \
  }

rcl_publisher_t publisher;
rcl_subscription_t subscriber;
rclc_executor_t executor;
rclc_executor_t executor2;
rcl_node_t node;
rclc_support_t support;
std_msgs__msg__Int64MultiArray msg;
std_msgs__msg__Int32 sub_msg;
rcl_timer_t timer;


esp_now_peer_info_t peerInfo;
int potPrint = 1;
typedef struct struct_message {
  uint16_t potValue[N_POT];
} struct_message;

struct_message myData;


void subscription_callback(const void *msgin) {
  const std_msgs__msg__Int32 *msg = (const std_msgs__msg__Int32 *)msgin;
  Serial.printf("Received: %d\n", (int)msg->data);
}

void OnDataRecv(const uint8_t *mac, const uint8_t *incomingData, int len) {
  memcpy(&myData, incomingData, sizeof(myData));
}
void timer_callback(rcl_timer_t *timer, int64_t last_call_time) {
  RCLC_UNUSED(last_call_time);
  if (timer != NULL) {
    for (int i = 0; i < N_POT; i++) {
      msg.data.data[i] = myData.potValue[i];
      Serial.print(myData.potValue[i]);
      Serial.print("    ");
    }
    Serial.println(millis());
    msg.data.data[9]=millis();
    
    RCSOFTCHECK(rcl_publish(&publisher, &msg, NULL));
  }
}

void setup() {

  // ------------------------------------------------------------------------------------------
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) return;

  esp_now_register_recv_cb(OnDataRecv);

  uint8_t broadcastAddress[] = { 0x08, 0xD1, 0xF9, 0x27, 0x9E, 0xDC };
  memcpy(peerInfo.peer_addr, broadcastAddress, 6);
  peerInfo.channel = 0;
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }

  // -----------------------------------------------------------------------------------------------

  set_microros_transports();
  rcl_allocator_t allocator = rcl_get_default_allocator();


  // create init_options
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));

  // create node
  RCCHECK(rclc_node_init_default(&node, "int64_array_node", "", &support));

  // create publisher
  RCCHECK(rclc_publisher_init_default(&publisher, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int64MultiArray), "int64_array_publisher"));

  // Create subscriber.
  RCCHECK(rclc_subscription_init_default(&subscriber, &node, ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, Int32), "subscriber"));

  // create timer
  const unsigned int timer_timeout = 100;
  RCCHECK(rclc_timer_init_default(&timer, &support, RCL_MS_TO_NS(timer_timeout), timer_callback));

  // create executor

  RCCHECK(rclc_executor_init(&executor, &support.context, 2, &allocator));
  unsigned int rcl_wait_timeout = 100;
  RCCHECK(rclc_executor_set_timeout(&executor, RCL_MS_TO_NS(rcl_wait_timeout)));
  RCCHECK(rclc_executor_add_timer(&executor, &timer));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &sub_msg, &subscription_callback, ON_NEW_DATA));

  // Assing memory to msg
  int64_t buffer[BUFFER_SIZE] = {};
  msg.data.data = buffer;
  msg.data.size = 0;
  msg.data.capacity = BUFFER_SIZE;

  std_msgs__msg__MultiArrayDimension dim[BUFFER_SIZE] = {};
  msg.layout.dim.data = dim;
  msg.layout.dim.size = 0;
  msg.layout.dim.capacity = BUFFER_SIZE;

  char labels[BUFFER_SIZE][STRING_SIZE] = {};
  for (size_t i = 0; i < BUFFER_SIZE; i++) {
    msg.layout.dim.data[i].label.data = labels[i];
    msg.layout.dim.data[i].label.size = 0;
    msg.layout.dim.data[i].label.capacity = STRING_SIZE;
  }

  // Fill the message with dummy data
  for (size_t i = 0; i < BUFFER_SIZE; i++) {
    msg.data.data[i] = 0;
    msg.data.size++;
  }

  msg.layout.data_offset = 42;
  for (size_t i = 0; i < BUFFER_SIZE; i++) {
    snprintf(msg.layout.dim.data[i].label.data, STRING_SIZE, "label_%lu", i);
    msg.layout.dim.data[i].label.size = strlen(msg.layout.dim.data[i].label.data);
    msg.layout.dim.data[i].size = 42;
    msg.layout.dim.data[i].stride = 42;
  }
}
void loop() {
  rclc_executor_spin_some(&executor, RCL_MS_TO_NS(1));
  usleep(100000);
}
