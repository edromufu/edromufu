import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for onePort in ports:
    portList.append(str(onePort))
    #print(str(onePort))

    for x in range(0, len(portList)):
        if portList[x].startswith("/dev/ttyACM0"):
            portVar = portList[x]
            
    
    serialInst.baudrate = 9600
    serialInst.port = "/dev/ttyACM0"
    serialInst.open()

    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode('utf')) 