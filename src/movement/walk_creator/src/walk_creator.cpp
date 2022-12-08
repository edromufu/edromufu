#include "walk_creator.h"

bool WalkCreator::parametersUpdateRequest(movement_msgs::WalkTestParametersSrv::Request  &req, movement_msgs::WalkTestParametersSrv::Response &res)
{
    
    paramsEqualsReq(req);

    res.success = true;

    if(interfaceOn)
    {
        reqEqualsParam();
        interface_parameters_update.call(parameters2update);
    }

    return true;
}

void WalkCreator::paramsEqualsReq(movement_msgs::WalkTestParametersSrv::Request  &req)
{
    params.freq                 = req.freq;
    params.supportPhaseRatio    = req.supportPhaseRatio;
    params.footYOffset          = req.footYOffset;
    params.riseGain             = req.riseGain;
    params.trunkZOffset         = req.trunkZOffset;
    params.swingGain            = req.swingGain;
    params.swingRollGain        = req.swingRollGain;
    params.swingPhase           = req.swingPhase;
    params.stepUpVel            = req.stepUpVel;
    params.stepDownVel          = req.stepDownVel;
    params.riseUpVel            = req.riseUpVel;
    params.riseDownVel          = req.riseDownVel;
    params.swingPause           = req.swingPause;
    params.swingVel             = req.swingVel;
    params.trunkXOffset         = req.trunkXOffset;
    params.trunkYOffset         = req.trunkYOffset;
    params.trunkPitch           = req.trunkPitch;
    params.trunkRoll            = req.trunkRoll;
    params.extraLeftX           = req.extraLeftX;
    params.extraLeftY           = req.extraLeftY;
    params.extraLeftZ           = req.extraLeftZ;
    params.extraRightX          = req.extraRightX;
    params.extraRightY          = req.extraRightY;
    params.extraRightZ          = req.extraRightZ;
    params.extraLeftYaw         = req.extraLeftYaw;
    params.extraLeftPitch       = req.extraLeftPitch;
    params.extraLeftRoll        = req.extraLeftRoll;
    params.extraRightYaw        = req.extraRightYaw;
    params.extraRightPitch      = req.extraRightPitch;
    params.extraRightRoll       = req.extraRightRoll;

    step = req.stepGain;
    lateral = req.lateralGain;
    turn = req.turnGain;
}

void WalkCreator::reqEqualsParam()
{
    parameters2update.request.freq = params.freq;
    parameters2update.request.supportPhaseRatio = params.supportPhaseRatio;
    parameters2update.request.footYOffset = params.footYOffset;
    parameters2update.request.riseGain = params.riseGain;
    parameters2update.request.trunkZOffset = params.trunkZOffset;
    parameters2update.request.swingGain = params.swingGain;
    parameters2update.request.swingRollGain = params.swingRollGain;
    parameters2update.request.swingPhase = params.swingPhase;
    parameters2update.request.stepUpVel = params.stepUpVel;
    parameters2update.request.stepDownVel = params.stepDownVel;
    parameters2update.request.riseUpVel = params.riseUpVel;
    parameters2update.request.riseDownVel = params.riseDownVel;
    parameters2update.request.swingPause = params.swingPause;
    parameters2update.request.swingVel = params.swingVel;
    parameters2update.request.trunkXOffset = params.trunkXOffset;
    parameters2update.request.trunkYOffset = params.trunkYOffset;
    parameters2update.request.trunkPitch = params.trunkPitch;
    parameters2update.request.trunkRoll = params.trunkRoll;
    parameters2update.request.extraLeftX = params.extraLeftX;
    parameters2update.request.extraLeftY = params.extraLeftY;
    parameters2update.request.extraLeftZ = params.extraLeftZ;
    parameters2update.request.extraRightX = params.extraRightX;
    parameters2update.request.extraRightY = params.extraRightY;
    parameters2update.request.extraRightZ = params.extraRightZ;
    parameters2update.request.extraLeftYaw = params.extraLeftYaw;
    parameters2update.request.extraLeftPitch = params.extraLeftPitch;
    parameters2update.request.extraLeftRoll = params.extraLeftRoll;
    parameters2update.request.extraRightYaw = params.extraRightYaw;
    parameters2update.request.extraRightPitch = params.extraRightPitch;
    parameters2update.request.extraRightRoll = params.extraRightRoll;

    parameters2update.request.stepGain = step;
    parameters2update.request.lateralGain = lateral;
    parameters2update.request.turnGain = turn;
}

