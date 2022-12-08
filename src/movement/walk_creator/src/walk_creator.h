#ifndef WALK_CREATORH
#define WALK_CREATORH

#include <cstdlib>
#include <jsoncpp/json/value.h>
#include <jsoncpp/json/json.h>
#include <fstream>
#include <string>

#include "../include/IKWalk.hpp"
#include "ros/ros.h"
#include "movement_msgs/WalkingPositionsMsg.h"
#include "movement_msgs/WalkCreatorRequestMsg.h"
#include "movement_msgs/WalkTestParametersSrv.h"

class WalkCreator
{
    public:
        WalkCreator(ros::NodeHandle nh);

        struct Rhoban::IKWalkParameters params;
        struct Rhoban::IKWalkOutputs outputs;

        bool runWalk(const Rhoban::IKWalkParameters& params, double timeLength, double& phase, double& time);
        bool parametersUpdateRequest(movement_msgs::WalkTestParametersSrv::Request  &req_params, movement_msgs::WalkTestParametersSrv::Response &res);
        
        void walkRequest(const movement_msgs::WalkCreatorRequestMsg& msg);
        void reqEqualsParam();
        void initParams();
        void paramsEqualsReq(movement_msgs::WalkTestParametersSrv::Request  &req);

        movement_msgs::WalkingPositionsMsg positions;
        movement_msgs::WalkTestParametersSrv parameters2update;

        double engineFrequency = 20;
        double stepNumber = 12;
        
        double phase = 0.0;
        double time = 0.0;
        
        float step;
        float lateral;
        float turn;

        bool interfaceOn;

        std::string default_path = std::getenv("HOME");
        std::string edrom_path = "/edrom/src/movement/movement_utils/walk_test_jsons/default.json";

        Json::Value paramsJson;
        Json::Reader reader;

        ros::Publisher walk_motor_positions_pub;
        ros::Subscriber request_walk_creation;
        ros::ServiceServer request_parameters_update;
        ros::ServiceClient interface_parameters_update;
};


#endif