void WalkCreator::initParams()
{
    std::ifstream params_file(default_path+edrom_path);
    reader.parse(params_file, paramsJson);

    params.freq = paramsJson["walk_parameters"]["freq"].asDouble();
    params.supportPhaseRatio = paramsJson["walk_parameters"]["supportPhaseRatio"].asDouble();
    params.footYOffset = paramsJson["walk_parameters"]["footYOffset"].asDouble();
    params.riseGain = paramsJson["walk_parameters"]["riseGain"].asDouble();
    params.trunkZOffset = paramsJson["walk_parameters"]["trunkZOffset"].asDouble();
    params.swingGain = paramsJson["walk_parameters"]["swingGain"].asDouble();
    params.swingRollGain = paramsJson["walk_parameters"]["swingRollGain"].asDouble();
    params.swingPhase = paramsJson["walk_parameters"]["swingPhase"].asDouble();
    params.stepUpVel = paramsJson["walk_parameters"]["stepUpVel"].asDouble();
    params.stepDownVel = paramsJson["walk_parameters"]["stepDownVel"].asDouble();
    params.riseUpVel = paramsJson["walk_parameters"]["riseUpVel"].asDouble();
    params.riseDownVel = paramsJson["walk_parameters"]["riseDownVel"].asDouble();
    params.swingPause = paramsJson["walk_parameters"]["swingPause"].asDouble();
    params.swingVel = paramsJson["walk_parameters"]["swingVel"].asDouble();
    params.trunkXOffset = paramsJson["walk_parameters"]["trunkXOffset"].asDouble();
    params.trunkYOffset = paramsJson["walk_parameters"]["trunkYOffset"].asDouble();
    params.trunkPitch = paramsJson["walk_parameters"]["trunkPitch"].asDouble();
    params.trunkRoll = paramsJson["walk_parameters"]["trunkRoll"].asDouble();
    params.extraLeftX = paramsJson["walk_parameters"]["extraLeftX"].asDouble();
    params.extraLeftY = paramsJson["walk_parameters"]["extraLeftY"].asDouble();
    params.extraLeftZ = paramsJson["walk_parameters"]["extraLeftZ"].asDouble();
    params.extraRightX = paramsJson["walk_parameters"]["extraRightX"].asDouble();
    params.extraRightY = paramsJson["walk_parameters"]["extraRightY"].asDouble();
    params.extraRightZ = paramsJson["walk_parameters"]["extraRightZ"].asDouble();
    params.extraLeftYaw = paramsJson["walk_parameters"]["extraLeftYaw"].asDouble();
    params.extraLeftPitch = paramsJson["walk_parameters"]["extraLeftPitch"].asDouble();
    params.extraLeftRoll = paramsJson["walk_parameters"]["extraLeftRoll"].asDouble();
    params.extraRightYaw = paramsJson["walk_parameters"]["extraRightYaw"].asDouble();
    params.extraRightPitch = paramsJson["walk_parameters"]["extraRightPitch"].asDouble();
    params.extraRightRoll = paramsJson["walk_parameters"]["extraRightRoll"].asDouble();

    params.distHipToKnee = paramsJson["structural_parameters"]["distHipToKnee"].asDouble();
    params.distKneeToAnkle = paramsJson["structural_parameters"]["distKneeToAnkle"].asDouble();
    params.distAnkleToGround = paramsJson["structural_parameters"]["distAnkleToGround"].asDouble();
    params.distFeetLateral = paramsJson["structural_parameters"]["distFeetLateral"].asDouble();

    step = paramsJson["step_parameters"]["stepGain"].asDouble();
    lateral = paramsJson["step_parameters"]["lateralGain"].asDouble();
    turn = paramsJson["step_parameters"]["turnGain"].asDouble();
}

void WalkCreator::walkRequest(const movement_msgs::WalkCreatorRequestMsg& msg)
{
    params.enabledGain = msg.enabledGain;
    params.stepGain = msg.stepGain*step;
    params.lateralGain = msg.lateralGain*lateral;
    params.turnGain = msg.turnGain*turn;

    runWalk(params, stepNumber, phase, time);
}

bool WalkCreator::runWalk(const Rhoban::IKWalkParameters& params, double stepNumber, double& phase, double& time)
{
    ros::Rate loop_rate(engineFrequency);
    for (double t = 0.0;  t < stepNumber/params.freq;  t += 1.0/engineFrequency) {
        time += 1.0/params.freq;
        bool success = Rhoban::IKWalk::walk(params, 1.0/engineFrequency, phase, outputs);

        if (!success) {
            std::cout << time << " Inverse Kinematics error. Position not reachable." << std::endl;

            return false;
        } else {
            positions.positions = { outputs.right_hip_yaw, outputs.left_hip_yaw,
                                    outputs.right_hip_roll, outputs.left_hip_roll, 
                                    outputs.right_hip_pitch, outputs.left_hip_pitch,                                    
                                    outputs.right_knee, outputs.left_knee, 
                                    outputs.right_ankle_roll, outputs.left_ankle_roll,
                                    outputs.right_ankle_pitch, outputs.left_ankle_pitch                                    
                                  };

            walk_motor_positions_pub.publish(positions);
            loop_rate.sleep();
        }
    }

    return true;
}

WalkCreator::WalkCreator(ros::NodeHandle nh)
{
    nh.getParam("walk_creator/interface", interfaceOn);

    walk_motor_positions_pub = nh.advertise<movement_msgs::WalkingPositionsMsg>("/walk_creator/positions", 1000);
    interface_parameters_update = nh.serviceClient<movement_msgs::WalkTestParametersSrv>("/walk_creator/walking_params");

    request_walk_creation = nh.subscribe("/approved_movement_prep/IKWalk", 10, &WalkCreator::walkRequest, this);
    request_parameters_update = nh.advertiseService("/movement_interface/walking_params", &WalkCreator::parametersUpdateRequest, this);

    initParams();

    if(interfaceOn)
    {
        ros::service::waitForService("/walk_creator/walking_params");
        reqEqualsParam();
        interface_parameters_update.call(parameters2update);
    }
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "Walk_creator_node");
    ros::NodeHandle nh;
    
    WalkCreator WalkCreatorObject(nh);

    ros::spin();
    return 0;
}